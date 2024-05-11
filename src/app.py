from flask import Flask, jsonify, request

app = Flask(__name__)

todos = [
   {"label": "My first task", "done": False},
   {"label": "My second task", "done": False},
   {"label": "My third task", "done": False},
   {"label": "My fourth task", "done": False},
   {"label": "My five task", "done": False}
]

@app.route('/todos',methods=['GET'])

def  hello_world():
  todos_json = jsonify(todos)
  return todos_json,200

@app.route('/todos', methods=['POST'])
def add_new_todo():
    request_body = request.json(silent = True)
    print("Incoming request with the following body", request_body)
    todos.append({"label" : request_body["label"], "done" : request_body["done"]})
    return jsonify({"msg" : "Task is requerid"},201)




if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)