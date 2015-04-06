# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423607341.897491
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/orders.html'
_template_uri = 'orders.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def contents():
            return render_contents(context._locals(__M_locals))
        orders = context.get('orders', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
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


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contents():
            return render_contents(context)
        orders = context.get('orders', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\t\r\n')
        if request.user.has_perm('home.is_agent'):
            __M_writer('\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Order Date</th>\r\n\t\t\t\t<th>Phone</th>\r\n\t\t\t\t<th>Packed</th>\r\n\t\t\t\t<th>Paid</th>\r\n\t\t\t\t<th>Shipped</th>\r\n\t\t\t\t<th>Tracking Number</th>\r\n\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for order in orders:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(order.order_date))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.phone))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.date_packed))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.date_paid))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.date_shipped))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.tracking_number))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/orders.edit/')
                __M_writer(str(order.id))
                __M_writer('">Edit</a> | \r\n\t\t\t\t<a href="/home/orders.delete/')
                __M_writer(str(order.id))
                __M_writer('">Delete</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\t\t<div class="text-right">\r\n\t\t\t<a href="/home/orders.create/" class="btn btn-success">Add Item</a>\r\n\t\t</div>\r\n\r\n')
        elif request.user.has_perm('home.is_customer'):
            __M_writer('\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Order Date</th>\r\n\t\t\t\t<th>Phone</th>\r\n\t\t\t\t<th>Packed</th>\r\n\t\t\t\t<th>Paid</th>\r\n\t\t\t\t<th>Shipped</th>\r\n\t\t\t\t<th>Tracking Number</th>\r\n\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for order in orders:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(order.order_date))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.phone))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.date_packed))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.date_paid))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.date_shipped))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.tracking_number))
                __M_writer('</td>\r\n\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\t\t<div class="text-right">\r\n\t\t\t<a href="/home/orders.create/" class="btn btn-success">Make an Order</a>\r\n\t\t</div>\r\n\r\n')
        else:
            __M_writer('\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Order Date</th>\r\n\t\t\t\t<th>Phone</th>\r\n\t\t\t\t<th>Packed</th>\r\n\t\t\t\t<th>Paid</th>\r\n\t\t\t\t<th>Shipped</th>\r\n\t\t\t\t<th>Tracking Number</th>\r\n\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for order in orders:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(order.order_date))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.phone))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.date_packed))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.date_paid))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.date_shipped))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(order.tracking_number))
                __M_writer('</td>\r\n\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Orders</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "orders.html", "line_map": {"128": 3, "134": 128, "27": 0, "38": 1, "43": 5, "53": 9, "61": 9, "62": 12, "63": 13, "64": 26, "65": 27, "66": 27, "67": 27, "68": 28, "69": 28, "70": 29, "71": 29, "72": 30, "73": 30, "74": 31, "75": 31, "76": 32, "77": 32, "78": 34, "79": 34, "80": 35, "81": 35, "82": 39, "83": 45, "84": 46, "85": 58, "86": 59, "87": 59, "88": 59, "89": 60, "90": 60, "91": 61, "92": 61, "93": 62, "94": 62, "95": 63, "96": 63, "97": 64, "98": 64, "99": 68, "100": 74, "101": 75, "102": 87, "103": 88, "104": 88, "105": 88, "106": 89, "107": 89, "108": 90, "109": 90, "110": 91, "111": 91, "112": 92, "113": 92, "114": 93, "115": 93, "116": 97, "122": 3}, "source_encoding": "ascii", "filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/orders.html"}
__M_END_METADATA
"""
