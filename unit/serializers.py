from rest_framework import serializers
from models_app.models import UnitModel
from utilities.image_validation import validate_image


class UnitSerializers(serializers.ModelSerializer):
    def validate_pdf(self, val):
        validate_image(val)

    class Meta:
        model = UnitModel
        fields = ("unitId", "title", "name", "pdf", "subject")

