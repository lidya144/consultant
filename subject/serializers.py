from rest_framework import serializers
from models_app.models import SubjectModel
from unit.serializers import UnitSerializers


class SubjectSerializers(serializers.ModelSerializer):
    subject_unit = UnitSerializers(many=True, read_only=True)

    class Meta:
        model = SubjectModel
        fields = ("subjectId", "subjectName", "subject_unit", "grade")

