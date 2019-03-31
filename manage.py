# -*- coding:utf-8 -*-
#@Auhor : Agam
#@Time  : 2018-12-08
#@Email : agamgn@163.com

from application import app,manager
from flask_script import Server


import www


manager.add_command("runserver",Server(host="127.0.0.1",port=app.config['SERVER_PORT'],use_debugger=True))

def main():
    manager.run()

if __name__ == '__main__':
    try:
        import sys
        sys.exit(main())

    except Exception as e:
        import traceback

        traceback.print_exc()
