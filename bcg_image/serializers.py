from rest_framework import serializers
from .models import Image

class ImageSerializer(serializers.ModelSerializer):

  class Meta():
    model = Image
    fields = ('id', 'image', 'name', 'timestamp', 'extension')
    extra_kwargs = {
      'extension': {'read_only': True},
    }
