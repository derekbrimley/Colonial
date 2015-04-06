# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428032363.639278
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\product\\templates/products.detail.html'
_template_uri = 'products.detail.html'
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
        product = context.get('product', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        photo = context.get('photo', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n')
        __M_writer('#\r\n')
        __M_writer('#\r\n')
        __M_writer('#\r\n')
        __M_writer('#\r\n#\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        product = context.get('product', UNDEFINED)
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">')
        __M_writer(str( product.name ))
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        photo = context.get('photo', UNDEFINED)
        product = context.get('product', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        __M_writer('\t \t<div class="text-center">\r\n\t \t<div class="item_container">\r\n\t  \t\t\t<img id="product_image" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('product/media/products/')
        __M_writer(str( photo.id))
        __M_writer('.jpg" />\r\n\t  \t\t\t<div class="text-muted">')
        __M_writer(str( product.name ))
        __M_writer('</div>\r\n\t  \t\t\t<div class="text-muted">')
        __M_writer(str( product.price ))
        __M_writer('</div>\r\n\t  \t\t\t<br />\r\n\t  \t\t\t<div class="product_dropdown selectpicker" "text-center">\r\n  \t\t\t        Qty:\r\n  \t\t\t        <select>\r\n  \t\t\t            <option value="1">1</option>\r\n  \t\t\t            <option value="2">2</option>\r\n  \t\t\t            <option value="3">3</option>\r\n  \t\t\t            <option value="4">4</option>\r\n  \t\t\t            <option value="5">5</option>\r\n  \t\t\t        </select>\r\n\t \t\t\t\t<button data-product_id="')
        __M_writer(str( product.id ))
        __M_writer('" data-photo_id="')
        __M_writer(str( photo.id ))
        __M_writer('" class="add_button btn btn btn-warning">Add to Cart</button>\r\n\t \t\t\t</div>\r\n\t \t</div>\r\n\t \t</div>\r\n\t \r\n')
        __M_writer('\t<h3>')
        __M_writer(str( product.name ))
        __M_writer(' Details</h3>\r\n\t<table id="display_table" class="table table-striped table-bordered">\t\r\n\t\t<tr>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Description</th>\r\n\t\t\t<th>Price</th>\r\n\t\t\t<th>Avg Price</th>\r\n\t\t\t<th>Manufacturer</th>\r\n\t\t</tr>\r\n\t\t<tr>\r\n\t\t\t<td>')
        __M_writer(str(product.name))
        __M_writer('</td>\r\n\t\t\t<td>')
        __M_writer(str(product.description))
        __M_writer('</td>\r\n\t\t\t<td>')
        __M_writer(str(product.price))
        __M_writer('</td>\r\n\t\t\t<td>')
        __M_writer(str(product.average_cost))
        __M_writer('</td>\r\n\t\t\t<td>')
        __M_writer(str(product.manufacturer))
        __M_writer('</td>\r\n\t\t</tr>\r\n\t</table>\r\n\r\n\t<div class="text-left">\r\n\t\t<a href="/product/products/" class="btn btn btn-primary">Back</a>\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "products.detail.html", "filename": "C:\\Python34\\Projects\\colonial\\product\\templates/products.detail.html", "line_map": {"66": 3, "67": 4, "68": 4, "108": 48, "74": 8, "83": 8, "84": 12, "85": 14, "86": 16, "87": 16, "88": 16, "89": 16, "90": 17, "27": 0, "92": 18, "93": 18, "94": 29, "95": 29, "96": 29, "97": 29, "98": 35, "91": 17, "100": 35, "101": 45, "102": 45, "39": 1, "104": 46, "105": 47, "106": 47, "103": 46, "44": 5, "109": 49, "110": 49, "99": 35, "49": 57, "50": 65, "51": 68, "52": 70, "53": 77, "116": 110, "59": 3, "107": 48}, "source_encoding": "ascii"}
__M_END_METADATA
"""
