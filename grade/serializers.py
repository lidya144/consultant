from rest_framework import serializers
from models_app.models import GradeModel
from subject.serializers import SubjectSerializers


class GradeSerializers(serializers.ModelSerializer):
    grade_subejct = SubjectSerializers(many=True, read_only=True)

    class Meta:
        model = GradeModel
        fields = "__all__"

