from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import api_view, permission_classes
from .serializers import FoodItemSerializer, RecipeSerializer
from account.renderers import UserRenderer
from .models import FoodItem, Recipe
from .util import CalculateRecipeMacros
import time


# Food Items
class FoodItemModelViewSet(viewsets.ModelViewSet):
    serializer_class = FoodItemSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    # TODO : update food item
    def partial_update(self, request, *args, **kwargs):
        return super().partial_update(request, *args, **kwargs)

    def get_queryset(self):
        return FoodItem.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            data={"message": "food item deleted succesfully"}, status=status.HTTP_200_OK
        )


# search food item
@api_view(["GET"])
@permission_classes(
    [
        IsAuthenticated,
    ]
)
def searchFoodItem(request, query):
    user = request.user
    foodItemsInstances = FoodItem.objects.filter(user=user).filter(
        name__icontains=query
    )
    print(foodItemsInstances)
    serialized = FoodItemSerializer(foodItemsInstances, many=True)
    return Response(serialized.data, status=status.HTTP_200_OK)


# Recipe


# Get Recipes - One / All
class RecipeModelViewSet(viewsets.ModelViewSet):
    serializer_class = RecipeSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get_queryset(self):
        return Recipe.objects.filter(user=self.request.user)

    def perform_create(self, serializer):
        return serializer.save(user=self.request.user)

    def partial_update(self, request, *args, **kwargs):
        # modify request.data
        recipeMacros = CalculateRecipeMacros.calculateRecipeMacros(
            request.data.get("recipe_items", None)
        )
        for key in recipeMacros:
            request.data[key] = recipeMacros[key]
        return super().partial_update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            data={"message": "recipe deleted succesfully"}, status=status.HTTP_200_OK
        )
