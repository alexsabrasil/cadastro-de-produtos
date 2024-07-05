from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

# Lista de produtos para simular um banco de dados
produtos = []

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/list')
def list():
    # Ordenar produtos pelo valor
    sorted_produtos = sorted(produtos, key=lambda x: x['valor'])
    return render_template('list.html', produtos=sorted_produtos)

@app.route('/add', methods=['POST'])
def add():
    nome = request.form['nome']
    descricao = request.form['descricao']
    valor_str = request.form['valor']
    disponivel = request.form['disponivel'] == 'sim'
    
    # Converter o valor de string para float
    valor_str = valor_str.replace('.', '').replace(',', '.')
    valor = float(valor_str)
    
    produto = {
        'nome': nome,
        'descricao': descricao,
        'valor': valor,
        'disponivel': disponivel
    }
    
    produtos.append(produto)
    
    return redirect(url_for('list'))

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)
