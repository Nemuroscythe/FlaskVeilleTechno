from flask import (
    Blueprint, jsonify, request, current_app as app
)

from main.hello.service import helloService

# Ce fichier contient tous nos points d'entrées (endpoints) pour la partie "hello"

# Créer un blueprint qu'on doit lier à notre app instance dans __init__
bp = Blueprint('hello', __name__, url_prefix='/')


# Une simple page sur /hello HTTP method par défaut : GET
@bp.route('/hello')
def get_hello_messages():
    hello_messages = helloService.getHelloMessages()
    app.logger.info(hello_messages)
    hello_messages_dict = map(lambda hello_message: hello_message.__dict__, hello_messages)
    return jsonify(list(hello_messages_dict))


@bp.route('/hello/<id>')
def get_hello_message(id):
    message = helloService.getHelloMessage(id)
    return jsonify(message.__dict__)


@bp.route('/hello', methods=["POST"])
def create_hello_message():
    body = request.json  # request permet de récupérer des informations, ici le body s'il est en json
    message = helloService.createHelloMessage(body)
    return jsonify(message.__dict__), 201  # 201 --> HTTP code/status pour "created"


@bp.route('/hello/<id>', methods=["PUT"])
def update_hello_message(id):  # Notez comment je passe et récupère une variable dans l'URL
    body = request.json
    helloService.updateHelloMessage(id, body)
    return "", 204  # 204 --> HTTP code/status pour "no content" qui signifie que l'appel est réussi, mais ne renvoie rien


@bp.route('/hello/<id>', methods=["DELETE"])
def delete_hello_message(id):
    helloService.deleteHelloMessage(id)
    return "", 204  # 204 --> HTTP code/status pour "no content" qui signifie que l'appel est réussi, mais ne renvoie rien
