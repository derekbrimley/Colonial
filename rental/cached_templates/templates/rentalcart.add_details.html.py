# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428035069.012917
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rentalcart.add_details.html'
_template_uri = 'rentalcart.add_details.html'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['contents', 'content', 'top_banner']


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
        photos_as_string = context.get('photos_as_string', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        forms = context.get('forms', UNDEFINED)
        def content():
            return render_content(context._locals(__M_locals))
        products_as_string = context.get('products_as_string', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        rentalform = context.get('rentalform', UNDEFINED)
        dailyfee = context.get('dailyfee', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        __M_writer('\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'content'):
            context['self'].content(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        rentalform = context.get('rentalform', UNDEFINED)
        dailyfee = context.get('dailyfee', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n<form method="POST">\r\n\r\n\t<table class="table table-striped">\r\n\r\n\t\t')
        __M_writer(str( rentalform ))
        __M_writer('\r\n\r\n\t</table>\r\n\r\n\t<div class="text-center">\r\n\t\t<h3 class="total_price">Daily Fee: $')
        __M_writer(str(dailyfee))
        __M_writer('</h3>\r\n\t</div>\r\n\t<div id="form_buttons">\r\n\t\t<button type="submit" class="btn btn-primary">Submit</button>\r\n\t</div>\r\n</form>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_content(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        photos_as_string = context.get('photos_as_string', UNDEFINED)
        request = context.get('request', UNDEFINED)
        forms = context.get('forms', UNDEFINED)
        def content():
            return render_content(context)
        products_as_string = context.get('products_as_string', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n\r\n')
        __M_writer('\t<table class="table table-striped">\r\n\r\n')
        for product in products_as_string:
            __M_writer('\r\n')
            for photo in photos_as_string:
                __M_writer('\r\n')
                if photo == product:
                    __M_writer('\t\t\t \t\t\r\n\t\t\t\t\t<tr>\r\n')
                    __M_writer('\t\t\t\t\t\t<td>\r\n\t\t\t\t        \t<img class="image" src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('product/media/products/')
                    __M_writer(str( photo ))
                    __M_writer('.jpg" />\r\n\t\t\t\t        </td>\r\n\r\n\t\t\t\t       \t<td>\r\n')
                    for form in forms:
                        for field in form:
                            if field.label == "Rentable Product":
                                for value in field:
                                    if value.value == product:
                                        __M_writer('\t\t\t\t       \t\t\t\t\t\t\t')
                                        __M_writer(str(form))
                                        __M_writer('\r\n')
                    __M_writer('\t\t\t\t       \t</td>\r\n\r\n\t\t\t\t    </tr>\r\n\r\n')
        __M_writer('\r\n\t</table>\r\n\r\n')
        __M_writer('\r\n')
        if request.user.is_authenticated():
            __M_writer('\t<div id="form_buttons">\r\n\t<button type="submit" class="btn btn-primary">Submit</button>\r\n    </div>\r\n')
        else:
            __M_writer('\t<div id="form_buttons">\r\n        <button class="show_login_dialog btn btn-primary">Sign In</button>\r\n   \t</div>\r\n')
        __M_writer('\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Complete Rental</div>\r\n\t<div class="text-center"><h4>Almost finished</h4></div>\r\n\t<br>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"129": 3, "135": 3, "141": 135, "27": 0, "45": 1, "50": 7, "51": 17, "56": 37, "66": 20, "74": 20, "75": 25, "76": 25, "77": 30, "78": 30, "84": 66, "95": 66, "96": 70, "97": 72, "98": 73, "99": 74, "100": 75, "101": 76, "102": 77, "103": 80, "104": 81, "105": 81, "106": 81, "107": 81, "108": 85, "109": 86, "110": 87, "111": 88, "112": 89, "113": 90, "114": 90, "115": 90, "116": 96, "117": 103, "118": 109, "119": 111, "120": 112, "121": 115, "122": 116, "123": 120}, "uri": "rentalcart.add_details.html", "source_encoding": "ascii", "filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rentalcart.add_details.html"}
__M_END_METADATA
"""
