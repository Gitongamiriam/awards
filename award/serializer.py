from rest_framework import serializers
from .models import ProfileMerch

class MerchSerializers(serializers,ModelSerializers):
    class Meta:
        model = ProfileMerch
        fields  =('user','prof_pic','bio','contact')
