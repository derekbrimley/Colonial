from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
import requests
from django.core.mail import send_mail

templater = get_renderer('product')


#Shopping cart
@view_function
def process_request(request):
    params = {}

    #Get all the photos, they will be passed as a param and loaded into the shopping cart
    photos = hmod.Photograph.objects.all()

    cart = request.session.get('cart', {})

    total_price = 0

    #Create a cart list
    cart_list = []

    #Put the products from all the 
    for productid in cart:
        product = hmod.ProductSpecification.objects.get(id=productid)

        quantity = cart.get(productid)
        price = int(product.price) * int(quantity)
        total_price += price
        cart_list.append(product)


    params = {
        'cart' : cart,
        'cart_list': cart_list,
        'photos': photos,
        'total_price': total_price
    }



    #Get the items in the shopping cart in an ajax ($.loadmodal dialog)
    #Just shows the shopping cart

    return templater.render_to_response(request, 'shopping_cart.html', params)



#Add to cart
@view_function
def add(request):
	#This gets called by the add_button and these are the params on the url
    #'/product/shopping_cart.add/' + photo_id + "/" + product_id + "/" + qty + "/",
    #/photo[0]/product[1]/qty[2]


    #Add item to cart
    photo_id = request.urlparams[0]
    product_id = request.urlparams[1]
    qty = request.urlparams[2]

    cart = request.session.get('cart', {})
    rcart = request.session.get('rental_cart', {})
    print("cart",cart)
    print("rcart",rcart)

    try:
        keys = request.session['cart'].keys()
        if product_id not in keys:
            cart[product_id] = qty
            request.session['cart'] = cart
        else:
            value = cart.get(product_id)
            new_qty = int(value) + int(qty) 
            cart[product_id] = new_qty
            request.session['cart'] = cart
    except:
        cart[product_id] = qty
        request.session['cart'] = cart

    return HttpResponseRedirect('/product/shopping_cart/')



@view_function
def delete(request):
    #This is called by the delete button in shopping_cart.html
    #Params [0]=$(this).attr('data-product_id') + "/",
    
    #Get cart object
    cart = request.session.get('cart', {})

    #Get the product id of the product we are deleting from the cart
    product_id = request.urlparams[0]

    if product_id in cart:

        del cart[product_id]

    request.session['cart'] = cart

    #Return to view the cart (reload the modal)
    return HttpResponseRedirect('/product/shopping_cart/')


#Check out shoppingcart
@view_function
def checkout(request):
    #This gets called by the checkout_button and these are the params on the url
    #"/product/shopping_cart.checkout/${total_price}/ request.user.id"
    #/totalprice= [0]

    total_cost = request.urlparams[0]
    user = hmod.User.objects.get(id=request.urlparams[1])

    params = {}
    
    params['total_cost'] = total_cost
    params['user'] = user

    return templater.render_to_response(request, 'checkout.html', params)


#Submit Payment cart
@view_function
def purchase(request):
    #This gets called by the checkout_button and these are the params on the url
    #"/product/shopping_cart.checkout/${total_price}/"
    #/totalprice= [0]
    
    params = {}
    total = request.urlparams[0]
    params['total'] = total
    print(">>>>>>Total Cost: ",request.urlparams[0])

    ##Conan Code from March 24
    #Send the request with the data
    API_URL = 'http://dithers.cs.byu.edu/iscore/api/v1/charges'
    API_KEY = '477070d45ad5ea0bd7b060d2243c4fdf'

    r = requests.post(API_URL, data={
        'apiKey': API_KEY,
        'currency': 'USD',
        'amount': request.urlparams[0],
        'type': 'Visa',
        'number': '4732817300654',
        'exp_month': '10',
        'exp_year': '15',
        'cvc': '411',
        'name': 'Cosmo Limesandal',
        'description': 'Charge for Cosmo',
    })

    #Print response
    print(r.text)

    #Parse the response to a dictionary
    resp = r.json()

    if 'error' in resp: #error?
        print('ERROR: ', resp['error'])

    else:
        print(resp.keys())
        print(resp['ID'])


    # params['ID'] = resp['ID']
    # params['Amount'] = resp['Amount']
    # params['Date'] = resp['Date']
    # params['Description'] = resp['Description']

    params['resp'] = resp

    cart = request.session.get('cart', {})
    print(cart.keys())

    ##Email Receipt
    subject = "Colonial Heritage Foundation Receipt"
    message = "Dear " + request.user.first_name + " " + request.user.last_name + ",\n\n"

    message += "Thank you for your recent purchase:\n"
    message += "Date: "  + str(resp['Date'])
    message += "\nAmount: "  + str(resp['Amount'])

    message += "\n\n\nYour friends at Colonial!"

    send_mail( subject , message, 'group13chf@gmail.com',
    ['group13chf@gmail.com'], fail_silently=False)


    return templater.render_to_response(request, 'payment_receipt.html', params)


































##Conans code--cant get it to work
	#If the cart is not created, create it
	# if 'shopping_cart' not in request.session:
	# 	request.session['shopping_cart'] = {}
	# 	print('Shopping cart was not in session, It is now created')

	# #If/else checks if existing, then adds
	# if photo_id not in request.session['shopping_cart']:
	# 	request.session['shopping_cart'][photo_id] += qty
	# else:
	# 	print(qty)
	# 	request.session['shopping_cart'][photo_id] += qty

	# print('>>>>>>>Add in SC', request.session['shopping_cart'])

	# if product.id in request.session['shopping_cart']:
	# 	request.session['shopping_cart'][product.id] += 1
	# else:
	# 	request.session['shopping_cart'][product.id] = 1

	# params = {}

    



