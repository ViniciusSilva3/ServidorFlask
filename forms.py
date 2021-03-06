from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
class cleanerForm(FlaskForm):
    entrada1 = BooleanField("entrada1")
    entrada2 = BooleanField("entrada2")
    entrada3 = BooleanField("entrada3")

class SoftwareForm(FlaskForm):
	stopWord = BooleanField('Marcar esta opção no caso de inserir lista de stop-words')
	lang = StringField('Lingua escolhida: entre \'english\' e \'portuguese\'')
	max_word = StringField('Insira numero maximo de tamanho de uma stop-word')	# pesquisar numberField
	rem_ac = BooleanField('remover acentos')
	rem_alp = BooleanField('remover carateres alpha-numericos')
	tokenizer = BooleanField('tokenizer')
	stemizer = BooleanField('stemizer')
	submit = SubmitField('Obter json de parâmetros')
