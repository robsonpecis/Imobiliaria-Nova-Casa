# @app.route("/imoveis")
# def imoveis():
#     labels = os.popen('python3 db.py').read()
#     return render_template_string('''


#     <table>
#             <tr>
#                 <td>Id</td>
#                 <td>Nome</td>
#                 <td>Imovel</td>
#                 <td>Valor</td>
#             </tr>


#     {% for id, nome, imovel, valor in labels.items() %}

#             <tr>
#                 <td>{{ id }}</td>
#                 <td>{{ nome }}</td>
#                 <td>{{ imovel }}</td>
#                 <td>{{ valor }}</td>
#             </tr>

#     {% endfor %}


#     </table>
# ''', labels=labels)

'''@app.route("/perfil_usuario/<nome_cliente>")
def perfil_usuario(nome_cliente):
    return render_template("perfil_usuario.html", nome_cliente=nome_cliente)'''

# number = 0
#             while number <= len(Clientes):
#                 if (number  + 1) < Clientes[number]["Id"]:
#                     Clientes.insert(number, new_submit(number + 1, request.form['client_name'], request.form['combobox'], request.form['price']))
#                     sucesso = 'Adicionado com sucesso 1'
#                     break
#                 elif (number + 1) > Clientes[number]["Id"] and (number + 1) < Clientes[number + 1]["Id"]:
#                     Clientes.insert(number, new_submit(number + 1, request.form['client_name'], request.form['combobox'], request.form['price']))
#                     sucesso = 'Adicionado com  sucesso 2'
#                     break
#                 number += 1