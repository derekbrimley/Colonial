# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423330965.040738
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/orders.edit.html'
_template_uri = 'orders.edit.html'
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
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        form = context.get('form', UNDEFINED)
        order = context.get('order', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
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
        __M_writer('\r\n\t<div class="top_banner">Edit Orders</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        form = context.get('form', UNDEFINED)
        order = context.get('order', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<form method="POST">\r\n<table id="form">\r\n\r\n')
        __M_writer(str(form))
        __M_writer('\r\n\r\n</table>\r\n<div id="form_buttons">\r\n\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t<a href="/home/orders.delete/')
        __M_writer(str(order.id))
        __M_writer('/" class="btn btn-warning">Delete Order</a>\r\n</div>\r\n</form>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "orders.edit.html", "filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/orders.edit.html", "line_map": {"65": 8, "27": 0, "38": 1, "73": 8, "74": 13, "75": 13, "76": 18, "77": 18, "43": 5, "83": 77, "53": 3, "59": 3}, "source_encoding": "ascii"}
__M_END_METADATA
"""
