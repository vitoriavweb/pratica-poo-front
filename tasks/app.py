from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

tasks = []
next_id = 1


@app.get("/")
def index():
    return render_template("index.html", tasks=tasks)


@app.post("/add")
def add_task():
    global next_id
    title = request.form.get("title", "").strip()
    if title:
        tasks.append({"id": next_id, "title": title, "done": False})
        next_id += 1
    return redirect(url_for("index"))


@app.post("/toggle/<int:task_id>")
def toggle_task(task_id: int):
    for t in tasks:
        if t["id"] == task_id:
            t["done"] = not t["done"]
            break
    return redirect(url_for("index"))


@app.post("/delete/<int:task_id>")
def delete_task(task_id: int):
    global tasks
    tasks = [t for t in tasks if t["id"] != task_id]
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
