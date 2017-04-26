from flask import Flask, request, render_template


app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home_list(data_list=[], methods=['GET', 'POST']):
    data_table = get_table_from_file()
    return render_template("list.html", data_list=data_table)

@app.route('/story/<story_id>', methods=['GET', 'POST'])
def story_edit(story_id=None, form_data=[]):
    table = get_table_from_file()
    ID = request.form['edit_option']
    ID_string = str(ID)
    datas_to_fill = []
    for element in table:
        if element[0] == ID_string:
            datas_to_fill.append(element)
    return render_template("form.html",  story_id=story_id, form_data=datas_to_fill)

@app.route('/story', methods=['GET', 'POST'])
def story_create(story_id=None):
    return render_template("form.html", story_id=story_id)


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
    return render_template("list.html", data_list=table)


@app.route('/delete-story', methods=['POST'])
def delete_data(data_list=[]):
    table = get_table_from_file()
    ID = request.form['delete']
    ID_string = str(ID)
    for element in table:
        if element[0] == ID_string:
            table.remove(element)
    write_table_to_file(table)
    return render_template("list.html", data_list=table)


@app.route("/edit-story", methods=['GET', 'POST'])
def edit_story(data_list=[]):
    table = get_table_from_file()
    ID = request.form["edit"]
    ID_string = str(ID)
    changed_story = []
    changed_story.append(ID_string)
    changed_story.append(request.form['changed-story-title'])
    changed_story.append(request.form['changed-user-story'])
    changed_story.append(request.form['changed-accept-crit'])
    changed_story.append(request.form['changed-bussines-value'])
    changed_story.append(request.form['changed-estimation'])
    changed_story.append(request.form['changed-status'])
    for element in table:
        for index, item in enumerate(element):
            if item == ID_string:
                table.remove(element)
                table.insert(index, changed_story)
    write_table_to_file(table)
    return render_template("list.html", data_list=table)


if __name__ == '__main__':
    app.run()