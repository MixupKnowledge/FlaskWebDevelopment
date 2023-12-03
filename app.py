from flask import Flask, jsonify, request, render_template

app = Flask(__name__)

# first route
@app.route('/')
def hello_world():
    return 'Hello, World!'

# show data into json format
@app.route('/api/data')
def get_data():
    data = {'message': 'Welcome in flask api by Narendra kumar'}
    return jsonify(data)

# post data using postman
@app.route('/api/post_data', methods=['POST'])
def post_data():
    data = request.json
    return jsonify(data)

# render html tags
@app.route('/api/welcome')
def username():
    return '<h1>Welcome Hello world</h1>'

# render html file
@app.route('/api/<name>')
def index(name):
    return render_template('index.html', name=name)

# render form and get data from form 
@app.route('/api/signup')
def signup_form():
    return render_template('Signup.html')

# show collected data from form
@app.route('/api/subimt/signup_form', methods=['POST'])
def signup_form_data():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    data = {"username": username, "email": email, "password": password}
    return jsonify(data)

@app.route('/v1/user/name')
def method_name():
    return "<h1>Hi Welcome in Flask Web Development</h1>"


if __name__ == '__main__':
    app.run(debug=True, host="192.168.29.110", port=12000)
