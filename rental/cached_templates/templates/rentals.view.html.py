# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428047794.45198
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.view.html'
_template_uri = 'rentals.view.html'
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
        users = context.get('users', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        transactions = context.get('transactions', UNDEFINED)
        fees = context.get('fees', UNDEFINED)
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


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        users = context.get('users', UNDEFINED)
        def contents():
            return render_contents(context)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        products = context.get('products', UNDEFINED)
        request = context.get('request', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        transactions = context.get('transactions', UNDEFINED)
        fees = context.get('fees', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        if request.user.has_perm('home.agent'):
            if transactions:
                __M_writer('\t\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>Rental ID</th>\r\n\t\t\t\t\t<th>Name</th>\r\n\t\t\t\t\t<th>Email</th>\r\n\t\t\t\t\t<th>Price</th>\r\n\t\t\t\t\t<th>Date Rented</th>\r\n\t\t\t\t\t<th>Date Due</th>\r\n\t\t\t\t\t<th>Status</th>\r\n\t\t\t\t\t<th>Product</th>\r\n\t\t\t\t\t<th>Fee</th>\r\n\t\t\t\t\t<th>Actions</th>\r\n\t\t\t\t</tr>\r\n\r\n')
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
                    __M_writer('">Delete</a>\r\n\t\t\t\t\t\t</td>\r\n\r\n\t\t\t\t\t</tr>\r\n')
                __M_writer('\t\t\t</table>\r\n\r\n\t\t\t<div class="text-center">\r\n\t\t\t\t<a href="/rental/rentals/" class="btn btn btn-primary ">Back</a>\r\n\t\t\t\t<a href="/rental/rentals.add_customer/" class="btn btn btn-success">Add New Rental</a>\r\n\t\t\t</div>\r\n\t\t\r\n')
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
                __M_writer('\t\t\t</table>\r\n\t\t\r\n')
            else:
                __M_writer('\t\t\t<div class="text-center" >\r\n\t\t\t\t<h3>Dear ')
                __M_writer(str( request.user.first_name ))
                __M_writer(', No rentals found! Either you dont have anything checked out, or our inventory was thrown in the Boston Harbor!</h3>\r\n\t\t\t</div>\r\n\t\t\t<img id="boston" src="')
                __M_writer(str( STATIC_URL ))
                __M_writer('rental/media/icons/boston.jpg" />\r\n')
            __M_writer('\r\n')
        __M_writer('\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "rentals.view.html", "line_map": {"27": 0, "43": 1, "48": 5, "53": 168, "59": 3, "65": 3, "71": 9, "84": 9, "85": 16, "86": 17, "87": 19, "88": 20, "89": 36, "90": 37, "91": 38, "92": 39, "93": 40, "94": 40, "95": 40, "96": 42, "97": 43, "98": 44, "99": 44, "100": 44, "101": 44, "102": 44, "103": 45, "104": 45, "105": 48, "106": 49, "107": 49, "108": 50, "109": 50, "110": 51, "111": 51, "112": 53, "113": 54, "114": 55, "115": 56, "116": 58, "117": 59, "118": 60, "119": 61, "120": 61, "121": 61, "122": 66, "123": 68, "124": 70, "125": 71, "126": 72, "127": 75, "128": 84, "129": 88, "130": 90, "131": 90, "132": 90, "133": 90, "134": 90, "135": 90, "136": 90, "137": 90, "138": 91, "139": 91, "140": 91, "141": 91, "142": 91, "143": 91, "144": 91, "145": 91, "146": 91, "147": 91, "148": 96, "149": 104, "150": 105, "151": 106, "152": 106, "153": 108, "154": 108, "155": 110, "156": 116, "157": 118, "158": 119, "159": 132, "160": 133, "161": 134, "162": 135, "163": 136, "164": 136, "165": 136, "166": 137, "167": 137, "168": 138, "169": 138, "170": 139, "171": 139, "172": 141, "173": 142, "174": 143, "175": 144, "176": 146, "177": 147, "178": 148, "179": 149, "180": 149, "181": 149, "182": 154, "183": 156, "184": 159, "185": 160, "186": 161, "187": 161, "188": 163, "189": 163, "190": 165, "191": 167, "197": 191}, "filename": "C:\\Python34\\Projects\\colonial\\rental\\templates/rentals.view.html", "source_encoding": "ascii"}
__M_END_METADATA
"""
