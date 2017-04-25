from flask import Flask, request, render_template
app = Flask(__name__)

@app.route('/')
def home_list(file_name="templates/list.html", methods=['GET']):
    # Return this to the user who visited this page. The browser will render it.
    return render_template("list.html")


@app.route('/story', methods=['GET', 'POST'])
def story_form():
    return render_template("form.html")


@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
def story_id(story_id):
    return render_template("form.html",  name=story_id)

if __name__ == '__main__':
    app.run()