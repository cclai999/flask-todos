from flask import Flask, jsonify, abort

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
    return jsonify({'task': task})


if __name__ == '__main__':
    app.run()
