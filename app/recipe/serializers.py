from core.models import Tag
from rest_framework import serializers


class TagSerializer(serializers.ModelSerializer):
    """Serializer for the tag objects"""

    class Meta:
        model = Tag
        fields = ('id', 'name')
        read_only_fields = ('id',)
