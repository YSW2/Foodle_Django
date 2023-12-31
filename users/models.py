from django.contrib.auth.models import AbstractUser
from django.db import models

# Create your models here.

class User(AbstractUser):
    profile_image = models.ImageField(
        "프로필 이미지", upload_to="users/profile", blank=True)
    nickname = models.CharField(default=f"user{id}", max_length=20)
    like_posts = models.ManyToManyField(
        'posts.Post',
        verbose_name="좋아요 목록",
        related_name="like_users",
        blank=True,
    )