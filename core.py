from flask import Flask, request, render_template
import csv
app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home_list(data_list=[], methods=['GET', 'POST']):
    data_table = get_table_from_file()
    return render_template("list.html", data_list=data_table)


@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
@app.route('/story', methods=['GET', 'POST'])
def story(story_id=None):
    return render_template("form.html",  story_id=story_id)


def get_table_from_file(file_name="stories.csv"):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table


def write_table_to_file(table, file_name="stories.csv"):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def ID_generator():
    table = get_table_from_file()
    return str(len(table) + 1)


@app.route('/read-input', methods=['POST'])
def add_data():
    table = get_table_from_file()
    data_list = []
    data_list.insert(0, ID_generator())
    data_list.append(request.form['story-title'])
    data_list.append(request.form['user-story'])
    data_list.append(request.form['accept-crit'])
    data_list.append(request.form['bussines-value'])
    data_list.append(request.form['estimation'])
    data_list.append(request.form['status'])
    table.append(data_list)
    write_table_to_file(table)
    return """<h2>New story added</h2>\n <button onclick="location.href='http://127.0.0.1:5000/'" type="button">List page</button> """

if __name__ == '__main__':
    app.run()