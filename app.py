import flask

app = flask.Flask (__name__)

@app.route('/')
def hello_world():
    return '2023-04-20_11:30'
    
if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
