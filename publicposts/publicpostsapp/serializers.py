from rest_framework import serializers
from .models import *


class PostSerializer(serializers.ModelSerializer):

    class Meta:
        model = Post
        fields = ('id',
                  'text',
                  'likes_count',
                  'date',)
