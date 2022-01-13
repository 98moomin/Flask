from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def call_API():
    return render_template('index.html')

@app.route('/test', methods =['POST'])
def test():
    data = {
        'msg' : 'msg',
        'code' : '200'
    }
    return data

if __name__ == "__main__":
    app.run(port=5000, debug=True)