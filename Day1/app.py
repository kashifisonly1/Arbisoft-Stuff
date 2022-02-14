from flask import Flask, request, jsonify, render_template

app = Flask(__name__)

stds = [{
    "name": "kashif",
    "id": 1
},
{
    "name": "baqir",
    "id": 3
}]


@app.route("/")
def index():
    return render_template("index.html")

@app.route("/students")
def students():
    if request.args.get("id") is None:
        return jsonify(stds)
    new_list = []
    for std in stds:
        if int(request.args.get("id"))==std["id"]:
            new_list.append(std)
    return jsonify(new_list)

@app.route("/students/new", methods=["POST"])
def new_student():
    if request.form.get("name") is None or request.form.get("id") is None:
        return jsonify({"error": "invalid data"}), 400
    stds.append({ "name":  request.form["name"], "id": int(request.form["id"])})
    return jsonify(stds[-1])

app.run()