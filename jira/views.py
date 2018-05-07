from django.http import HttpResponse
from django.http import JsonResponse
import json

def saveToFile(request):
	print('RECEIVED REQUEST: ' + request.method)
	""" logic to save the keywords to new file, which in turn will be picked by JIRA runner to get proper data"""
	if request.method == 'POST':
		received_json_data = json.loads(request.body.decode('utf-8'))
		if 'text' in received_json_data :
			print('***********Received Text********* '+ received_json_data['text'])
			message = received_json_data['text']
			text_file = open("C://python//SearchJira.txt", "a")
			text_file.write("- - %s" % message +"\n")
			text_file.close()
		print('Chatbot : ', 'Thank you for the inputs. We will initiate the serach. Please search again after few minutes.')
		return JsonResponse({'text':'Thank you for the inputs. We will initiate the serach. Please search again after few minutes.'}) 
	else: #GET
		return HttpResponse("Get method not supported")
