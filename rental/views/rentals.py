from django.conf import settings
from django import forms
from django.forms.formsets import formset_factory
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission
import time
from datetime import date
import decimal 


templater = get_renderer('rental')

#This is called from the base.htm link

#Rental
@view_function
def process_request(request):
	params = {}

	return templater.render_to_response(request, 'rentals.html', params)


#Add Customer
@view_function
#@permission_required('home.is_agent',login_url='/home/login/')
def add_customer(request):
	params = {}

	#Pull photo graph and product information, order by id
	photographs = hmod.Photograph.objects.all().order_by('id')
	users = hmod.User.objects.all().order_by('id')

	#Fill the params with the objects, we will send them to the webpage
	params['photographs'] = photographs
	params['users'] = users

	return templater.render_to_response(request, 'rentals.add_customer.html', params)

#Add Rentals
@view_function
#@permission_required('home.is_agent',login_url='/home/login/')
def add_rentals(request):
    #Params sent here from rentals.add_customer  user.id in [0]
    params = {}

    #Pull photo graph and product information, order by id
    photographs = hmod.Photograph.objects.all().order_by('id')
    rentable = hmod.RentableProduct.objects.all().order_by('id')
    wardrobe = hmod.WardrobeItem.objects.all().order_by('id')
    products = hmod.ProductSpecification.objects.all().order_by('id')
    customer = hmod.User.objects.get(id=request.urlparams[0])

    #Fill the params with the objects, we will send them to the webpage
    params['photographs'] = photographs
    params['rentable'] = rentable
    params['wardrobe'] = wardrobe
    params['products'] = products
    params['customer'] = customer

    return templater.render_to_response(request, 'rentals.add_rentals.html', params)

#View
@view_function
def view(request):
	#If I am a customer just show my rentals, if >= agent, show me all
	
	if request.user.has_perm('home.agent'):
		params = {}

		transactions = hmod.Transaction.objects.all()
		rentals = hmod.RentalItem.objects.all()
		products = hmod.ProductSpecification.objects.all()
		users = hmod.User.objects.all()
		fees = hmod.Fee.objects.all()
		
		params['transactions'] = transactions
		params['rentals'] = rentals
		params['products'] = products
		params['users'] = users
		params['fees'] = fees
		print(users)



		return templater.render_to_response(request, 'rentals.view.html', params)




	elif request.user.is_authenticated():
		params = {}

		transactions = hmod.Transaction.objects.filter(customer_id=request.user.id)
		rentals = hmod.RentalItem.objects.all()
		products = hmod.ProductSpecification.objects.all()
		fees = hmod.Fee.objects.all()

		print(request.user.id)
		
		params['transactions'] = transactions
		params['rentals'] = rentals
		params['products'] = products
		params['fees'] = fees


		return templater.render_to_response(request, 'rentals.view.html', params)


