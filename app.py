from flask import Flask, render_template,redirect,url_for,request
from models import todos
from forms import TodoForm

app = Flask(__name__)
app.config["SECRET_KEY"] = "nininini"

@app.route("/", methods=["GET", "POST"])
def todos_list():
    form = TodoForm()
    error = ""
    if request.method == "POST":
        if form.validate_on_submit():
            todos.create(form.data)
            todos.save_all()
        return redirect(url_for("todos_list"))

    return render_template("todos.html", form=form, todos=todos.all(), error=error)


if __name__ == "__main__":
    app.run(debug=True)