from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def pagina_inicial():
    resultado = False

    if request.method == 'POST':
        
        nome = request.form['nome']
        altura = request.form['altura']
        peso = request.form['peso']

        altura = float(altura)
        peso = float(peso)

        imc = peso / (altura * altura)

        if imc < 18.5:
            mensagem = '🔵 Abaixo do peso'
            cor='alert-info'
        elif imc >= 18.5 and imc < 25:
            mensagem = '🟢 Peso normal'
            cor='alert-success'
        elif imc < 30:
            mensagem = '🟡 Sobrepeso'
            cor = 'alert-warning'
        else:
            mensagem = '🔴 Obesidade'
            cor = 'alert-danger'

        resultado = True

        return render_template('index.html', 
                               nome=nome, 
                               altura=altura, 
                               peso=peso,
                               imc=imc,
                               mensagem=mensagem,
                               cor=cor,
                               resultado=resultado)

    return render_template('index.html', resultado=resultado)

@app.route('/equipe')
def equipe():
    return render_template('equipe.html')

if __name__ == '__main__':
    app.run(debug=True) 