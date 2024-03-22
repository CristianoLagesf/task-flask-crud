from flask import Flask, request,jsonify
from models.task import Task
app = Flask(__name__)

tasks = []
task_id_control = 1

@app.route('/tasks', methods=['POST'])
def create_task():
    global task_id_control
    data = request.get_json()
    new_task = Task(
            id=task_id_control,
            title=data.get("title"), 
            description=data.get("description", ""))
    task_id_control +=1
    tasks.append(new_task)
    print(tasks)
    return jsonify({
        "code": 200,
        "mensagem":"Nova tarefa criada com sucesso"})

@app.route('/tasks', methods=['GET'])
def get_task():
    task_list = []
    for task in tasks:
        task_list.append(task.to_dict())
    output ={
        "tasks": task_list,
        "total_tasks": len(task_list)
    }
    return jsonify(output)


@app.route('/tasks/<int:id>', methods=['GET'])
def find_task(id):
    for t in tasks:
        if t.id == id:
            return jsonify(t.to_dict())
    return jsonify({
                "code": 404,
        "mensagem":"Not found."})

@app.route('/tasks/<int:id>', methods=['PUT'])
def update_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
    print(task)
    if task == None:
        return jsonify({
                "code": 404,
        "mensagem":"Not found."})
    
    data = request.get_json()
    task.title = data['title']
    task.description = data['description']
    task.completed = data['completed']
    print(task)
    return jsonify({
                "code": 200,
        "mensagem":"Tarefa atualizada com sucesso."})
    
    
@app.route('/tasks/<int:id>', methods=['DELETE'])
def delete_task(id):
    task = None
    for t in tasks:
        if t.id == id:
            task = t
            break
    if not task:
        return jsonify({
                "code": 404,
        "mensagem":"Not found."})
    tasks.remove(task)
    return jsonify({
                "code": 200,
        "mensagem":"Tarefa deletada."})

if __name__ == "__main__":  
    app.run(debug=True)