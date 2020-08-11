from rest_framework import serializers
from models_app.models import GradeModel
from subject.serializers import SubjectSerializers


class GradeSerializers(serializers.ModelSerializer):
    class Meta:
        model = GradeModel
        fields = "__all__"

