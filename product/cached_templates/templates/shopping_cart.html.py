# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428053341.8687
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\product\\templates/shopping_cart.html'
_template_uri = 'shopping_cart.html'
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
    return runtime._inherit_from(context, '/user/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def contents():
            return render_contents(context._locals(__M_locals))
        str = context.get('str', UNDEFINED)
        request = context.get('request', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart_list = context.get('cart_list', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        total_price = context.get('total_price', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
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
        str = context.get('str', UNDEFINED)
        request = context.get('request', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        cart_list = context.get('cart_list', UNDEFINED)
        cart = context.get('cart', UNDEFINED)
        total_price = context.get('total_price', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="text-center">\r\n\t<img class="headertitle" height="100" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/colonialheritage.png" alt="The Colonial Heritage Foundation">\r\n</div>\r\n\r\n\r\n')
        __M_writer('<table class="table">\r\n\r\n')
        for product in cart_list:
            for photo in photos:
                if photo.id == product.id:
                    __M_writer('\t\t\t\t<tr>\r\n\t\t\t\t\t<td>\r\n\t\t\t        <img class="image" src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('product/media/products/')
                    __M_writer(str( photo.id ))
                    __M_writer('.jpg" />\r\n\t\t\t        </td>\r\n\t\t\t       \t<td>')
                    __M_writer(str(product.name))
                    __M_writer('</td>\r\n\t\t\t        <td>Quantity: ')
                    __M_writer(str(cart[str(product.id)]))
                    __M_writer('</td>\r\n\t\t\t        <td><a data-product_id="')
                    __M_writer(str( product.id ))
                    __M_writer('" class="delete_button btn btn-danger btn-xs" role="button">Delete</a></td>\r\n\t\t\t    </tr>\r\n')
        __M_writer('\r\n</table>\r\n<div class="text-center">\r\n<h3 class="total_price">TOTAL: $')
        __M_writer(str(total_price))
        __M_writer('</h3>\r\n</div>\r\n\r\n')
        if request.user.is_authenticated():
            __M_writer('\t<div class="text-center">\r\n    <td><a href="/product/shopping_cart.checkout/')
            __M_writer(str(total_price))
            __M_writer('/')
            __M_writer(str( request.user.id ))
            __M_writer('" class="checkout_button btn btn-warning btn" role="button">Check Out</a></td>\r\n    </div>\r\n')
        else:
            __M_writer('\t<div class="text-center">\r\n        <button class="show_login_dialog btn btn-primary">Sign In</button>\r\n   \t</div>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"65": 11, "66": 14, "67": 14, "68": 19, "69": 21, "70": 22, "71": 23, "72": 24, "73": 26, "74": 26, "75": 26, "76": 26, "77": 28, "78": 28, "79": 29, "80": 29, "81": 30, "82": 30, "83": 35, "84": 38, "85": 38, "86": 42, "87": 43, "88": 44, "89": 44, "90": 44, "27": 0, "92": 46, "93": 47, "94": 51, "91": 44, "100": 94, "41": 1, "42": 9, "52": 11}, "filename": "C:\\Python34\\Projects\\colonial\\product\\templates/shopping_cart.html", "uri": "shopping_cart.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
