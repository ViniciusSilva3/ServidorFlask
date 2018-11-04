from flask import Flask, send_file, request, flash, redirect
from flask import render_template
from forms import cleanerForm
from controller import Controller

control = Controller()
app = Flask(__name__)
app.config.from_object('config') #seta as configuracoes
@app.route("/")
def init():
    return redirect('/home')

#Route que cuida do cleaner:
@app.route("/home/cleaner", methods=['GET', 'POST'])
def index():
    form = cleanerForm()
    if request.method == 'POST':
        control.listaCleaner = request.form.getlist('nome1') # passa para o objeto a lista
    control.geraJsonCleaner()
    #return send_file('exemplo1.py', attachment_filename='novo.py'), render_template('return.html')
    #return render_template('return.html') # por enquanto nao foi adicionado outro retorno de arquivo
    return render_template('exem.html', form=form)

#Route apenas de exemplo por enquanto
@app.route("/retornos")
def retorno():
    flash('Arquivo Baixado com Sucesso')
    return render_template('return.html')

#Route da Home, é de onde serão selecionados os metodos de preprocessamento
@app.route("/home")
def home():
    return render_template('home.html')


@app.route("/home/envio")
def envio():
    if control.cleanerAtivo == 0: 
        control.geraDefault()
    #devem ser feitas as verificacoes para os outros

    return render_template("envio.html")

#falta o route 'download'

if __name__ == "__main__":
    app.run()


