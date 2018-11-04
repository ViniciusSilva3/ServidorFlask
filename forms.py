from flask_wtf import FlaskForm
from wtforms import BooleanField

class cleanerForm(FlaskForm):
    entrada1 = BooleanField("entrada1")
    entrada2 = BooleanField("entrada2")
    entrada3 = BooleanField("entrada3")
