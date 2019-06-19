from __init__ import app
from routes import routes_blueprint

app.register_blueprint(routes_blueprint)

if __name__ == '__main__':
    app.run(debug=True, ssl_context = ('cert.pem', 'key.pem'))