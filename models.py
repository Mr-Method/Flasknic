from werkzeug import import_string, cached_property
from main import App
import views

class View(object):
	def __init__(self, import_name):
		self.__module__, self.__name__ = import_name.rsplit('.',1)
		self.import_name = import_name
	@cached_property
	def view(self):
		return import_string(self.import_name)
	def __call__(self,*args,**kwargs):
		return self.view(*args, **kwargs)

def url(import_name, url_rules=[], **options):
	view = View(import_name)
	for url_rule in url_rules:
		App.add_url_rule(url_rule,view_func=view,**options)
	return (import_name, url_rules)

def error(import_name, codes_or_exceptions=[], **options):
	view = View(import_name)
	for code_or_exception in codes_or_exceptions:
		App.register_error_handler(code_or_exception, view)

import urls