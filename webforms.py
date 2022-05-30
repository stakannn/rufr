from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, SelectField, PasswordField, TextAreaField
from wtforms.validators import DataRequired, Email, EqualTo


class BigForm(FlaskForm):
    user_answer = TextAreaField('')
    submit = SubmitField('Отправить')


class OptionsForm(FlaskForm):
    user_answer = SelectField('Варианты ответа')
    submit = SubmitField('Проверить')


class TeacherForm(FlaskForm):
    name = StringField('Фамилия и имя', validators=[
        DataRequired(message='Это поле надо обязательно заполнить')])

    login = StringField('Логин', validators=[
        DataRequired(message='Это поле надо обязательно заполнить')])

    password_hash = PasswordField('Пароль', validators=[
        DataRequired(message='Это поле надо обязательно заполнить'),
        EqualTo('password_hash2', message='Пароли должны совпадать')])

    password_hash2 = PasswordField('Повторите пароль', validators=[
        DataRequired(message='Это поле надо обязательно заполнить')])

    mail = StringField('Почта', validators=[
        DataRequired(message='Это поле надо обязательно заполнить'),
        Email(message='Это не похоже на адрес электронной почты')])
    submit = SubmitField('Готово')


class UserForm(FlaskForm):
    name = StringField('Фамилия и имя', validators=[
        DataRequired(message='Это поле надо обязательно заполнить')])

    login = StringField('Логин', validators=[
        DataRequired(message='Это поле надо обязательно заполнить')])

    password_hash = PasswordField('Пароль', validators=[
        DataRequired(message='Это поле надо обязательно заполнить'),
        EqualTo('password_hash2', message='Пароли должны совпадать')])

    password_hash2 = PasswordField('Повторите пароль', validators=[
        DataRequired(message='Это поле надо обязательно заполнить')])

    mail = StringField('Почта', validators=[
        DataRequired(message='Это поле надо обязательно заполнить'),
        Email(message='Это не похоже на адрес электронной почты')])

    level = SelectField('Уровень', choices=[('', 'Уровень владения русским языком'), ('A1', 'A1'), ('A2', 'A2'),
                                            ('B1', 'B1'), ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')])

    gender = SelectField('Пол', choices=[('', 'Пол'), ('male', 'Мужской'), ('female', 'Женский')])
    age = StringField('Возраст')
    native_langs = StringField('Родной язык')
    country = StringField('Страна')
    city = StringField('Город')
    lang1 = StringField('Язык')
    level1 = SelectField('Уровень', choices=[(None, 'Уровень владения'), ('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'),
                                             ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')])
    lang2 = StringField('Язык')
    level2 = SelectField('Уровень', choices=[(None, 'Уровень владения'), ('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'),
                                             ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')])
    lang3 = StringField('Язык')
    level3 = SelectField('Уровень', choices=[(None, 'Уровень владения'), ('A1', 'A1'), ('A2', 'A2'), ('B1', 'B1'),
                                             ('B2', 'B2'), ('C1', 'C1'), ('C2', 'C2')])
    submit = SubmitField('Готово')


class LogInForm(FlaskForm):
    login = StringField('Логин', validators=[DataRequired()])
    password = PasswordField('Пароль', validators=[DataRequired()])
    submit = SubmitField('Войти')


class TypeSelectForm(FlaskForm):
    sel = SelectField('Тип упражнения', choices=[(None, 'без фильтра'), (1, 1), (2, 2), (3, 3), (4, 4), (5, 5), (6, 6),
                                                 (7, 7), (8, 8), (9, 9), (10, 10), (11, 11), (12, 12), (13, 13),
                                                 (14, 14), (15, 15), (16, 16), (17, 17), (18, 18), (19, 19), (20, 20),
                                                 (21, 21), (22, 22), (23, 23), (24, 24), (25, 25), (26, 26), (27, 27)])
    submit = SubmitField('Отфильтровать')


# простая форма с 1 полем
class AnswerForm(FlaskForm):
    user_answer = StringField(validators=[DataRequired()])
    submit = SubmitField('Проверить')


# простая флома с 4 полями
class AnswerForm4(FlaskForm):
    user_answer1 = StringField(validators=[DataRequired()])
    user_answer2 = StringField(validators=[DataRequired()])
    user_answer3 = StringField(validators=[DataRequired()])
    user_answer4 = StringField(validators=[DataRequired()])
    submit = SubmitField("Проверить")


# простая форма с 5 полями
class AnswerForm5(FlaskForm):
    user_answer1 = StringField(validators=[DataRequired()])
    user_answer2 = StringField(validators=[DataRequired()])
    user_answer3 = StringField(validators=[DataRequired()])
    user_answer4 = StringField(validators=[DataRequired()])
    user_answer5 = StringField(validators=[DataRequired()])
    submit = SubmitField("Проверить")


# простая форма с 10 полями
class AnswerForm10(FlaskForm):
    user_answer1 = StringField(validators=[DataRequired()])
    user_answer2 = StringField(validators=[DataRequired()])
    user_answer3 = StringField(validators=[DataRequired()])
    user_answer4 = StringField(validators=[DataRequired()])
    user_answer5 = StringField(validators=[DataRequired()])
    user_answer6 = StringField(validators=[DataRequired()])
    user_answer7 = StringField(validators=[DataRequired()])
    user_answer8 = StringField(validators=[DataRequired()])
    user_answer9 = StringField(validators=[DataRequired()])
    user_answer10 = StringField(validators=[DataRequired()])
    submit = SubmitField("Проверить")
