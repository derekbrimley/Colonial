from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as vmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission

templater = get_renderer('product')

#This is called from the base.htm link

#Products
@view_function
#@permission_required('home.is_agent',login_url='/home/login/')
def process_request(request):
	params = {}

	#Pull photo graph and product information, order by id
	photographs = vmod.Photograph.objects.all().order_by('id')
	products = vmod.ProductSpecification.objects.all().order_by('id')

	#Fill the params with the objects, we will send them to the webpage
	params['photographs'] = photographs
	params['products'] = products


	# request.session['shopping_cart'] = 'Shopping Cart'
	# print(request.session)

	return templater.render_to_response(request, 'products.html', params)


#Detail
@view_function
def detail(request):
	#Params passed to this def by products.html
	#"/product/products.detail/${ product.id }/${ photo.id }"
	#Product @@ request.urlparams[0]
	#Photo @@ request.urlparams[1]

	params = {}
	product = vmod.ProductSpecification.objects.get(id=request.urlparams[0])
	photo = vmod.Photograph.objects.get(id=request.urlparams[1])

	params['product'] = product
	params['photo'] = photo


	return templater.render_to_response(request, 'products.detail.html', params)


#Search
@view_function
def search(request):
    #Params passed to this def by products.js
    #/product/products.search/" input "/","
    #Search Input @@ data dictionary where input = search

    params = {}
    #This is the contents currently in the search box
    search = request.REQUEST.get('input')
    search_string = search.lower()
    print('s>>>>>>>>>>>>>>>>>>>>>>>',search_string)


    #Pull photo graph and product information, order by id
    photographs = vmod.Photograph.objects.all().order_by('id')
    products = vmod.ProductSpecification.objects.all().order_by('id')

    #This array will have the products search for
    search_products = []
    search_photos = []

    for product in products:
        product_name = product.name.lower()
        if search_string in product_name:
            print('Product name: ', product.name)

            #Get the product object and then add it in the list
            product_object = vmod.ProductSpecification.objects.get(id=product.id)
            search_products.append(product_object)

            #Get the photo object and then add it in the list
            photo_object = vmod.Photograph.objects.get(id=product.id)
            search_photos.append(photo_object)

        else:
            print(search_string,' not in', product.name)

    print('>>>>',search_products)
    print('>>>>',search_photos)

    #Fill the params with the objects, we will send them to the webpage
    params['photographs'] = search_photos
    params['products'] = search_products

    ##return HttpResponseRedirect('/product/product.search/{}', params)
    return templater.render_to_response(request, '/product.search.html/', params)
    ##return HttpResponse('Hey Hey')
































# #############################Edit
# @view_function
# @permission_required('home.is_agent',login_url='/home/products/')
# def edit(request):

# 	params = {}
# 	print(request.urlparams[0])

# 	try:
# 		product = imod.Product.objects.get(id=request.urlparams[0])

# 	except imod.product.DoesNotExist:

# 		return HttpResponseRedirect('/home/products/')



# 	form = productEditForm(initial={
# 		'name' : product.name,
# 		'description': product.description,
# 		'category': product.category,
# 		'current_price' : product.current_price,
# 		'is_bulk' : product.is_bulk,
# 		'is_custom' : product.is_custom,
# 		'is_individual' : product.is_individual})

# 	if request.method == "POST":
# 		form = productEditForm(request.POST)
# 		if form.is_valid():
# 			product.name = form.cleaned_data['name']
# 			product.description = form.cleaned_data['description']
# 			product.category = form.cleaned_data['category']
# 			product.current_price = form.cleaned_data['current_price']
# 			product.is_bulk = form.cleaned_data['is_bulk']
# 			product.is_custom = form.cleaned_data['is_custom']
# 			product.is_individual = form.cleaned_data['is_individual']
			
# 			product.save()

# 			return HttpResponseRedirect('/home/products/')



# 	params['form'] = form
# 	params['product'] = product

# 	return templater.render_to_response(request, 'products.edit.html', params)




# class productEditForm(forms.Form):

# 	name = forms.CharField(label='Name', required=True)
# 	description = forms.CharField(label='Description', required=False)
# 	category = forms.CharField(label='Category', required=True)
	
# 	current_price = forms.DecimalField(label='Current Price', required=False)
	
# 	is_bulk = forms.BooleanField(label='Bulk?', required=False)
# 	is_custom = forms.BooleanField(label='Custom?', required=False)
# 	is_individual = forms.BooleanField(label='Individual?', required=False)
	


# #############################Create
# @view_function
# @permission_required('home.is_manager',login_url='/home/products/')
# def create(request):
# 	'''create a new product'''
# 	product = imod.Product()
# 	product.name = ''
# 	product.description = ''
# 	product.category = 0
	
# 	product.current_price = 0.0
	
# 	product.is_bulk = ''
# 	product.is_custom = ''
# 	product.is_individual = ''
	
# 	product.save()


# 	return HttpResponseRedirect('/home/products.edit/{}/'.format(product.id))




# #############################Delete
# @view_function
# @permission_required('home.is_manager',login_url='/home/products/')
# def delete(request):
# 	'''Deletes a new product'''

# 	try:
# 		product = imod.Product.objects.get(id=request.urlparams[0])
# 	except imod.DoesNotExist:
# 		return HttpResponseRedirect('/home/products/')

# 	product.delete()

# 	return HttpResponseRedirect('/home/products/')