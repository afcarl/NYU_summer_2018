from flask import Flask

app = Flask(__name__)

@app.route("/<name>", methods=["GET"])
def index(name):
    return "Hello " + name

if __name__ == '__main__':
    app.run(port=5001)

    
