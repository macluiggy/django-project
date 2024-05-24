from rest_framework import serializers
from django.contrib.auth.models import User
from posts.serializers import PostSerializer

class UserSerializer(serializers.ModelSerializer):
    # posts = PostSerializer(many=True, read_only=True)
    posts = serializers.SerializerMethodField()
    class Meta:
        model = User
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super(UserSerializer, self).__init__(*args, **kwargs)
        if self.instance is not None:  # Updating an existing user
            self.fields['username'].required = False
            self.fields['password'].required = False
            
    def get_posts(self, obj):
        return PostSerializer(obj.post_set.all(), many=True).data