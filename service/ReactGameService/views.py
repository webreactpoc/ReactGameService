from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseServerError, HttpResponse
from .models import *
from django.core import serializers
import json 

from django.views.decorators.csrf import csrf_exempt # TODO REMOVE THIS

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

@csrf_exempt#TODO REMOVE THIS AND SECURE ENDPOINT
def POST_test(request):
    return singularPostRequest(request,Test)

@csrf_exempt#TODO REMOVE THIS AND SECURE ENDPOINT
def POST_testee(request):
    return singularPostRequest(request,Attempt)

@csrf_exempt#TODO REMOVE THIS AND SECURE ENDPOINT
def POST_status(request):
    return singularPostRequest(request,Attempt)

@csrf_exempt#TODO REMOVE THIS AND SECURE ENDPOINT
def POST_organisation(request):
    return singularPostRequest(request,Attempt)
    
@csrf_exempt#TODO REMOVE THIS AND SECURE ENDPOINT
def POST_attempt(request):
    return singularPostRequest(request,Attempt)

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

def singularPostRequest(request,model):
    if request.method == "POST":
        json_data = json.loads(request.body)
    try:
        for i in json_data:
            model.createObject(0)
        data = json_data[0]
        print(data)
    except KeyError:
        return HttpResponseServerError("Malformed json body")
    return HttpResponse("Ok")
        # for deserialized_object in serializers.deserialize("json", request.body):
        #      deserialized_object.save()