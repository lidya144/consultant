from django.db import models
from subject.models import SubjectModel
# Create your models here.
class UnitModel(models.Model):
    unitId=models.AutoField(primary_key=True)
    title=models.CharField(max_length=255) #this is the title of unit e.g Introduction of computer science
    subject=models.ForeignKey(SubjectModel,related_name="subject_unit",  on_delete=models.CASCADE) # grade have many subject relationship
    name=models.CharField(max_length=255) # this is the name of the chapter or unit e.g Chapter 9, Unit 9
    
