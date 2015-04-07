# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428376875.079703
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\product\\templates/products.html'
_template_uri = 'products.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents', 'title', 'top_banner']


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
        products = context.get('products', UNDEFINED)
        photographs = context.get('photographs', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        photographs = context.get('photographs', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="search">\r\n\t<label for="search_input">Search Product:</label>\r\n    <input id="search_input" type="text">\r\n</div>\r\n<div class="products">\r\n\r\n')
        __M_writer('\r\n')
        __M_writer('\t\r\n\t\t\r\n')
        for product in products:
            __M_writer('\t\t<div class="item_container text-center">\r\n')
            for photo in photographs:
                if product.id == photo.id:
                    __M_writer('\t\t\t\t<img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('product/media/products/')
                    __M_writer(str( photo.id))
                    __M_writer('.jpg" />\r\n\t\t\t\t<div class="text-muted">')
                    __M_writer(str( product.name ))
                    __M_writer('</div>\r\n\t\t\t\t<div class="text-muted">')
                    __M_writer(str( product.price ))
                    __M_writer('</div>\r\n\t\t\t\t<div class="text-right">\r\n\t\t\t\t\t<a href="/product/products.detail/')
                    __M_writer(str( product.id ))
                    __M_writer('/')
                    __M_writer(str( photo.id ))
                    __M_writer('" data-product_id="')
                    __M_writer(str( product.id ))
                    __M_writer('" data-photo_id="')
                    __M_writer(str( photo.id ))
                    __M_writer('" class="show_detail btn btn-xs btn-primary">Show Detail</a>\r\n\r\n\t\t\t\t</div>\r\n')
            __M_writer('\t\t</div>\r\n')
        __M_writer('\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<title>Colonial Products</title>\r\n\t<meta name="Colonial Heritage Foundation Home Page" content="The Colonial Heritage Foundation promotes actively engaging the mind in history. TPurchase colonial products on this page for discounted prices.">\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Products</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.html", "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\product\\templates/products.html", "source_encoding": "ascii", "line_map": {"70": 14, "71": 25, "72": 27, "73": 29, "74": 30, "75": 31, "76": 32, "77": 33, "78": 33, "79": 33, "80": 33, "81": 33, "82": 34, "83": 34, "84": 35, "85": 35, "86": 37, "87": 37, "88": 37, "89": 37, "90": 37, "27": 0, "92": 37, "93": 37, "94": 42, "95": 44, "91": 37, "101": 3, "41": 1, "107": 3, "46": 6, "125": 119, "113": 8, "51": 10, "119": 8, "61": 14}}
__M_END_METADATA
"""
