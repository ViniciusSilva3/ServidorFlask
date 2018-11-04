from flask import Flask, send_file, request, flash, redirect
from flask import render_template
from forms import cleanerForm
from controller import Controller

control = Controller()
app = Flask(__name__)
app.config.from_object('config') #seta as configuracoes
@app.route("/")
def init():
    return redirect('/index')


@app.route("/index", methods=['GET', 'POST'])
def index():
    form = cleanerForm()
    if request.method == 'POST':
        control.getOpcoesCleaner(request.form.getlist('nome1'))
    control.geraJsonCleaner()
    #return send_file('exemplo1.py', attachment_filename='novo.py'), render_template('return.html')
    #return render_template('return.html') # por enquanto nao foi adicionado outro retorno de arquivo
    return render_template('exem.html', form=form)

@app.route("/retornos")
def retorno():
    flash('Arquivo Baixado com Sucesso')
    return render_template('return.html')

@app.route("/test", defaults={'name': None}, methods=['GET'])
@app.route("/test/<name>")
def test(name):
    return "Ola, %s" %name

if __name__ == "__main__":
    app.run()


