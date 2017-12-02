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
                    return 'project already exists'
            x = open('projectdb/'+proj['projectID'], 'w+')
            x.write(json.dumps(proj))
            x.close()
            return 'ok', 200
        return 'bad data', 400
    return 'bad data type', 422

@app.route('/delete-proj', methods =['POST'])
def api_delete_project():
    if request.headers['Content-Type'] == 'application/json':
        proj = request.get_json()
        if 'projectID' in proj.keys():
            for i in os.listdir('projectdb'):
                if proj['projectID'] == i:
                    os.remove(i)
                    return "ok", 200
            return 'can\'t find projectID', 400
        return 'bad data type', 422
    return 'bad request', 400

@app.route('/search-user-id', methods =['POST'])
def api_search_user_id():
    if request.headers['Content-Type'] == 'application/json':
        proj = request.get_json()
        if 'userID' in proj.keys():
            r = ""
            for i in os.listdir('projectdb'):
                f = json.load(open('projectdb/'+i))
                if f['userID'] == proj['userID']:
                    r = r + f.dump()
            return Response(r, 200, 'application/json')
    return 'bad data', 400

@app.route('/search-project-id', methods=['POST'])
def api_search_project_id():
    if request.headers['Content-Type'] == 'application/json':
        proj = request.get_json()
        if 'projectID' in proj.keys():
            for i in os.listdir('projectdb'):
                if str(proj['projectID']) == i:
                    with open('projectdb/'+i) as jd:
                        return Response(response=str(json.load(jd)), status=200, mimetype="application/json")
    return 'bad data', 400

@app.route('/search-project-name', methods=['POST'])
def api_project_name():
    if request.headers['Content-Type'] == 'application/json':
        proj = request.get_json()
        if 'projectName' in proj.keys():
            r = ""
            for i in os.listdir('projectdb'):
                f = json.load(open('projectdb/'+i))
                if f['projectName'].lower() == proj['projectName'].lower():
                    r = r + f.dump()
            return Response(r, 200, 'application/json')
    return 'bad data', 400

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

if __name__ == '__main__':
    with open('projectdb/1') as jd:
        print (json.load(jd))
    app.run()