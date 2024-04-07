from rest_framework import serializers
from UserProfile.models import UserProfile
from documents.models import Document


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class DocumentsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = '__all__'

class DocumentsSerializerFront(serializers.ModelSerializer):
    class Meta:
        model = Document
        fields = ["name", "created", "id","url"]