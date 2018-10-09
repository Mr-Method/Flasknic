# -*- coding: utf-8 -*-
import logging
import os,sys
import random 
import hashlib
import time

from flask import Flask

FS_ENCODING = sys.getfilesystemencoding()
PY_LEGACY = sys.version_info < (3, )
def fsdecode(path, os_name=os.name, fs_encoding=FS_ENCODING, errors=None):
    if not isinstance(path, bytes):
        return path
    if not errors:
        use_strict = PY_LEGACY or os_name == 'nt'
        errors = 'strict' if use_strict else 'surrogateescape'
    return path.decode(fs_encoding, errors=errors)

__basedir__ = os.path.abspath(os.path.dirname(fsdecode(__file__)))

App = Flask(__name__,
	static_url_path = '/static', # or /assets
	static_folder = os.path.join(__basedir__, 'static'),
	template_folder = os.path.join(__basedir__, 'templates'),
)
import models, views

App.logger.setLevel(10)
App.config.update({
	'DEBUG': True,
	'APP_NAME': __name__,
	'SECRET_KEY': 'wkwkwland',
	'JSONIFY_MIMETYPE': 'application/json;charset=UTF-8',
})