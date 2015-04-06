# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428050080.939706
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rental.edit_fee.html'
_template_uri = 'rental.edit_fee.html'
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
        def contents():
            return render_contents(context._locals(__M_locals))
        feeform = context.get('feeform', UNDEFINED)
        rental = context.get('rental', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        fee = context.get('fee', UNDEFINED)
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
        def contents():
            return render_contents(context)
        feeform = context.get('feeform', UNDEFINED)
        fee = context.get('fee', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if request.user.has_perm('home.agent'):
            __M_writer('\r\n\t\t<form method="POST">\r\n\r\n\t\t\t<table id="form">\r\n\r\n\t\t\t\t')
            __M_writer(str( feeform ))
            __M_writer('\r\n\r\n\r\n\t\t\t</table>\r\n\t\t\t<div id="form_buttons">\r\n\t\t\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t\t\t\t<a href="/rental/rentals.delete/')
            __M_writer(str( fee.id ))
            __M_writer('/" class="btn btn-warning">Delete Fee</a>\r\n\t\t\t</div>\r\n\t\t</form>\r\n\r\n')
        else:
            __M_writer('\t<h1 class="text-center">Down for maintenance</h1>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        rental = context.get('rental', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Edit Fee for Rental ')
        __M_writer(str( rental.id ))
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rental.edit_fee.html", "source_encoding": "ascii", "filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rental.edit_fee.html", "line_map": {"64": 8, "65": 10, "66": 11, "67": 16, "68": 16, "69": 22, "70": 22, "71": 26, "40": 1, "73": 29, "87": 4, "45": 5, "79": 3, "72": 27, "86": 3, "55": 8, "88": 4, "27": 0, "94": 88}}
__M_END_METADATA
"""
