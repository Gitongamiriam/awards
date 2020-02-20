from rest_framework import serializers
from .models import Profile,Project

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields  = ('user','prof_pic','bio','contact')


class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = ('author','title','description','project_pic','live_site')