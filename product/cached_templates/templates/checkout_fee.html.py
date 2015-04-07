# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428388410.387161
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\Colonial\\product\\templates/checkout_fee.html'
_template_uri = 'checkout_fee.html'
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
        fee = context.get('fee', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        customer = context.get('customer', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        total_cost = context.get('total_cost', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n')
        __M_writer('\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        fee = context.get('fee', UNDEFINED)
        def contents():
            return render_contents(context)
        customer = context.get('customer', UNDEFINED)
        total_cost = context.get('total_cost', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\t\r\n\t<h1 class="heading">Payment Information</h1>\r\n\t<div class="checkout_form">\r\n\t    <form>\r\n\t        Card Type:\r\n\t        \r\n\t        <br><select>\r\n\t            <option value="Visa">Visa</option>\r\n\t            <option value="Discover">Discover</option>\r\n\t            <option value="AmericanExpress">American Express</option>\r\n\t            <option value="MasterCard">Master Card</option>\r\n\t        </select><br>\r\n\r\n\t        Name on Card:<br>\r\n\t        <input type="text" maxlength="100" name="Name" value=')
        __M_writer(str( customer.first_name ))
        __M_writer('><br>\r\n\t        \r\n\t        Card Number:<br>\r\n\t        <input type="number" maxlength="40" name="Lastname" value="4732817300654"><br>\r\n\r\n\t        Exp Month: <br>\r\n\t        <input type="number" maxlength="10" name="Pin" value="10"><br>\r\n\t        \r\n\t        Exp Year:<br>\r\n\t        <input type="text" maxlength="500" name="Address" value="15"><br>\r\n\t        \r\n\t        CVC Code:<br>\r\n\t        <input type="text" maxlength="500" name="City" value="411"><br>\r\n\t        \r\n\t        <br><br>\r\n\t        <a href="/rental/rentals.pay_fee/')
        __M_writer(str(total_cost))
        __M_writer('/')
        __M_writer(str(customer.id))
        __M_writer('/')
        __M_writer(str(fee.id))
        __M_writer('" class="purchase_button btn btn-success btn" role="button">Pay Fee</a>\r\n\t    </form>\r\n\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        total_cost = context.get('total_cost', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Total Cost: $')
        __M_writer(str(total_cost))
        __M_writer(' </div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"filename": "C:\\Python34\\Projects\\Colonial\\product\\templates/checkout_fee.html", "line_map": {"64": 9, "65": 14, "66": 28, "67": 28, "68": 43, "69": 43, "70": 43, "39": 1, "72": 43, "73": 43, "71": 43, "44": 5, "45": 8, "79": 3, "86": 3, "55": 9, "88": 4, "87": 4, "27": 0, "94": 88}, "uri": "checkout_fee.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
