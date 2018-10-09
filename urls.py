from models import url, error
allpatterns = [
	url('views.index', ['/']),
	url('views.helps_index', 
		['/helps/', '/helps/<id>/']),
	error('views.handler404', [404]),
	error('views.handler500', [500]),
]