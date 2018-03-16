from django.db import models
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField  

# Create your models here.
class Cate(models.Model):
    type_name = models.CharField(max_length = 30)

    def __str__(self):
        return self.type_name
class Blog(models.Model):
    title = models.CharField(max_length = 100)
    blog_type = models.ForeignKey(Cate,on_delete = models.DO_NOTHING)
    content = RichTextUploadingField()
    author = models.ForeignKey(User,on_delete = models.DO_NOTHING)
    created_time = models.DateTimeField(auto_now_add = True)
    last_updated = models.DateTimeField(auto_now = True)
    is_delete = models.BooleanField(default = False)

    def __str__(self):
        return '<Blog: %s>' %self.title


