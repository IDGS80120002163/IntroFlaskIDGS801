from wtforms import Form, StringField, TelField, EmailField, IntegerField
# Aquí de los validadores importamos el dato obligatorio y el email
from wtforms.validators import DataRequired, Email

class UserForm(Form):
    nombre = StringField('nombre')
    email = EmailField('email')
    aPaterno = StringField('aPaterno')
    aMaterno = StringField('aMaterno')
    edad = IntegerField('edad')
