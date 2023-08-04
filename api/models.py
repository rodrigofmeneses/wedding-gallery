from django.db import models
from django.contrib.auth.models import User


class Photo(models.Model):
    STATUS_CHOICE = (
        (0, 'PENDING'),
        (1, 'APPROVED'),
        (2, 'DECLINED'),
    )

    author = models.ForeignKey(User, on_delete=models.CASCADE)
    url = models.TextField()
    status = models.IntegerField(choices=STATUS_CHOICE, default=0)
    created_at = models.DateTimeField(auto_now_add=True)


class Comment(models.Model):
    post = models.ForeignKey(Photo, on_delete=models.CASCADE)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class Like(models.Model):
    photo = models.ForeignKey(Photo, on_delete=models.CASCADE,
                              related_name="likes")
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        unique_together = ["photo", "user"]
