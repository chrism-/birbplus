from flask import Flask, url_for, Response, json, request
import json as json2

app = Flask(__name__)

@app.route('/')
def api_root():
    return 'Welcome'

@app.route('/groups')
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/articles/<articleid>')
def api_article(articleid):
    return 'You are reading ' + articleid

@app.route('/all-projects', methods = ['GET'])
def api_hello():
    data = {
        'hello'  : 'world',
        'number' : 3
    }
    js = json.dumps(data)

    resp = Response(js, status=200, mimetype='application/json')
    resp.headers['Link'] = 'http://luisrei.com'

    return resp

@app.route('/all-projects-id', methods = ['GET'])
def api_get_projects_id():
    if request.headers['Content-Type'] == 'application/json':
        print(request.get_json())
        return "JSON Message: " + json.dumps(request.json)
    else:
        return "id needs to be specified in json"
    # data = {
    #     'hello'  : 'world',
    #     'number' : 3
    # }
    # js = json.dumps(data)
    #
    # resp = Response(js, status=200, mimetype='application/json')
    # resp.headers['Link'] = 'http://luisrei.com'
    #
    # return resp

# @app.route('/all-projects', methods = ['GET'])
# def api_message():
#     if request.headers['Content-Type'] == 'text/plain':
#         return "Text Message: " + request.data
#
#     elif request.headers['Content-Type'] == 'application/json':
#         return "JSON Message: " + json.dumps(request.json)
#
#     elif request.headers['Content-Type'] == 'application/octet-stream':
#         f = open('./binary', 'wb')
#         f.write(request.data)
#                 f.close()
#         return "Binary message written!"
#
#     else:
#         return "415 Unsupported Media Type ;)"

def get_user_projects(user):
    return

def get_user_project_id(id):
    return

def search_projects():
    return

if __name__ == '__main__':
    app.run()