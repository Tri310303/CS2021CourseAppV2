from django.db import models
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass

class BaseModels(models.Model):
    create_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True , null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True



class Category(BaseModels):
    name = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name




class Course (BaseModels):
    subject = models.CharField(max_length=255 ,null=False)
    description = models.TextField()
    image = models.CharField(max_length=100)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)

    def __str__(self):
        return self.subject