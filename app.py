from flask import Flask, render_template, request, flash, redirect, url_for
import json
from flask_sqlalchemy import SQLAlchemy
import random
from datetime import datetime
import re
from flask_login import login_user, LoginManager, login_required, logout_user, current_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from webforms import TypeSelectForm, BigForm, TeacherForm, UserForm, LogInForm, AnswerForm, AnswerForm4, AnswerForm5, AnswerForm10

app = Flask(__name__)
db = SQLAlchemy(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'


class exercise_type_1(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    video = db.Column(db.String)
    options = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_2(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_3(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_4(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_5(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_6(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_7(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_8(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_9(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_10(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_11(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_12(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_13(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_14(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_15(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_16(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_17(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_18(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_19(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    audio = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_20(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_21(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_22(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_23(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_24(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_25(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    picture = db.Column(db.String)


class exercise_type_26(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class exercise_type_27(db.Model):
    exercise_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_url = db.Column(db.String)
    add_timestamp = db.Column(db.DateTime)
    expert_id = db.Column(db.Integer)
    exercise_level = db.Column(db.String)
    task = db.Column(db.String)
    right_answer = db.Column(db.String)


class users_answers(db.Model):
    answer_id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer)
    answer = db.Column(db.String)
    exercise_type_id = db.Column(db.Integer)
    exercise_id = db.Column(db.Integer)
    answer_timestamp = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.Integer)
    teacher_id = db.Column(db.Integer)
    right_answer = db.Column(db.String)


class exercise_types(db.Model):
    exercise_type_id = db.Column(db.Integer, primary_key=True)
    exercise_type_section = db.Column(db.String)
    exercise_type_table = db.Column(db.String)
    exercise_type_html = db.Column(db.String)
    description = db.Column(db.String)


class users(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String, nullable=False)
    login = db.Column(db.String, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)
    level = db.Column(db.String, nullable=False)
    mail = db.Column(db.String, unique=True, nullable=False)
    gender = db.Column(db.String)
    age = db.Column(db.Integer)
    country = db.Column(db.String)
    city = db.Column(db.String)
    native_langs = db.Column(db.String)
    studied_langs_level = db.Column(db.String)
    status = db.Column(db.String, default='student')

    def get_id(self):
        return self.user_id

    @property
    def password(self):
        raise AttributeError('password is not a readable attribute')

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)


@login_manager.user_loader
def load_user(user_id):
    return users.query.get(int(user_id))


tables = {'1': exercise_type_1, '2': exercise_type_2, '3': exercise_type_3, '4': exercise_type_4,
          '5': exercise_type_5, '6': exercise_type_6, '7': exercise_type_7, '8': exercise_type_8,
          '9': exercise_type_9, '10': exercise_type_10, '11': exercise_type_11, '12': exercise_type_12,
          '13': exercise_type_13, '14': exercise_type_14, '15': exercise_type_15, '16': exercise_type_16,
          '17': exercise_type_17, '18': exercise_type_18, '19': exercise_type_19, '20': exercise_type_20,
          '21': exercise_type_21, '22': exercise_type_22, '23': exercise_type_23, '24': exercise_type_24,
          '25': exercise_type_25, '26': exercise_type_26, '27': exercise_type_27}


ru_alphabet = ['а', 'б', 'в', 'г', 'д', 'е', 'ё', 'ж', 'з', 'и', 'й', 'к', 'л', 'м', 'н', 'о', 'п', 'р',
               'с', 'т', 'у', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ъ', 'ы', 'ь', 'э', 'ю', 'я']
ru_vowels = ['ё', 'у', 'е', 'э', 'о', 'а', 'ы', 'я', 'и', 'ю']
ru_consonants = ['й', 'ц', 'к', 'н', 'г', 'ш', 'щ', 'з', 'х', 'ъ', 'ж', 'д', 'л', 'р', 'п', 'в', 'ф',
                 'ч', 'с', 'м', 'т', 'ь', 'б']


def picture_exercise(que, exe_no):
    exercise = que.query.get(int(exe_no))
    exercise_level = exercise.exercise_level
    section = exercise.exercise_type_section
    task = exercise.task
    picture = exercise.picture
    next_exercise = que.query.get(int(exe_no) + 1)
    url = exercise.exercise_url
    if next_exercise:
        next_exercise = next_exercise.exercise_url
    else:
        next_exercise = None
    return exercise_level, section, task, picture, next_exercise, url


def video_exercise(que, exe_no):
    exercise = que.query.get(int(exe_no))
    options = list(json.loads(exercise.options).items())
    exercise_level = exercise.exercise_level
    section = exercise.exercise_type_section
    task = exercise.task
    video = exercise.video
    right_answer = str(exercise.right_answer)
    next_exercise = que.query.get(int(exe_no) + 1)
    url = exercise.exercise_url
    if next_exercise:
        next_exercise = next_exercise.exercise_url
    else:
        next_exercise = None
    return exercise_level, section, task, video, options, right_answer, next_exercise, url


def str_answer(que, exe_no):
    exercise = que.query.get(int(exe_no))
    exercise_level = exercise.exercise_level
    section = exercise.exercise_type_section
    task = exercise.task
    right_answer = str(exercise.right_answer)
    next_exercise = que.query.get(int(exe_no) + 1)
    url = exercise.exercise_url
    if next_exercise:
        next_exercise = next_exercise.exercise_url
    else:
        next_exercise = None
    return exercise_level, section, task, right_answer, next_exercise, url


def str_from_list(que, exe_no):
    exercise = que.query.get(int(exe_no))
    exercise_level = exercise.exercise_level
    section = exercise.exercise_type_section
    task = exercise.task
    right_answer = list(json.loads(exercise.right_answer))
    next_exercise = que.query.get(int(exe_no) + 1)
    url = exercise.exercise_url
    if next_exercise:
        next_exercise = next_exercise.exercise_url
    else:
        next_exercise = None
    return exercise_level, section, task, right_answer, next_exercise, url


def convow(letters):
    ranswer = ''
    for letter in letters:
        if letter in ru_vowels:
            ranswer += letter
    return ranswer, letters


def several_forms_str(que, exe_no):
    exercise = que.query.get(int(exe_no))
    exercise_level = exercise.exercise_level
    section = exercise.exercise_type_section
    task, items = re.split('\n', exercise.task)
    right_answer = json.loads(exercise.right_answer)
    next_exercise = que.query.get(int(exe_no) + 1)
    url = exercise.exercise_url
    if next_exercise:
        next_exercise = next_exercise.exercise_url
    else:
        next_exercise = None
    return exercise_level, section, task, right_answer, items, next_exercise, url


def audio_exercise(que, exe_no):
    exercise = que.query.get(int(exe_no))
    exercise_level = exercise.exercise_level
    section = exercise.exercise_type_section
    audio = exercise.audio
    task, items = re.split('\n', exercise.task)
    right_answer = json.loads(exercise.right_answer)
    next_exercise = que.query.get(int(exe_no) + 1)
    url = exercise.exercise_url
    if next_exercise:
        next_exercise = next_exercise.exercise_url
    else:
        next_exercise = None
    return exercise_level, section, task, right_answer, items, next_exercise, audio, url


def several_forms_in_text(que, exe_no):
    exercise = que.query.get(int(exe_no))
    exercise_level = exercise.exercise_level
    section = exercise.exercise_type_section
    task, text = re.split('\n', exercise.task)
    right_answer = exercise.right_answer
    next_exercise = que.query.get(int(exe_no) + 1)
    url = exercise.exercise_url
    if next_exercise:
        next_exercise = next_exercise.exercise_url
    else:
        next_exercise = None
    return exercise_level, section, task, right_answer, text, next_exercise, url


def answer_writer(user_id, answer, exercise_type_id, exercise_id, teacher_id, right_answer):
    if type(right_answer) is str or type(right_answer) is dict:
        if answer == right_answer:
            grade = 1
        else:
            grade = 0
    elif type(right_answer) is list:
        if answer in right_answer:
            grade = 1
        else:
            grade = 0
    elif right_answer is None:
        grade = 0
    user_answer = users_answers(user_id=user_id, answer=answer, exercise_type_id=exercise_type_id,
                                exercise_id=exercise_id, grade=grade, teacher_id=teacher_id,
                                right_answer=right_answer)
    db.session.add(user_answer)
    db.session.commit()


def admin_verify():
    some_user = users.query.get(current_user.user_id)
    if some_user.status == 'admin':
        return True
    else:
        return False


def teacher_verify():
    some_user = users.query.get(current_user.user_id)
    if some_user.status == 'teacher':
        return True
    else:
        return False


@app.route('/', methods=['GET', 'POST'])
def check():
    form = LogInForm()
    if form.validate_on_submit():
        user = users.query.filter_by(login=form.login.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                return redirect(url_for('profile'))
            else:
                flash('Неверный пароль')
        else:
            flash('Пользователя с таким логином не существует')
    return render_template('fine.html', form=form)


@app.route('/admin/add_teacher', methods=['GET', 'POST'])
@login_required
def add_teacher():
    form = TeacherForm()
    if admin_verify() is True:

        if form.validate_on_submit():
            user = users.query.filter_by(mail=form.mail.data).first()

            if user is None:
                hashed_pw = generate_password_hash(form.password_hash.data, 'sha256')
                user = users(name=form.name.data, login=form.login.data, level='C2', mail=form.mail.data,
                             status='teacher', password_hash=hashed_pw)
                form.name.data = ''
                form.login.data = ''
                form.password_hash.data = ''
                form.mail.data = ''
                db.session.add(user)
                db.session.commit()
                flash('Преподаватель зарегистрирован')
                return redirect(url_for('admin'))
            else:
                flash('Такой пользователь уже зарегистрирован')

        return render_template('teacher_registration.html', form=form)

    else:
        flash('Туда может попасть только администратор')
        return redirect(url_for('profile'))


@app.route('/registration', methods=['GET', 'POST'])
def registration():
    form = UserForm()
    if form.validate_on_submit():
        user = users.query.filter_by(mail=form.mail.data).first()
        if user is None:
            hashed_pw = generate_password_hash(form.password_hash.data, "sha256")
            studied_langs = {form.lang1.data: form.level1.data, form.lang2.data: form.level2.data,
                             form.lang3.data: form.level3.data}
            user = users(name=form.name.data, login=form.login.data, level=form.level.data, mail=form.mail.data,
                         gender=form.gender.data, age=form.age.data, country=form.country.data, city=form.city.data,
                         native_langs=form.native_langs.data, studied_langs_level=str(studied_langs),
                         password_hash=hashed_pw)
            db.session.add(user)
            db.session.commit()
            form.name.data = ''
            form.login.data = ''
            form.password_hash.data = ''
            form.level.data = ''
            form.mail.data = ''
            form.gender.data = ''
            form.age.data = ''
            form.country.data = ''
            form.city.data = ''
            form.native_langs.data = ''
            form.lang1.data = ''
            form.lang2.data = ''
            form.lang3.data = ''
            form.level1.data = ''
            form.level2.data = ''
            form.level3.data = ''
            flash('Добро пожаловать!')
            return redirect(url_for('login'))
        else:
            flash('Такой пользователь уже зарегистрирован')
    return render_template('registration.html', form=form)


@app.route('/profile', methods=['GET', 'POST'])
@login_required
def profile():
    form = TypeSelectForm()
    if current_user.status == 'student':
        answers = list(users_answers.query.filter_by(user_id=current_user.user_id))
        if form.validate_on_submit():
            type_no = form.sel.data
            answers = list(users_answers.query.filter_by(user_id=current_user.user_id, exercise_type_id=type_no))
        return render_template('profile.html', answers=answers, form=form)
    elif current_user.status == 'teacher':
        answers = list(users_answers.query.order_by(users_answers.answer_timestamp).all())
        if form.validate_on_submit():
            type_no = form.sel.data
            answers = list(users_answers.query.filter_by(exercise_type_id=type_no))
        return render_template('profile.html', answers=answers, form=form)
    elif current_user.status == 'admin':
        teachers = users.query.filter_by(status='teacher')
        students = users.query.filter_by(status='student')
        return render_template('profile.html', teachers=teachers, students=students)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LogInForm()
    if form.validate_on_submit():
        user = users.query.filter_by(login=form.login.data).first()
        if user:
            if check_password_hash(user.password_hash, form.password.data):
                login_user(user)
                return redirect(url_for('profile'))
            else:
                flash('Неверный пароль')
        else:
            flash('Пользователя с таким логином не существует')
    return render_template('login.html', form=form)


@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/update_teacher/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update_teacher(user_id):
    form = TeacherForm()
    user_to_update = users.query.get_or_404(user_id)
    if request.method == "POST":
        user_to_update.name = request.form['name']
        user_to_update.email = request.form['mail']
        user_to_update.login = request.form['login']
        try:
            db.session.commit()
            flash("Информация обновлена")
            return redirect(url_for('admin'))
        except:
            flash("Возникла какая-то проблема")
            return render_template("update_teacher.html", form=form, user_to_update=user_to_update, user_id=user_id,
                                   adm=admin_verify())
    else:
        return render_template("update_teacher.html", form=form, user_to_update=user_to_update, user_id=user_id,
                               adm=admin_verify())


@app.route('/update/<int:user_id>', methods=['GET', 'POST'])
@login_required
def update_user(user_id):
    form = UserForm()
    user_to_update = users.query.get(user_id)
    if request.method == "POST":
        user_to_update.name = request.form['name']
        print(request.form['name'])
        user_to_update.email = request.form['mail']
        user_to_update.login = request.form['login']
        user_to_update.level = request.form['level']
        user_to_update.gender = request.form['gender']
        user_to_update.age = request.form['age']
        user_to_update.native_langs = request.form['native_langs']
        user_to_update.country = request.form['country']
        user_to_update.city = request.form['city']
        db.session.commit()
        flash("Информация обновлена")
        return redirect(url_for('profile'))
    else:
        return render_template("update_user.html", form=form, user_to_update=user_to_update, user_id=user_id,
                               adm=admin_verify())


@app.route('/allexercises', methods=['GET', 'POST'])
def showall():
    alphabet_phonology = exercise_types.query.filter(exercise_types.exercise_type_section == 'алфавит и фонология').all()
    morphology = exercise_types.query.filter(exercise_types.exercise_type_section == 'морфология').all()
    writing = exercise_types.query.filter(exercise_types.exercise_type_section == 'письмо').all()
    translating = exercise_types.query.filter(exercise_types.exercise_type_section == 'перевод').all()
    listening = exercise_types.query.filter(exercise_types.exercise_type_section == 'аудирование').all()
    video = exercise_types.query.filter(exercise_types.exercise_type_section == 'видео').all()
    return render_template('all_exercises.html', alphabet_phonology=alphabet_phonology, morphology=morphology,
                           writing=writing, translating=translating, listening=listening, video=video)


@app.route('/exercise/<type_no>', methods=['GET', 'POST'])
def show_type(type_no):
    que = tables[str(type_no)]
    result = que.query.all()
    return render_template('type_page.html', result=result)


@app.route('/check/<answer_id>', methods=['GET', 'POST'])
@login_required
def set_grade(answer_id):
    if teacher_verify() is True:
        form = AnswerForm()
        answer_to_update = users_answers.query.get(answer_id)
        if request.method == 'POST':
            answer_to_update.grade = int(request.form['user_answer'])
            answer_to_update.teacher_id = current_user.user_id
            db.session.commit()
            flash('Оценка выставлена')
        return render_template('set_grade.html', form=form, answer_to_update=answer_to_update)
    else:
        flash('Туда может попасть только преподаватель')
        return redirect(url_for('profile'))


@app.route('/exercise/<type_no>/<exe_no>', methods=['GET', 'POST'])
@login_required
def exerciser(type_no, exe_no):
    if type_no in ['1']:
        que = tables[str(type_no)]
        result = video_exercise(que, exe_no)
        form = AnswerForm()
        user_answer = request.form.get('flexRadioDefault')
        if user_answer:
            answer_writer(current_user.get_id(), user_answer, type_no, exe_no, 0, result[5])
        return render_template('video_exercise.html', exercise_id=exe_no, exercise_level=result[0], section=result[1],
                               task=result[2], video=result[3], options=result[4], right_answer=result[5], form=form,
                               user_answer=user_answer, next_exercise=result[6], this_exercise=result[7])

    elif type_no in ['2', '3', '5', '23']:
        que = tables[str(type_no)]
        result = str_answer(que, exe_no)
        user_answer = None
        task, item = re.split(r'\n', result[2])
        form = AnswerForm()
        if form.validate_on_submit():
            user_answer = form.user_answer.data
            form.user_answer.data = ''
            answer_writer(current_user.get_id(), user_answer, type_no, exe_no, 0, result[3])
        return render_template('exercise_page.html', exercise_id=exe_no, exercise_level=result[0], section=result[1],
                               task=task, right_answer=result[3], form=form, user_answer=user_answer,
                               next_exercise=result[4], this_exercise=result[5], item=item)

    elif type_no in ['4']:
        que = tables[str(type_no)]
        result = str_from_list(que, exe_no)
        user_answer = None
        task, item = re.split(r'\n', result[2])
        form = AnswerForm()
        if form.validate_on_submit():
            user_answer = form.user_answer.data
            form.user_answer.data = ''
            answer_writer(current_user.get_id(), user_answer, type_no, exe_no, 0, str(result[3]))
        return render_template('exercise_page.html', exercise_id=exe_no, exercise_level=result[0], section=result[1],
                               task=task, right_answer=result[3], form=form, user_answer=user_answer,
                               next_exercise=result[4], this_exercise=result[5], item=item)

    elif type_no in ['6']:
        que = tables[str(type_no)]
        result = several_forms_in_text(que, exe_no)
        user_answers = None
        form = AnswerForm10()
        text = re.sub(r'\)', ')*', result[4])
        parts = re.split(r'\*', text)
        if form.validate_on_submit():
            user_answer1 = form.user_answer1.data
            user_answer2 = form.user_answer2.data
            user_answer3 = form.user_answer3.data
            user_answer4 = form.user_answer4.data
            user_answer5 = form.user_answer5.data
            user_answer6 = form.user_answer6.data
            user_answer7 = form.user_answer7.data
            user_answer8 = form.user_answer8.data
            user_answer9 = form.user_answer9.data
            user_answer10 = form.user_answer10.data
            user_answers = {'1': user_answer1, '2': user_answer2, '3': user_answer3, '4': user_answer4,
                            '5': user_answer5, '6': user_answer6, '7': user_answer7, '8': user_answer8,
                            '9': user_answer9, '10': user_answer10}
            answer_writer(current_user.get_id(), str(user_answers), type_no, exe_no, 0, str(result[3]))
        return render_template('10_forms_in_text_exercise.html', exercise_id=exe_no, exercise_level=result[0],
                               section=result[1], task=result[2], parts=parts, right_answer=result[3],
                               user_answers=user_answers, form=form, next_exercise=result[5], this_exercise=result[6])

    elif type_no in ['7', '8', '9']:
        que = tables[str(type_no)]
        result = several_forms_str(que, exe_no)
        user_answers = None
        items = re.split(r'\;', result[4])
        form = AnswerForm4()
        if form.validate_on_submit():
            user_answer1 = form.user_answer1.data
            user_answer2 = form.user_answer2.data
            user_answer3 = form.user_answer3.data
            user_answer4 = form.user_answer4.data
            user_answers = {'1': user_answer1, '2': user_answer2, '3': user_answer3, '4': user_answer4}
            answer_writer(current_user.get_id(), str(user_answers), type_no, exe_no, 0, str(result[3]))
        return render_template('4_forms_exercise.html', exercise_id=exe_no, exercise_level=result[0], section=result[1],
                               task=result[2], items=items, right_answer=result[3], user_answers=user_answers,
                               form=form, next_exercise=result[5], this_exercise=result[6])

    elif type_no in ['14', '15', '18']:
        que = tables[str(type_no)]
        result = several_forms_in_text(que, exe_no)
        user_answers = None
        form = AnswerForm4()
        four_parts = re.split(r'\;', result[4])
        parts = []
        for part in four_parts:
            items = re.split(r'\.\.\.', part)
            parts.append(items)
        if form.validate_on_submit():
            user_answer1 = form.user_answer1.data
            user_answer2 = form.user_answer2.data
            user_answer3 = form.user_answer3.data
            user_answer4 = form.user_answer4.data
            user_answers = {'1': user_answer1, '2': user_answer2, '3': user_answer3, '4': user_answer4}
            user_answers = re.sub(r'\'', r'"', str(user_answers))
            answer_writer(current_user.get_id(), str(user_answers), type_no, exe_no, 0, str(result[3]))
        return render_template('4_forms_in_text_exercise.html', exercise_id=exe_no, exercise_level=result[0],
                               section=result[1], task=result[2], parts=parts, right_answer=str(result[3]),
                               user_answers=user_answers, form=form, next_exercise=result[5], this_exercise=result[6])

    elif type_no in ['16', '17', '22', '26']:
        que = tables[str(type_no)]
        result = str_answer(que, exe_no)
        user_answer = None
        form = AnswerForm()
        task, item = re.split(r'\n', result[2])
        items = re.split(r'\*', item)
        if form.validate_on_submit():
            if type_no == '17':
                user_answer = str(re.findall(r'\w+', form.user_answer.data))
                user_answer = re.sub('\'', '\"', user_answer)
            else:
                user_answer = form.user_answer.data
            form.user_answer.data = ''
            answer_writer(current_user.get_id(), str(user_answer), type_no, exe_no, 0, str(result[3]))
        return render_template('exercise_page.html', exercise_id=exe_no, exercise_level=result[0], section=result[1],
                               task=task, right_answer=result[3], form=form, user_answer=user_answer,
                               next_exercise=result[4], items=items, this_exercise=result[5])

    elif type_no in ['19']:
        que = tables[str(type_no)]
        result = audio_exercise(que, exe_no)
        user_answers = None
        form = AnswerForm4()
        four_parts = re.split(r'\;', result[4])
        parts = []
        for part in four_parts:
            items = re.split(r'\.\.\.', part)
            parts.append(items)
        if form.validate_on_submit():
            user_answer1 = form.user_answer1.data
            user_answer2 = form.user_answer2.data
            user_answer3 = form.user_answer3.data
            user_answer4 = form.user_answer4.data
            user_answers = {'1': user_answer1, '2': user_answer2, '3': user_answer3, '4': user_answer4}
            answer_writer(current_user.get_id(), str(user_answers), type_no, exe_no, 0, str(result[3]))
        return render_template('4_forms_in_text_exercise.html', exercise_id=exe_no, exercise_level=result[0],
                               section=result[1], task=result[2], parts=parts, right_answer=result[3],
                               user_answers=user_answers, form=form, next_exercise=result[5], audio=result[6],
                               this_exercise=result[7])

    elif type_no in ['10']:
        options_name = 'Основы глаголов'
        options = [1, 2, 3, 4, 5, 6]
        columns = ['На первый', 'На второй', 'На третий']
        return render_template('dragndrop_exercise.html', option1=options[0], option2=options[1], option3=options[2],
                               option4=options[3], option5=options[4], option6=options[5], options_name=options_name,
                               column1=columns[0], column2=columns[1], column3=columns[2])

    elif type_no in ['13']:
        que = tables[str(type_no)]
        result = several_forms_str(que, exe_no)
        user_answers = None
        items = re.split(r'\;', result[4])
        right_answer = result[3]
        form = AnswerForm5()
        if form.validate_on_submit():
            user_answer1 = form.user_answer1.data
            user_answer2 = form.user_answer2.data
            user_answer3 = form.user_answer3.data
            user_answer4 = form.user_answer4.data
            user_answer5 = form.user_answer5.data
            user_answers = {items[0]: user_answer1, items[1]: user_answer2, items[2]: user_answer3,
                            items[3]: user_answer4, items[4]: user_answer5}
            answer_writer(current_user.get_id(), user_answers, type_no, exe_no, 0, result[3])
            c = 0
            for i in range(0, 5):
                if list(user_answers.values())[i] in list(right_answer.values())[i]:
                    c += 1
            if c == 5:
                user_answers = right_answer

        return render_template('5_forms_exercise.html', exercise_id=exe_no, exercise_level=result[0],
                               section=result[1], task=result[2], items=items, right_answer=right_answer,
                               user_answers=user_answers, form=form, next_exercise=result[5])

    elif type_no in ['20']:
        letters = random.sample(ru_alphabet, 8)
        result = convow(letters)
        db.session.add(exercise_type_20(exercise_type_section="фонетика",
                                        exercise_url="http://127.0.0.1:5000/exercise/20/1",
                                        add_timestamp="2007-04-30 13:10:02.047", expert_id=0, exercise_level="A1",
                                        task=str(letters), right_answer=result[0]))
        db.session.commit()
        user_answer = ''.join(request.form.getlist('vc'))
        exercise = db.session.query(exercise_type_20).order_by(exercise_type_20.exercise_id.desc()).all()[1]
        right_answer = exercise.right_answer
        answer_writer(current_user.get_id(), user_answer, type_no, exe_no, 0, right_answer)
        return render_template('vow_cons_exercise.html', letters=result[1], level=exercise.exercise_level,
                               section=exercise.exercise_type_section, user_answer=user_answer,
                               right_answer=right_answer)

    elif type_no in ['25']:
        que = tables[str(type_no)]
        result = picture_exercise(que, exe_no)
        user_answer = None
        form = BigForm()
        if form.validate_on_submit():
            user_answer = form.user_answer.data
            form.user_answer.data = ''
            answer_writer(current_user.get_id(), str(user_answer), type_no, exe_no, 0, str(None))
        return render_template('picture_exercise.html', form=form, exercise_id=exe_no, exercise_level=result[0],
                               section=result[1], task=result[2], picture=result[3], user_answer=user_answer,
                               next_exercise=result[4], this_exercise=result[5])


# Invalid URL
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404


# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=False)