#Edit
@view_function
#This permission required will allow managers and agents to see this edit page
@permission_required('home.agent',login_url='/home/login/')
def edit(request):
	#rental/rentals.edit/${rental.id}/${transaction.id}/${user.id}/${product.id
	params = {}

	#Get params objects
	rental = hmod.RentalItem.objects.get(id=request.urlparams[0])
	transaction = hmod.Transaction.objects.get(id=request.urlparams[1])
	user = hmod.User.objects.get(id=request.urlparams[2])
	product = hmod.ProductSpecification.objects.get(id=request.urlparams[3])
	
	form = TransactionForm(initial={
		'date' : transaction.date,
		'date_packed' : transaction.date_packed,
		#'packed_by' : transaction.packed_by,
		'date_paid' : transaction.date_paid,
		#'payment_handler' : transaction.payment_handler,
		'date_shipped' : transaction.date_shipped,
		#'shipped_by' : transaction.shipped_by,
		'tracking_number' : transaction.tracking_number,
		#'ships_to' : transaction.ships_to,
		#'packed_by' : transaction.packed_by,
		#'payment_processed_by' : transaction.payment_processed_by,
		#'shipped_by' : transaction.shipped_by,
		#'handled_by' : transaction.handled_by,
		#'customer' : transaction.customer,
		'date_out' : rental.date_out,
		'date_in' : rental.date_in,
		'date_due' : rental.date_due,
		#'discount_percent' : rental.discount_percent,
		#'rentable_product' : rental.rentable_product,
		})

	if request.method == "POST":
		form = TransactionForm(request.POST)
		if form.is_valid():
			transaction.date = form.cleaned_data['date']
			transaction.date_packed = form.cleaned_data['date_packed']
			#transaction.packed_by = form.cleaned_data['packed_by']
			transaction.date_paid = form.cleaned_data['date_paid']
			#transaction.payment_handler = form.cleaned_data['payment_handler']
			transaction.date_shipped = form.cleaned_data['date_shipped']
			#transaction.shipped_by = form.cleaned_data['shipped_by']
			transaction.tracking_number = form.cleaned_data['tracking_number']
			#transaction.ships_to = form.cleaned_data['ships_to']
			#transaction.packed_by = form.cleaned_data['packed_by']
			#transaction.payment_processed_by = form.cleaned_data['payment_processed_by']
			#transaction.shipped_by = form.cleaned_data['shipped_by']
			#transaction.handled_by = form.cleaned_data['handled_by']
			#transaction.customer = form.cleaned_data['customer']
			rental.date_out = form.cleaned_data['date_out']
			rental.date_in = form.cleaned_data['date_in']
			rental.date_due = form.cleaned_data['date_due']
			#rental.discount_percent = form.cleaned_data['discount_percent']
			#rental.rentable_product = form.cleaned_data['rentable_product']

			transaction.save()
			rental.save()

			return HttpResponseRedirect('/rental/rentals.view')

	params['form'] = form
	params['rental'] = rental

	return templater.render_to_response(request, 'rentals.edit.html', params)

#Edit
@view_function
#This permission required will allow managers and agents to see this edit page
@permission_required('home.agent',login_url='/home/login/')
def edit_fee(request):
	#"/rental/rentals.edit_fee/${ rental.id }"
	params = {}

	#Get params objects
	rental = hmod.RentalItem.objects.get(id=request.urlparams[0])

	try:
		print(">>>>",rental.id)
		fee = hmod.Fee.objects.get(rental_item_id=rental.id)

	except:
		fee = hmod.Fee()
		fee.rental_item_id = rental.id
		fee.save()
	
	print("Fee",fee.description)

	feeform = FeeForm(initial={
	'amount' : fee.amount,
	'waived' : fee.waived,
	'days_late' : fee.days_late,
	'description' : fee.description,
	'rental_item' : fee.rental_item_id,
	})


	if request.method == "POST":
		feeform = FeeForm(request.POST)
		if feeform.is_valid():
			fee = hmod.Fee.objects.get(rental_item_id=rental.id)
			fee.amount = feeform.cleaned_data['amount']
			fee.waived = feeform.cleaned_data['waived']
			fee.days_late = feeform.cleaned_data['days_late']
			fee.description = feeform.cleaned_data['description']
			fee.rental_item_id = feeform.cleaned_data['rental_item']

			fee.save()

			return HttpResponseRedirect('/rental/rentals.view')

	params['feeform'] = feeform
	params['rental'] = rental
	params['fee'] = fee

	return templater.render_to_response(request, 'rental.edit_fee.html', params)

#Transaction Edit Form
class TransactionForm(forms.Form):
	date = forms.CharField(label="Date", required=True)
	date_packed = forms.CharField(label="Date Packed", required=True)
	#packed_by = forms.CharField(label="packed_by", required=True)
	date_paid = forms.CharField(label="Date Paid", required=False)
	#payment_handler = forms.CharField(label="payment_handler", required=True)
	date_shipped = forms.CharField(label="Date Shipped", required=False)
	#shipped_by = forms.CharField(label="shipped_by", required=True)
	tracking_number = forms.CharField(label="Tracking Number", required=True)
	#ships_to = forms.CharField(label="ships_to", required=True)
	#packed_by = forms.CharField(label="packed_by", required=True)
	#payment_processed_by = forms.CharField(label="payment_processed_by", required=True)
	#shipped_by = forms.CharField(label="shipped_by", required=True)
	#handled_by = forms.CharField(label="handled_by", required=True)
	#customer = forms.CharField(label="customer", required=True)
	date_out = forms.CharField(label="Date Out", required=True)
	date_in = forms.CharField(label="Date In", required=False)
	date_due = forms.CharField(label="Date Due", required=True)
	#discount_percent = forms.CharField(label="Discount Percent", required=False)
	#rentable_product = forms.CharField(label="rentable_product", required=True)


