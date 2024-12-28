from controllers.imagenController import BlueprintImagen
from controllers.usuarioController import BlueprintUsuario
from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app)

app.register_blueprint(BlueprintUsuario)
app.register_blueprint(BlueprintImagen)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4000, debug=True)