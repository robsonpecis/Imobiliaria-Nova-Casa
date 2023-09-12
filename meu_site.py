from flask import Flask, render_template, request, redirect, url_for, jsonify, render_template_string
import os
from db import Clientes

app = Flask(__name__)

# Rota para homepage e redirecionamento dos botões
@app.route("/", methods=["POST", "GET"])
def button_imoveis_redirect():
    if request.method == "POST" and request.form == "imoveis":
        return redirect(url_for("imoveis"))
    elif request.method == 'POST' and request.form == 'perfil_usuario':
        return redirect(url_for(f"perfil_usuario"))
    elif request.method == "GET":
        return render_template("homepage.html")

#rota para a pagina de imoveis/clientes e a tabela do banco de dados
headings = ("Id", "Nome", "Imovel", "Valor")
data = []
for indice, cliente in enumerate(Clientes):
        conjunto = []
        for indice in headings:
            conjunto.append(cliente[indice])
        conjunto_tuple = tuple(conjunto)
        data.append(conjunto_tuple)
print(data)
data_tuple = tuple(data)
print(headings)
print(data_tuple)

@app.route("/imoveis")
def imoveis():
    return render_template("imoveis.html", headings=headings, data_tuple=data_tuple)


#Rota para o cadastro de novos clientes no banco de dados
@app.route("/perfil_usuario")
def perfil_usuario():
    return render_template("perfil_usuario.html")

if __name__ == "__main__":
    app.run(debug=True)