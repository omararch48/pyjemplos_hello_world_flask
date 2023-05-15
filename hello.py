from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1>Hola mundo!!!</h1>'


template = '''
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta http-equiv="refresh" content="5" />
    <meta charset="UTF-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0" />
    <title>Hello World Flask</title>
  </head>
  <body style="background: #484848;">
    <h1 style="color: white; font-family: arial;">
      Hola mundo desde un template
    </h1>
  </body>
</html>
'''


@app.route('/template')
def hello_template():
    return template