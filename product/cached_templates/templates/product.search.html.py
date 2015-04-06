# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427469129.213916
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\product\\templates/product.search.html'
_template_uri = '/product.search.html/'
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
        photographs = context.get('photographs', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
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
        photographs = context.get('photographs', UNDEFINED)
        products = context.get('products', UNDEFINED)
        def contents():
            return render_contents(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n\r\n')
        __M_writer('\r\n')
        for photo in photographs:
            __M_writer('\t\t<div class="item_container text-center">\r\n')
            for product in products:
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
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Projects\\colonial\\product\\templates/product.search.html", "line_map": {"64": 17, "65": 17, "66": 17, "67": 18, "68": 18, "69": 19, "70": 19, "71": 21, "72": 21, "73": 21, "74": 21, "75": 21, "76": 21, "77": 21, "78": 21, "79": 26, "80": 28, "86": 80, "27": 0, "37": 1, "47": 4, "56": 4, "57": 11, "58": 13, "59": 14, "60": 15, "61": 16, "62": 17, "63": 17}, "source_encoding": "ascii", "uri": "/product.search.html/"}
__M_END_METADATA
"""
