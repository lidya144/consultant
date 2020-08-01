from rest_framework import serializers
from models_app.models import TransactionModel


class TransactionSerializers(serializers.ModelSerializer):
    class Meta:
        model = TransactionModel
        fields = "__all__"

