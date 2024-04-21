from django.shortcuts import render
import os

# Create your views here.
from django.http import JsonResponse
from .models import Document,QrCode
from firebase_admin import credentials, initialize_app, storage
import firebase_admin

def upload_file(request):
    print(request)
    if request.method == 'POST' and request.FILES.get('file'):
        uploaded_file = request.FILES['file']
        # Handle the uploaded file as needed (e.g., save to filesystem or database)
        # Example: UploadedFile.objects.create(file=uploaded_file)
        return JsonResponse({'message': 'File uploaded successfully'})
    else:
        return JsonResponse({'error': 'No file uploaded'}, status=400)


def getFiles(pk):
    documents = Document.objects.filter(userId = pk)
    return documents

def getFilesQr(pk):
    documents = Document.objects.filter(userId = pk)
    return documents

def getFile(pk):
    document = Document.objects.get(id=pk)
    return document.file.path

def getFileQr(pk):
    document = QrCode.objects.get(id=pk)
    return document.file.path

def upload_file_cloud(filePath):

    if not firebase_admin._apps:
        path = r"C:\Coding\Mariam's Graduation Project\Backend\HealthKeeper\documents\first-data-base-94a72-firebase-adminsdk-107u8-d57fe868f7.json"
        cred = credentials.Certificate(path)
        initialize_app(cred, {'storageBucket': 'first-data-base-94a72.appspot.com'})
        # Put your local file path 
    fileName = filePath
    bucket = storage.bucket()
    blob = bucket.blob(fileName)
    blob.upload_from_filename(fileName)
    
    # Opt : if you want to make public access from the URL
    blob.make_public()

    print("your file url", blob.public_url)
    return blob.public_url

def updateUrl(pk,url):
    document = Document.objects.get(id=pk)
    document.url = url
    document.save()

def updateUrlQr(pk,url):
    document = QrCode.objects.get(id=pk)
    document.url = url
    document.save()

def deleteDocument(pk):
    document = Document.objects.get(id=pk)
    deleteCloud(document.name)
    document.delete()
  

def deleteCloud(filePath):

    if not firebase_admin._apps:
        path = r"C:\Coding\Mariam's Graduation Project\Backend\HealthKeeper\documents\first-data-base-94a72-firebase-adminsdk-107u8-d57fe868f7.json"
        cred = credentials.Certificate(path)
        initialize_app(cred, {'storageBucket': 'first-data-base-94a72.appspot.com'})
        # Put your local file path 
    fileName = os.path.splitext(filePath)[0]
    bucket = storage.bucket()
    blobs = bucket.list_blobs()
    print(fileName)
    for blob in blobs:
        if fileName in blob.name:
                print(' * deleting', blob)
                blob.delete()
    return
