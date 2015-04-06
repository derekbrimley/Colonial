# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427944889.883097
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.add.html'
_template_uri = 'rentals.add.html'
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
        rentable = context.get('rentable', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
        photographs = context.get('photographs', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        wardrobe = context.get('wardrobe', UNDEFINED)
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


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Choose Rental</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rentable = context.get('rentable', UNDEFINED)
        def contents():
            return render_contents(context)
        products = context.get('products', UNDEFINED)
        photographs = context.get('photographs', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        wardrobe = context.get('wardrobe', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="search">\r\n\t<label for="search_input">Search Product:</label>\r\n    <input id="search_input" type="text">\r\n</div>\r\n\r\n\r\n\r\n')
        __M_writer('\r\n<div class="row">\r\n\r\n\t<div class="col-md-6 wardrobe"><h2 class="text-center">Wardrobe Items</h2>\r\n\r\n')
        for item in wardrobe:
            __M_writer('\t\t\t<div class="item_container text-center">\r\n')
            for photo in photographs:
                if item.id == photo.id:
                    __M_writer('\t\t\t\t\t\t<img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('product/media/products/')
                    __M_writer(str( photo.id))
                    __M_writer('.jpg" />\r\n')
                    for product in products:
                        if item.id == product.id:
                            __M_writer('\t\t\t\t\t\t\t\t<div class="text-muted">')
                            __M_writer(str( product.name ))
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<div class="text-muted">')
                            __M_writer(str( product.price ))
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<div class="text-right">\r\n\t\t\t\t\t\t\t\t\t<button data-product_id="')
                            __M_writer(str( product.id ))
                            __M_writer('" data-photo_id="')
                            __M_writer(str( photo.id ))
                            __M_writer('" data-item_id="')
                            __M_writer(str( item.id ))
                            __M_writer('" class="add_rental btn btn-xs btn-warning">Add</a>\r\n\t\t\t\t\t\t\t\t</div>\r\n')
            __M_writer('\t\t\t</div>\r\n')
        __M_writer('\r\n\t</div>\r\n\r\n\t<div class="col-md-6 rentable"><h2 class="text-center"class="text-center">Other Items</h2>\r\n\r\n')
        for item in rentable:
            __M_writer('\t\t\t<div class="item_container text-center">\r\n')
            for photo in photographs:
                if item.id == photo.id:
                    __M_writer('\t\t\t\t\t\t<img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('product/media/products/')
                    __M_writer(str( photo.id))
                    __M_writer('.jpg" />\r\n')
                    for product in products:
                        if item.id == product.id:
                            __M_writer('\t\t\t\t\t\t\t\t<div class="text-muted">')
                            __M_writer(str( product.name ))
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<div class="text-muted">')
                            __M_writer(str( product.price ))
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<div class="text-right">\r\n\t\t\t\t\t\t\t\t\t<button data-product_id="')
                            __M_writer(str( product.id ))
                            __M_writer('" data-photo_id="')
                            __M_writer(str( photo.id ))
                            __M_writer('" data-item_id="')
                            __M_writer(str( item.id ))
                            __M_writer('" class="add_rental btn btn-xs btn-warning">Add</a>\r\n\t\t\t\t\t\t\t\t</div>\r\n')
            __M_writer('\t\t\t</div>\r\n')
        __M_writer('\t</div>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "uri": "rentals.add.html", "line_map": {"128": 69, "134": 128, "27": 0, "41": 1, "46": 5, "56": 3, "62": 3, "68": 9, "79": 9, "80": 23, "81": 28, "82": 29, "83": 30, "84": 31, "85": 32, "86": 32, "87": 32, "88": 32, "89": 32, "90": 33, "91": 34, "92": 35, "93": 35, "94": 35, "95": 36, "96": 36, "97": 38, "98": 38, "99": 38, "100": 38, "101": 38, "102": 38, "103": 44, "104": 46, "105": 51, "106": 52, "107": 53, "108": 54, "109": 55, "110": 55, "111": 55, "112": 55, "113": 55, "114": 56, "115": 57, "116": 58, "117": 58, "118": 58, "119": 59, "120": 59, "121": 61, "122": 61, "123": 61, "124": 61, "125": 61, "126": 61, "127": 67}, "filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.add.html"}
__M_END_METADATA
"""
