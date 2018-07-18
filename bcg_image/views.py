from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser, FormParser
from rest_framework.response import Response
from rest_framework import status
from .models import Image
from rest_framework import generics
from rest_framework.decorators import api_view
from .serializers import ImageSerializer

@api_view(['GET', 'POST'])
def image_list(request):

  if request.method == 'GET':

    # check if we have an extension
    extension = request.query_params.get('extension', None)

    # check if the extension is there or not
    if extension is not None:
      # filter if we have an extension
      image = Image.objects.filter(extension=extension)
    else:
      # get them all
      image = Image.objects.all()

    serializer = ImageSerializer(image, many=True)
    return Response(serializer.data)

  elif request.method == 'POST':
    image_serializer = ImageSerializer(data=request.data)
    if image_serializer.is_valid():
      image_serializer.save()
      return Response(image_serializer.data, status=status.HTTP_201_CREATED)
    else:
      return Response(image_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET'])
def image_detail(request, id):

    # do we have a file with the id of...
    try:
      image = Image.objects.get(id=id)
    except Image.DoesNotExist:
      return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
      serializer = ImageSerializer(image)
      return Response(serializer.data)

# 3. Write a series of automated tests that test the image upload, download and file format conversion capabilities.
