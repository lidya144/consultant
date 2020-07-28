from django.db import models
from datetime import datetime
from unit.models import UnitModel

def upload_path(instance, filename):
    """Storing an image with directory post_image with custom file name"""
    now = datetime.now()
    now_string = now.strftime("%d-%m-%Y %H:%M:%S")
    new_filename = now_string + filename
    return "/".join(["post_image", new_filename])


class SubUnitModel(models.Model):
   subjectId= models.AutoField(primary_key=True)
   unit=models.ForeignKey(UnitModel,related_name="unit_subunit",  on_delete=models.CASCADE) # One unit have many subunit relationship
   title= models.CharField(max_length=255) # this is the title of sub-unit tile of a model 
   body= models.TextField(max_length=10000) # this is the body of the subunit of model
   image= models.FileField(null=False, blank=False, upload_to=upload_path)

