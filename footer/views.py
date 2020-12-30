from django.shortcuts import render
from .forms import ContactForm
from django.http import JsonResponse
from .models import Facts
import random
# Create your views here.

def contact(request):

	if request.method == 'POST':
		form = ContactForm(request.POST)
		if form.is_valid():
			form.save()
			message = "Your Message/Feedback is sent, manager@nccbuddies will contact you soon. Thank You."
			return render(request,'footer/contact.html',{'message':message})
	else:
		form = ContactForm()
		context = {'form':form}
		return render(request,'footer/contact.html',context)

def contribute(request):
	return render(request,'footer/contribute.html')

def sponsor(request):
	return render(request,'footer/sponsor.html')

def guidelines(request):
	return render(request,'footer/guidelines.html')

def about(request):
	return render(request,'footer/about.html')

def facts(request):
	facts = Facts.objects.all()
	facts_list = []
	for fact in facts:
		facts_list.append(fact.fact)
	random_facts = random.sample(facts_list, 3)
	data = {

		'facts':random_facts

	}
	return JsonResponse(data)
	

def error_404_view(request,exception):
	return render(request,'footer/404.html')