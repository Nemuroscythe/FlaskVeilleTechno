from main.hello.repository import helloRepository
from main.hello.service import helloMapper


# Ce fichier contient notre logique et manipulations de données
def getHelloMessages():
    helloMessage = helloRepository.get_hello_messages()
    return helloMapper.convertHelloMessageListToDTO(helloMessage)


def getHelloMessage(id):
    helloMessage = helloRepository.get_hello_message(id)
    return helloMapper.convert_hello_message_to_dto(helloMessage)


def createHelloMessage(helloMessageJson):
    helloMessage = helloMapper.convert_json_to_hello_message(helloMessageJson)
    helloRepository.create_hello_message(helloMessage)
    return helloMapper.convert_hello_message_to_dto(helloMessage)


def updateHelloMessage(id, helloMessageJson):
    helloMessage = helloMapper.convert_json_to_hello_message(helloMessageJson, id)
    helloRepository.update_hello_message(helloMessage)
    return None


def deleteHelloMessage(id):
    helloRepository.delete_hello_message(id)
    return None
