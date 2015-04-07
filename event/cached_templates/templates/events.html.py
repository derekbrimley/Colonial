# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428380978.793613
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\event\\templates/events.html'
_template_uri = 'events.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['title', 'top_banner', 'contents']


def _mako_get_namespace(context, name):
    try:
        return context.namespaces[(__name__, name)]
    except KeyError:
        _mako_generate_namespaces(context)
        return context.namespaces[(__name__, name)]
def _mako_generate_namespaces(context):
    pass
def _mako_inherit(template, context):
    _mako_generate_namespaces(context)
    return runtime._inherit_from(context, '/home/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        photos = context.get('photos', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        def contents():
            return render_contents(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        addresses = context.get('addresses', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<title>Colonial Events</title>\r\n\t<meta name="Colonial Heritage Foundation Home Page" content="The Colonial Heritage Foundation promotes actively engaging the mind in history. This page will show you the many different colonial events going on! Fun around every corner. Family and Friends are all welcome.">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Events</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        photos = context.get('photos', UNDEFINED)
        def contents():
            return render_contents(context)
        events = context.get('events', UNDEFINED)
        addresses = context.get('addresses', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        str = context.get('str', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        if request.user.has_perm('home.manager'):
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Start Date</th>\r\n\t\t\t\t<th>End Date</th>\r\n\t\t\t\t<th>Map File</th>\r\n\t\t\t\t<th>Venue Name</th>\r\n\t\t\t\t<th>Address</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for event in events:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(event.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(event.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(event.start_date))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(event.end_date))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(event.map_file))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(event.venue_name))
                __M_writer('</td>\r\n')
                for address in addresses:
                    if address.id == event.address_id:
                        __M_writer('\t\t\t\t\t\t<td>')
                        __M_writer(str(address.address1))
                        __M_writer(', ')
                        __M_writer(str(address.city))
                        __M_writer(' ')
                        __M_writer(str(address.state))
                        __M_writer('</td>\r\n')
                __M_writer('\t\t\t\t<td>\r\n\t\t\t\t<a href="/event/events.edit/')
                __M_writer(str(event.id))
                __M_writer('">Edit</a> | \r\n\t\t\t\t<a href="/event/events.delete/')
                __M_writer(str(event.id))
                __M_writer('">Delete</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\t\t<div class="text-right">\r\n\t\t\t<a href="/event/events.create/" class="btn btn-success">Add an Event</a>\r\n\t\t</div>\r\n\t  \r\n')
        elif request.user.has_perm('home.is_agent'):
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Start Date</th>\r\n\t\t\t\t<th>End Date</th>\r\n\t\t\t\t<th>Map File</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for event in events:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(event.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(event.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(event.start_date))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(event.end_date))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(event.map_file))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/event/events.edit/')
                __M_writer(str(event.id))
                __M_writer('">Edit</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n')
        else:
            __M_writer('\r\n\t<div class="events">\r\n\r\n')
            __M_writer('\t\t\t\t\r\n')
            for event in events:
                __M_writer('\t\t\t\t<div class="item_container text-center">\r\n')
                for photo in photos:
                    if str(event.id) in photo.image:
                        __M_writer('\t\t\t\t\t\t\t<img src="')
                        __M_writer(str( STATIC_URL ))
                        __M_writer('event/media/')
                        __M_writer(str( photo.image ))
                        __M_writer('" />\r\n\t\t\t\t\t\t\t<div class="event_name"><h1>')
                        __M_writer(str( event.name ))
                        __M_writer('</h1></div>\r\n\t\t\t\t\t\t\t<div class="text-muted"><h1><small>')
                        __M_writer(str( event.description ))
                        __M_writer('</small></h1></div>\r\n\t\t\t\t\t\t\t<div class="text-center">\r\n\t\t\t\t\t\t\t\t<a href="/event/events.detail/')
                        __M_writer(str( event.id ))
                        __M_writer('/')
                        __M_writer(str( photo.id ))
                        __M_writer('" data-event_id="')
                        __M_writer(str( event.id ))
                        __M_writer('" data-photo_id="')
                        __M_writer(str( photo.id ))
                        __M_writer('" class="show_detail btn btn-lg btn-primary">More Info!</a>\r\n\r\n\t\t\t\t\t\t\t</div>\r\n')
                __M_writer('\t\t\t\t</div>\r\n')
            __M_writer('\t</div>\r\n\t\t\r\n\t\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "events.html", "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\event\\templates/events.html", "line_map": {"27": 0, "44": 1, "49": 6, "54": 10, "59": 116, "65": 3, "71": 3, "77": 8, "83": 8, "89": 14, "101": 14, "102": 16, "103": 17, "104": 18, "105": 32, "106": 33, "107": 33, "108": 33, "109": 34, "110": 34, "111": 35, "112": 35, "113": 36, "114": 36, "115": 37, "116": 37, "117": 38, "118": 38, "119": 39, "120": 40, "121": 41, "122": 41, "123": 41, "124": 41, "125": 41, "126": 41, "127": 41, "128": 44, "129": 45, "130": 45, "131": 46, "132": 46, "133": 50, "134": 56, "135": 57, "136": 69, "137": 70, "138": 70, "139": 70, "140": 71, "141": 71, "142": 72, "143": 72, "144": 73, "145": 73, "146": 74, "147": 74, "148": 76, "149": 76, "150": 80, "151": 82, "152": 83, "153": 96, "154": 97, "155": 98, "156": 99, "157": 100, "158": 101, "159": 101, "160": 101, "161": 101, "162": 101, "163": 102, "164": 102, "165": 103, "166": 103, "167": 105, "168": 105, "169": 105, "170": 105, "171": 105, "172": 105, "173": 105, "174": 105, "175": 110, "176": 112, "182": 176}}
__M_END_METADATA
"""
