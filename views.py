from flask import (
	render_template, abort,
	request, Response, url_for,
	session, jsonify, redirect,
)
import traceback
import models

def index():
	return "Yo sup!", 200
def helps_index(id=None):
	return f"This is help message<br>Showing ID:{id}"

# Custom error
def handler404(*k):
	return "Hmm, not found m8"