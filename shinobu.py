#!/usr/bin/python
from bottle import Bottle, static_file
import tenjin
from tenjin.helpers import *
import time

app = Bottle()

log = '/home/jones/.znc/users/jo_nes/moddata/log/#?tv?shows_' + time.strftime('%Y%m%d') + '.log'
engine = tenjin.Engine(path=['templates'])

@app.route('/')
def index():
	context = { 'log' : open(log, 'r').readlines() }
	return engine.render('index.template', context)

@app.route('/dl/<id:int>')
def dl(id):
	context = { 'log' : open(log, 'r').readlines(), 'id' : id }
	return engine.render('dl.template', context)

@app.route('/s/<filename>')
def s(filename):
	return static_file(filename, root='static/')


