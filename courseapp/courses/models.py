from django.db import models
from django.contrib.auth.models import AbstractUser
from ckeditor.fields import RichTextField

class User(AbstractUser):
    pass

class BaseModels(models.Model):
    create_date = models.DateField(auto_now_add=True, null=True)
    update_date = models.DateField(auto_now=True , null=True)
    active = models.BooleanField(default=True)

    class Meta:
        abstract = True
        ordering = ['-id']


class Category(BaseModels):
    name = models.CharField(max_length=50,null=False)

    def __str__(self):
        return self.name




class Course (BaseModels):
    subject = models.CharField(max_length=255 ,null=False)
    description = RichTextField()
    image = models.ImageField(upload_to='courses/%y/%m')
    category = models.ForeignKey(Category,on_delete=models.RESTRICT)
    tags = models.ManyToManyField('Tag')

    def __str__(self):
        return self.subject
    class Meta:
        unique_together = ('subject' , 'category')


class Lesson (BaseModels):
    subject = models.CharField(max_length=255)
    content = RichTextField()
    image = models.ImageField(upload_to='lessons/%y/%m')
    course = models.ForeignKey(Course , on_delete=models.CASCADE)
    tags = models.ManyToManyField('Tag')
    class Meta:
        unique_together = ('subject' , 'course')



class Tag (BaseModels):
    name = models.CharField(max_length=50 , unique=True)

    def __str__(self):
        return self.name