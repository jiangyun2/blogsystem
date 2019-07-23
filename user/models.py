from django.db import models
import datetime


# Create your models here.


class BlogUser(models.Model):
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=30)
    email = models.EmailField()

    def __str__(self):
        return 'BlogUser<usename={},password={},email={}>'.format(self.username, self.password, self.email)


class BlogContent(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    createtime = models.DateTimeField(default=datetime.datetime.now())
    lasttime = models.DateTimeField(default=datetime.datetime.now())

    def __str__(self):
        return 'BlogContent<title={}, content={}, createtime={}>'.format(self.title, self.content, self.createtime)


