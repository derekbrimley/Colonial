from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as imod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission

templater = get_renderer('home')


#############################Orders
@view_function
@permission_required('home.is_customer',login_url='/home/orders/')
def process_request(request):
	params = {}

	orders = imod.Order.objects.all().order_by('order_date')

	params['orders'] = orders

	return templater.render_to_response(request, 'orders.html', params)



#############################Edit
@view_function
@permission_required('home.is_customer',login_url='/home/orders/')
def edit(request):

	params = {}
	print(request.urlparams[0])

	try:
		order = imod.Order.objects.get(id=request.urlparams[0])

	except imod.Order.DoesNotExist:

		return HttpResponseRedirect('/home/orders/')



	form = orderEditForm(initial={
		'order_date' : order.order_date,
		'phone': order.phone,
		'date_packed': order.date_packed,
		'date_paid' : order.date_paid,
		'date_shipped' : order.date_shipped,
		'tracking_number' : order.tracking_number})

	if request.method == "POST":
		form = orderEditForm(request.POST)
		if form.is_valid():
			order.order_date = form.cleaned_data['order_date']
			order.phone = form.cleaned_data['phone']
			order.date_packed = form.cleaned_data['date_packed']
			order.date_paid = form.cleaned_data['date_paid']
			order.date_shipped = form.cleaned_data['date_shipped']
			order.tracking_number = form.cleaned_data['tracking_number']
			
			order.save()

			return HttpResponseRedirect('/home/orders/')



	params['form'] = form
	params['order'] = order

	return templater.render_to_response(request, 'orders.edit.html', params)

class orderEditForm(forms.Form):

	order_date = forms.CharField(label='Order Date', required=True)
	phone = forms.CharField(label='Phone', required=False)
	date_packed = forms.CharField(label='Packed', required=False)
	date_paid = forms.CharField(label='Paid', required=False)
	date_shipped = forms.CharField(label='Shipped', required=False)
	tracking_number = forms.CharField(label='Tracking Number', required=False)
	


#############################Create
@view_function
@permission_required('home.is_customer',login_url='/home/orders/')
def create(request):
	'''create a new order'''
	order = imod.Order()
	order.order_date = '2015-1-1'
	order.phone = '801-123-4567'
	order.date_packed = '2015-1-1'
	order.date_paid = '2015-1-1'
	order.date_shipped = '2015-1-1'
	order.tracking_number = 1000
	
	order.save()

	return HttpResponseRedirect('/home/orders.edit/{}/'.format(order.id))



#############################Delete
@view_function
@permission_required('home.is_agent',login_url='/home/orders/')
def delete(request):
	'''Deletes a new order'''
	
	try:
		order = imod.Order.objects.get(id=request.urlparams[0])
	except imod.DoesNotExist:
		return HttpResponseRedirect('/home/orders/')

	order.delete()

	return HttpResponseRedirect('/home/orders/')