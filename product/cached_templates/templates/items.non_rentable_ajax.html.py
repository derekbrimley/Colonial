# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428385231.495708
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\product\\templates/items.non_rentable_ajax.html'
_template_uri = 'items.non_rentable_ajax.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['content']


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
    return runtime._inherit_from(context, '/product/templates/base_ajax.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def content():
            return render_content(context._locals(__M_locals))
        product_infos = context.get('product_infos', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def content():
            return render_content(context)
        product_infos = context.get('product_infos', UNDEFINED)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t<tr>\r\n\t\t\t<th>Name</th>\r\n\t\t\t<th>Description</th>\r\n\t\t\t<th>Price</th>\r\n\t\t\t<th>Category</th>\r\n\t\t\t<th>Vendor</th>\r\n\t\t\t<th>Quantity</th>\r\n\t\t\t<th>Actions</th>\r\n\t\t</tr>\r\n')
        for product in products:
            if product.is_rentable == False:
                for product_info in product_infos:
                    if product_info.id == product.id:
                        __M_writer('\t\t\t\t\t\t<tr>\r\n\t\t\t\t\t\t\t<td>')
                        __M_writer(str(product_info.name))
                        __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                        __M_writer(str(product_info.description))
                        __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                        __M_writer(str(product_info.price))
                        __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                        __M_writer(str(product_info.category))
                        __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                        __M_writer(str(product_info.vendor))
                        __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>')
                        __M_writer(str(product.quantity_on_hand))
                        __M_writer('</td>\r\n\t\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t\t<a href="/product/items.edit/')
                        __M_writer(str(product.id))
                        __M_writer('">Edit</a> | \r\n\t\t\t\t\t\t\t\t<a href="/product/items.delete/')
                        __M_writer(str(product.id))
                        __M_writer('">Delete</a>\r\n\t\t\t\t\t\t\t</td>\r\n\t\t\t\t\t\t</tr>\r\n')
        __M_writer('\t</table>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "items.non_rentable_ajax.html", "line_map": {"64": 21, "65": 21, "66": 22, "67": 22, "68": 23, "69": 23, "70": 24, "71": 24, "72": 26, "73": 26, "74": 27, "75": 27, "76": 34, "82": 76, "27": 0, "36": 1, "46": 3, "54": 3, "55": 14, "56": 15, "57": 16, "58": 17, "59": 18, "60": 19, "61": 19, "62": 20, "63": 20}, "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\product\\templates/items.non_rentable_ajax.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
