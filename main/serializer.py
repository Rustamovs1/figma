from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = 'all'


class BannerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Banner
        fields = 'all'


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = News
        fields = 'all'


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = 'all'


class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = 'all'


class InformationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Information
        fields = 'all'


class TeamSerializer(serializers.ModelSerializer):
    class Meta:
        model = Team
        fields = 'all'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = 'all'


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = 'all'


class PostVideosSerializer(serializers.ModelSerializer):
    class Meta:
        model = PostVidio
        fields = 'all'
