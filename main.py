from flask import Flask, request
from caesar import rotate_string

app = Flask(__name__)
app.config['DEBUG'] = True

form = """
<!DOCTYPE html>

<html>
    <head>
        <style>
            form {{
                background-color: #eee;
                padding: 20px;
                margin: 0 auto;
                width: 540px;
                font: 16px sans-serif;
                border-radius: 10px;
            }}
            textarea {{
                margin: 10px 0;
                width: 540px;
                height: 120px;
            }}
        </style>
    </head>
    <body>
        <form method="POST" action="/">
            <label>
                Rotate By 
                <input type="text" name="rot" value="0"/>
                    <textarea name="text">{0}</textarea>
                </label>
            <input type="submit" value="Submit query"/> 
    </body>
</html>
"""

@app.route("/")
def index():
    return form

@app.route("/", methods=["POST"])
def encrypt():
    rot = request.form["rot"]
    text = request.form["text"]
    rot= int(float(rot))

    new_text = rotate_string(text,rot)

    return form.format(new_text)


app.run()