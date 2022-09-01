from rest_framework import serializers
from django.core.exceptions import ValidationError
import re

class Rollserializer(serializers.Serializer):
    name=serializers.CharField(required=True)
    roll_no=serializers.IntegerField(required=True)
    city=serializers.CharField(required=True)
    state=serializers.CharField(required=True)
    def validate_roll_no(self,roll_no):
        if len(str(roll_no))<=3:
            return True
        raise ValidationError("incorrect roll_no provided")


