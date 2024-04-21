from rest_framework import serializers
from UserProfile.models import UserProfile, ChronicCondition
from documents.models import Document
from medications.models import Medications
from appointments.models import Appointmets
from documents.models import QrCode

from django.core.validators import EmailValidator

class UserProfileSerializer(serializers.ModelSerializer):
    id = serializers.ReadOnlyField()

    class Meta:
        model = UserProfile
        fields = '__all__'

    def validate(self, data):
        """
        Validate the data, bypassing the unique validation for the email field.
        """
        # If 'email' field is present in the data, remove it before validating
        data.pop('email', None)
        return data



class UserProfileSerializer2(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = ['email']

class ChronicConditionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ChronicCondition
        fields = '__all__'

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class QRcodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = QrCode
        fields = '__all__'

class MedicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Medications
        fields = '__all__'

class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointmets
        fields = '__all__'


class DocumentsSerializerFront(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ["name", "created", "id","url"]