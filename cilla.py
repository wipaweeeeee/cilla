from flask import Flask, render_template
import cilla_for_cilla

app = Flask(__name__)

@app.route("/")
def hello(name="name"):
	name = cilla_for_cilla.make_sentence()	
	return render_template('home.html', name=name)

if __name__ == "__main__":
    app.run()
