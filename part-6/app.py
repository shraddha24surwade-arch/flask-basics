"""
Part 6: Homework - Personal To-Do List App
==========================================
See Instruction.md for full requirements.

How to Run:
1. Make sure venv is activated
2. Run: python app.py
3. Open browser: http://localhost:5000
"""

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Sample data - your tasks list
TASKS = [
    {
        'id': 1,
        'title': 'Learn Flask',
        'status': 'Completed',
        'priority': 'High',
        'due_date': '2026-01-09'
    },
    {
        'id': 2,
        'title': 'Build To-Do App',
        'status': 'In Progress',
        'priority': 'Medium',
        'due_date': '2026-01-12'
    },
    {
        'id': 3,
        'title': 'Push to GitHub',
        'status': 'Pending',
        'priority': 'Low',
        'due_date': '2026-01-13'
    }
]


# Home page – list all tasks
@app.route('/')
def index():
    selected_priority = request.args.get('priority', 'All')

    if selected_priority != 'All':
        tasks = [t for t in TASKS if t['priority'] == selected_priority]
    else:
        tasks = TASKS

    # Dashboard stats (always calculated from ALL tasks)
    total = len(TASKS)
    completed = sum(1 for t in TASKS if t['status'] == 'Completed')
    in_progress = sum(1 for t in TASKS if t['status'] == 'In Progress')
    pending = sum(1 for t in TASKS if t['status'] == 'Pending')

    return render_template(
        'index.html',
        tasks=tasks,
        selected_priority=selected_priority,
        total=total,
        completed=completed,
        in_progress=in_progress,
        pending=pending
    )

@app.route('/priority/<name>')
def priority_filter(name):
    return redirect(url_for('index', priority=name))

# Add new task
@app.route('/add', methods=['GET', 'POST'])
def add_task():
    if request.method == 'POST':
        new_task = {
            'id': len(TASKS) + 1,
            'title': request.form['title'],
            'status': request.form['status'],
            'priority': request.form['priority'],
            'due_date': request.form['due_date']
        }
        TASKS.append(new_task)
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/edit/<int:id>', methods=['GET', 'POST'])
def edit_task(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    if not task:
        return redirect(url_for('index'))

    if request.method == 'POST':
        task['title'] = request.form['title']
        task['status'] = request.form['status']
        task['priority'] = request.form['priority']
        task['due_date'] = request.form['due_date']
        return redirect(url_for('task_detail', id=id))
    return render_template('edit.html', task=task)

# View single task
@app.route('/task/<int:id>')
def task_detail(id):
    task = next((t for t in TASKS if t['id'] == id), None)
    return render_template('task.html', task=task)

# About page
@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
