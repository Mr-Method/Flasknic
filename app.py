from main import App
# Adding support for gunicorn
if __name__ == '__main__':
	App.run(port=2233)