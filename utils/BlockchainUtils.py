from Crypto.Hash import SHA256
import json
import jsonpickle

class BlockchainUtils:

    @staticmethod
    def hash(data):
        datastring = json.dumps(data).encode('utf-8')
        datahash = SHA256.new(datastring)
        return datahash
    
    @staticmethod
    def encode(objetToEncode):
        return jsonpickle.encode(objetToEncode,unpicklable=True)
    
    @staticmethod
    def decode(objectToDecode):
        return jsonpickle.decode(objectToDecode)