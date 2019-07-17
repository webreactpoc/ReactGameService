from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import *
from django.core import serializers
import json 

## TODO IMPLEMENT WITH CLASS BASED VIEWS
## TODO check for POST/GET etc

def index(request):
    return JsonResponse({'Hello':'World'})

##### GET BY name/id && GET ALL

def GET_test(request,id=-1):
    serializedData = objectByIdOrAll(id,Test,"Test")
    return JsonResponse(serializedData)

def GET_testee(request,id=-1):
    serializedData = objectByIdOrAll(id,Testee,"Testee")
    return JsonResponse(serializedData)
    
def GET_status(request,id=-1):
    serializedData = objectByIdOrAll(id,Status,"Status")
    return JsonResponse(serializedData)

def GET_organisation(request,id=-1):
    serializedData = objectByIdOrAll(id,Organisation,"Organisation")
    return JsonResponse(serializedData)
    
def GET_attempt(request,id=-1):
    serializedData = objectByIdOrAll(id,Attempt,"Attempt")
    return JsonResponse(serializedData)

##### POST
## TODO CHECK FOR UPDATE/CREATE
def POST_test(request):
    serializedData = modelToJson(Test.objects.all(),"Tests")
    return JsonResponse(serializedData)

def POST_testee(request):
    serializedData = modelToJson(Testee.objects.all(),"Testees")
    return JsonResponse(serializedData)
    
def POST_status(request):
    serializedData = modelToJson(Status.objects.all(),"Statuss")
    return JsonResponse(serializedData)

def POST_organisation(request):
    serializedData = modelToJson(Organisation.objects.all(),"Organisations")
    return JsonResponse(serializedData)
    
def POST_attempt(request):
    serializedData = modelToJson(Attempt.objects.all(),"Attempts")
    return JsonResponse(serializedData)

#####

def modelToJson(modelObjects,modelName):
    serializedObjects = serializers.serialize("json", modelObjects)
    data = {modelName: json.loads(serializedObjects)}
    return data

def objectByIdOrAll(id,model,modelName):
    object = model.objects.filter(pk=id)
    if id == -1:
        return modelToJson(model.objects.all(),modelName)
    else:
        return modelToJson(object,modelName)