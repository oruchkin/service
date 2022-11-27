from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Room, Request
from django.http import HttpResponse

# Create your views here.

ROOM_PAGE_SIZE = 100

def index(request):
    return render(request, 'request/index.html')


@csrf_exempt
def room(request, room):
    if request.method == "GET":
        room_obj, _ = Room.objects.get_or_create(number = room)
        room_requests = Request.objects.filter(room=room_obj).order_by("-pk")
        return render(request, 'request/room.html',{
            "room":room_obj,
            "room_requests":room_requests,
        })
    
    elif request.method == "POST":
        room_obj, _ = Room.objects.get_or_create(number = room)
        data = request.POST
        post_data = {}
        if len(data) > 0:
            for i in data:
                post_data[i] = data[i]
        headers = {} 
        for i in request.headers:
            headers[i] = request.headers[i]
        new_request = Request(room=room_obj,
                              json_data = post_data,
                              headers = headers)
        new_request.save()
        room_requests = Request.objects.filter(room=room_obj)
        if len(room_requests) > ROOM_PAGE_SIZE:
            delete_me = room_requests[ROOM_PAGE_SIZE+1]
            delete_me.delete()

        return HttpResponse("ok", content_type="text/plain")