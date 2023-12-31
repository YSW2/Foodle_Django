from django.db import models

# Create your models here.

class Post(models.Model):
    TAG_CHOICE = {
        ('all', '자유'),
    }
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )
    title = models.CharField("제목", max_length=50)
    content = models.TextField("내용")
    created = models.DateTimeField("작성일시", auto_now_add=True)
    tags = models.CharField("태그", max_length=20, choices=TAG_CHOICE)
    views = models.ManyToManyField(
        'users.User',
        verbose_name="조회수",
        related_name="view_user",
        blank=True,
    )

    def __str__(self):
        return f"{self.user.nickname}의 글(id : {self.id})"

class Comment(models.Model):
    user = models.ForeignKey(
        "users.User",
        verbose_name="작성자",
        on_delete=models.CASCADE,
    )
    post = models.ForeignKey(
        "posts.Post",
        verbose_name="게시글",
        on_delete=models.CASCADE,
    )
    content = models.TextField("내용")
    created = models.DateTimeField("작성일시", auto_now_add=True)