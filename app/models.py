from django.db import models

# Create your models here.
 

class htmlforms(models.Model):
    sname=models.CharField(max_length=100,primary_key=True)
    slocation=modles.CharField(max_length=100)
    sprincipal=models.CharField(max_length=100)


    def __str__(self):
        return self.htmlforms_name
