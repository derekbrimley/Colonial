# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428383288.142509
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\Colonial\\rental\\templates/bulk_rentals_ajax.html'
_template_uri = 'bulk_rentals_ajax.html'
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
    return runtime._inherit_from(context, '/home/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        bulk_items = context.get('bulk_items', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contents():
            return render_contents(context)
        bulk_items = context.get('bulk_items', UNDEFINED)
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\nBulk return for ')
        __M_writer(str(user.username))
        __M_writer('<br />\r\n')
        for bulk_itemss in bulk_items:
            __M_writer('    Rented Item: ')
            __M_writer(str(bulk_itemss.name))
            __M_writer(' Item ID: ')
            __M_writer(str(bulk_itemss.id))
            __M_writer('<br />\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Rentals</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Scripts\\Colonial\\rental\\templates/bulk_rentals_ajax.html", "uri": "bulk_rentals_ajax.html", "source_encoding": "ascii", "line_map": {"64": 10, "65": 11, "66": 12, "67": 12, "68": 12, "69": 12, "38": 1, "43": 5, "76": 3, "48": 14, "82": 3, "54": 9, "88": 82, "27": 0, "70": 12, "62": 9, "63": 10}}
__M_END_METADATA
"""
