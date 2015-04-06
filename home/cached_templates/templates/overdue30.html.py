# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428138122.34377
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\home\\templates/overdue30.html'
_template_uri = 'overdue30.html'
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
        def contents():
            return render_contents(context._locals(__M_locals))
        users = context.get('users', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        transactions = context.get('transactions', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
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
        users = context.get('users', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        transactions = context.get('transactions', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<br>\r\n\r\n')
        __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Rental ID</th>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Email</th>\r\n\t\t\t\t<th>Price</th>\r\n\t\t\t\t<th>Date Rented</th>\r\n\t\t\t\t<th>Date Due</th>\r\n\t\t\t\t<th>Product</th>\r\n\t\t\t</tr>\r\n\r\n')
        __M_writer('\t\t\t\t<tr>\r\n')
        for rental in rentals:
            for transaction in transactions:
                if rental.transaction_id == transaction.id:
                    __M_writer('\t\t\t\t\t\t\t\t<td>')
                    __M_writer(str(rental.id))
                    __M_writer('</td>\r\n\r\n')
                    for user in users:
                        if transaction.customer_id == user.id:
                            __M_writer('\t\t\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(user.first_name))
                            __M_writer(' ')
                            __M_writer(str(user.last_name))
                            __M_writer('</td>\r\n\t\t\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(user.email))
                            __M_writer('</td>\r\n')
                    __M_writer('\r\n\t\t\t\t\t\t\t\t<td>')
                    __M_writer(str(rental.price))
                    __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                    __M_writer(str(rental.date_out))
                    __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                    __M_writer(str(rental.date_due))
                    __M_writer('</td>\r\n\r\n\r\n')
                    for product in products:
                        if product.id == rental.rentable_product_id:
                            __M_writer('\t\t\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(product.name))
                            __M_writer('</td>\r\n')
            __M_writer('\r\n\r\n\t\t\t\t\t</tr>\r\n')
        __M_writer('\t\t\t</table>\r\n\r\n\t\t\t<div class="text-center">\r\n\t\t\t\t<a href="/rental/rentals/" class="btn btn btn-primary ">Back</a>\r\n\t\t\t\t<a href="/rental/rentals.add_customer/" class="btn btn btn-success">Add New Rental</a>\r\n\t\t\t</div>\r\n\t\t\r\n\r\n')
        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Projects\\colonial\\home\\templates/overdue30.html", "line_map": {"64": 31, "65": 31, "66": 31, "67": 33, "68": 34, "69": 35, "70": 35, "71": 35, "72": 35, "73": 35, "74": 36, "75": 36, "76": 39, "77": 40, "78": 40, "79": 41, "80": 41, "81": 42, "82": 42, "83": 45, "84": 46, "85": 47, "86": 47, "87": 47, "88": 52, "89": 56, "90": 70, "27": 0, "96": 90, "38": 1, "48": 4, "58": 4, "59": 14, "60": 27, "61": 28, "62": 29, "63": 30}, "uri": "overdue30.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
