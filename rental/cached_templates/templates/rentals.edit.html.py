# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428048257.136023
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.edit.html'
_template_uri = 'rentals.edit.html'
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
    return runtime._inherit_from(context, '/home/templates/base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        rental = context.get('rental', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        def contents():
            return render_contents(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
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


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Edit Rental</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rental = context.get('rental', UNDEFINED)
        def contents():
            return render_contents(context)
        form = context.get('form', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if request.user.has_perm('home.agent'):
            __M_writer('\r\n\t\t<form method="POST">\r\n\r\n\t\t\t<table id="form">\r\n\r\n\t\t\t\t')
            __M_writer(str( form ))
            __M_writer('\r\n\r\n\r\n\t\t\t</table>\r\n\t\t\t<div id="form_buttons">\r\n\t\t\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t\t\t\t<a href="/rental/rentals.edit_fee/')
            __M_writer(str( rental.id ))
            __M_writer('" class="btn btn-danger">Edit Fee</a>\r\n\t\t\t</div>\r\n\t\t</form>\r\n\r\n')
        else:
            __M_writer('\t<h1 class="text-center">Down for maintenance</h1>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.edit.html", "uri": "rentals.edit.html", "line_map": {"66": 8, "39": 1, "44": 5, "75": 8, "76": 10, "77": 11, "78": 16, "79": 16, "80": 22, "81": 22, "82": 26, "83": 27, "84": 29, "54": 3, "90": 84, "27": 0, "60": 3}}
__M_END_METADATA
"""
