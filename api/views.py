from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import UserProfileSerializer,UserProfileSerializer2,DocumentsSerializer,AppointmentSerializer , MedicationSerializer,DocumentsSerializerFront, ChronicConditionSerializer
from UserProfile import views as userViews
from medications import views as mediactionViews
from documents import views  as documentViews
from appointments import views as appointmentsViews
from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import FormParser, MultiPartParser
from rest_framework.response import Response
from rest_framework import status
from django.views.decorators.csrf import csrf_exempt
from django.contrib.staticfiles.views import serve
from django.core import serializers
import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
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

@api_view(['GET'])
def getChronicConditions(request, id):
    conditions = userViews.getChronicConditions(id)
    serializer = ChronicConditionSerializer(conditions, many=True)
    return Response(serializer.data)

@api_view(['POST'])
@csrf_exempt
def addUser(request):
  

    if request.method == 'POST':
        serializer = UserProfileSerializer2(data=request.data)
        if serializer.is_valid():
            print(serializer)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
@csrf_exempt
def updateUser(request):
  
   
    print(request.data['name'])        

    user = userViews.updateUser(request.data)
    # record_dict = model_to_dict(user)
    # json_data = json.dumps(record_dict)

    return Response("json_data", status=status.HTTP_201_CREATED)


@api_view(['POST'])
@csrf_exempt
def addMedication(request):
  
    if request.method == 'POST':
        serializer = MedicationSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['POST'])
@csrf_exempt
def login(request):
    print("asdasdasdadad")
    data = request.data['email']

    print("asdasdasdadad")
    return Response(userViews.login(data), status=status.HTTP_201_CREATED)


@api_view(['POST'])
@csrf_exempt
def addChronicConditions(request):
  
    if request.method == 'POST':
        serializer = ChronicConditionSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        

@api_view(['POST'])
@csrf_exempt
def addAppointment(request):
  
    print(request.data)
    if request.method == 'POST':
        serializer = AppointmentSerializer(data=request.data)
        if serializer.is_valid():
            print(serializer)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
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
    serializer = DocumentsSerializerFront(documents, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@csrf_exempt
def viewFile(request,pk):
    document = documentViews.getFile(pk)
    url = documentViews.upload_file_cloud(document)
    return Response(url, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@csrf_exempt
def getMedications(request,pk):
    medications = mediactionViews.getMedications(pk)
    serializer = MedicationSerializer(medications, many=True)
    return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
@csrf_exempt
def getAppointments(request,pk):
    appointment = appointmentsViews.getAppointments(pk)
    serializer = AppointmentSerializer(appointment, many=True)
    return Response(serializer.data, status=status.HTTP_200_OK)

@api_view(['DELETE'])
@csrf_exempt
def deleteDocument(request,pk):
    documentViews.deleteDocument(pk)
    return Response("DELETED", status=status.HTTP_201_CREATED)

@api_view(['DELETE'])
@csrf_exempt
def deleteMedication(request,pk):
    mediactionViews.deleteMedication(pk)
    return Response("DELETED", status=status.HTTP_200_OK)

@api_view(['DELETE'])
@csrf_exempt
def deleteAppointment(request,pk):
    appointmentsViews.deleteAppointment(pk)
    return Response("DELETED", status=status.HTTP_200_OK)

@api_view(['DELETE'])
@csrf_exempt
def deleteChronicCondition(request,pk):
    userViews.deleteChronicConditions(pk)
    return Response("DELETED", status=status.HTTP_200_OK)