# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428383607.370669
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\Colonial\\rental\\templates/rentals.view.html'
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
        transactions = context.get('transactions', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        def contents():
            return render_contents(context._locals(__M_locals))
        fees = context.get('fees', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        users = context.get('users', UNDEFINED)
        products = context.get('products', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        request = context.get('request', UNDEFINED)
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
        transactions = context.get('transactions', UNDEFINED)
        def contents():
            return render_contents(context)
        fees = context.get('fees', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        users = context.get('users', UNDEFINED)
        products = context.get('products', UNDEFINED)
        rentals = context.get('rentals', UNDEFINED)
        request = context.get('request', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        if request.user.has_perm('home.agent'):
            if transactions:
                __M_writer('\t\t\t<table id="display_table" class="table table-striped table-bordered">\r\n\t\t\t\t\r\n\t\t\t\t<tr>\r\n\t\t\t\t\t<th>Rental ID</th>\r\n\t\t\t\t\t<th>Name</th>\r\n\t\t\t\t\t<th>Email</th>\r\n\t\t\t\t\t<th>Price</th>\r\n\t\t\t\t\t<th>Date Rented</th>\r\n\t\t\t\t\t<th>Date Due</th>\r\n\t\t\t\t\t<th>Status</th>\r\n\t\t\t\t\t<th>Product</th>\r\n\t\t\t\t\t<th>Fee</th>s\r\n\t\t\t\t\t<th>Actions</th>\r\n\t\t\t\t</tr>\r\n\r\n')
                __M_writer('\t\t\t\t<tr>\r\n')
                for rental in rentals:
                    for transaction in transactions:
                        if rental.transaction_id == transaction.id:
                            __M_writer('\t\t\t\t\t\t\t\t<td>')
                            __M_writer(str(rental.id))
                            __M_writer('</td>\r\n\r\n')
                            for person in users:
                                if transaction.customer_id == person.id:
                                    __M_writer('\t\t\t\t\t\t\t\t\t\t<td>')
                                    __M_writer(str(person.first_name))
                                    __M_writer(' ')
                                    __M_writer(str(person.last_name))
                                    __M_writer('</td>\r\n\t\t\t\t\t\t\t\t\t\t<td>')
                                    __M_writer(str(person.email))
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
                            if fee.paid == True:
                                __M_writer('\t\t\t\t\t\t\t\t\t\t<p id="green">Yes</p>\r\n')
                            else:
                                __M_writer('\t\t\t\t\t\t\t\t\t\t<p id="red">Yes</p>\r\n')
                    __M_writer('\t\t\t\t\t\t</td>\r\n')
                    __M_writer('\r\n')
                    __M_writer('\r\n\t\t\t\t\t\t<td>\r\n\t\t\t\t\t\t\t<a href="/rental/rentals.edit/')
                    __M_writer(str(rental.id))
                    __M_writer('/">Edit</a> | \r\n\t\t\t\t\t\t\t<a href="/rental/rentals.delete/')
                    __M_writer(str(rental.id))
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
{"source_encoding": "ascii", "filename": "C:\\Python34\\Projects\\Colonial\\rental\\templates/rentals.view.html", "line_map": {"27": 0, "43": 1, "48": 5, "53": 172, "59": 9, "72": 9, "73": 16, "74": 17, "75": 19, "76": 20, "77": 36, "78": 37, "79": 38, "80": 39, "81": 40, "82": 40, "83": 40, "84": 42, "85": 43, "86": 44, "87": 44, "88": 44, "89": 44, "90": 44, "91": 45, "92": 45, "93": 48, "94": 49, "95": 49, "96": 50, "97": 50, "98": 51, "99": 51, "100": 53, "101": 54, "102": 55, "103": 56, "104": 58, "105": 59, "106": 60, "107": 61, "108": 61, "109": 61, "110": 66, "111": 68, "112": 70, "113": 71, "114": 72, "115": 73, "116": 74, "117": 75, "118": 79, "119": 88, "120": 92, "121": 94, "122": 94, "123": 95, "124": 95, "125": 95, "126": 95, "127": 100, "128": 108, "129": 109, "130": 110, "131": 110, "132": 112, "133": 112, "134": 114, "135": 120, "136": 122, "137": 123, "138": 136, "139": 137, "140": 138, "141": 139, "142": 140, "143": 140, "144": 140, "145": 141, "146": 141, "147": 142, "148": 142, "149": 143, "150": 143, "151": 145, "152": 146, "153": 147, "154": 148, "155": 150, "156": 151, "157": 152, "158": 153, "159": 153, "160": 153, "161": 158, "162": 160, "163": 163, "164": 164, "165": 165, "166": 165, "167": 167, "168": 167, "169": 169, "170": 171, "176": 3, "182": 3, "188": 182}, "uri": "rentals.view.html"}
__M_END_METADATA
"""
