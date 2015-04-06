# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425770470.967346
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/areas.html'
_template_uri = 'areas.html'
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
        areas = context.get('areas', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        def contents():
            return render_contents(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
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
        __M_writer('\r\n\t<div class="top_banner">Areas</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        areas = context.get('areas', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if request.user.has_perm('home.manager'):
            __M_writer('\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Place Number</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for area in areas:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(area.area_name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(area.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(area.place_number))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/areas.edit/')
                __M_writer(str(area.id))
                __M_writer('">Edit</a> | \r\n\t\t\t\t<a href="/home/areas.delete/')
                __M_writer(str(area.id))
                __M_writer('">Delete</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\t\t<div class="text-right">\r\n\t\t\t<a href="/home/areas.create/" class="btn btn-success">Add an Area</a>\r\n\t\t</div>\r\n\r\n')
        elif request.user.has_perm('home.agent'):
            __M_writer('\t\t\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Place Number</th>\r\n\t\t\t\t<th>Actions</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for area in areas:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(area.area_name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(area.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(area.place_number))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/areas.edit/')
                __M_writer(str(area.id))
                __M_writer('">Edit</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n')
        else:
            __M_writer('\t\t\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Place Number</th>\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for area in areas:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(area.area_name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(area.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(area.place_number))
                __M_writer('</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "areas.html", "line_map": {"27": 0, "38": 1, "43": 6, "53": 4, "59": 4, "65": 9, "73": 9, "74": 11, "75": 12, "76": 21, "77": 22, "78": 22, "79": 22, "80": 23, "81": 23, "82": 24, "83": 24, "84": 26, "85": 26, "86": 27, "87": 27, "88": 31, "89": 37, "90": 38, "91": 48, "92": 49, "93": 49, "94": 49, "95": 50, "96": 50, "97": 51, "98": 51, "99": 53, "100": 53, "101": 57, "102": 59, "103": 60, "104": 69, "105": 70, "106": 70, "107": 70, "108": 71, "109": 71, "110": 72, "111": 72, "112": 75, "118": 112}, "source_encoding": "ascii", "filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/areas.html"}
__M_END_METADATA
"""
