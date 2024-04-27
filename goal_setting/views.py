from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets
from account.renderers import UserRenderer
from .models import Goal
from .serializers import GoalSerializer


class GoalModelViewSet(viewsets.ModelViewSet):
    serializer_class = GoalSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get_queryset(self):
        return Goal.objects.filter(user=self.request.user)

    def create(self, request, *args, **kwargs):
        doesGoalExists = Goal.objects.filter(user=request.user).exists()
        if doesGoalExists:
            return Response(
                {"error": "Goal already exists. Try updating instead."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data["user"] = request.user
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        return super().update(request, *args, **kwargs)

    def destroy(self, request, *args, **kwargs):
        return Response(
            {"error": "Delete method not allowed."}, status=status.HTTP_400_BAD_REQUEST
        )
