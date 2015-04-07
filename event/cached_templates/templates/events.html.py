# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428377585.754257
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\event\\templates/events.html'
_template_uri = 'events.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents', 'title', 'top_banner']


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
        events = context.get('events', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
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


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        events = context.get('events', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def contents():
            return render_contents(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        if request.user.has_perm('home.manager'):
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


"""
__M_BEGIN_METADATA
{"uri": "events.html", "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\event\\templates/events.html", "source_encoding": "ascii", "line_map": {"128": 95, "129": 97, "130": 97, "131": 97, "132": 97, "133": 97, "134": 97, "135": 97, "136": 97, "137": 102, "138": 104, "144": 3, "150": 3, "27": 0, "156": 8, "162": 8, "168": 162, "43": 1, "48": 6, "53": 10, "58": 108, "64": 14, "75": 14, "76": 16, "77": 17, "78": 18, "79": 30, "80": 31, "81": 31, "82": 31, "83": 32, "84": 32, "85": 33, "86": 33, "87": 34, "88": 34, "89": 35, "90": 35, "91": 37, "92": 37, "93": 38, "94": 38, "95": 42, "96": 48, "97": 49, "98": 61, "99": 62, "100": 62, "101": 62, "102": 63, "103": 63, "104": 64, "105": 64, "106": 65, "107": 65, "108": 66, "109": 66, "110": 68, "111": 68, "112": 72, "113": 74, "114": 75, "115": 88, "116": 89, "117": 90, "118": 91, "119": 92, "120": 93, "121": 93, "122": 93, "123": 93, "124": 93, "125": 94, "126": 94, "127": 95}}
__M_END_METADATA
"""
