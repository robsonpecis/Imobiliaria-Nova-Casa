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
        if request.form['username'] != 'admin' or request.form['password'] != 'admin': # Verifica se o usuario e senha estão corretos 
            error = 'Credenciais invalidas. Tente novamente'
        else:
            return redirect(url_for("perfil_adm"))
    return render_template("login.html", error=error)

#Rota para o perfil do admin
@app.route("/perfil_adm", methods=["POST", "GET"])
def perfil_adm():
    error_submit = None
    error_delete = None
    error_client_not_found = None
    error_client_id = None
    sucesso = None
    sucesso_delete = None
    sucesso_update = None

    if request.method == "POST":
        if 'submit_client' in request.form: # Verifica se é o formulario de submit/cadastro
                if len(request.form['client_name']) <= 0 or request.form['combobox']  == 'default' or len(request.form['price']) < 1 or int(float(request.form['price'])) < 1:
                    error_submit = 'Dados invalidos. Verifique as informações inseridas'
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
        elif 'delete_client' in request.form: # Verifica se é o formulario de delete
                if len(request.form['delete_client_id']) < 1 or int(request.form['delete_client_id']) < 1:
                        error_delete = "Insira um valor valido"
                else:
                    for indice, cliente in enumerate(Clientes):
                            if cliente["Id"] == int(request.form['delete_client_id']):
                                del Clientes[indice]
                                sucesso_delete = 'Usuario deletado com sucesso'
                                break
                            elif int(cliente["Id"]) < int(request.form['delete_client_id']):
                                None
                            elif int(cliente["Id"]) > int(request.form['delete_client_id']):
                                error_client_not_found = "Usuario não encontrado"
        elif 'update_client' in request.form: #Verifica se é o formulario de update
            if  len(request.form['update_client_id']) < 1:
                 error_client_id = "Insira uma Id válida"
            else:
                if len(request.form['update_client_name']) <= 0 or request.form['combobox']  == 'default' or len(request.form['update_price']) < 1 or int(float(request.form['update_price'])) < 1:
                    error_client_id = 'Insira dados validos.'
                else:
                    for indice, cliente in  enumerate(Clientes):
                            if cliente["Id"] == int(request.form['update_client_id']):
                                Clientes[indice].update(new_submit(request.form['update_client_id'], request.form['update_client_name'], request.form['combobox'], request.form['update_price']))
                                sucesso_update = 'Cliente atualizado com sucesso.'
                                break
                            elif int(cliente["Id"]) < int(request.form['update_client_id']):
                                None
                            elif int(cliente["Id"]) > int(request.form['update_client_id']):
                                error_client_id = 'Usuario não encontrado. Insira uma Id valida.'
                    
    return render_template("perfil_adm.html", error_submit=error_submit, sucesso=sucesso, error_delete=error_delete, 
                           error_client_not_found=error_client_not_found, sucesso_delete=sucesso_delete, error_client_id=error_client_id, sucesso_update=sucesso_update)

# Função usada pela rota de cadastro para adicionar no banco de dados
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