#Fee Edit Form
class FeeForm(forms.Form):
	amount = forms.CharField(label="Fee Amount", required=True)
	waived = forms.CharField(label="Fee Waived", required=True)
	days_late = forms.CharField(label="Days Late", required=True)
	description = forms.CharField(label="Description", required=True)
	rental_item = forms.CharField(label="Rental item", required=True)


#Delete
@view_function
#This permission required will allow managers to delete
@permission_required('home.agent',login_url='/user/user/')
def delete(request):
	fee = hmod.Fee.objects.get(id=request.urlparams[0])

	fee.delete()

	return HttpResponseRedirect('/rental/rentals.view')


#Add to cart
@view_function
def add_rental_into_cart(request):
	#This gets called by the choose rental product add button and these are the params on the url
    #'/rental/rentals.rentalcart_add/' + photo_id + "/" + product_id + "/" + item_id + "/" customer_id,
    #/photo[0]/product[1]/item[2]/customer[3]/qty[4]/item_cost[5]


    #Add item to cart
    photo_id = request.urlparams[0]
    product_id = request.urlparams[1]
    item_id = request.urlparams[2]
    customer_id = request.urlparams[3]
    qty = request.urlparams[4]
    item_cost = request.urlparams[5]

    print('Photo', photo_id)
    print('Product', product_id)
    print('Item', item_id)
    print('Customer', customer_id)
    print('Quantity', qty)
    print('Item Cost', item_cost)

    cart = request.session.get('rental_cart', {})



    print(">>>Before:", cart)

    #Check if the cart has the product, if not add it + qty, else ad the new quantity
    try:
        keys = request.session['rental_cart'].keys()
        if product_id not in keys:
            cart[product_id] = qty
            request.session['rental_cart'] = cart
        else:
            value = cart.get(product_id)
            new_qty = int(value) + int(qty) 
            cart[product_id] = new_qty
            request.session['rental_cart'] = cart

    except:
        cart[product_id] = qty
        request.session['rental_cart'] = cart

    cart['Customer'] = customer_id

    request.session['rental_cart'] = cart

    print(">>>After:", cart)

    return HttpResponseRedirect('/rental/rentals.show_rentalcart/')


#Show cart
@view_function
def show_rentalcart(request):
    params = {}

    #Get all the photos, they will be passed as a param and loaded into the shopping cart
    photos = hmod.Photograph.objects.all()
    cart = request.session.get('rental_cart', {})
    
    total_price = 0

    #Create a cart list
    cart_list = []

    #My cart has the ids for all the products and the customer.
    #EX: 15:1 10:1 Customer:5
    for product_id in cart:
        if product_id != 'Customer':
            if product_id != 'Transaction':
                if product_id != 'Total':
                    product = hmod.ProductSpecification.objects.get(id=product_id)
                    cart_list.append(product)
                    try:
                        wardrobeitem = hmod.WardrobeItem.objects.get(id=product_id)
                        quantity = cart.get(product_id)
                        price = int(wardrobeitem.cost) * int(quantity)
                        total_price += price
                    except:
                        rentalitem = hmod.RentableProduct.objects.get(id=product_id)
                        quantity = cart.get(product_id)
                        price = int(rentalitem.cost) * int(quantity)
                        total_price += price

    print(cart)        

    params = {
        'cart' : cart,
        'cart_list': cart_list,
        'photos': photos,
        'total_price' : total_price,
    }

    #Get the items in the shopping cart in an ajax ($.loadmodal dialog)
    #Just shows the shopping cart

    return templater.render_to_response(request, 'rental_cart.html', params)


