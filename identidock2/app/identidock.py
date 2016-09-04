import requests
import hashlib

from flask import Flask, Response, request

app = Flask(__name__)
default_name = 'Hoai-Thu Vuong'
salt = 'change me plz'

@app.route('/', methods=['GET', 'POST'])
def index():
    name = default_name
    if request.method == 'POST':
        name = request.form['name']

    salted_name = salt + name
    hashed_name = hashlib.sha256(salted_name.encode()).hexdigest()

    header = '<html><head><title>Identidock</title></head><body>'
    body = '''<form method="POST">
              Hello <input type="text" name="name" value="{0}">
              <input type="submit" value="submit">
              </form>
              <br />
              <p>You look like a:
              <img src="/monster/{1}"/>
              '''.format(name, hashed_name)
    footer = '</body></html>'

    return header + body + footer


@app.route('/monster/<name>')
def get_identicon(name):
    r = requests.get('http://dnmonster:8080/monster/' + name + '?size=80')
    image = r.content

    return Response(image, mimetype='image/png')

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')

