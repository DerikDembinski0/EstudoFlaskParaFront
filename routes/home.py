from flask import Blueprint, render_template

#BLUE PRINTS
#Agrupa rotas dentro de um agrupador
#Cria um grupo de rotas. Dentro desse grupo tem varias rotas referente ao agrupador



#Blue Print da Pagina da Home
home_route = Blueprint('home', __name__)

@home_route.route('/') # Definindo rota
def home():
    return render_template('index.html')


