# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428379600.59039
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\event\\templates/events.edit.html'
_template_uri = 'events.edit.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents', 'top_banner']


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
        event = context.get('event', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        event = context.get('event', UNDEFINED)
        def contents():
            return render_contents(context)
        form = context.get('form', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<form method="POST">\r\n<table id="form">\r\n\r\n')
        __M_writer(str(form))
        __M_writer('\r\n\r\n</table>\r\n<div id="form_buttons">\r\n\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t<a href="/home/events.delete/')
        __M_writer(str(event.id))
        __M_writer('/" class="btn btn-warning">Delete Area</a>\r\n</div>\r\n\r\n</form>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Edit Events</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 18, "65": 18, "38": 1, "71": 3, "43": 5, "77": 3, "83": 77, "53": 8, "27": 0, "61": 8, "62": 13, "63": 13}, "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\event\\templates/events.edit.html", "source_encoding": "ascii", "uri": "events.edit.html"}
__M_END_METADATA
"""
