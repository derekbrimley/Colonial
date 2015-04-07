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
def process_request(request):

	params = {}

	events = hmod.Event.objects.all().order_by('id')
	addresses = hmod.Address.objects.all()
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
	params['addresses'] = addresses
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
@permission_required('home.agent',login_url='/event/events/')
def edit(request):

	params = {}
	print("PARAMETER::::::",request.urlparams[0])

	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
		print("EVENT EXISTS")
	except hmod.event.DoesNotExist:
		print("EVENT DOES NOT EXIST>>>>>>>>>>>>>>>>")
		return HttpResponseRedirect('/event/events/')



	form = eventEditForm(initial={
		'name': event.name,
		'description': event.description,
		'start_date' : event.start_date,
		'end_date' : event.end_date,
		'map_file' : event.map_file,
		'venue_name' : event.venue_name,
		'address_id' : event.address_id
		}
	)

	if request.method == "POST":
		print("POSTING....")
		form = eventEditForm(request.POST)
		if form.is_valid():
			event.name = form.cleaned_data['name']
			event.description = form.cleaned_data['description']
			event.start_date = form.cleaned_data['start_date']
			event.end_date = form.cleaned_data['end_date']
			event.map_file = form.cleaned_data['map_file']
			event.venue_name = form.cleaned_data['venue_name']
			event.address_id = form.cleaned_data['address_id']
			event.save()
			return HttpResponseRedirect('/event/events/')

	params['form'] = form
	params['event'] = event

	return templater.render_to_response(request, 'events.edit.html', params)

class eventEditForm(forms.Form):
	name = forms.CharField(label="Name",required=True,max_length=100)
	description = forms.CharField(label="Description",required=True,max_length=100)
	start_date = forms.CharField(label="Start Date",required=True,max_length=100)
	end_date = forms.CharField(label="End Date",required=True,max_length=100)
	map_file = forms.IntegerField(label="Map File",required=True)
	venue_name = forms.CharField(label="Venue Name",required=True,max_length=100)
	address_id = forms.CharField(label="Address ID",required=True,max_length=100)

#########################Create
@view_function
#This permission required will allow managers and agents to access
@permission_required('home.manager',login_url='/event/events/')
def create(request):
	'''create a new event'''
	event = hmod.Event()
	event.name = ''
	event.description = ''
	event.start_date = '1111-1-1'
	event.end_date = '1111-1-1'
	event.map_file = '111'
	event.venue_name = ''
	event.address_id = 1
	event.save()


	return HttpResponseRedirect('/event/events.edit/{}/'.format(event.id))


##########################Delete
@view_function
#This permission required will allow managers and agents to access
@permission_required('home.manager',login_url='/event/events/')
def delete(request):
	'''Deletes a new event'''
	
	try:
		event = hmod.Event.objects.get(id=request.urlparams[0])
	except hmod.DoesNotExist:
		return HttpResponseRedirect('/event/events/')

	event.delete()

	return HttpResponseRedirect('/event/events/')