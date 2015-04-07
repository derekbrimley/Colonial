# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428384618.542048
_enable_loop = True
_template_filename = 'C:\\Python34\\Scripts\\Colonial\\rental\\templates/rentals.view.html'
_template_uri = 'rentals.view.html'
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
        users = context.get('users', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        fees = context.get('fees', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        transactions = context.get('transactions', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        fees = context.get('fees', UNDEFINED)
        def contents():
            return render_contents(context)
        transactions = context.get('transactions', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n<div class="replace_me2">\r\n\r\n')
        __M_writer('\r\n')
        if request.user.has_perm('home.agent'):
            if transactions:
                __M_writer('\t\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>Rental ID</th>\r\n\t\t\t\t\t<th>Name</th>\r\n\t\t\t\t\t<th>Email</th>\r\n\t\t\t\t\t<th>Price</th>\r\n\t\t\t\t\t<th>Date Rented</th>\r\n\t\t\t\t\t<th>Date Due</th>\r\n\t\t\t\t\t<th>Status</th>\r\n\t\t\t\t\t<th>Product</th>\r\n\t\t\t\t\t<th>Fee</th>\r\n\t\t\t\t\t<th>Actions</th>\r\n                    <th><input class="bulk-return" type="checkbox"></th>\r\n\t\t\t\t</tr>\r\n\r\n')
                __M_writer('\t\t\t\t<tr>\r\n')
                for rental in rentals:
                    for transaction in transactions:
                        if rental.transaction_id == transaction.id:
                            __M_writer('\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(rental.id))
                            __M_writer('</td>\r\n\r\n')
                            for user in users:
                                if transaction.customer_id == user.id:
                                    __M_writer('\t\t\t\t\t\t\t\t\t\t<td>')
                                    __M_writer(str(user.first_name))
                                    __M_writer(' ')
                                    __M_writer(str(user.last_name))
                                    __M_writer('</td>\r\n\t\t\t\t\t\t\t\t\t\t<td>')
                                    __M_writer(str(user.email))
                                    __M_writer('</td>\r\n')
                            __M_writer('\r\n\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(rental.price))
                            __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(rental.date_out))
                            __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(rental.date_due))
                            __M_writer('</td>\r\n\t\t\t\t\t\t\t\t\r\n')
                            if rental.date_in is not None:
                                __M_writer('\t\t\t\t\t\t\t\t\t<td id="green">Returned</td>\r\n')
                            else:
                                __M_writer('\t\t\t\t\t\t\t\t\t<td id="red">Renting</td>\r\n')
                            __M_writer('\r\n')
                            for product in products:
                                if product.id == rental.rentable_product_id:
                                    __M_writer('\t\t\t\t\t\t\t\t\t\t<td>')
                                    __M_writer(str(product.name))
                                    __M_writer('</td>\r\n')
                    __M_writer('\r\n')
                    __M_writer('\r\n\t\t\t\t\t\t<td>\r\n')
                    for fee in fees:
                        if fee.rental_item_id == rental.id:
                            __M_writer('\t\t\t\t\t\t\t\t\t<p id="red">Yes</p>\r\n')
                    __M_writer('\t\t\t\t\t\t</td>\r\n')
                    __M_writer('\r\n')
                    __M_writer('\r\n\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t<a href="/rental/rentals.edit/')
                    __M_writer(str(rental.id))
                    __M_writer('/')
                    __M_writer(str(transaction.id))
                    __M_writer('/')
                    __M_writer(str(user.id))
                    __M_writer('/')
                    __M_writer(str(product.id))
                    __M_writer('/">Edit</a> | \r\n\t\t\t\t\t\t\t<a href="/rental/rentals.delete/')
                    __M_writer(str(rental.id))
                    __M_writer('/')
                    __M_writer(str(transaction.id))
                    __M_writer('/')
                    __M_writer(str(user.id))
                    __M_writer('/')
                    __M_writer(str(product.id))
                    __M_writer('/')
                    __M_writer(str(fee.id))
                    __M_writer('">Delete</a>\r\n\t\t\t\t\t\t</td>\r\n')
                    if rental.date_in == None:
                        __M_writer('                        <td><input  type="checkbox" class="actice-checkbox" value="')
                        __M_writer(str(rental.id))
                        __M_writer('"></td>\r\n')
                    else:
                        __M_writer('                        <td><input type="checkbox" disabled readonly></td>\r\n')
                    __M_writer('\r\n\t\t\t\t\t</tr>\r\n')
                __M_writer('\t\t\t</table>\r\n\r\n\t\t\t<div class="text-center">\r\n\t\t\t\t<a href="/rental/rentals/" class="btn btn btn-primary ">Back</a>\r\n\t\t\t\t<a href="/rental/rentals.add_customer/" class="btn btn btn-success">Add New Rental</a>\r\n                <td><a data-userid="')
                __M_writer(str(user.id))
                __M_writer('" class="btn btn btn-success mass-return">Bulk Return</a></td>\r\n\t\t\t</div>\r\n\t\t\r\n')
            else:
                __M_writer('\t\t\t<div class="text-center" >\r\n\t\t\t\t<h3>Dear ')
                __M_writer(str( request.user.first_name ))
                __M_writer(', No rentals found! Either you dont have anything checked out, or our inventory was thrown in the Boston Harbor!</h3>\r\n\t\t\t</div>\r\n\t\t\t<img id="boston" src="')
                __M_writer(str( STATIC_URL ))
                __M_writer('rental/media/icons/boston.jpg" />\r\n')
            __M_writer('\r\n\r\n')
        elif request.user.is_authenticated():
            if transactions:
                __M_writer('\t\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>Rental ID</th>\r\n\t\t\t\t\t<th>Price</th>\r\n\t\t\t\t\t<th>Date Rented</th>\r\n\t\t\t\t\t<th>Date Due</th>\r\n\t\t\t\t\t<th>Status</th>\r\n\t\t\t\t\t<th>Product</th>\r\n\t\t\t\t\t<th>Fee</th>\r\n\t\t\t\t</tr>\r\n\r\n')
                __M_writer('\t\t\t\t<tr>\r\n')
                for rental in rentals:
                    for transaction in transactions:
                        if rental.transaction_id == transaction.id:
                            __M_writer('\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(rental.id))
                            __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(rental.price))
                            __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(rental.date_out))
                            __M_writer('</td>\r\n\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(rental.date_due))
                            __M_writer('</td>\r\n\t\t\t\t\t\t\t\t\r\n')
                            if rental.date_in is not None:
                                __M_writer('\t\t\t\t\t\t\t\t\t<td id="green">Returned</td>\r\n')
                            else:
                                __M_writer('\t\t\t\t\t\t\t\t\t<td id="red">Renting</td>\r\n')
                            __M_writer('\r\n')
                            for product in products:
                                if product.id == rental.rentable_product_id:
                                    __M_writer('\t\t\t\t\t\t\t\t\t\t<td>')
                                    __M_writer(str(product.name))
                                    __M_writer('</td>\r\n')
                    __M_writer('\t\t\t\t\t</tr>\r\n')
                __M_writer('\r\n\t\t\t</table>\r\n\t\t\r\n')
            else:
                __M_writer('\t\t\t<div class="text-center" >\r\n\t\t\t\t<h3>Dear ')
                __M_writer(str( request.user.first_name ))
                __M_writer(', No rentals found! Either you dont have anything checked out, or our inventory was thrown in the Boston Harbor!</h3>\r\n\t\t\t</div>\r\n\t\t\t<img id="boston" src="')
                __M_writer(str( STATIC_URL ))
                __M_writer('rental/media/icons/boston.jpg" />\r\n')
            __M_writer('\r\n')
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">Rentals</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"line_map": {"27": 0, "43": 1, "48": 5, "53": 180, "59": 9, "72": 9, "73": 18, "74": 19, "75": 21, "76": 22, "77": 39, "78": 40, "79": 41, "80": 42, "81": 43, "82": 43, "83": 43, "84": 45, "85": 46, "86": 47, "87": 47, "88": 47, "89": 47, "90": 47, "91": 48, "92": 48, "93": 51, "94": 52, "95": 52, "96": 53, "97": 53, "98": 54, "99": 54, "100": 56, "101": 57, "102": 58, "103": 59, "104": 61, "105": 62, "106": 63, "107": 64, "108": 64, "109": 64, "110": 69, "111": 71, "112": 73, "113": 74, "114": 75, "115": 78, "116": 87, "117": 91, "118": 93, "119": 93, "120": 93, "121": 93, "122": 93, "123": 93, "124": 93, "125": 93, "126": 94, "127": 94, "128": 94, "129": 94, "130": 94, "131": 94, "132": 94, "133": 94, "134": 94, "135": 94, "136": 96, "137": 98, "138": 98, "139": 98, "140": 99, "141": 101, "142": 103, "143": 106, "144": 111, "145": 111, "146": 115, "147": 116, "148": 117, "149": 117, "150": 119, "151": 119, "152": 121, "153": 127, "154": 129, "155": 130, "156": 143, "157": 144, "158": 145, "159": 146, "160": 147, "161": 147, "162": 147, "163": 148, "164": 148, "165": 149, "166": 149, "167": 150, "168": 150, "169": 152, "170": 153, "171": 154, "172": 155, "173": 157, "174": 158, "175": 159, "176": 160, "177": 160, "178": 160, "179": 165, "180": 167, "181": 171, "182": 172, "183": 173, "184": 173, "185": 175, "186": 175, "187": 177, "188": 179, "194": 3, "200": 3, "206": 200}, "source_encoding": "ascii", "uri": "rentals.view.html", "filename": "C:\\Python34\\Scripts\\Colonial\\rental\\templates/rentals.view.html"}
__M_END_METADATA
"""