@view_function
def rentalcart_delete(request):
    #This is called by the delete button in shopping_cart.html
    #Params [0]=$(this).attr('data-product_id') + "/",
    
    #Get cart object
    cart = request.session.get('rental_cart', {})

    #Get the product id of the product we are deleting from the cart
    product_id = request.urlparams[0]

    if product_id in cart:

        del cart[product_id]

    request.session['rental_cart'] = cart

    #Return to view the cart (reload the modal)
    return HttpResponseRedirect('/rental/rentals.show_rentalcart/')



class RentalItemForm(forms.Form):
    date_out = forms.CharField(label="Date Out", required=True)
    date_due = forms.CharField(label="Date Due", required=True)
    discount_percent = forms.CharField(label="Discount Percent", required=False)
    dailyfee = forms.CharField(label="Daily Fee", required=True)


#Transaction Build Form
class TransactionBuildForm(forms.Form):
	#price = forms.CharField(label="Price")
    #transaction = forms.CharField(label="Transaction")
	date_out = forms.CharField(label="Date Out", required=True)
    #date_in = forms.CharField(label="Date In", required=True)
	date_due = forms.CharField(label="Date Due", required=True)
	discount_percent = forms.DecimalField(label="Discount Percent", required=True)
	rentable_product = forms.CharField(label="Rentable Product", required=True)
	##Fee Info
	#amount = forms.CharField(label="Fee Amount", required=True)
	#waived = forms.CharField(label="Fee Waived", required=True)
	#days_late = forms.CharField(label="Days Late", required=False)
	#description = forms.CharField(label="Description", required=True)
	#rental_item = forms.CharField(label="Rental_item", required=True)

#This is a set of the Transaction Build Forms
#TransactionBuildFormSet = formset_factory(TransactionBuildForm, extra=2)

#Build
@view_function
def rentalcart_build(request):
    #This gets called by the continue button in the rental cart, show the rentals and add detail
    dailyfee = request.urlparams[0]

    cart = request.session.get('rental_cart', {})
    print(">>>Build ",cart)

    #Create a cart list for product ids, product_id is the key
    cart_list = []
    for product_id in cart:
        #This is will print the qty
        print(cart[product_id])
        if product_id != 'Customer':
            if product_id != 'Transaction':
                if product_id != 'Total':
                    product = hmod.ProductSpecification.objects.get(id=product_id)
                    cart_list.append(product)

    for product in cart_list:
        print(">>>Product ID = ", product.id)

    print(">>>Customer ID", cart['Customer'])

    #Build A Transaction for the customer
    transaction = hmod.Transaction()
    transaction.date = date.today()
    transaction.date_packed =  date.today()
    transaction.packed_by_id = 3
    transaction.date_paid = date.today()
    transaction.payment_handler_id =  3
    transaction.date_shipped =  date.today()
    transaction.shipped_by_id = 3
    #This places a tracking number based on seconds.
    transaction.tracking_number = 'Tracking:' + str((time.time()))
    transaction.ships_to_id =  1
    transaction.payment_processed_by_id =  3
    transaction.shipped_by_id =  3
    transaction.handled_by_id =  3
    transaction.customer_id = cart['Customer']
    transaction.save()

    #Get the transaction ID and put it in the cart
    transaction_id = transaction.id
    cart['Transaction'] = transaction_id

    photos = hmod.Photograph.objects.all()

    rentalform = RentalItemForm(initial={
        'date_out' : date.today(),
        'date_due' : date.today(),
        'dailyfee' : dailyfee,
        'discount_percent' : 0.0,
        })

    params = {}
    params = {
        'cart' : cart,
        'cart_list': cart_list,
        'photos': photos,
        'transaction_id': transaction_id,
        'rentalform' : rentalform,
        'dailyfee' : dailyfee
    }

    print(request.method)
    if request.method == "POST":
        rentalform = RentalItemForm(request.POST)
        if rentalform.is_valid():
            print('form is valid')
            ##Save the rental items in the database
            rental_cart = cart
            cart_list = cart_list
            discount_percent = rentalform.cleaned_data['discount_percent']
            transaction = transaction_id
            date_out = rentalform.cleaned_data['date_out']
            date_due = rentalform.cleaned_data['date_due']
            dailyfee = rentalform.cleaned_data['dailyfee']
            

            cart['Total'] = str(dailyfee)


            request.session['rental_cart'] = cart


            print("Here",cart)
            #rental is the product id
            #cart[rental] is quantity
            for rental in cart: 
                if rental != 'Customer':
                    if rental != 'Transaction':
                        if rental != 'Total':
                            qty = cart[rental]
                            n = int(qty)
                            print("Rental ID: ",rental," QTY: ",n)
                            #I now want to iterate through each rental for the defined quantity
                            i = 0
                            while i < n:
                                u = hmod.RentalItem()
                                u.price = dailyfee
                                u.transaction_id = transaction
                                u.date_out = date_out
                                u.date_due = date_due
                                u.discount_percent = discount_percent
                                u.rentable_product_id = rental
                                u.save()
                                i += 1

            return HttpResponseRedirect('/rental/rentals.rentalcart_complete/')
        else:
            print("Form not Valid")


    return templater.render_to_response(request, 'rentalcart.add_details.html', params)


