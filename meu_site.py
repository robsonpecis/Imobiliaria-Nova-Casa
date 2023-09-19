from flask import Flask, render_template, request, redirect, url_for
from db import Clientes

app = Flask(__name__)

# Rota para homepage e redirecionamento dos botões
@app.route("/", methods=["POST", "GET"])
def button_imoveis_redirect():
    if request.method == "POST" and request.form == "imoveis":
        return redirect(url_for("imoveis"))
    elif request.method == 'POST' and request.form == 'login':
        return redirect(url_for(f"login"))
    elif request.method == "GET":
        return render_template("homepage.html")

#rota para a pagina de imoveis/clientes e a tabela do banco de dados
@app.route("/imoveis")
def imoveis():
    headings = ("Id", "Nome", "Imovel", "Valor")
    data = []
    for indice, cliente in enumerate(Clientes):
        conjunto = []
        for indice in headings:
            conjunto.append(cliente[indice])
        conjunto_tuple = tuple(conjunto)
        data.append(conjunto_tuple)
    data_tuple = tuple(data)
    return render_template("imoveis.html", headings=headings, data_tuple=data_tuple)

#Rota pagina de login do adm
@app.route("/login", methods=["POST", "GET"])
def login():
    error = None
    if request.method == "POST":
        if request.form['username'] != 'admin' or request.form['password'] != 'admin':
            error = 'Credenciais invalidas. Tente novamente'
        else:
            return redirect(url_for("perfil_adm"))
    return render_template("login.html", error=error)

#Rota para o perfil do admin
@app.route("/perfil_adm", methods=["POST", "GET"])
def perfil_adm():
    error = None
    sucesso = None
    # validation_form = request.form.get()
    if request.method == "POST":
        # if validation_form == 'submit_client':
                if len(request.form['client_name']) <= 0 or request.form['combobox']  == 'default' or len(request.form['price']) < 1 or int(float(request.form['price'])) < 1:
                    error = 'Dados invalidos. Verifique as informações inseridas'
                else:
                        number = 0
                        while number < len(Clientes):
                            if (number  + 1) < Clientes[number]["Id"]:
                                Clientes.insert(number, new_submit(number + 1, request.form['client_name'], request.form['combobox'], request.form['price']))
                                sucesso = 'Adicionado com sucesso'
                                break
                            elif (number + 1) == len(Clientes):
                                Clientes.append(new_submit(number + 2, request.form['client_name'], request.form['combobox'], request.form['price']))
                                sucesso = 'Adicionado com  sucesso'
                                break
                            number += 1
        # else:
        #         print('detectou o metodo')
        #         for indice, cliente in enumerate(Clientes):
        #             if cliente["Id"] == request.form['client_id']:
        #                 del Clientes[indice]
        #                 print('funcionou')
    return render_template("perfil_adm.html", error=error, sucesso=sucesso)

new_client = {}
def new_submit(number, name, type, price):
    new_client = {
   "Id" : number,
   "Nome" : name,
   "Imovel" : type,
   "Valor" : price
   }
    return new_client

if __name__ == "__main__":
    app.run(debug=True)