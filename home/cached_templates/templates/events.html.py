# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423289471.94035
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/events.html'
_template_uri = 'events.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top_banner', 'contents']


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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        request = context.get('request', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        events = context.get('events', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

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
        request = context.get('request', UNDEFINED)
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
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Start Date</th>\r\n\t\t\t\t<th>End Date</th>\r\n\t\t\t\t<th>Map File</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
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
                __M_writer('</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\t\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/events.html", "uri": "events.html", "line_map": {"131": 125, "27": 0, "38": 1, "43": 5, "53": 3, "59": 3, "65": 9, "73": 9, "74": 11, "75": 12, "76": 13, "77": 25, "78": 26, "79": 26, "80": 26, "81": 27, "82": 27, "83": 28, "84": 28, "85": 29, "86": 29, "87": 30, "88": 30, "89": 32, "90": 32, "91": 33, "92": 33, "93": 37, "94": 43, "95": 44, "96": 56, "97": 57, "98": 57, "99": 57, "100": 58, "101": 58, "102": 59, "103": 59, "104": 60, "105": 60, "106": 61, "107": 61, "108": 63, "109": 63, "110": 67, "111": 69, "112": 70, "113": 81, "114": 82, "115": 82, "116": 82, "117": 83, "118": 83, "119": 84, "120": 84, "121": 85, "122": 85, "123": 86, "124": 86, "125": 89}, "source_encoding": "ascii"}
__M_END_METADATA
"""
