from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField,EmailField
from wtforms.validators import DataRequired, URL
from flask_ckeditor import CKEditorField

##WTForm
class CreatePostForm(FlaskForm):
    title = StringField("Blog Post Title", validators=[DataRequired()])
    subtitle = StringField("Subtitle", validators=[DataRequired()])
    img_url = StringField("Blog Image URL", validators=[DataRequired(), URL()])
    body = CKEditorField("Blog Content", validators=[DataRequired()])
    submit = SubmitField("Submit Post")

class RegisterForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    email = EmailField(label= 'email')
    password = PasswordField(label = 'password',validators=[DataRequired()])
    submit = SubmitField(label = 'Register')

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[DataRequired()])
    password = PasswordField(label = 'password',validators=[DataRequired()])
    submit = SubmitField(label = 'login')


class CommentForm(FlaskForm):
    commentstr = CKEditorField('Comment',validators=[DataRequired()])
    submit = SubmitField(label = 'Post Comment')