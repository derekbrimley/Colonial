from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as vmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
import random

templater = get_renderer('user')

# #Process Request/Not needed?
# @view_function
# def process_request(request):

# 	params = {}

# 	#This brings in the form created below.
# 	form = UserJoinForm()

# 	params['form'] = form

# 	return templater.render_to_response(request, 'join.joinform.html', params)




#Join Form
@view_function
def joinform(request):

	params = {}

	#This brings in the form created below.
	form = UserJoinForm()

	#When I call this funtion as a POST run this. Otherwise, skip to below
	if request.method == "POST":
		form = UserJoinForm(request.POST)
		print("Before Valid")
		if form.is_valid():
			print("After Valid")

			#Create the user
			user = vmod.User()

			address = vmod.Address()
			address.address1 = ''
			address.city = ''
			address.state = ''
			address.zip = '12345'
			address.save()
			address_id = address.id

	
			user.address_id = address_id

			#Use the form data as the attributes
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.security_question = form.cleaned_data['security_question']
			user.security_answer = form.cleaned_data['security_answer']
			user.set_password(form.cleaned_data['password'])
			#Save the user	
			user.save()

			return templater.render_to_response(request, 'join.thankyou.html', params)
		else:
			print("Form Not Valid")



	params['form'] = form

	return templater.render_to_response(request, 'join.joinform.html', params)




class UserJoinForm(forms.Form):
	username = forms.CharField(label="Username", required=True, max_length=30)
	first_name = forms.CharField(label="First", required=True, max_length=100)
	last_name = forms.CharField(label="Last", required=True, max_length=100)
	email = forms.CharField(label="Email", required=True, max_length=100)
	security_question = forms.CharField(label="Security Question", required=True, max_length=100)
	security_answer = forms.CharField(label="Security Answer", required=True, max_length=100)
	password = forms.CharField(label="Password", required=True, max_length=100)



@view_function
def check_username(request):

	#Gets the new username
	username = request.REQUEST.get('username')
	print('>>>>>>>NEW', username)

	users = vmod.User.objects.all().order_by('id')
	
	for item in users:
		if item.username == username:
			print("INVALID @ " + item.username +" & " + username)
			return HttpResponse("0")
		else:
			print("VALID")
			return HttpResponse("1")



		
	return HttpResponse("0")



#Thank You
@view_function
def thankyou(request):

	return templater.render_to_response(request, 'join.thankyou.html', params)