from flask import Flask, render_template
app = Flask(__name__,  static_folder='static', static_url_path='', 
            template_folder='templates')


@app.route("/", methods=["GET"])
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="localhost", port=1234, debug=True)