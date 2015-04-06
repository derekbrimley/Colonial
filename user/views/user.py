from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as vmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
import psycopg2
import psycopg2.extras
import sys
import random

#This chooses the app
templater = get_renderer('user')


#List Users
@view_function
#This permission required will allow managers and agents to access
#@permission_required('home.agent', login_url='/home/index')
def process_request(request):

	if request.user.is_authenticated():
		if request.user.has_perm('home.agent'):
			#Conans pretty code to figure out the users permissions
			# for group in request.user.groups.all():
			# 	print('>>>', group)
			# 	for perm in group.permissions.all():
			# 		print(perm)
			# print('<<<', request.user.has_perm('admin.is_manager'))
			# print(request.user.get_all_permissions())

			params = {}
			users = vmod.User.objects.all().order_by('id')
			addresses = vmod.Address.objects.all()
			photos = vmod.Photograph.objects.all()

			params['users'] = users
			params['addresses'] = addresses
			params['photos'] = photos

			# #Connect to database and run query returning the info needed. Pass to params
			# con = psycopg2.connect("dbname='colonial' user='postgres' password='kevntseeg'")
			# cur = con.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) 
			# cur.execute("SELECT home_user.id, home_user.email, home_user.phone, home_user.last_name, home_user.first_name, home_user.username, home_address.zip,home_address.address1 FROM home_user JOIN home_address ON home_user.address_id = home_address.id")
			# users = cur.fetchall()
			# print(users)

			return templater.render_to_response(request, 'user.html', params)

		#A customer on the site. Show their account
		else:
			params = {}

			#Get the user object and the address for the user
			try:
				user_object = vmod.User.objects.get(id=request.user.id)
				address_object = vmod.Address.objects.get(id=request.user.address_id)

				#Pass as params
				params['users'] = user_object
				params['addresses'] = address_object

				#params['user', 'address'] = users

				return templater.render_to_response(request, 'user.html', params)

			except:
				return HttpResponseRedirect('/home/login')

	#Not a user on the site. Redirect
	else:
		return HttpResponseRedirect('/home/login')



#Edit
@view_function
#This permission required will allow managers and agents to see this edit page
@permission_required('home.agent',login_url='/home/login/')
def edit(request):

	params = {}
	# #Connect to database and run query returning the info needed. Pass to params
	# con = psycopg2.connect("dbname='colonial' user='postgres' password='kevntseeg'")
	# cur = con.cursor(cursor_factory=psycopg2.extras.NamedTupleCursor) 
	# cur.execute("SELECT home_address.id FROM home_user JOIN home_address ON home_user.address_id = home_address.id WHERE home_user.id = %s" % (request.urlparams[0]))
	# request_address = cur.fetchone()
	# print(request_address.id)
	print('>>>>>>>>>>>>>>>>>>', request.urlparams[0])

	#Get the user object and the address for the user
	try:
		users = vmod.User.objects.get(id=request.urlparams[0])
		address = vmod.Address.objects.get(id=users.address_id)
		print('>>>>>>>>>>>>>>>>>>', users.username)

	except vmod.User.DoesNotExist:
		return HttpResponseRedirect('user.html')


	form = UserEditForm(initial={
		'username' : users.username,
		'first_name': users.first_name,
		'last_name': users.last_name,
		'email' : users.email,
		'phone' : users.phone,
		'address1' : address.address1,
		'address2' : address.address2,
		'city' : address.city,
		'state' : address.state,
		'zip' : address.zip,
		'organization_name' : users.organization_name,
		'organization_type' : users.organization_type,
		'bio_sketch': users.bio_sketch,
		'emergency_contact': users.emergency_contact,
		'emergency_phone': users.emergency_phone,
		'emergency_relationship': users.emergency_relationship})

	if request.method == "POST":
		form = UserEditForm(request.POST)
		if form.is_valid():
			users.username = form.cleaned_data['username']
			users.first_name = form.cleaned_data['first_name']
			users.last_name = form.cleaned_data['last_name']
			users.email = form.cleaned_data['email']
			users.phone = form.cleaned_data['phone']
			address.address1 = form.cleaned_data['address1']
			address.address2 = form.cleaned_data['address2']
			address.city = form.cleaned_data['city']
			address.state = form.cleaned_data['state']
			address.zip = form.cleaned_data['zip']
			users.organization_name = form.cleaned_data['organization_name']
			users.organization_type = form.cleaned_data['organization_type']
			users.bio_sketch = form.cleaned_data['bio_sketch']
			users.emergency_contact = form.cleaned_data['emergency_contact']
			users.emergency_phone = form.cleaned_data['emergency_phone']
			users.emergency_relationship = form.cleaned_data['emergency_relationship']

			users.save()
			address.save()

			return HttpResponseRedirect('/user/user')

	params['form'] = form
	params['users'] = users

	return templater.render_to_response(request, 'user.edit.html', params)



