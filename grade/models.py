from django.db import models

# Create your models here.
class GradeModel(models.Model):
    gradeId=models.AutoField(primary_key=True)
    gradeTitle= models.CharField(max_length=100) # this is the title of grade e.g grade 9, grade 10



