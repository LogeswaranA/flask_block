from Crypto.Hash import SHA256
import json

class BlockchainUtils:

    @staticmethod
    def hash(data):
        datastring = json.dumps(data).encode('utf-8')
        datahash = SHA256.new(datastring)
        return datahash