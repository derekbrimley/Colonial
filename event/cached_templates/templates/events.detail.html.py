# -*- coding:ascii -*-
from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 10
_modified_time = 1427831623.801459
_enable_loop = True
_template_filename = 'C:\\Python34\\Projects\\colonial\\event\\templates/events.detail.html'
_template_uri = 'events.detail.html'
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
        hf_photos = context.get('hf_photos', UNDEFINED)
        sale_items = context.get('sale_items', UNDEFINED)
        historical_figures = context.get('historical_figures', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        area_photos = context.get('area_photos', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contents():
            return render_contents(context._locals(__M_locals))
        event = context.get('event', UNDEFINED)
        def top_banner():
            return render_top_banner(context._locals(__M_locals))
        __M_writer = context.writer()
        __M_writer('\r\n\r\n')
        if 'parent' not in context._data or not hasattr(context._data['parent'], 'top_banner'):
            context['self'].top_banner(**pageargs)
        

        __M_writer('\r\n\r\n\r\n')
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
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n\t<div class="top_banner">')
        __M_writer(str( event.name ))
        __M_writer('</div>\r\n\t<div class="text-muted text-center">')
        __M_writer(str( event.description ))
        __M_writer('</div>\r\n\t<div class=" text-center">')
        __M_writer(str( event.start_date ))
        __M_writer(' at ')
        __M_writer(str( event.venue_name ))
        __M_writer('</div>\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


def render_contents(context,**pageargs):
    __M_caller = context.caller_stack._push_frame()
    try:
        hf_photos = context.get('hf_photos', UNDEFINED)
        sale_items = context.get('sale_items', UNDEFINED)
        historical_figures = context.get('historical_figures', UNDEFINED)
        areas = context.get('areas', UNDEFINED)
        area_photos = context.get('area_photos', UNDEFINED)
        STATIC_URL = context.get('STATIC_URL', UNDEFINED)
        def contents():
            return render_contents(context)
        event = context.get('event', UNDEFINED)
        __M_writer = context.writer()
        __M_writer('\r\n')
        __M_writer('\r\n \t<div class="text-center">\r\n \t\t<div class="map_image">\r\n \t\t\t<img class="event_image" src="')
        __M_writer(str( STATIC_URL ))
        __M_writer('event/media/mapFiles/')
        __M_writer(str( event.map_file ))
        __M_writer('.jpg" />\r\n \t\t</div>\r\n\t\r\n\t<hr>\r\n\r\n')
        for area in areas:
            __M_writer('\t\t\t<div class="item_container">\r\n\r\n')
            for photo in area_photos:
                if area.area_name in photo.image:
                    __M_writer('\t\t\t\t\t\t<img src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('event/media/areas/')
                    __M_writer(str( photo.image ))
                    __M_writer('" />\r\n')
            __M_writer('\r\n\t\t\t\t<div class="area_header"><h1>')
            __M_writer(str( area.place_number ))
            __M_writer(' ')
            __M_writer(str( area.area_name ))
            __M_writer('</h1></div>\r\n\t\t\t\t<div class="area_description"><h1><small>')
            __M_writer(str( area.description ))
            __M_writer('</small></h1></div>\r\n\t\t\t\t\r\n\r\n\t\t\t\t<div class="hover"><a href="#" id=')
            __M_writer(str( area.area_name ))
            __M_writer('>Items Here?</a></div>\r\n\t\t\t\t\r\n\t\t\t\t<!-- HIDDEN / POP-UP DIV -->\r\n\t\t\t\t<div id=')
            __M_writer(str( area.area_name ))
            __M_writer('>\r\n\t\t\t      \t<h4>For purchase here:</h4>\r\n\t\t\t      \t\t<p>\r\n')
            for item in sale_items:
                if item.area_id == area.id:
                    __M_writer('\t\t\t\t\t\t\t\t\t<div class="text-center"><h2>')
                    __M_writer(str( item.name ))
                    __M_writer('<br><small>')
                    __M_writer(str( item.description ))
                    __M_writer('</small></h2></div>\r\n')
            __M_writer('\t\t     \t \t\t</p>\r\n\t\t\t\t</div>\r\n\r\n\r\n\t\t\t\t\r\n\t\t\t\t\r\n\r\n\r\n\r\n\t\t\t\t\t\t\r\n\t\t\t</div>\r\n')
        __M_writer('\r\n\t\r\n\r\n\t</div>\r\n\t\r\n\t<hr>\r\n\r\n\t<div class="historical_figures text-center"><h1>Historical Figures at this Event</h1>\r\n\t\t\r\n')
        for person in historical_figures:
            __M_writer('\t\t\t<div class="row">\r\n')
            for photo in hf_photos:
                if person.name in photo.image:
                    __M_writer('\t\t\t\t\t\t\t<div id="person_name" class="col-md-2 text-left"><h3>')
                    __M_writer(str( person.name ))
                    __M_writer('</h3></div>\r\n\t\t\t\t\t\t\t<img class="col-md-3 historical_figure_image" src="')
                    __M_writer(str( STATIC_URL ))
                    __M_writer('event/media/figures/')
                    __M_writer(str( photo.image ))
                    __M_writer('" />\r\n\t\t\t\t\t\t\t<div class="col-md-4 text-left"><h3><small>')
                    __M_writer(str( person.biographical_note ))
                    __M_writer('</small></h3></div>\r\n\t\t\t\t\t\t\t<div class="col-md-1 text-left"><h3><small><strong>Birth</strong> ')
                    __M_writer(str( person.birth_date ))
                    __M_writer(' ')
                    __M_writer(str( person.birth_place ))
                    __M_writer('</small></h3></div>\r\n\t\t\t\t\t\t\t<div class="col-md-1 text-left"><h3><small><strong>Death</strong> ')
                    __M_writer(str( person.death_date ))
                    __M_writer(' ')
                    __M_writer(str( person.death_place ))
                    __M_writer('</small></h3></div>\r\n\t\t\t\t\t\t\t\r\n')
            __M_writer('\t\t\t</div>\r\n\t\t\t<hr>\r\n')
        __M_writer('\t</div>\r\n\r\n\t<div class="text-left">\r\n\t\t<a href="/event/events/" class="btn btn btn-primary">Back to events</a>\r\n\t</div>\r\n\r\n')
        return ''
    finally:
        context.caller_stack._pop_frame()


"""
__M_BEGIN_METADATA
{"uri": "events.detail.html", "filename": "C:\\Python34\\Projects\\colonial\\event\\templates/events.detail.html", "line_map": {"128": 71, "129": 72, "130": 73, "131": 74, "132": 75, "133": 75, "134": 75, "135": 76, "136": 76, "137": 76, "138": 76, "139": 77, "140": 77, "141": 78, "142": 78, "143": 78, "144": 78, "145": 79, "146": 79, "147": 79, "148": 79, "149": 83, "150": 86, "27": 0, "156": 150, "43": 1, "48": 7, "53": 92, "59": 3, "66": 3, "67": 4, "68": 4, "69": 5, "70": 5, "71": 6, "72": 6, "73": 6, "74": 6, "80": 10, "93": 10, "94": 18, "95": 21, "96": 21, "97": 21, "98": 21, "99": 26, "100": 27, "101": 29, "102": 30, "103": 31, "104": 31, "105": 31, "106": 31, "107": 31, "108": 34, "109": 35, "110": 35, "111": 35, "112": 35, "113": 36, "114": 36, "115": 39, "116": 39, "117": 42, "118": 42, "119": 45, "120": 46, "121": 47, "122": 47, "123": 47, "124": 47, "125": 47, "126": 50, "127": 62}, "source_encoding": "ascii"}
__M_END_METADATA
"""
