from flask import Flask, render_template, request, redirect, session, url_for
import os
import random
import string


app = Flask(__name__)

@app.route("/", methods=['POST'])
def fileupload():
        filestring = str(''.join(random.choice(string.ascii_lowercase + string.digits) for _ in range(8)))
        f = request.files['file']
        filename = filestring + "." + str(f.filename).split(".")[1]
        f.save("static/" + filename)
        return render_template("download.html", downloadlink = request.url + "static/" + filename )


@app.route("/")
def index():
    return render_template("index.html")

if __name__ == '__main__':
    app.run()
