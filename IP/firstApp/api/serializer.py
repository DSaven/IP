from rest_framework import serializers
from firstApp.models import CarSpecs


class CarSpecsSerializer(serializers.ModelSerializer):
    class Meta:
        model = CarSpecs
        fields = '__all__'
