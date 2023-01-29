from rest_framework import serializers
from .models import User


class UserSerializer(serializers.ModelSerializer):


    class Meta:
        model = User
        fields = ['name','mobile_no','minimum_quantity','maximum_quantity','pincode']


class UserValidationSerializer(serializers.Serializer):
    name = serializers.CharField()
    mobile_no = serializers.IntegerField()
    minimum_quantity = serializers.IntegerField()
    maximum_quantity = serializers.IntegerField()
    pincode = serializers.IntegerField()

    def validate(minimum_quantity):
        if minimum_quantity ==0:
            raise serializers.ValidationError("it can't be zero")
        return minimum_quantity

    def validate(maximum_quantity):
        if (maximum_quantity == 0) or (maximum_quantity==1):
            raise serializers.ValidationError("it can't be zero and one")
        return maximum_quantity

