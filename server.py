from flask import Flask, url_for, render_template, request, redirect
import datetime
import database_manager
import common

app = Flask(__name__)

TODO_LABELS = ['title', 'details', 'submission_time']


@app.route('/')
def route_index():
    data = database_manager.query_select_all()
    data_dict = common.query_to_dict(data, TODO_LABELS)
    return render_template('index.html', data_dict=data_dict)


@app.route('/save', methods=['POST'])
def route_save():
    data_dict = request.form.to_dict()
    data_dict['submission_time'] = datetime.datetime.now()
    database_manager.query_modify("INSERT INTO test (title, details, submission_time) \
                                   VALUES (%(title)s, %(details)s, %(submission_time)s)", data_dict)
    return redirect(url_for('route_index'))


@app.route('/<int:todo_id>/edit')
def route_todo_id_edit(todo_id):
    data = database_manager.query_select("SELECT * FROM test WHERE id = %s", (todo_id,))
    data_dict = common.query_to_dict(data, TODO_LABELS)
    return render_template('form.html', data_dict=data_dict, todo_id=todo_id)


@app.route('/<int:todo_id>/update', methods=['POST'])
def route_todo_id_update(todo_id):
    print('update form', request.form)
    database_manager.query_modify("UPDATE test SET title = %s, details = %s WHERE id = %s",
                                  (request.form['title'], request.form['details'], todo_id))
    return redirect(url_for('route_index'))


@app.route('/<int:todo_id>/delete')
def route_todo_id_delete(todo_id):
    database_manager.query_modify("DELETE FROM test WHERE id = %s", (todo_id,))
    return redirect(url_for('route_index'))


if __name__ == "__main__":
    app.run(debug=True)