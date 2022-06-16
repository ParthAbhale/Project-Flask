from flask import Flask,jsonify,request

app = Flask(__name__)




task = [
    {
        "Contact":"9987644456",
        "name":"Raju",
        "Done":False,
        "id":1
    },
    {
        "Contact":"9876543222",
        "name":"Rahul",
        "Done":False,
        "id":4
    },
    
]

@app.route('/')
def greet():
    return jsonify({"task":task})

@app.route('/add-data',methods=["POST"])
def add_data():
    if not request.json:
        return jsonify({
            "Error":"Please Provide Data for updating..."
        },404)
    else:
        updated_tasks = {
            "name":request.json["name"],
            "Contact":request.json["Contact"],
            "Done":True,
            "id":task[-1]["id"] + 1
        }
        task.append(updated_tasks)
        return jsonify({"updated_task": task , "Message": "Task added successfully"},200)


if __name__ == "__main__":
    app.run(debug=True)