from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Like(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='likes')
    
    class Meta:
        db_table = 'likes'
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_like')
        ]