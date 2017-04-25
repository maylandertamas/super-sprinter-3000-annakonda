from flask import Flask, request, render_template
app = Flask(__name__)


@app.route('/')
def home_list(file_name="templates/list.html", methods=['GET']):
    # Return this to the user who visited this page. The browser will render it.
    return render_template("list.html")

"""
@app.route('/story', methods=['GET', 'POST'])
def story_form():
    return "<h1></h1>\n" + "<title></title>\n" + render_template("form.html")
"""


@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
@app.route('/story', methods=['GET', 'POST'])
def story_id(story_id=None):
    return render_template("form.html",  story_id=story_id)


if __name__ == '__main__':
    app.run()