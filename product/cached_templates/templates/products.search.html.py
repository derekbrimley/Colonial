# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1425794099.807721
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\product\\templates/products.search.html'
_template_uri = 'products.search.html'
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
        photographs = context.get('photographs', UNDEFINED)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
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
        photographs = context.get('photographs', UNDEFINED)
        products = context.get('products', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t\t<div class="top_banner">Search Results</div>\r\n\r\n')
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
                    __M_writer('</div>\r\n')
            __M_writer('\t\t</div>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"64": 15, "65": 15, "66": 15, "27": 0, "68": 16, "37": 1, "70": 17, "71": 20, "72": 22, "78": 72, "47": 3, "67": 16, "69": 17, "56": 3, "57": 9, "58": 11, "59": 12, "60": 13, "61": 14, "62": 15, "63": 15}, "uri": "products.search.html", "filename": "C:\\Python34\\Scripts\\colonial\\product\\templates/products.search.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
