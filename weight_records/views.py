from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework import generics, views
from rest_framework.permissions import IsAuthenticated
from .serializers import WeightRecordSerializer
from .models import WeightRecord
from datetime import date, timedelta
from account.renderers import UserRenderer


# to get all the records or create a new record
class WeightListCreate(generics.ListCreateAPIView):
    permission_classes = [IsAuthenticated]
    serializer_class = WeightRecordSerializer
    renderer_classes = [UserRenderer]

    def get_queryset(self):
        user = self.request.user
        return WeightRecord.objects.filter(user=user)

    def perform_create(self, serializer):
        if serializer.is_valid():
            serializer.save(user=self.request.user)
        else:
            print(serializer.errors)


# to get latest record
class GetLatestWeight(views.APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get(self, request):
        latest_record = WeightRecord.objects.filter(user=request.user).latest(
            "created_at"
        )
        serializer = WeightRecordSerializer(latest_record)
        return Response(serializer.data, status=status.HTTP_200_OK)


# to get earliest record
class GetEarliestWeight(views.APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get(self, request):
        earliest_record = WeightRecord.objects.filter(user=request.user).earliest(
            "created_at"
        )
        serializer = WeightRecordSerializer(earliest_record)
        return Response(serializer.data, status=status.HTTP_200_OK)


# to get records from last X days
class GetDaysAgoWeight(views.APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get(self, request, days):
        today = date.today()
        xDaysAgo = today - timedelta(days=days)
        records = WeightRecord.objects.filter(
            user=request.user, created_at__range=(xDaysAgo, today)
        )
        serializer = WeightRecordSerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
