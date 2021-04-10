from flask import Flask, jsonify, abort, request

app = Flask(__name__)

tasks = [
    {
        'id': 1,
        'title': '交電話費',
        'note': '500元',
        'done': False
    },
    {
        'id': 2,
        'title': '錄教學影片',
        'note': 'rest api for todo app',
        'done': False
    }
]


@app.route('/api/tasks', methods=['GET'])
def get_tasks():
    return jsonify({'tasks': tasks})


@app.route('/api/tasks/<int:task_id>', methods=['GET'])
def get_task(task_id):
    task = [x for x in tasks if x['id'] == task_id]
    if len(task) == 0:
        abort(404)
    return jsonify({'task': task[0]})


@app.route('/api/tasks', methods=['POST'])
def create_task():
    if request.json is None or 'title' not in request.json:
        abort(400)
    task = {
        'id': tasks[-1]['id'] + 1,
        'title': request.json['title'],
        'note': request.json.get('note', ''),
        'done': False
    }
    tasks.append(task)
    return jsonify({'task': task}), 201


@app.route('/api/tasks/<int:task_id>', methods=['DELETE'])
def delete_task(task_id):
    task = [x for x in tasks if x['id'] == task_id]
    if len(task) == 0:
        abort(404)
    tasks.remove(task[0])
    return jsonify({'result': True})


@app.route('/api/tasks/<int:task_id>', methods=['PUT'])
def update_task(task_id):
    task = [x for x in tasks if x['id'] == task_id]
    if len(task) == 0:
        abort(404)
    if request.json is None:
        abort(400, "No JSON data!!!")
    if 'title' in request.json and type(request.json['title']) != str:
        abort(400, "title field is not a string!!!")
    if 'note' in request.json and type(request.json['note']) != str:
        abort(400, "note field is not a string!!!")
    if 'done' in request.json and type(request.json['done']) != bool:
        abort(400, "done field is not boolean!!!")

    task[0]['title'] = request.json.get('title', task[0]['title'])
    task[0]['note'] = request.json.get('note', task[0]['note'])
    task[0]['done'] = request.json.get('done', task[0]['done'])

    return jsonify({'task': task[0]})


if __name__ == '__main__':
    app.run()
