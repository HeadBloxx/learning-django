from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat

import json

def missing_data():
    return JsonResponse({"error": "Missing data"}, status=400)
def invalid_json():
    return JsonResponse({"error": "Invalid JSON"}, status=400)

def ajax_request(request):
    if request.method == "POST":
            try:
                data = json.loads(request.body)
                message = data.message
                if not message:
                    return missing_data()
                if len(message) <= 0 or len(message) > 1000:
                    return JsonResponse({"error": "Message too long"}, status=400)
                
                new_chat = Chat(text=message)
                new_chat.save()
                return JsonResponse({"message": "success"})
            except:
                return invalid_json()
    elif request.method == "GET":
        try:
            starting_iteration = request.GET.get("last_id")
            if starting_iteration is None or not isinstance(starting_iteration, int) or starting_iteration < 1:
                return missing_data()
            
            return_payload = []
            all_chats = Chat.objects.all()
            for i in range(starting_iteration, all_chats.count()): # i essentially acts as the id here, since the chat model automatically sorts itself by id
                return_payload.append(Chat.objects.get(i))

            return JsonResponse({"payload": return_payload})
        except:
            return invalid_json()
        return JsonResponse({"error": "Invalid request"}, status=400)

# ------------------------------------- VIEWS ------------------------------------- #
def general(request):
    if request.is_ajax():
        return ajax_request()
    return render(request, "chat/general.html")