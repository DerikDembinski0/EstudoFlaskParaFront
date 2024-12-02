from flask import Blueprint, render_template, request
from database.models.cliente import Cliente



#Blue Print da Pagina dos Clientes
cliente_route = Blueprint('cliente', __name__)

#LISTAGEM
@cliente_route.route('/') # Definindo rota Principal
def lista_clientes(): #Listar os clientes
    clientes = Cliente.select()
    return render_template('lista_clientes.html', clientes=clientes)


                       
#INSERIR CLIENTE 
@cliente_route.route('/', methods=['POST']) 
def inserir_cliente(): #Inserir os dados do cliente

    data = request.json
    
    novo_usuario = Cliente.create(
        nome = data['nome'],
        email = data['email'],
    )
    return render_template('item_cliente.html', cliente=novo_usuario)



#RENDERIZAR O FORM 
@cliente_route.route('/new') 
def form_cliente(): #Formulario para cadastrar  um cliente
    return render_template('form_cliente.html')



#OBTER OS DADOS DE UM CLIENTE
@cliente_route.route('/<int:cliente_id>') 
def detalhe_cliente(cliente_id): #Exibir detalhes do cliente

    cliente = Cliente.get_by_id(cliente_id)

    return render_template('detalhe_cliente.html', cliente= cliente)


#FORM PARA EDITAR CLIENTE
@cliente_route.route('/<int:cliente_id>/edit') 
def form_edit_cliente(cliente_id): #Form para editar um cliente
    cliente = Cliente.get_by_id(cliente_id)
    return render_template('form_cliente.html', cliente=cliente)


#ATUALIZAR DADOS CLIENTE
@cliente_route.route('/<int:cliente_id>/update', methods=['PUT']) 
def update_cliente(cliente_id): #Atualizar info do cliente

    # Obter Dados Do Form De Edicao
    data = request.json

    cliente_editado = cliente = Cliente.get_by_id(cliente_id)
    cliente_editado.nome = data['nome']
    cliente_editado.email = data['email']
    cliente_editado.save()

    return render_template('item_cliente.html', cliente=cliente_editado)
    



#DELETAR CLIENTE
@cliente_route.route('/<int:cliente_id>/delete', methods=['DELETE']) 
def delete_cliente(cliente_id): #Deletar cliente

    cliente = Cliente.get_by_id(cliente_id)
    cliente.delete_instance()
    return {'deleted': 'ok'}











