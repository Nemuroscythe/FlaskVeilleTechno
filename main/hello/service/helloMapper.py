from flask import current_app as app

from main.hello.models.HelloMessage import HelloMessage
from main.hello.service.dto.HelloMessageDTO import HelloMessageDTO
from main.hello.service.dto.HelloMessagesDTO import HelloMessagesDTO


# Ce fichier nous permet de convertir un objet de type entité (lié à une table)
# en objet visible par l'utilisateur sous le pattern DTO (Data Transfer Object)
# L'idée de ce pattern est de filtrer les données que l'on veut pouvoir montrer à l'utilisateur

def convert_hello_message_to_dto(hello_message):
    return HelloMessageDTO(hello_message.content)


def convert_json_to_hello_message(hello_message_json, id=None):
    app.logger.debug(hello_message_json)
    content = hello_message_json["content"]
    hello_message = HelloMessage(content, id)
    return hello_message


def convert_hello_message_row_to_dto(hello_message):
    hello_message = hello_message[0]  # Row est une classe de SQLAlchemy qui fonctionne comme un tuple
    return HelloMessagesDTO(hello_message.id, hello_message.content)


def convertHelloMessageListToDTO(helloMessages):
    helloMessagesDTO = map(convert_hello_message_row_to_dto, helloMessages)  # appelle la fonction convertHelloMessageToDTO
    # pour chaque élément de la liste helloMessages
    return list(helloMessagesDTO)
