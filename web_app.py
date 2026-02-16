from flask import Flask, request, render_template, flash

from core_converter import convert_markdown_to_html

app = Flask(__name__)
app.secret_key = "super secret key"

@app.route("/", methods = ['GET', 'PoST'])
def index():
    html_output = ""
    markdown_input = ""

    if request.method == "POST":
        markdown_input = request.form.get('markdown_text', '')
        if not markdown_input:
            flash('please enter some Markdown text.')
        else:
            html_output = convert_markdown_to_html(markdown_input)

    return render_template('index.html', markdown_input = markdown_input, html_output = html_output)

if __name__ == "__main__":
    app.run(debug=True, port=5001)