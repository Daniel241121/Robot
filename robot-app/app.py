from flask import Flask, render_template, send_from_directory

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

# (Opcional) servir videos locales desde /static/videos/ por si quieres verificar rutas
@app.route("/videos/<path:filename>")
def videos(filename):
    return send_from_directory("static/videos", filename)

if __name__ == "__main__":
    app.run(debug=True)
