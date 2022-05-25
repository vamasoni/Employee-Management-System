from django.db import models
 
# Create your models here.
 
class Member(models.Model):
    firstname=models.CharField(max_length=30)
    lastname=models.CharField(max_length=30)
    emailid=models.EmailField()
    username=models.CharField(max_length=30)
    password=models.CharField(max_length=20)

    def __str__(self):
        return self.id

