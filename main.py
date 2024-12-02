from flask import Flask
from configuration import configure_all





#Inicializando o flask
app = Flask(__name__)



configure_all(app)




#Funcao Responsavel por executar o servidor web
app.run(debug=True)



