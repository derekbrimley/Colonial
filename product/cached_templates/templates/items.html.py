# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428387258.903801
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial\\product\\templates/items.html'
_template_uri = 'items.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents', 'top_banner']


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
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

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
        __M_writer = context.writer()
        __M_writer('\r\n\t<span class="text-right">\r\n\t\t<a id="non-rentable" class="btn btn-primary">Non-Rentable Items</a>\r\n\t\t<a id="wardrobe" class="btn btn-primary">Wardrobe Items</a>\r\n\t\t<a id="rentable" class="btn btn-primary">Rentable Items</a>\r\n\t</span>\r\n\t<div id="items_container">\r\n\t</div>\r\n\r\n\t<div class="text-right">\r\n\t\t<a href="/product/items.create/" class="btn btn-success">Add an Item</a>\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Inventory</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"75": 69, "51": 7, "36": 1, "69": 3, "57": 7, "41": 5, "27": 0, "63": 3}, "source_encoding": "ascii", "uri": "items.html", "filename": "C:\\Users\\Derek\\python\\colonial\\colonial\\product\\templates/items.html"}
__M_END_METADATA
"""
