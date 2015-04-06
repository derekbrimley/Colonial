# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427917235.572978
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rentalcart.detail.html'
_template_uri = 'rentalcart.detail.html'
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
        request = context.get('request', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        __M_writer('\r\n\r\n')
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
        __M_writer('\r\n\t<div class="top_banner">Modify Rental</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        cart_list = context.get('cart_list', UNDEFINED)
        request = context.get('request', UNDEFINED)
        photos = context.get('photos', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        __M_writer('\t<table class="table">\r\n\r\n')
        for product in cart_list:
            for photo in photos:
                if photo.id == product.id:
                    __M_writer('\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t<td>\r\n\t\t\t\t        <img class="image" src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('product/media/products/')
                    __M_writer(str( photo.id ))
                    __M_writer('.jpg" />\r\n\t\t\t\t        </td>\r\n\t\t\t\t       \t<td>')
                    __M_writer(str(product.name))
                    __M_writer('</td>\r\n\t\t\t\t        <td>Quantity: ?</td>\r\n\t\t\t\t    </tr>\r\n')
        __M_writer('\r\n\t</table>\r\n\r\n\r\n')
        if request.user.is_authenticated():
            __M_writer('\t<div class="text-center">\r\n    <td><a href="/rental/rentals.rentalcart_checkout/" class="checkout_button btn btn-warning btn" role="button">Checkout</a></td>\r\n    </div>\r\n')
        else:
            __M_writer('\t<div class="text-center">\r\n        <button class="show_login_dialog btn btn-primary">Sign In</button>\r\n   \t</div>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rentalcart.detail.html", "source_encoding": "ascii", "filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rentalcart.detail.html", "line_map": {"68": 14, "78": 14, "79": 18, "80": 20, "81": 21, "82": 22, "83": 23, "84": 25, "85": 25, "86": 25, "87": 25, "88": 27, "89": 27, "90": 33, "91": 38, "92": 39, "93": 42, "94": 43, "95": 47, "27": 0, "101": 95, "40": 1, "45": 5, "46": 12, "56": 3, "62": 3}}
__M_END_METADATA
"""
