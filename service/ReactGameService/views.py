from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseServerError, HttpResponse
from .models import *
from django.core import serializers
import json 

from django.views.decorators.csrf import csrf_exempt # TODO REMOVE THIS

## TODO IMPLEMENT WITH CLASS BASED VIEWS

def index(request):
    return JsonResponse({'Hello':'World'})

##### GET BY name/id && GET ALL

def GET_test(request,id=-1):
    serializedData = objectByIdOrAll(id,Test,"Test")
    return JsonResponse(serializedData,safe=False)

def GET_testee(request,id=-1):
    serializedData = objectByIdOrAll(id,Testee,"Testee")
    return JsonResponse(serializedData,safe=False)
    
def GET_status(request,id=-1):
    serializedData = objectByIdOrAll(id,Status,"Status")
    return JsonResponse(serializedData,safe=False)

def GET_organisation(request,id=-1):
    serializedData = objectByIdOrAll(id,Organisation,"Organisation")
    return JsonResponse(serializedData,safe=False)
    
def GET_attempt(request,id=-1):
    serializedData = objectByIdOrAll(id,Attempt,"Attempt")
    return JsonResponse(serializedData,safe=False)

##### POST

@csrf_exempt#TODO REMOVE THIS AND SECURE ENDPOINT
def POST_request(request):
    return singularPostRequest(request)

#####

def modelToJson(modelObjects,modelName):
    serializedObjects = serializers.serialize("json", modelObjects)
    return json.loads(serializedObjects)

def objectByIdOrAll(id,model,modelName):
    object = model.objects.filter(pk=id)
    if id == -1:
        return modelToJson(model.objects.all(),modelName)
    else:
        return modelToJson(object,modelName)

def singularPostRequest(request):
    if request.method == "POST":
        for obj in serializers.deserialize("json",request):
            obj.object.created_at=timezone.now();##TODO: unhardcode (already in model but deserializedObject.save() bypasses model-defined save()
            obj.save()
        return HttpResponse("Ok")
    return HttpResponse("Pas Ok")


