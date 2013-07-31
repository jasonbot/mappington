# coding: utf-8

import os

import bottle

__all__ = ['register_routes']

routes = []
def route(route_text):
    def decorate(fn_):
        routes.append((route_text, fn_))
        return fn_
    return decorate

@route('/')
def index():
    return bottle.redirect('/static/index.html')

@route('/static/<path:path>')
def callback(path):
    return bottle.static_file(path,
                              root=os.path.join(os.path.dirname(__file__),
                                                'static'))

def register_routes(mappington_app):
    for route, fn in routes:
        mappington_app.route(route)(fn)

if __name__ == "__main__":
    mappington_app = bottle.Bottle()
    register_routes(mappington_app)
    bottle.run(app=mappington_app, host='0.0.0.0', port=8098, debug=True, reloader=True)
