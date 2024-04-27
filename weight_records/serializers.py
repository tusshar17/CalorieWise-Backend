from rest_framework import serializers
from weight_records.models import WeightRecord


class WeightRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightRecord
        fields = ["user", "weight", "created_at"]
        extra_kwargs = {"user": {"read_only": True}, "created_at": {"read_only": True}}
