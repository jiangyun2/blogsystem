from django.db import models

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

    def __str__(self):
        return 'BlogContent<title={}, content={}>'.format(self.title, self.content)
