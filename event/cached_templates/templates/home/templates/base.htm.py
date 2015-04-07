# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1428381269.335146
_enable_loop = True
_template_filename = 'C:\\Users\\Derek\\python\\colonial\\colonial/home/templates/base.htm'
_template_uri = '/home/templates/base.htm'
_source_encoding = 'ascii'
import os, os.path, re
_exports = ['top_banner', 'title', 'contents']


from django_mako_plus.controller import static_files 

def render_body(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        request = context.get('request', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        self = context.get('self', UNDEFINED)
        def title():
            return render_title(context._locals(__M_locals))
        user = context.get('user', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n')
        static_renderer = static_files.StaticRenderer(self) 
        
        __M_locals_builtin_stored = __M_locals_builtin()
        __M_locals.update(__M_dict_builtin([(__M_key, __M_locals_builtin_stored[__M_key]) for __M_key in ['static_renderer'] if __M_key in __M_locals_builtin_stored]))
        __M_writer('\r\n\r\n<!DOCTYPE html>\r\n<html>\r\n  <meta charset="UTF-8">\r\n\r\n  <head>\r\n    ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'title'):
            context['self'].title(**pageargs)
        

        __M_writer('\r\n  \r\n')
        __M_writer('    <script src="http://ajax.googleapis.com/ajax/libs/jquery/1.9.1/jquery.min.js"></script>\r\n    <!-- Latest compiled and minified CSS -->\r\n    <link rel="stylesheet" href="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/css/bootstrap.min.css">\r\n    <!-- Latest compiled and minified JavaScript -->\r\n    <script src="https://maxcdn.bootstrapcdn.com/bootstrap/3.3.2/js/bootstrap.min.js"></script>\r\n    <script src=')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/jquery.form.js></script>\r\n    <script src=')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/jquery.loadmodal.js></script>\r\n  \r\n  \r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_css(request, context)  ))
        __M_writer('\r\n  \r\n  </head>\r\n\r\n\r\n  <!-- <body background="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/paper2.jpg"> -->\r\n\r\n  \r\n  \r\n')
        if request.user.is_authenticated():
            __M_writer('\t\t<div class="login_button" style="white-space:nowrap;">\r\n\t\t\t<label class="welcome label label-success">Welcome, ')
            __M_writer(str(user.get_username()))
            __M_writer('</label>\r\n\t\t\t\t<a href="/user/login.logout_view/" class="btn btn-primary">Sign Out</a>\r\n\t\t\t<button class="show_button btn btn btn-warning">Show Cart</button>\r\n\t\t</div>\r\n')
        else:
            __M_writer('\t  <div class="login_button" style="white-space:nowrap;">\r\n        <label class="welcome label label-danger">Welcome, Guest</label>\r\n        <!-- <a href="/user/login" class="btn btn-primary">Sign In</a> -->\r\n        <button class="show_login_dialog btn btn-primary">Sign In</button>\r\n        <a href="/password_reset/" class="btn btn-default">Forgot Password?</a>\r\n      </div>\r\n\r\n')
        __M_writer('\r\n\r\n\r\n  <header background=\'none\'>\r\n    <img class="headertitle" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/colonialheritage.png" alt="The Colonial Heritage Foundation" >\r\n  </header>\r\n  \r\n    \r\n  <body>\r\n    <div class="container-fluid">      \r\n      <!--<div class="row">\r\n          <div class="col-xs-12">\r\n           <img class="headerphoto" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/sign.jpg" alt="The Signing" > \r\n          </div>\r\n        </div> -->\r\n\r\n      <div class="row">\r\n        <nav id="myNavbar" role="navigation">\r\n          <!-- Brand and toggle get grouped for better mobile display -->\r\n          <div class="container-nav">\r\n\r\n')
        if request.user.has_perm('home.agent'):
            __M_writer('              <!-- If the person is not a guest -->\r\n              <div class="collapse navbar-collapse" id="navbarCollapse">\r\n                <ul class="nav nav-justified">\r\n                  <li><a href="http://localhost:8000/home/index" target="">Home</a></li>\r\n                  <li><a href="http://localhost:8000/user/user" target="">Accounts</a></li>\r\n                  <li><a href="http://localhost:8000/event/events" target="">Events</a></li>\r\n                  <li><a href="http://localhost:8000/product/items" target="">Inventory</a></li>\r\n                  <li><a href="http://localhost:8000/product/products" target="">Products</a></li>\r\n                  <li><a href="http://localhost:8000/rental/rentals" target="">Rentals</a></li>\r\n                  <li><a href="http://localhost:8000/home/tools" target="">Tools</a></li>\r\n                  <li><a href="http://localhost:8000/home/about" target="">About Us</a></li>\r\n                </ul>\r\n              </div> \r\n\r\n')
        elif request.user.is_authenticated():
            __M_writer('              <!--Guest-->\r\n                <div class="collapse navbar-collapse" id="navbarCollapse">\r\n                  <ul class="nav nav-justified">\r\n                      <li><a href="http://localhost:8000/home/index" target="">Home</a></li>\r\n                      <li><a href="http://localhost:8000/user/user" target="">My Account</a></li>\r\n                      <li><a href="http://localhost:8000/rental/rentals.view" target="">My Rentals</a></li>\r\n                      <li><a href="http://localhost:8000/home/orders" target="">My Orders</a></li>\r\n                      <li><a href="http://localhost:8000/event/events" target="">Events</a></li>\r\n                      <li><a href="http://localhost:8000/product/products" target="">Products</a></li>\r\n\r\n                      <li><a href="http://localhost:8000/home/about" target="">About Us</a></li>\r\n                  </ul>\r\n                </div>\r\n\r\n')
        else:
            __M_writer('              <!--Guest-->\r\n                <div class="collapse navbar-collapse" id="navbarCollapse">\r\n                  <ul class="nav nav-justified">\r\n                      <li><a href="http://localhost:8000/home/index" target="">Home</a></li>\r\n                      <li><a href="http://localhost:8000/event/events" target="">Events</a></li>\r\n                      <li><a href="http://localhost:8000/product/products" target="">Products</a></li>\r\n                      <li><a href="http://localhost:8000/home/about" target="">About Us</a></li>\r\n                      <li><a class="show_join_dialog" target="">Join Us</a></li>\r\n                      <!-- <li><a class="show_join_dialog" href="http://localhost:8000/user/join" target="">Join Us</a></li> -->\r\n            \r\n                  </ul>\r\n                </div>\r\n\r\n')
        __M_writer('  \r\n              \r\n          </div>\r\n        </nav>\r\n      </div>\r\n    </div>\r\n\r\n  <hr>\r\n\r\n    <div class="container-fluid">\r\n\r\n      <div class="row">\r\n        <div class="col-xs-12">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer(' \r\n        </div>\r\n      </div>\r\n\r\n      <div class="row">\r\n        <div class="col-xs-12">\r\n          ')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'contents'):
            context['self'].contents(**pageargs)
        

        __M_writer(' \r\n        </div>\r\n      </div>\r\n        \r\n    <hr>\r\n\r\n      <div class="row">\r\n        <div class="col-xs-12">\r\n          <footer>\r\n            <p>&copy; Copyright 2015 dwb</p>\r\n          </footer>\r\n        </div>\r\n      </div>\r\n\r\n    </div>\r\n  \r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n\r\n')
        __M_writer('    ')
        __M_writer(str( static_renderer.get_template_js(request, context)  ))
        __M_writer('\r\n  \r\n  </body>\r\n</html>')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_top_banner(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def top_banner():
            return render_top_banner(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <div class="top_banner">Welcome to the Colonial Heritage Foundation</div>\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_title(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        def title():
            return render_title(context)
        __M_writer = context.writer()
        __M_writer('\r\n      <title>Colonial</title>\r\n      <meta name="Colonial Heritage Foundation Home Page" content="The Colonial Heritage Foundation promotes actively engaging the mind in history. The foundation will provide you with the resources to go back in time and live the colonial years. Attend colonial events, purchase colonial products, rent colonial wardrobe and other items. ">\r\n    ')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contents():
            return render_contents(context)
        __M_writer = context.writer()
        __M_writer('\r\n            <img id="maincenter" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('home/media/colonialman.jpg" alt="Colonial Man" border="5" >\r\n          ')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"source_encoding": "ascii", "line_map": {"130": 124, "16": 4, "18": 0, "33": 2, "34": 4, "35": 5, "39": 5, "44": 15, "45": 18, "46": 23, "47": 23, "48": 24, "49": 24, "50": 28, "51": 28, "52": 28, "53": 33, "54": 33, "55": 37, "56": 38, "57": 39, "58": 39, "59": 43, "60": 44, "61": 52, "62": 56, "63": 56, "64": 64, "65": 64, "66": 73, "67": 74, "68": 88, "69": 89, "70": 103, "71": 104, "72": 118, "77": 133, "82": 141, "83": 170, "84": 170, "85": 170, "91": 131, "97": 131, "103": 12, "109": 12, "115": 139, "122": 139, "123": 140, "124": 140}, "uri": "/home/templates/base.htm", "filename": "C:\\Users\\Derek\\python\\colonial\\colonial/home/templates/base.htm"}
__M_END_METADATA
"""
