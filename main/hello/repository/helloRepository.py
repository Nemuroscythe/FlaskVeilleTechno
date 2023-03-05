from flask import current_app as app

from main.hello.models.HelloMessage import HelloMessage
from main.model import db


# Ce fichier sert à la communication avec la base de données
def get_hello_messages():
    db_response = db.session.execute(db.select(HelloMessage)).all()
    app.logger.info(type(db_response))
    return db_response


def get_hello_message(id):
    db_response = db.get_or_404(HelloMessage, id)
    return db_response


def create_hello_message(hello_message):
    db.session.add(hello_message)
    db.session.commit()
    return None


def update_hello_message(hello_message):
    app.logger.debug(hello_message)
    hello_message_db = db.get_or_404(HelloMessage,
                                     hello_message.id)  # Je récupère la donnée liée à l'id, nécessaire pour l'ORM
    hello_message_db.content = hello_message.content  # J'effectue une mise à jour de la donnée, ce qui est repéré par l'ORM
    db.session.commit()  # Sauvegarde ce changement dans la bdd
    return None


def delete_hello_message(id):
    hello_message_db = db.get_or_404(HelloMessage, id)  # Je récupère la donnée liée à l'id, nécessaire pour l'ORM
    db.session.delete(hello_message_db)
    db.session.commit()  # Sauvegarde ce changement dans la bdd
    return None
