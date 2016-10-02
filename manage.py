from  flask.ext.script import Manager, Server
from app import app
#fixme: there is an error

manager = Manager(app)
manager.add_command("runserber", Server(host="127.0.0.1", port=5000, use_debugger=True))

if __name__ == '__main__':
	manager.run()
	