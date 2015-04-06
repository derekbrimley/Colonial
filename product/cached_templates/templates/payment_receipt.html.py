# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427912926.817109
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\product\\templates/payment_receipt.html'
_template_uri = 'payment_receipt.html'
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
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        resp = context.get('resp', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n')
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        resp = context.get('resp', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t   \t<div class="row">\r\n            <div class="col-xs-12">   \r\n             \t<img class="photo" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/receipt.png" alt="Receipt" >\r\n    \t\t</div>\r\n        </div> \r\n\r\n        <div class="text-center">\r\n\r\n        <h1>Receipt</h1>\r\n        <table class="table table-condensed">\r\n        \t<tr>\r\n\t        \t<th>Currency</th>\r\n\t        \t<th>Amount</th>\r\n\t        \t<th>Date</th>\r\n\t        \t<th>Description</th>\r\n\t\t\t\t<th>ID</th>\r\n        \t</tr>\r\n\r\n        \t<tr>\r\n\t        \t<td>')
        __M_writer(str( resp['Currency'] ))
        __M_writer('</td>\r\n\t        \t<td>')
        __M_writer(str( resp['Amount'] ))
        __M_writer('</td>\r\n\t        \t<td>')
        __M_writer(str( resp['Date'] ))
        __M_writer('</td>\r\n\t        \t<td>')
        __M_writer(str( resp['Description'] ))
        __M_writer('</td>\r\n\t        \t<td>')
        __M_writer(str( resp['ID'] ))
        __M_writer('</td>\r\n\t        </tr>\r\n\r\n')
        __M_writer('\r\n\r\n\t\t</table>\r\n\r\n\r\n\r\n\t    <div class="text-center">\r\n\t    <a href="/home/index/" class="btn btn-info">Home</a>\r\n\t    </div>\r\n\r\n\t\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Payment Approved</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"64": 28, "65": 28, "66": 29, "67": 29, "68": 30, "69": 30, "38": 1, "71": 31, "72": 32, "73": 32, "74": 42, "43": 6, "80": 4, "92": 86, "53": 8, "86": 4, "27": 0, "70": 31, "61": 8, "62": 11, "63": 11}, "uri": "payment_receipt.html", "filename": "C:\\Python34\\Projects\\colonial\\product\\templates/payment_receipt.html"}
__M_END_METADATA
"""