#User Edit Form
class UserEditForm(forms.Form):
	username = forms.CharField(label="Username", required=True, max_length=30)
	first_name = forms.CharField(label="First", required=True, max_length=100)
	last_name = forms.CharField(label="Last", required=True, max_length=100)
	email = forms.CharField(label="Email", required=True, max_length=100)
	phone = forms.CharField(label="Phone", required=True, max_length=100)
	address1 = forms.CharField(label="Address", required=True, max_length=100)
	address2 = forms.CharField(label="Address", required=False, max_length=100)
	city = forms.CharField(label='City', required=True, max_length=100)
	state = forms.CharField(label='State', required=True, max_length=100)
	zip = forms.CharField(label='Zip', required=True, max_length=100)
	organization_name = forms.CharField(label='Organization Name', required=False, max_length=100)
	organization_type = forms.CharField(label='Organization Type', required=False, max_length=100)
	bio_sketch = forms.CharField(label='Bio Sketch', required=False, max_length=200)
	emergency_contact = forms.CharField(label='Emergency Contact', required=False, max_length=100)
	emergency_phone = forms.CharField(label='Emergency Phone', required=False, max_length=14)
	emergency_relationship = forms.CharField(label='Emergency Relationship', required=False, max_length=100)



#Edit Self
@view_function
def editself(request):
	params = {}
	print(request.urlparams[0])

	#Get the user object and the address for the user
	try:
		user = vmod.User.objects.get(id=request.user.id)
		address = vmod.Address.objects.get(id=request.user.address_id)

	except vmod.User.DoesNotExist:

		return HttpResponseRedirect('user.html')

	form = UserEditForm(initial={
		'username' : user.username,
		'first_name': user.first_name,
		'last_name': user.last_name,
		'email' : user.email,
		'phone' : user.phone,
		'address1' : address.address1,
		'address2' : address.address2,
		'city' : address.city,
		'state' : address.state,
		'zip' : address.zip,
		'organization_name' : user.organization_name,
		'organization_type' : user.organization_type,
		'bio_sketch': user.bio_sketch,
		'emergency_contact': user.emergency_contact,
		'emergency_phone': user.emergency_phone,
		'emergency_relationship': user.emergency_relationship})

	if request.method == "POST":
		form = UserEditForm(request.POST)
		if form.is_valid():
			user.username = form.cleaned_data['username']
			user.first_name = form.cleaned_data['first_name']
			user.last_name = form.cleaned_data['last_name']
			user.email = form.cleaned_data['email']
			user.phone = form.cleaned_data['phone']
			address.address1 = form.cleaned_data['address1']
			address.address2 = form.cleaned_data['address2']
			address.city = form.cleaned_data['city']
			address.state = form.cleaned_data['state']
			address.zip = form.cleaned_data['zip']
			user.organization_name = form.cleaned_data['organization_name']
			user.organization_type = form.cleaned_data['organization_type']
			user.bio_sketch = form.cleaned_data['bio_sketch']
			user.emergency_contact = form.cleaned_data['emergency_contact']
			user.emergency_phone = form.cleaned_data['emergency_phone']
			user.emergency_relationship = form.cleaned_data['emergency_relationship']

			user.save()
			address.save()

			return HttpResponseRedirect('/user/user')

	params['form'] = form
	params['user'] = user

	return templater.render_to_response(request, 'user.edit.html', params)



#Create
@view_function
#This permission required will allow managers to create
@permission_required('home.manager',login_url='/user/user/')
def create(request):
	'''create a new user with address'''
	users = vmod.User()
	users.username = ''
	users.first_name = ''
	users.last_name = ''
	users.email = ''
	users.password = ''
	users.security_answer = 'to seek the holy grail'
	users.security_question = 'What is your quest?'
	users.address_id = 1
	users.save()

	return HttpResponseRedirect('/user/user.edit/{}/'.format(users.id))



#Delete
@view_function
#This permission required will allow managers to delete
@permission_required('home.manager',login_url='/user/user/')
def delete(request):
	'''Deletes a user'''
	
	try:
		users = vmod.User.objects.get(id=request.urlparams[0])
	except:
		return HttpResponseRedirect('user.html')

	users.delete()

	return HttpResponseRedirect('/user/user')



#Change Password
@view_function
def changepassword(request):
	params = {}
	print(request.urlparams[0])

	try:
		users = vmod.User.objects.get(id=request.urlparams[0])

	except vmod.User.DoesNotExist:

		return HttpResponseRedirect('/user/user')

	form = PasswordEditForm(initial={
		'password' : "password"})
	
	form.users = users

	if request.method == "POST":
		form = PasswordEditForm(request.POST)
		form.users = users
		if form.is_valid():
			users.set_password(form.cleaned_data['password'])
			users.save()

			return HttpResponseRedirect('/user/passwordchanged/')

	params['form'] = form
	params['users'] = users

	return templater.render_to_response(request, 'changepassword.html', params)



#Password Edit Form
class PasswordEditForm(forms.Form):
	security_answer = forms.CharField(label="Answer", required=True, max_length=200)
	password = forms.CharField(label="New Password", required=True, max_length=30)

##Checks to see if the security answer matches the stored answer
	def clean_security_answer(self):
		if self.cleaned_data['security_answer'] != self.users.security_answer:
			raise forms.ValidationError('Answer is incorrect')

		return self.cleaned_data['security_answer']



##This checks to see if the username is already taken
##New username is compared against all the existing usernames
##If no matches are found, excluding the existing username, returns '1' for postive
@view_function
def check_username(request):

	#Gets the current username and the new username
	username = request.REQUEST.get('username')
	current_username = request.REQUEST.get('current_username')
	print('>>>>>>>NEW', username)
	print('>>>>>>>CURRENT', current_username)

	users = vmod.User.objects.all().order_by('id')
	
	for item in users:
		print(item.username)
		if item.username == username:
			print("MATCH @ " + item.username +" & " + username)
			if item.username == current_username:
				print("VALID")
				return HttpResponse("1")
			else:
				print("INVALID")
				return HttpResponse("0")
	
	return HttpResponse("1")




