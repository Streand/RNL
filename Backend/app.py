from flask import Flask

app = Flask(__name__)



@app.route('/')
def okay():
    return 'nuisrsgnb'

if __name__ == '__main__':
    context = ('cert.pem', 'key.pem')
    app.run(host='0.0.0.0',ssl_context=context)