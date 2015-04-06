# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428040708.094394
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rental_cart.html'
_template_uri = 'rental_cart.html'
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
    return runtime._inherit_from(context, '/rental/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        cart_list = context.get('cart_list', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        total_price = context.get('total_price', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cart_list = context.get('cart_list', UNDEFINED)
        str = context.get('str', UNDEFINED)
        def contents():
            return render_contents(context)
        request = context.get('request', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        total_price = context.get('total_price', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="text-center">\r\n\t<div>')
        __M_writer(str( request.urlparams[0] ))
        __M_writer('</div>\r\n\t<img class="headertitle" height="100" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/colonialheritage.png" alt="The Colonial Heritage Foundation">\r\n</div>\r\n<br>\r\n\r\n')
        __M_writer('\t<table class="table">\r\n\t    \t<tr>\r\n\t\t    \t<th>Product</th>\r\n\t\t    \t<th>Name</th>\r\n\t\t    \t<th>Quantity</th>\r\n\t\t    \t<th>Delete</th>\r\n\t    \t</tr>\r\n\t    <tr>\r\n')
        for product in cart_list:
            for photo in photos:
                if photo.id == product.id:
                    __M_writer('\r\n\t\t\t\t\t\r\n\t\t\t\t\t\t<td class="text-center">\r\n\t\t\t\t        <img class="image" src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('product/media/products/')
                    __M_writer(str( photo.id ))
                    __M_writer('.jpg" />\r\n\t\t\t\t        </td>\r\n\t\t\t\t       \t<td>')
                    __M_writer(str(product.name))
                    __M_writer('</td>\r\n\t\t\t\t       \t<td>Quantity: ')
                    __M_writer(str(cart[str(product.id)]))
                    __M_writer('</td>\r\n\t\t\t\t        <td><a data-product_id="')
                    __M_writer(str( product.id ))
                    __M_writer('" class="delete_button btn btn-danger btn-xs" role="button">Delete</a></td>\r\n\t\t\t\t    </tr>\r\n')
            __M_writer('\t\t\t</tr>\r\n')
        __M_writer('\r\n\t</table>\r\n\r\n\t<div class="text-center">\r\n\t\t<h3 class="total_price">Daily Fee: $')
        __M_writer(str(total_price))
        __M_writer('</h3>\r\n\t</div>\r\n\r\n\t<div class="text-center">\r\n    \t<td><a href="/rental/rentals.rentalcart_build/')
        __M_writer(str(total_price))
        __M_writer('/" class="checkout_button btn btn-success btn" role="button">Build Rental</a></td>\r\n    </div>\r\n\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 8, "66": 11, "67": 11, "68": 12, "69": 12, "70": 17, "71": 25, "72": 26, "73": 27, "74": 28, "75": 31, "76": 31, "77": 31, "78": 31, "79": 33, "80": 33, "81": 34, "82": 34, "83": 35, "84": 35, "85": 39, "86": 41, "87": 45, "88": 45, "89": 49, "90": 49, "27": 0, "96": 90, "41": 1, "42": 7, "52": 8}, "uri": "rental_cart.html", "filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rental_cart.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
