from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserProfileSerializer,DocumentsSerializer, DocumentsSerializerFront
from UserProfile import views as userViews
from documents import views  as documentViews
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.views import serve

@api_view(['GET'])
def getRoutes(request):

    routes = [
        {'GET': '/api/userprofile/id'}
    ]

    return Response(routes)


@api_view(['GET'])
def getUserProfile(request, id):

    userProfile = userViews.getUserProfile(id)
    serializer = UserProfileSerializer(userProfile, many=False)
    return Response(serializer.data)



@api_view(['POST'])
@parser_classes([MultiPartParser])
@csrf_exempt
def file_upload_api_view(request):
  
    if request.method == 'POST':
        serializer = DocumentsSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            
            serializer.save()
            document = documentViews.getFile(serializer.data['id'])
            url = documentViews.upload_file_cloud(document)
            documentViews.updateUrl(serializer.data['id'], url)

            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET'])
@csrf_exempt
def getFiles(request,pk):
    documents = documentViews.getFiles(pk)
    print(documents)
    serializer = DocumentsSerializerFront(documents, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@csrf_exempt
def viewFile(request,pk):
    document = documentViews.getFile(pk)
    url = documentViews.upload_file_cloud(document)
    return Response(url, status=status.HTTP_201_CREATED)