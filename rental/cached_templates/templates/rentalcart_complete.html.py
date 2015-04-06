# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428044723.859768
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rentalcart_complete.html'
_template_uri = 'rentalcart_complete.html'
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
        cart_list = context.get('cart_list', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        dailyfee = context.get('dailyfee', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        __M_writer('\r\n')
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
        __M_writer('\r\n\t<div class="top_banner">Confirm Rentals</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cart_list = context.get('cart_list', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        def contents():
            return render_contents(context)
        str = context.get('str', UNDEFINED)
        dailyfee = context.get('dailyfee', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<br>\r\n\r\n\t<table class="table">\r\n\r\n    \t<tr>\r\n\t    \t<th>Product</th>\r\n\t    \t<th>Name</th>\r\n\t    \t<th>Quantity</th>\r\n    \t</tr>\r\n\r\n\t    <tr>\r\n')
        for product in cart_list:
            for photo in photos:
                if photo.id == product.id:
                    __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td class="text-center">\r\n\t\t\t\t        <img class="image" src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('product/media/products/')
                    __M_writer(str( photo.id ))
                    __M_writer('.jpg" />\r\n\t\t\t\t        </td>\r\n\t\t\t\t       \t<td>')
                    __M_writer(str(product.name))
                    __M_writer('</td>\r\n\t\t\t\t       \t<td>Quantity: ')
                    __M_writer(str(cart[str(product.id)]))
                    __M_writer('</td>\r\n\t\t\t\t    </tr>\r\n')
            __M_writer('\t\t</tr>\r\n')
        __M_writer('\r\n\t</table>\r\n\r\n\t<div class="text-center">\r\n\t\t<h3 class="total_price">Daily Fee: $')
        __M_writer(str(dailyfee))
        __M_writer('</h3>\r\n\t</div>\r\n\r\n\t<div class="text-center">\r\n    \t<td><a href="/rental/rentals.checkout/" class="checkout_button btn btn-warning btn" role="button">Check Out</a></td>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 3, "70": 13, "82": 13, "83": 25, "84": 26, "85": 27, "86": 28, "87": 30, "88": 30, "89": 30, "90": 30, "91": 32, "92": 32, "93": 33, "94": 33, "95": 37, "96": 39, "97": 43, "98": 43, "27": 0, "104": 98, "42": 1, "47": 5, "48": 12, "58": 3}, "filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rentalcart_complete.html", "source_encoding": "ascii", "uri": "rentalcart_complete.html"}
__M_END_METADATA
"""
