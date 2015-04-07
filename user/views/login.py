from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth import authenticate, login, logout
from ldap3 import Server, Connection, AUTH_SIMPLE, STRATEGY_SYNC, GET_ALL_INFO
from datetime import date, datetime

templater = get_renderer('user')

##This is used for the login form
class LoginForm(forms.Form):
	username = forms.CharField(label="Username")
	password = forms.CharField(label="Password", widget=forms.PasswordInput)


@view_function
def logout_view(request):
    logout(request)
    # Redirect to a success page.
    return HttpResponseRedirect('/home/index')


@view_function
def loginform(request):

	params = {}
	form = LoginForm()

	if request.method == "POST":
		form = LoginForm(request.POST)

		if form.is_valid():

			username=form.cleaned_data['username']
			print(">>>>Username",username)
			sauce=form.cleaned_data['password']
			print(">>>>Sauce",sauce)

			try: #Colonial Server connection for LDAP
				s = Server('www.colonialheritage.space', port=8889, get_info=GET_ALL_INFO)
				print('>>>>LDAP-S ',s)
				c = Connection(s, auto_bind = True, client_strategy = STRATEGY_SYNC, 
								user='%s@colonialheritage.local' %username,
								password='%s' %sauce, authentication = AUTH_SIMPLE)

				# #If good login
				if c != None:
					print('>>>>LDAP-C ',c)
					#Update the website with information from AD

					search_results = c.search(
						search_base = 'CN=Users,DC=colonialheritage,DC=local',
						search_filter = '(samAccountName=%s)' %username,
						attributes = [
						'givenName',
						'sn',
						'userPrincipalName'])

					user_info = c.response[0]['attributes']

					print(">>>>LDAP-C.Info ", user_info)

					first_name = user_info['givenName']
					last_name = user_info['sn']
					email = user_info['userPrincipalName']

					print('>>>>Username ', username)
					print('>>>>First_name ',first_name)
					print('>>>>Last_name ',last_name)
					print('>>>>Email ',email)

					try:
						u = hmod.User.objects.get(username=username)
						u.first_name = first_name
						u.last_name = last_name
						u.email = email
						u.set_password(sauce)
						u.save()

					except:
						u = hmod.User()
						u.first_name =first_name
						u.last_name = last_name
						u.email = email
						u.username = username
						u.set_password(sauce)
						u.is_staff = True
						u.is_superuser = False
						u.last_login = str(datetime.now())
						u.address_id = 1
						u.save()
						print("LDAP3 CREATED, SAVED")

					print(">>>>LDAP-Complete")


					u2 = authenticate(username, sauce)
					login(request, u2)
					return HttpResponse('<script> window.location.href="/home/index/";</script>')

				else:
					print('>>>>C-None')

			except: #Log in just on website
				print(">>>LDAP-Abort")
				try:
					user = authenticate(username=username, password=sauce)
					print("USERNAME: ",username)
					print("PASSWORD: ",sauce)
					if user == None:
						print("Invalid Credentials")
						raise forms.ValidationError('Invalid Credentials')
					else:	
						#Log the user in with the following code
						login(request, user)
						return HttpResponse('<script> window.location.href="/home/index/";</script>')

				except:
					pass
		else:
			print('Form Not Valid')



	params['form'] = form

	return templater.render_to_response(request, 'login.loginform.html', params)