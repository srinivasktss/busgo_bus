from rest_framework import serializers
from .models import Operator


class OperatorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Operator
        fields = [
            'id', 'name',
            'contact_person', 'email', 'phone_number',
            'address', 'city', 'state', 'country',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']