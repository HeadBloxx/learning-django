from django.shortcuts import render
from django.http import JsonResponse
from .models import Chat
from django.core import serializers
import json

def missing_data():
    return JsonResponse({"error": "Missing data"}, status=400)

def invalid_json():
    return JsonResponse({"error": "Invalid JSON"}, status=400)

def ajax_request(request):
    print('ajax')
    if request.method == "POST":
        print('post')
        try:
            data = json.loads(request.body)
            message = data.get("message")  # Use .get() to prevent KeyError
            if not message:
                return missing_data()
            if len(message) <= 0 or len(message) > 1000:
                return JsonResponse({"error": "Message too long"}, status=400)

            new_chat = Chat(text=message)
            new_chat.save()
            return JsonResponse({"message": "success"})
        except json.JSONDecodeError:
            return invalid_json()
    
    elif request.method == "GET":
        print('get')
        try:
            starting_iteration = request.GET.get("last_id")
            if not starting_iteration:
                return missing_data()
            
            try:
                starting_iteration = int(starting_iteration)
            except ValueError:
                return missing_data()
            
            if starting_iteration < 1:
                return missing_data()
            
            return_payload = []
            all_chats = Chat.objects.filter(id__gte=starting_iteration)
            for chat in all_chats:
                return_payload.append({
                    "text": chat.text,
                })
            print(return_payload)
            return JsonResponse({"payload": return_payload})
        except Exception:
            return invalid_json()

# ------------------------------------- VIEWS ------------------------------------- #
def general(request):
    if request.headers.get('X-Requested-With') == 'XMLHttpRequest':
        return ajax_request(request)
    else:
        print("not ajax")
    
    return render(request, "chat/general.html", {"messages": Chat.objects.all()})
