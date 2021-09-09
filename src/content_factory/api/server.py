from flask import Flask
import flask
import json

app = Flask(__name__)

@app.route("/")
def hello():
  file = open('src/content_factory/api/content.json', 'r')
  data = file.read()
  file.close()
  return flask.Response(
    response=data,
    status=200,
    mimetype='application/json'
  )

if __name__ == '__main__':
  app.run(debug=True, port=8085)
