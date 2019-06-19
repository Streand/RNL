from __init__ import app
from routes import routes_blueprint

app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run(host='192.168.1.105',port=5000,ssl_context=('cert.pem', 'key.pem'))