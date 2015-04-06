# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423283333.788398
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/products.html'
_template_uri = 'products.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        products = context.get('products', UNDEFINED)
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
        __M_writer('\r\n\t<div class="top_banner">Products</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context)
        products = context.get('products', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        if request.user.has_perm('home.is_manager'):
            __M_writer('\t\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Category</th>\r\n\t\t\t\t<th>Current Price</th>\r\n\t\t\t\t<th>Bulk</th>\r\n\t\t\t\t<th>Custom</th>\r\n\t\t\t\t<th>Individual</th>\r\n\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for product in products:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(product.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.category))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.current_price))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.is_bulk))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.is_custom))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.is_individual))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/products.edit/')
                __M_writer(str(product.id))
                __M_writer('">Edit</a> | \r\n\t\t\t\t<a href="/home/products.delete/')
                __M_writer(str(product.id))
                __M_writer('">Delete</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\t\t<div class="text-right">\r\n\t\t\t<a href="/home/products.create/" class="btn btn-success">Add Item</a>\r\n\t\t</div>\r\n\r\n')
        elif request.user.has_perm('home.is_agent'):
            __M_writer('\t\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Category</th>\r\n\t\t\t\t<th>Current Price</th>\r\n\t\t\t\t<th>Bulk</th>\r\n\t\t\t\t<th>Custom</th>\r\n\t\t\t\t<th>Individual</th>\r\n\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for product in products:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(product.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.category))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.current_price))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.is_bulk))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.is_custom))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.is_individual))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/products.edit/')
                __M_writer(str(product.id))
                __M_writer('">Edit</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n')
        else:
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Category</th>\r\n\t\t\t\t<th>Current Price</th>\r\n\t\t\t\t<th>Bulk</th>\r\n\t\t\t\t<th>Custom</th>\r\n\t\t\t\t<th>Individual</th>\r\n\t\t\t</tr>\r\n\r\n\t\t\t<tr>\r\n')
            for product in products:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(product.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.category))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.current_price))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.is_bulk))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.is_custom))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(product.is_individual))
                __M_writer('</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"128": 97, "129": 98, "130": 98, "131": 99, "132": 99, "133": 100, "134": 100, "135": 101, "136": 101, "137": 104, "143": 137, "27": 0, "38": 1, "43": 5, "53": 3, "59": 3, "65": 9, "73": 9, "74": 11, "75": 12, "76": 13, "77": 28, "78": 29, "79": 29, "80": 29, "81": 30, "82": 30, "83": 31, "84": 31, "85": 32, "86": 32, "87": 33, "88": 33, "89": 34, "90": 34, "91": 35, "92": 35, "93": 37, "94": 37, "95": 38, "96": 38, "97": 42, "98": 48, "99": 49, "100": 64, "101": 65, "102": 65, "103": 65, "104": 66, "105": 66, "106": 67, "107": 67, "108": 68, "109": 68, "110": 69, "111": 69, "112": 70, "113": 70, "114": 71, "115": 71, "116": 73, "117": 73, "118": 77, "119": 79, "120": 80, "121": 94, "122": 95, "123": 95, "124": 95, "125": 96, "126": 96, "127": 97}, "uri": "products.html", "source_encoding": "ascii", "filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/products.html"}
__M_END_METADATA
"""
