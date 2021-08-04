from flask import Flask
from flask import request

app = Flask(__name__)


@app.route("/")
def index():
    html_form = """
        <html><body>
            <h1> Enter any text so it can be reversed! </h1>
            <br>
            <br>
            <br>
            <form action="" method="get">
            Text: <input type="text" name="text">
            <input type="submit" value="Reverse this text">
                </form>
        </body></html>"""

    text = request.args.get("text", "")
    if text:
        reversed_text = str(reverse(text))
        print(reversed_text)
    else:
        reversed_text = ""

    return html_form + reversed_text


def reverse(text):
    return "Reversed text of ", text, " is ", text[::-1]  # [start:end:step], step is reversed, start and stop left out


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080, debug=True)
