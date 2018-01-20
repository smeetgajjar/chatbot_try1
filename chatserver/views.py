from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import chats
import random
import string

def generate_chat_id(N):
	return ''.join(random.SystemRandom().choice(string.ascii_uppercase + string.digits) for _ in range(N))

@csrf_exempt
def index(request):

	reply = 'hi'
	print("request is " + str(request.POST))

	if request.POST:

		if 'chat_id' in request.POST:

			print("creating new chat obj")
			chat = chats(chat_id = request.POST['chat_id'], text = request.POST['client_msg'])
			chat.save()
			return JsonResponse({'reply': reply})

		else: 
			#this is the start of the conversation, generate and send a new chat_id
			chat_id = generate_chat_id(30)
			print(chat_id)
			return JsonResponse({'chat_id':chat_id, 'reply': reply})

	return HttpResponse(status=400)