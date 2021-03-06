from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, PasswordField
from wtforms.fields import DateField, EmailField, TelField
from wtforms.validators import DataRequired, Length, EqualTo, Email

class UserCreateForm(FlaskForm):
    username = StringField('사용자이름', validators=[
        DataRequired(), Length(min=3, max=25)
    ])
    password1 = PasswordField('비밀번호', validators=[
        DataRequired(), EqualTo('Password2', '비밀번호가 일치하지 않습니다.')
    ])
    password2 = PasswordField('비밀번호확인', validators=[DataRequired()])
    email = EmailField('이메일', [DataRequired(), Email()])