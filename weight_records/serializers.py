from rest_framework import serializers
from weight_records.models import WeightRecord


class WeightRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = WeightRecord
        fields = ["user", "weight", "created_at", "id"]
        extra_kwargs = {
            "user": {"read_only": True},
            "id": {"read_only": True},
        }
