from rest_framework import serializers
from .models import *
from rest_framework.exceptions import ValidationError


class SuvSerializer(serializers.ModelSerializer):
    class Meta:
        model = Suv
        fields = '__all__'


class MijozSerializer(serializers.ModelSerializer):
    class Meta:
        model = Mijoz
        fields = '__all__'


class AdminSerializer(serializers.ModelSerializer):
    class Meta:
        model = Admin
        fields = '__all__'


class HaydovchiSerializer(serializers.ModelSerializer):
    class Meta:
        model = Haydovchi
        fields = '__all__'


class BuyurtmaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Buyurtma
        fields = '__all__'

    def validate_mijoz_qarz(self, qiymat):
        if qiymat.mijoz.qarz > 500000:
            raise ValidationError("Qarzingiz juda ko’p, buyurtma qilolmaysiz!")
        return qiymat
