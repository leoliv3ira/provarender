from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():

    with open('provaDevOps.html', 'r') as html_file:
        html_content = html_file.read()

    with open('styles DevOps.css', 'r') as css_file:
        css_content = css_file.read()


    return render_template('dashboard.html', html_content=html_content, css_content=css_content)

if __name__ == '__main__':
    app.run(debug=True)
