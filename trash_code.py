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