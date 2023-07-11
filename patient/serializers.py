from rest_framework import serializers
from .models import *
from rest_framework.validators import UniqueTogetherValidator


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        exclude = ['updated_at',]


class VisitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Visit
        exclude = ['updated_at',]


class VisitListSerializer(serializers.ModelSerializer):
    patient = PatientSerializer()

    class Meta:
        model = Visit
        exclude = ['updated_at',]
