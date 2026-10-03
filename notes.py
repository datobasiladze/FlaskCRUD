from flask import Flask, request, render_template, session

app = Flask(__name__)

app.secret_key = "kirva"


@app.route("/", methods=["POST", "GET"])
def writez():
    error = None
    notez = session.get("notez", [])

    if request.method == "POST":
        note = request.form["note"]
        notez.append(note)
        session["notez"] = notez

    return render_template("note.html", mynote=notez)


@app.route("/update/<int:id>", methods=["GET", "PUT"])
def update(id):
    notez = session.get("notez", [])
    if request.method == "GET":
        note = notez[id]
        return render_template("update.html", note=note, id=id)

    if request.method == "PUT":
        data = request.get_json()
        notez[id] = data["update"]
        session["notez"] = notez

    return "Updated Successfully"


if __name__ == "__main__":
    app.run(debug=True)
