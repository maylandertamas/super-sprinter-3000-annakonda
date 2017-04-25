from flask import Flask, request, render_template
import csv
app = Flask(__name__)


@app.route('/')
@app.route('/list')
def home_list(file_name="templates/list.html", methods=['GET', 'POST']):
    return render_template("list.html")


@app.route('/story/<int:story_id>', methods=['GET', 'POST'])
@app.route('/story', methods=['GET', 'POST'])
def story(story_id=None):
    return render_template("form.html",  story_id=story_id)



def get_table_from_file(file_name="stories.csv"):
    with open(file_name, "r") as file:
        lines = file.readlines()
    table = [element.replace("\n", "").split(";") for element in lines]
    return table
    

def write_table_to_file(file_name, table):
    with open(file_name, "w") as file:
        for record in table:
            row = ';'.join(record)
            file.write(row + "\n")


def ID_generator():
    table = get_table_from_file()
    for ID in table[0]:
        return int(max(ID))+1

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
    print(data_list)
    table.append(data_list)
    print(table)
    #write_to_file
    return "Lol"
    """
    with open('stories.csv','w') as inFile:
            inFile.write(row)
    return "Danke"
    """
"""
    if request.method == 'POST':
        name = request.form['name']
        with open('templates/stories.csv','w') as inFile:
            writer = csv.writer(inFIle)
            writer.writerow(name)
        return render_template("list.html")
"""
if __name__ == '__main__':
    app.run()