from django.db import models
from grade.models import GradeModel

class SubjectModel(models.Model):
   subjectId= models.AutoField(primary_key=True)
   grade=models.ForeignKey(GradeModel,related_name="grade_subejct",  on_delete=models.CASCADE) # grade have many subject relationship
   subjectName= models.CharField(max_length=255) # this is the name of the subject e.g biology, physics

