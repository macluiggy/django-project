from django.db import models
from django.contrib.auth.models import User
from posts.models import Post

# Create your models here.
class Like(models.Model):
    id = models.BigAutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    
    class Meta:
        db_table = 'likes'
        unique_together = ('user', 'post')
        constraints = [
            models.UniqueConstraint(fields=['user', 'post'], name='unique_like')
        ]