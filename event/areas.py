from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as vmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission

templater = get_renderer('home')


#############################Areas
@view_function
#@permission_required('home.is_agent',login_url='/home/areas/')
def process_request(request):
	params = {}

	areas = vmod.Area.objects.all().order_by('area_name')

	params['areas'] = areas

	return templater.render_to_response(request, 'areas.html', params)

#############################Edit
@view_function
@permission_required('home.is_agent',login_url='/home/areas/')
def edit(request):

	params = {}
	print(request.urlparams[0])

	try:
		area = vmod.Area.objects.get(id=request.urlparams[0])

	except vmod.area.DoesNotExist:

		return HttpResponseRedirect('/home/areas/')



	form = areaEditForm(initial={
		'area_name': area.area_name,
		'description': area.description,
		'place_number' : area.place_number,
		})

	if request.method == "POST":
		form = areaEditForm(request.POST)
		if form.is_valid():
			area.area_name = form.cleaned_data['area_name']
			area.description = form.cleaned_data['description']
			area.place_number = form.cleaned_data['place_number']


			area.save()
			return HttpResponseRedirect('/home/areas/')



	params['form'] = form
	params['area'] = area

	return templater.render_to_response(request, 'areas.edit.html', params)




class areaEditForm(forms.Form):
	area_name = forms.CharField(label="Area Name", required=True, max_length=100)
	description = forms.CharField(label="Description", required=True, max_length=100)
	place_number = forms.CharField(label="Place Number", required=True, max_length=100)



########################Create
@view_function
@permission_required('home.is_manager',login_url='/home/areas/')
def create(request):
	'''create a new area'''
	area = vmod.Area()
	area.area_name = ''
	area.description = ''
	area.place_number = ''
	area.save()


	return HttpResponseRedirect('/home/areas.edit/{}/'.format(area.id))


#########################Delete
@view_function
@permission_required('home.is_manager',login_url='/home/areas/')
def delete(request):
	'''Deletes a new area'''
	


	try:
		area = vmod.Area.objects.get(id=request.urlparams[0])
	except vmod.DoesNotExist:
		return HttpResponseRedirect('/home/areas/')

	area.delete()

	return HttpResponseRedirect('/home/areas/')