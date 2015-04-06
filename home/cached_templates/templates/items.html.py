# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1423296227.003454
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\colonial\\home\\templates/items.html'
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
    return runtime._inherit_from(context, 'base.htm', _template_uri)
def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        request = context.get('request', UNDEFINED)
        items = context.get('items', UNDEFINED)
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


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def contents():
            return render_contents(context)
        request = context.get('request', UNDEFINED)
        items = context.get('items', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        if request.user.has_perm('home.is_manager'):
            __M_writer('\t\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Value</th>\r\n\t\t\t\t<th>Standard Rental Price</th>\r\n\t\t\t\t<th>Rentable</th>\r\n\t\t\t\t<th>Size</th>\r\n\t\t\t\t<th>Size Modifier</th>\r\n\t\t\t\t<th>Gender</th>\r\n\t\t\t\t<th>Color</th>\r\n\t\t\t\t<th>Pattern</th>\r\n\t\t\t\t<th>Start Year</th>\r\n\t\t\t\t<th>End Year</th>\r\n\t\t\t\t<th>Notes</th>\r\n\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for item in items:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(item.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.value))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.standard_rental_price))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.rentable))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.size))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.size_modifier))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.gender))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.color))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.pattern))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.start_year))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.end_year))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.note))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/items.edit/')
                __M_writer(str(item.id))
                __M_writer('">Edit</a> | \r\n\t\t\t\t<a href="/home/items.delete/')
                __M_writer(str(item.id))
                __M_writer('">Delete</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n\t\t<div class="text-right">\r\n\t\t\t<a href="/home/items.create/" class="btn btn-success">Add an Item</a>\r\n\t\t</div>\r\n\r\n')
        elif request.user.has_perm('home.is_agent'):
            __M_writer('\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Value</th>\r\n\t\t\t\t<th>Standard Rental Price</th>\r\n\t\t\t\t<th>Rentable</th>\r\n\t\t\t\t<th>Size</th>\r\n\t\t\t\t<th>Size Modifier</th>\r\n\t\t\t\t<th>Gender</th>\r\n\t\t\t\t<th>Color</th>\r\n\t\t\t\t<th>Pattern</th>\r\n\t\t\t\t<th>Start Year</th>\r\n\t\t\t\t<th>End Year</th>\r\n\t\t\t\t<th>Notes</th>\r\n\t\t\t\t<th>Actions</th>\r\n\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for item in items:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(item.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.value))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.standard_rental_price))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.rentable))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.size))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.size_modifier))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.gender))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.color))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.pattern))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.start_year))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.end_year))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.note))
                __M_writer('</td>\r\n\t\t\t\t<td>\r\n\t\t\t\t<a href="/home/items.edit/')
                __M_writer(str(item.id))
                __M_writer('">Edit</a>\r\n\t\t\t\t</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n')
        else:
            __M_writer('\r\n\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\r\n\t\t\t<tr>\r\n\t\t\t\t<th>Name</th>\r\n\t\t\t\t<th>Description</th>\r\n\t\t\t\t<th>Value</th>\r\n\t\t\t\t<th>Standard Rental Price</th>\r\n\t\t\t\t<th>Rentable</th>\r\n\t\t\t\t<th>Size</th>\r\n\t\t\t\t<th>Size Modifier</th>\r\n\t\t\t\t<th>Gender</th>\r\n\t\t\t\t<th>Color</th>\r\n\t\t\t\t<th>Pattern</th>\r\n\t\t\t\t<th>Start Year</th>\r\n\t\t\t\t<th>End Year</th>\r\n\t\t\t\t<th>Notes</th>\r\n\r\n\t\t\t</tr>\r\n\t\t\t<tr>\r\n')
            for item in items:
                __M_writer('\t\t\t\t<td>')
                __M_writer(str(item.name))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.description))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.value))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.standard_rental_price))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.rentable))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.size))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.size_modifier))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.gender))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.color))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.pattern))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.start_year))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.end_year))
                __M_writer('</td>\r\n\t\t\t\t<td>')
                __M_writer(str(item.note))
                __M_writer('</td>\r\n\t\t\t</tr>\r\n')
            __M_writer('\t\t</table>\r\n\r\n')
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
{"uri": "items.html", "line_map": {"27": 0, "38": 1, "43": 5, "53": 9, "61": 9, "62": 11, "63": 12, "64": 13, "65": 34, "66": 35, "67": 35, "68": 35, "69": 36, "70": 36, "71": 37, "72": 37, "73": 38, "74": 38, "75": 39, "76": 39, "77": 40, "78": 40, "79": 41, "80": 41, "81": 42, "82": 42, "83": 43, "84": 43, "85": 44, "86": 44, "87": 45, "88": 45, "89": 46, "90": 46, "91": 47, "92": 47, "93": 49, "94": 49, "95": 50, "96": 50, "97": 54, "98": 60, "99": 61, "100": 80, "101": 81, "102": 81, "103": 81, "104": 82, "105": 82, "106": 83, "107": 83, "108": 84, "109": 84, "110": 85, "111": 85, "112": 86, "113": 86, "114": 87, "115": 87, "116": 88, "117": 88, "118": 89, "119": 89, "120": 90, "121": 90, "122": 91, "123": 91, "124": 92, "125": 92, "126": 93, "127": 93, "128": 95, "129": 95, "130": 99, "131": 101, "132": 102, "133": 122, "134": 123, "135": 123, "136": 123, "137": 124, "138": 124, "139": 125, "140": 125, "141": 126, "142": 126, "143": 127, "144": 127, "145": 128, "146": 128, "147": 129, "148": 129, "149": 130, "150": 130, "151": 131, "152": 131, "153": 132, "154": 132, "155": 133, "156": 133, "157": 134, "158": 134, "159": 135, "160": 135, "161": 138, "167": 3, "173": 3, "179": 173}, "filename": "C:\\Python34\\Scripts\\colonial\\home\\templates/items.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
