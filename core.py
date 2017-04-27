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


@app.route('/story', methods=['GET', 'POST'])
def story_create(story_id=None):
    return render_template("form.html", story_id=story_id)


@app.route('/read-added-data', methods=['POST'])
def add_data():
    table = common.get_table_from_file()
    data_list = []
    data_list.insert(0, common.ID_generator(table))
    data_list.append(request.form['story-title'])
    data_list.append(request.form['user-story'])
    data_list.append(request.form['accept-crit'])
    data_list.append(request.form['bussines-value'])
    data_list.append(request.form['estimation'])
    data_list.append(request.form['status'])
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


@app.route("/edit-story", methods=['GET', 'POST'])
def edit_story():
    table = common.get_table_from_file()
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
        if element[0] == ID_string:
            table.remove(element)
            table.insert(0, changed_story)
    common.write_table_to_file(table)
    return redirect(url_for('home_list'))


if __name__ == '__main__':
    app.run()