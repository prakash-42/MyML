from rest_framework import serializers
from .models import File
from drf_extra_fields.fields import Base64ImageField


class FileSerializer(serializers.ModelSerializer):
    file = Base64ImageField()

    class Meta:
        model = File
        fields = "__all__"

    def create(self, validated_data):
        file = validated_data.pop('file')
        remark = validated_data.pop('remark')

        file_object = File.objects.create(remark=remark, file=file)
        return file_object
