# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428143997.903541
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\home\\templates/overdue_ajax.html'
_template_uri = 'overdue_ajax.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents']


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
        overdue = context.get('overdue', UNDEFINED)
        product_specs = context.get('product_specs', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        overdue = context.get('overdue', UNDEFINED)
        product_specs = context.get('product_specs', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<br>\r\n\r\n')
        __M_writer('\r\n')
        if overdue:
            __M_writer('\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Rental ID</th>\r\n')
            __M_writer('\t\t\t\t<th>Price</th>\r\n\t\t\t\t<th>Date Rented</th>\r\n\t\t\t\t<th>Date Due</th>\r\n')
            __M_writer('\t\t\t\t<th>Product</th>\r\n\t\t\t\t\r\n\t\t\t</tr>\r\n\r\n\t\t\t\t<tr>\r\n')
            for rental in overdue:
                __M_writer('\t\t\t\t\t\t\t\t<td>')
                __M_writer(str(rental.id))
                __M_writer('</td>\r\n')
                __M_writer('\t\t\t\t\t\t\t\t<td>')
                __M_writer(str(rental.price))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                __M_writer(str(rental.date_out))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                __M_writer(str(rental.date_due))
                __M_writer('</td>\r\n\t\t\t\t\t\t\t\t\r\n')
                __M_writer('\t\t\t\t\t\t\t\t\r\n')
                for product in product_specs:
                    if rental.rentable_product_id == product.id:
                        __M_writer('\t\t\t\t\t\t\t\t\t\t<td>')
                        __M_writer(str(product.name))
                        __M_writer('</td>\r\n')
                __M_writer('\t\t\t\t\t\t\t\t</tr>\r\n\t\t\t\t\t\t\t\t</tr>\r\n')
                __M_writer('\t\t\t\t\t\t</tr>\r\n')
            __M_writer('\r\n')
            __M_writer('\r\n\t\t\t\t\t\r\n\t\t\t</table>\r\n\r\n\t\t\t<div class="text-center">\r\n\t\t\t\t<a href="/home/overdue_items/" class="btn btn btn-primary ">Reset</a>\r\n\t\t\t</div>\r\n\t\t\r\n\r\n')
        else:
            __M_writer('\t\t\t<div class="text-center" >\r\n\t\t\t\t<h3>Email Notifcations are sending.</h3>\r\n\t\t\t</div>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Projects\\colonial\\home\\templates/overdue_ajax.html", "source_encoding": "ascii", "line_map": {"64": 33, "65": 35, "66": 35, "67": 35, "68": 36, "69": 36, "70": 37, "71": 37, "72": 45, "73": 46, "74": 47, "75": 48, "76": 48, "77": 48, "78": 51, "79": 54, "80": 56, "81": 58, "82": 68, "83": 69, "84": 73, "90": 84, "27": 0, "36": 1, "41": 75, "47": 4, "55": 4, "56": 14, "57": 15, "58": 16, "59": 20, "60": 25, "61": 31, "62": 33, "63": 33}, "uri": "overdue_ajax.html"}
__M_END_METADATA
"""
