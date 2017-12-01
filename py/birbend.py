from flask import Flask, url_for, Response, json, request
import os

app = Flask(__name__)

@app.route('/add-proj', methods = ['POST'])
def api_store_project():
    if request.headers['Content-Type'] == 'application/json':
        proj = request.get_json()
        if 'projectID' in proj.keys():
            for i in os.listdir('projectdb'):
                if i == proj['projectID']:
                    return 'project alraedy exists'
        if 'projectOwnerID' in proj.keys():
            for i in os.listdir('projectdb'):
                if i == proj['projectOwnerID']:
                    return 'proj'
    else:
        return '520? wrong data type'

@app.route('/delete-proj', method =['POST'])
def api_delete_project():
    return 'List of ' + url_for('api_articles')

@app.route('/search-user-id', method =['POST'])
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/search-project-id', method=['POST'])
def api_articles():
    return 'List of ' + url_for('api_articles')

@app.route('/search-project-name', method=['POST'])
def api_articles():
    return 'List of ' + url_for('api_articles')

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


def get_user_projects(user):
    return

def get_user_project_id(id):
    return

def search_projects():
    return

if __name__ == '__main__':
    app.run()