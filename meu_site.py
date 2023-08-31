from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def homepage():
    return render_template("homepage.html")

@app.route("/imoveis")
def imoveis():
    return render_template("imoveis.html")

@app.route("/perfil_usuario/<nome_cliente>")
def perfil_usuario(nome_cliente):
    return render_template("perfil_usuario.html", nome_cliente=nome_cliente)

if __name__ == "__main__":
    app.run(debug=True)