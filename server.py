from waitress import serve

from upita_servers.wsgi import application

if __name__ == '__main__':
    serve(application, port='8081')