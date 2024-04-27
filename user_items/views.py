from django.shortcuts import render
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .serializers import FoodItemSerializer, RecipeSerializer
from account.renderers import UserRenderer
from .models import FoodItem, Recipe


# Food Items
class FoodItemModelViewSet(viewsets.ModelViewSet):
    serializer_class = FoodItemSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

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

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            data={"message": "food item deleted succesfully"}, status=status.HTTP_200_OK
        )
