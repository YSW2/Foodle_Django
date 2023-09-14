from django.db import models

# Create your models here.
class Fridge(models.Model):
    user = models.ForeignKey("users.User", on_delete=models.CASCADE)
    name = models.CharField("식품명", max_length=30)
    exp_date = models.DateTimeField("유통기한", null=True)

    def __str__(self):
        return f"{self.user.nickname}의 {self.name}"