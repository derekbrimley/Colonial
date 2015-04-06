from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
from datetime import datetime
from datetime import timedelta
import requests
from django.core.mail import send_mail

templater = get_renderer('home')

#This is called from the tools.html run

#Products
@view_function
@permission_required('home.agent',login_url='/home/index/')
def process_request(request):
	

	return templater.render_to_response(request, 'overdue_items.html')



#Run batch for overdue
@view_function
@permission_required('home.agent',login_url='/home/index/')
def batch_30(request):
	#This function gets all the objects, and returns the overdue rentals to params
	
	params = {}

	
	#Get overdue rentals
	overdue_rentals = hmod.RentalItem.objects.filter(date_in=None)
	product_specs = hmod.ProductSpecification.objects.all()

	#Set current time
	current_date = datetime.now().date()

	
	overdue30 = [] #We will store rentals that are overdue30
	transactions = [] 
	customers = [] 

	for rental in overdue_rentals:
		rental_duedate = rental.date_due
		if rental.date_due < current_date:
			days_pastdue = current_date - rental_duedate
			calc_days = str(days_pastdue).split(' ')
			if int(calc_days[0]) < 60 and int(calc_days[0]) >=30:
				overdue30.append(rental)
				#Get the transaction for the rental
				transaction = hmod.Transaction.objects.get(id=rental.transaction_id)
				transactions.append(transaction)
				#Get the User assigned to that rental
				customer = hmod.User.objects.get(id=transaction.customer_id)
				#Put that customer in the the list associated with rentalid
				customers.append(customer)

	params = {
	'overdue' : overdue30,
	'customers' : customers,
	'product_specs' : product_specs,
	'transactions' : transactions,
	}

	print(">>>>>>>>>30", overdue30)
	print(">>>>>>>>>Customer", customers)

	return templater.render_to_response(request, 'overdue_ajax.html', params)



#Run batch for overdue
@view_function
@permission_required('home.agent',login_url='/home/index/')
def batch_60(request):
	#This function gets all the objects, and returns the overdue rentals to params
	
	params = {}

	
	#Get overdue rentals
	overdue_rentals = hmod.RentalItem.objects.filter(date_in=None)
	product_specs = hmod.ProductSpecification.objects.all()

	#Set current time
	current_date = datetime.now().date()

	
	overdue60 = [] #We will store rentals that are overdue60
	transactions = [] 
	customers = [] 

	for rental in overdue_rentals:
		rental_duedate = rental.date_due
		if rental.date_due < current_date:
			days_pastdue = current_date - rental_duedate
			calc_days = str(days_pastdue).split(' ')
			if int(calc_days[0]) < 90 and int(calc_days[0]) >=60:
				overdue60.append(rental)
				#Get the transaction for the rental
				transaction = hmod.Transaction.objects.get(id=rental.transaction_id)
				transactions.append(transaction)
				#Get the User assigned to that rental
				customer = hmod.User.objects.get(id=transaction.customer_id)
				#Put that customer in the the list associated with rentalid
				customers.append(customer)

	params = {
	'overdue' : overdue60,
	'customers' : customers,
	'product_specs' : product_specs,
	'transactions' : transactions,
	}

	print(">>>>>>>>>60", overdue60)
	print(">>>>>>>>>Customer", customers)

	return templater.render_to_response(request, 'overdue_ajax.html', params)



#Run batch for overdue
@view_function
@permission_required('home.agent',login_url='/home/index/')
def batch_90(request):
	#This function gets all the objects, and returns the overdue rentals to params
	
	params = {}

	
	#Get overdue rentals
	overdue_rentals = hmod.RentalItem.objects.filter(date_in=None)
	product_specs = hmod.ProductSpecification.objects.all()

	#Set current time
	current_date = datetime.now().date()

	
	overdue90 = [] #We will store rentals that are overdue90
	transactions = [] 
	customers = [] 

	for rental in overdue_rentals:
		rental_duedate = rental.date_due
		if rental.date_due < current_date:
			days_pastdue = current_date - rental_duedate
			calc_days = str(days_pastdue).split(' ')
			if int(calc_days[0]) >=90:
				overdue90.append(rental)
				#Get the transaction for the rental
				transaction = hmod.Transaction.objects.get(id=rental.transaction_id)
				transactions.append(transaction)
				#Get the User assigned to that rental
				customer = hmod.User.objects.get(id=transaction.customer_id)
				#Put that customer in the the list associated with rentalid
				customers.append(customer)

	params = {
	'overdue' : overdue90,
	'customers' : customers,
	'product_specs' : product_specs,
	'transactions' : transactions,
	}

	print(">>>>>>>>>90", overdue90)
	print(">>>>>>>>>Customer", customers)

	return templater.render_to_response(request, 'overdue_ajax.html', params)
   





@view_function
@permission_required('home.agent',login_url='/home/index/')
def overdue_email(request):
	#This function gets all the objects, and returns the overdue rentals to params
	
	##Email Notification
	subject = "Colonial Heritage Foundation Rental Return Reminder"

	message = "Please return your overdue items\n\n\nYour friends at Colonial!"
	
	params = {}
	
	#Get all rentals
	all_rentals = hmod.RentalItem.objects.all()

	#Set current time
	current_date = datetime.now().date()

	print(">>>THIS IS WHERE I AM")

	overdue_all = []


	for rental in all_rentals:
		if rental.date_in is None:
			item_due_date = rental.date_due
			if current_date > item_due_date:
				overdue_rental = hmod.RentalItem.objects.get(id=rental.id)
				overdue_all.append(overdue_rental)

	for overdue in overdue_all:
		transaction_id = overdue.transaction_id
		transaction = hmod.Transaction.objects.get(id=transaction_id)
		customer_id = transaction.customer_id
		customer = hmod.User.objects.get(id=customer_id)
		send_mail( subject , message, customer.email, ['group13chf@gmail.com'], fail_silently=False)
		print(">>>>Email: ", customer.email, overdue.id)
							

	return templater.render_to_response(request, 'overdue_ajax.html')