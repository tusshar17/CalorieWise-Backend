from django.shortcuts import render
from rest_framework import viewsets, status, views
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from account.renderers import UserRenderer
from .serializer import MealLogSerializer, MacroSummarySerializer
from .models import MealLog
from datetime import *


class MealLogModelViewSet(viewsets.ModelViewSet):
    serializer_class = MealLogSerializer
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]
    queryset = MealLog.objects.all()

    def list(self, request, *args, **kwargs):
        user = request.user
        date = self.request.query_params.get("date")
        print(date)
        if date:
            meal_log = MealLog.objects.filter(user=user, date=date)
            if meal_log.exists():
                meal_log = meal_log[0]
            serializer = MealLogSerializer(meal_log)
            return Response(serializer.data)
        return Response(
            {"error": "please provide date."}, status=status.HTTP_400_BAD_REQUEST
        )

    def create(self, request, *args, **kwargs):
        log = MealLog.objects.filter(
            user=request.user, date=request.data.get("date", date.today())
        )
        if log.exists():
            return Response(
                {"error": "entry for today already exists. try updating."},
                status=status.HTTP_400_BAD_REQUEST,
            )
        # initiate log
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data["user"] = request.user
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)

    def update(self, request, *args, **kwargs):
        print("=========req data=====")
        print(request.data)
        if "logs" not in request.data.keys():
            return Response(
                {"Error": "no logs found"}, status=status.HTTP_400_BAD_REQUEST
            )
        return super().update(request, *args, **kwargs)

    """
    def create(self, request, *args, **kwargs):
        entryExists = MealLog.objects.filter(
            user=request.user, date=request.data.get("date", date.today())
        ).exists()
        if entryExists:
              status=status.HTTP_400_BAD_REQUEST,
            )return Response(
                {"error": "entry for today already exists. try updating."},
    
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.validated_data["user"] = request.user
            self.perform_create(serializer)
            return Response(serializer.data, status=status.HTTP_200_OK)
        """


# stats
class MacroSummary(views.APIView):
    permission_classes = [IsAuthenticated]
    renderer_classes = [UserRenderer]

    def get(self, request, days):
        today = date.today()
        xDaysAgo = today - timedelta(days=days)
        records = (
            MealLog.objects.all()
            .filter(user=request.user, date__range=(xDaysAgo, today))
            .order_by("date")
        )
        serializer = MacroSummarySerializer(records, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
