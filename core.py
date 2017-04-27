from flask import Flask, request, render_template, redirect, url_for
import common

app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home_list(data_list=[]):
    data_table = common.get_table_from_file()
    return render_template("list.html", data_list=data_table)


@app.route('/story/<story_id>', methods=['GET', 'POST'])
def story_edit(story_id=None, form_data=[]):
    table = common.get_table_from_file()
    ID = request.form['edit_option']
    ID_string = str(ID)
    datas_to_fill = []
    for element in table:
        if element[0] == ID_string:
            datas_to_fill.append(element)
    return render_template("form.html",  story_id=story_id, form_data=datas_to_fill)


@app.route('/story')
def story_create(story_id=None):
    return render_template("form.html", story_id=story_id)


@app.route('/read-added-data', methods=['POST'])
def add_data():
    table = common.get_table_from_file()
    data_list = []
    data_list.insert(0, common.ID_generator(table))
    request_names = ['story-title', 'user-story', 'accept-crit',
                     'bussines-value', 'estimation', 'status']
    for name in request_names:
        data_list.append(request.form[name])
    table.append(data_list)
    common.write_table_to_file(table)
    return redirect(url_for('home_list'))


@app.route('/delete-story', methods=['POST'])
def delete_data():
    table = common.get_table_from_file()
    ID = request.form['delete']
    ID_string = str(ID)
    for element in table:
        if element[0] == ID_string:
            table.remove(element)
    common.write_table_to_file(table)
    return redirect(url_for('home_list'))


@app.route("/edit-story", methods=['POST'])
def edit_story():
    table = common.get_table_from_file()
    ID = request.form["edit"]
    ID_string = str(ID)
    changed_story = []
    changed_story.append(ID_string)
    request_names = ['changed-story-title', 'changed-user-story', 'changed-accept-crit',
                     'changed-bussines-value', 'changed-estimation', 'changed-status']
    for names in request_names:
        changed_story.append(request.form[names])
    for element in table:
        if element[0] == ID_string:
            table.remove(element)
            table.insert(0, changed_story)
    common.write_table_to_file(table)
    return redirect(url_for('home_list'))


if __name__ == '__main__':
    app.run()