#Complete
@view_function
def rentalcart_complete(request):
    cart = request.session.get('rental_cart', {})


    print(">>>>COMPLETE",cart)

    dailyfee = cart['Total']
    

    #Create a cart list for product ids, product_id is the key
    cart_list = []
    for product_id in cart:
        #This is will print the qty
        print(cart[product_id])
        if product_id != 'Customer':
            if product_id != 'Transaction':
                if product_id != 'Total':
                    product = hmod.ProductSpecification.objects.get(id=product_id)
                    cart_list.append(product)

    for product in cart_list:
        print(">>>Product ID = ", product.id)

    print(">>>Customer ID", cart['Customer'])
    print(">>>Daily Fee",dailyfee)


    photos = hmod.Photograph.objects.all()



    params = {}
    params = {
        'cart' : cart,
        'cart_list': cart_list,
        'photos': photos,
        'dailyfee' : dailyfee,
    }


    return templater.render_to_response(request, 'rentalcart_complete.html', params)



#Check out rentalcart
@view_function
def checkout(request):
    cart = request.session.get('rental_cart', {})


    total_cost = cart['Total']
    user = hmod.User.objects.get(id=cart['Customer'])

    params = {}
    
    params['total_cost'] = total_cost
    params['user'] = user

    templater = get_renderer('product')

    return templater.render_to_response(request, 'checkout.html', params)





##Code for reference


    ##Form code for salvaging
    # #Create set of forms

    # formset = TransactionBuildFormSet(initial=[
    #     {
    #     'date_out' : date.today(),
    #     'date_due' : date.today(),
    #     'rentable_product' : "product_id",
    #     }   
    #     ])
    
    #This makes a list of unique form names
    #Then creates those forms for the specific product
    #forms = []
    # for product_id in cart:
    #     if product_id != 'Customer':
    #         build_form = 'form' + product_id
    #         build_form = TransactionBuildForm(initial={
    #           'date_out' : date.today(),
    #             'date_due' : date.today(),
    #           'rentable_product' : product_id,
    #           })
    #         forms.append(build_form)

    # #Make a list of product ids as strings
    # products_as_string = []
    # for product_id in cart:
    #     if product_id != 'Customer':
    #         string = str(product_id)
    #         products_as_string.append(string)
    # print(products_as_string)


    # #Make a list of photo ids as strings
    # photos_as_string = []
    # for photo in photos:
    #     string_id = str(photo.id)
    #     photos_as_string.append(string_id)
    # print(photos_as_string)
    # print(">>>>>Form set", forms)
    # for form in formset:
    #     print(">>>TABLE",form.as_table())
    #     print(">>>>FormRP", form['rentable_product'])
    #     print(">>>>FormDO", form['date_out'])
    #     for field in form:
    #         for value in field:
    #             print(">>>>>Form", field.name, value.value)