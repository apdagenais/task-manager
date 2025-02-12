from flask import Blueprint, render_template, request, redirect, url_for, flash
from flask_login import login_required, current_user
from app import db
from app.models import Task
from app.forms import TaskForm

main = Blueprint('main', __name__)

@main.route('/')
def index():
    return render_template('home.html')

@main.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    form = TaskForm()

    # Handle task creation directly on the dashboard
    if form.validate_on_submit():
        new_task = Task(
            title=form.title.data,
            description=form.description.data,
            category=form.category.data,
            due_date=form.due_date.data,
            user_id=current_user.id
        )
        db.session.add(new_task)
        db.session.commit()
        flash('Task added successfully!', 'success')
        return redirect(url_for('main.dashboard'))

    category_filter = request.args.get('category', '')

    if category_filter:
        tasks = Task.query.filter_by(user_id=current_user.id, category=category_filter).all()
    else:
        tasks = Task.query.filter_by(user_id=current_user.id).all()

    return render_template('dashboard.html', tasks=tasks, form=form)


@main.route('/complete_task/<int:task_id>', methods=['POST'])
@login_required
def complete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        task.completed = True
        db.session.commit()
    return redirect(url_for('main.dashboard'))

@main.route('/delete_task/<int:task_id>', methods=['POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    if task and task.user_id == current_user.id:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('main.dashboard'))

