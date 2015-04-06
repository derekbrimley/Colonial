# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428078253.19887
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\event\\templates/events.html'
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
        def title():
            return render_title(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        request = context.get('request', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        events = context.get('events', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
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
        str = context.get('str', UNDEFINED)
        request = context.get('request', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        events = context.get('events', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        if request.user.has_perm('home.is_manager'):
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
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/events.edit/')
                __M_writer(str(event.id))
                __M_writer('">Edit</a> | \r\n\t\t\t\t<a href="/home/events.delete/')
                __M_writer(str(event.id))
                __M_writer('">Delete</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\t\t<div class="text-right">\r\n\t\t\t<a href="/home/events.create/" class="btn btn-success">Add an Event</a>\r\n\t\t</div>\r\n\t  \r\n')
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
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/events.edit/')
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
{"source_encoding": "ascii", "uri": "events.html", "filename": "C:\\Python34\\Projects\\colonial\\event\\templates/events.html", "line_map": {"128": 64, "129": 64, "130": 65, "131": 65, "132": 66, "133": 66, "134": 68, "135": 68, "136": 72, "137": 74, "138": 75, "139": 88, "140": 89, "141": 90, "142": 91, "143": 92, "144": 93, "145": 93, "146": 93, "147": 93, "148": 93, "149": 94, "150": 94, "151": 95, "152": 95, "153": 97, "154": 97, "27": 0, "156": 97, "157": 97, "158": 97, "159": 97, "160": 97, "161": 102, "162": 104, "155": 97, "168": 162, "43": 1, "48": 6, "53": 10, "58": 108, "64": 3, "70": 3, "76": 8, "82": 8, "88": 14, "99": 14, "100": 16, "101": 17, "102": 18, "103": 30, "104": 31, "105": 31, "106": 31, "107": 32, "108": 32, "109": 33, "110": 33, "111": 34, "112": 34, "113": 35, "114": 35, "115": 37, "116": 37, "117": 38, "118": 38, "119": 42, "120": 48, "121": 49, "122": 61, "123": 62, "124": 62, "125": 62, "126": 63, "127": 63}}
__M_END_METADATA
"""
