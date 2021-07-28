from django.db import models


# Create your models here.

# class UserInfo(models.Model):
#     username = models.CharField(max_length=50, unique=True)
#     password = models.CharField(max_length=50)
#     info = models.TextField(max_length=200)


class Task01(models.Model):
    title = models.CharField(max_length=50)
    created_at = models.DateTimeField(auto_now_add=True)
    code = models.TextField()

    def __str__(self):
        return self.title


class Task02(models.Model):
    title1 = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add=True)

    # area = models.TextField(max_length=100)

    def __str__(self):
        return self.title1 + '  :  ' + self.created_at
        # return self.title1


class Task03(models.Model):
    name = models.CharField(max_length=30)
    contents = models.TextField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.id) + ' : ' + self.name
