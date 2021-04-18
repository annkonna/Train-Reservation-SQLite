import json

import bottle
import eventlet
import eventlet.wsgi

import bookings


@bottle.route('/')
def index():
    return bottle.static_file("index.html", root="")


@bottle.route('/myCode.js')
def static():
    return bottle.static_file("myCode.js", root="")


@bottle.route('/bookings')
def get_chat():
    return json.dumps(bookings.get_bookings())


@bottle.post('/add_booking')
def add_booking():
    content = bottle.request.body.read().decode()
    content = json.loads(content)
    bookings.add_booking(content)
    return json.dumps(bookings.get_bookings())


eventlet.wsgi.server(eventlet.listen(('localhost', 8080)), bottle.default_app())
