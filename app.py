from flask import Flask, render_template, request, redirect, url_for , session

app = Flask(__name__)

app.secret_key = 'chave_secreta123'

usuarios = {}

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/cadastro')
def cadastro():
    return render_template('cadastro.html')


@app.route('/registrar', methods=['POST'])
def registrar():
    nome = request.form.get('nome')
    login = request.form.get('login')
    senha = request.form.get('senha')

    usuarios[login] = {
        'nome': nome,
        'senha': senha
    }

    return redirect(url_for('home'))


@app.route('/login', methods=['POST'])
def login():
    login = request.form.get('login')
    senha = request.form.get('senha')

    if login in usuarios and usuarios[login]['senha'] == senha:

        session['usuario'] = usuarios[login]['nome']

        return redirect(url_for('inicial'))
    
    return "Login inválido"


@app.route('/inicial')
def inicial():

    if 'usuario' not in session:
        return redirect(url_for('home'))

    return render_template('inicial.html', nome=session['usuario'])



if __name__ == '__main__':
    app.run(debug=True)
