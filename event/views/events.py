from django.conf import settings
from django import forms
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.http import HttpRequest
from django_mako_plus.controller import view_function
from home import models as hmod
from django_mako_plus.controller.router import get_renderer
from django.contrib.auth.decorators import login_required, permission_required
from django.contrib.auth.models import User, Group, Permission

templater = get_renderer('event')

@view_function
# #This permission required will allow managers and agents and customers to see this account page
#@permission_required('home.is_agent',login_url='/home/login/')
def process_request(request):

	# for group in request.user.groups.all():
	# 	print('>>>', group)
	# 	for perm in group.permissions.all():
	# 		print(perm)
	# print('<<<', request.user.has_perm('admin.is_manager'))
	# print(request.user.get_all_permissions())

	params = {}

	events = hmod.Event.objects.all().order_by('id')
	photographs = hmod.Photograph.objects.all()
	photos = []

	for photo in photographs:
		if "event" in photo.image:
			photos.append(photo)
			print(photos)
		else: 
			print("Not a photo for events")


	params['events'] = events
	params['photos'] = photos

	return templater.render_to_response(request, 'events.html', params)



#Detail
@view_function
def detail(request):
	#Params passed to this def by events.html
	#"/event/events.detail/${ event.id }/${ photo.id }"
	#Event @@ request.urlparams[0]
	#Photo @@ request.urlparams[1]


	params = {}
	event = hmod.Event.objects.get(id=request.urlparams[0])
	historical_figures = hmod.HistoricalFigure.objects.filter(event_id=request.urlparams[0])
	areas = hmod.Area.objects.filter(event_id=request.urlparams[0])
	photo = hmod.Photograph.objects.get(id=request.urlparams[1])
	sale_items = hmod.ExpectedSaleItem.objects.all()
	all_photos = hmod.Photograph.objects.all()

	area_photos = []
	hf_photos = []

	for photo in all_photos:
		if "area" in photo.image:
			area_photos.append(photo)

	for photo in all_photos:
		if "hf" in photo.image:
			hf_photos.append(photo)


	params['event'] = event
	params['historical_figures'] = historical_figures
	params['areas'] = areas
	params['photo'] = photo
	params['area_photos'] = area_photos
	params['hf_photos'] = hf_photos
	params['sale_items'] = sale_items

	return templater.render_to_response(request, 'events.detail.html', params)



@view_function
#This permission required will allow managers and agents to access
@permission_required('home.is_agent',login_url='/home/events/')
def edit(request):

	params = {}
	print(request.urlparams[0])

	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])

	except hmod.event.DoesNotExist:

		return HttpResponseRedirect('/home/events/')



	form = eventEditForm(initial={
		'name': event.name,
		'description': event.description,
		'start_date' : event.start_date,
		'end_date' : event.end_date,
		'map_file' : event.map_file})

	if request.method == "POST":
		form = eventEditForm(request.POST)
		if form.is_valid():
			event.name = form.cleaned_data['name']
			event.description = form.cleaned_data['description']
			event.start_date = form.cleaned_data['start_date']
			event.end_date = form.cleaned_data['end_date']
			event.map_file = form.cleaned_data['map_file']
			event.save()
			return HttpResponseRedirect('/home/events/')



	params['form'] = form
	params['event'] = event

	return templater.render_to_response(request, 'events.edit.html', params)




class eventEditForm(forms.Form):
	name = forms.CharField(label="Name", required=True, max_length=100)
	description = forms.CharField(label="Description", required=True, max_length=100)
	start_date = forms.CharField(label="Start Date", required=True, max_length=100)
	end_date = forms.CharField(label="End Date", required=True, max_length=100)
	map_file = forms.IntegerField(label="Map File", required=True)



#########################Create
@view_function
#This permission required will allow managers and agents to access
@permission_required('home.is_manager',login_url='/home/events/')
def create(request):
	'''create a new event'''
	event = hmod.Event()
	event.name = ''
	event.description = ''
	event.start_date = '1111-1-1'
	event.end_date = '1111-1-1'
	event.map_file = '111'
	event.save()


	return HttpResponseRedirect('/home/events.edit/{}/'.format(event.id))


##########################Delete
@view_function
#This permission required will allow managers and agents to access
@permission_required('home.is_manager',login_url='/home/events/')
def delete(request):
	'''Deletes a new event'''
	
	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/home/events/')

	event.delete()

	return HttpResponseRedirect('/home/events/')