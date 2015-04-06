# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428034812.639029
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.add_rentals.html'
_template_uri = 'rentals.add_rentals.html'
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
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        photographs = context.get('photographs', UNDEFINED)
        customer = context.get('customer', UNDEFINED)
        products = context.get('products', UNDEFINED)
        wardrobe = context.get('wardrobe', UNDEFINED)
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


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        customer = context.get('customer', UNDEFINED)
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Choose Rentals for ')
        __M_writer(str( customer.first_name))
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rentable = context.get('rentable', UNDEFINED)
        def contents():
            return render_contents(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        photographs = context.get('photographs', UNDEFINED)
        customer = context.get('customer', UNDEFINED)
        products = context.get('products', UNDEFINED)
        wardrobe = context.get('wardrobe', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n<div class="search">\r\n\t<label for="search_input">Search Product:</label>\r\n    <input id="search_input" type="text">\r\n</div>\r\n\r\n\r\n\r\n\r\n\r\n')
        __M_writer('\r\n<div class="row">\r\n<div class="text-center">\r\n<div class="product_dropdown selectpicker" "text-center">\r\n    <h2>Choose Quantity</h2>\r\n    <select>\r\n        <option value="1">1</option>\r\n        <option value="2">2</option>\r\n        <option value="3">3</option>\r\n        <option value="4">4</option>\r\n        <option value="5">5</option>\r\n       \t<option value="6">6</option>\r\n        <option value="7">7</option>\r\n        <option value="8">8</option>\r\n        <option value="9">9</option>\r\n        <option value="10">10</option>\r\n    </select>\r\n</div>\r\n<h2>Choose Product</h2>\r\n</div>\r\n\r\n\t<div class="col-md-6 wardrobe"><h2 class="text-center"><small>Wardrobe Items</small></h2>\r\n\r\n')
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
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<div class="text-muted">Daily Fee: ')
                            __M_writer(str( item.cost ))
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<div class="text-muted">Available: ')
                            __M_writer(str( item.quantity_on_hand ))
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<button data-product_id="')
                            __M_writer(str( product.id ))
                            __M_writer('" data-photo_id="')
                            __M_writer(str( photo.id ))
                            __M_writer('" data-item_id="')
                            __M_writer(str( item.id ))
                            __M_writer('" data-customer_id="')
                            __M_writer(str( customer.id ))
                            __M_writer('" class="add_rental btn btn-xs btn-warning">Add</button>\r\n')
            __M_writer('\t\t\t</div>\r\n')
        __M_writer('\r\n\t</div>\r\n\r\n\t<div class="col-md-6 rentable"><h1 class="text-center"><small>Other Items</small></h1>\r\n\r\n')
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
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<div class="text-muted">Daily Fee: ')
                            __M_writer(str( item.cost ))
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<div class="text-muted">Available: ')
                            __M_writer(str( item.quantity_on_hand ))
                            __M_writer('</div>\r\n\t\t\t\t\t\t\t\t<div class="text-right">\r\n\t\t\t\t\t\t\t\t\t<button data-product_id="')
                            __M_writer(str( product.id ))
                            __M_writer('" data-photo_id="')
                            __M_writer(str( photo.id ))
                            __M_writer('" data-item_id="')
                            __M_writer(str( item.id ))
                            __M_writer('" data-customer_id="')
                            __M_writer(str( customer.id ))
                            __M_writer('"  class="add_rental btn btn-xs btn-warning">Add</a>\r\n\t\t\t\t\t\t\t\t</div>\r\n')
            __M_writer('\t\t\t</div>\r\n')
        __M_writer('\t</div>\r\n</div>\r\n\r\n<div class="text-center">\r\n\t<button class="show_rentalcart btn btn btn-primary">Show Cart</button>\r\n</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.add_rentals.html", "line_map": {"128": 79, "129": 79, "130": 80, "131": 80, "132": 82, "133": 82, "134": 82, "135": 82, "136": 82, "137": 82, "138": 82, "139": 82, "140": 88, "141": 90, "147": 141, "27": 0, "42": 1, "47": 5, "57": 3, "64": 3, "65": 4, "66": 4, "72": 9, "84": 9, "85": 26, "86": 49, "87": 50, "88": 51, "89": 52, "90": 53, "91": 53, "92": 53, "93": 53, "94": 53, "95": 54, "96": 55, "97": 56, "98": 56, "99": 56, "100": 57, "101": 57, "102": 58, "103": 58, "104": 59, "105": 59, "106": 59, "107": 59, "108": 59, "109": 59, "110": 59, "111": 59, "112": 64, "113": 66, "114": 71, "115": 72, "116": 73, "117": 74, "118": 75, "119": 75, "120": 75, "121": 75, "122": 75, "123": 76, "124": 77, "125": 78, "126": 78, "127": 78}, "uri": "rentals.add_rentals.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
