from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission

templater = get_renderer('product')


#############################
@view_function
#@permission_required('home.is_agent',login_url='/home/login/')
def process_request(request):
	params = {}

	products = hmod.SerializedProduct.objects.all()
	product_infos = hmod.ProductSpecification.objects.all()
	
	print(products)
	print(product_infos)
	params['product_infos'] = product_infos
	params['products'] = products

	return templater.render_to_response(request, 'items.html', params)

#############################
@view_function
def rentable(request):
	params = {}

	products = hmod.RentableProduct.objects.all()
	product_infos = hmod.ProductSpecification.objects.all()
	
	print(products)
	print(product_infos)
	params['product_infos'] = product_infos
	params['products'] = products

	return templater.render_to_response(request, 'items.rentable_ajax.html', params)
		
	
#############################
@view_function
def wardrobe(request):
	params = {}

	products = hmod.WardrobeItem.objects.all()
	product_infos = hmod.ProductSpecification.objects.all()
	
	print(products)
	print(product_infos)
	params['product_infos'] = product_infos
	params['products'] = products

	return templater.render_to_response(request, 'items.wardrobe_ajax.html', params)
	
#############################
@view_function
def non_rentable(request):
	params = {}

	products = hmod.SerializedProduct.objects.all()
	product_infos = hmod.ProductSpecification.objects.all()
	
	print(products)
	print(product_infos)
	params['product_infos'] = product_infos
	params['products'] = products

	return templater.render_to_response(request, 'items.non_rentable_ajax.html', params)


#############################Edit
@view_function
@permission_required('home.is_agent',login_url='/home/items/')
def edit_rentable(request):

	params = {}
	print(request.urlparams[0])

	try:
		item = hmod.RentableProduct.objects.get(id=request.urlparams[0])
	except hmod.Item.DoesNotExist:
		return HttpResponseRedirect('/home/items/')

	form = RentableItemEditForm(initial={
		'name' : item.name,
		'description': item.description,
		'value': item.value,
		'standard_rental_price' : item.standard_rental_price,
		'rentable' : item.rentable,
		'size' : item.size,
		'size_modifier' : item.size_modifier,
		'gender' : item.gender,
		'color' : item.color,
		'pattern' : item.pattern,
		'start_year' : item.start_year,
		'end_year' : item.end_year,
		'note' : item.note})

	if request.method == "POST":
		form = RentableItemEditForm(request.POST)
		if form.is_valid():
			item.name = form.cleaned_data['name']
			item.description = form.cleaned_data['description']
			item.value = form.cleaned_data['value']
			item.standard_rental_price = form.cleaned_data['standard_rental_price']
			item.rentable = form.cleaned_data['rentable']
			item.size = form.cleaned_data['size']
			item.size_modifier = form.cleaned_data['size_modifier']
			item.gender = form.cleaned_data['gender']
			item.color = form.cleaned_data['color']
			item.pattern = form.cleaned_data['pattern']
			item.start_year = form.cleaned_data['start_year']
			item.end_year = form.cleaned_data['end_year']
			item.note = form.cleaned_data['note']

			item.save()

			return HttpResponseRedirect('/home/items/')

	params['form'] = form
	params['item'] = item

	return templater.render_to_response(request, 'items.edit.html', params)

class RentableItemEditForm(forms.Form):

	name = forms.CharField(label='Name', required=True)
	description = forms.CharField(label='Description', required=False)
	value = forms.IntegerField(label='Value', required=True)
	standard_rental_price = forms.IntegerField(label='Standard Rental Price', required=False)
	rentable = forms.BooleanField(label='Rentable', required=False)
	size = forms.DecimalField(label='Size', required=False)
	size_modifier = forms.DecimalField(label='Modifier', required=False)
	gender = forms.CharField(label='Gender', required=False)
	color = forms.CharField(label='Color', required=False)
	pattern = forms.CharField(label='Pattern', required=False)
	start_year = forms.DateField(label='Start Year', required=False)
	end_year = forms.DateField(label='End Year', required=False)
	note = forms.CharField(label='Notes', required=False)

############################Create
@view_function
@permission_required('home.is_manager',login_url='/home/items/')
def create_rentable(request):
	'''create a new item'''
	item = hmod.Item()
	item.name = ''
	item.description = ''
	item.value = 0
	item.standard_rental_price = 0
	item.rentable = ''
	item.size = 0.0
	item.size_modifier = 0.0
	item.gender = ''
	item.color = ''
	item.pattern = ''
	item.start_year = '1111-11-11'
	item.end_year = '1111-11-11'
	item.note =''
	item.save()

	return HttpResponseRedirect('/home/items.edit_rentable/{}/'.format(item.id))

###########################Delete
@view_function
@permission_required('home.is_manager',login_url='/home/items/')
def delete(request):
	'''Deletes a new item'''
	try:
		item = hmod.StockedProduct.objects.get(id=request.urlparams[0])
		item_info = hmod.Product_Specification.objects.get(id=item.product_specification_id)
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/home/items/')

	item.delete()
	item_info.delete()

	return HttpResponseRedirect('/home/items/')
	
	
	
	
	
	
	
	
	
	
	
	
	
	
	