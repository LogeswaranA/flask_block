import time
import copy

class Block():
    def __init__(self,transactions,lasthash,forger,blockCount):
        self.transactions = transactions
        self.lasthash = lasthash
        self.forger = forger
        self.blockCount = blockCount
        self.timestamp = time.time()
        self.signature = ''

    @staticmethod
    def genesis():
        genesisblock = Block([],"genesishash","genesis",0)
        genesisblock.timestamp =0
        return genesisblock

    def toJson(self):
        data = {}
        data['lasthash'] = self.lasthash
        data['forger'] = self.forger
        data['blockCount'] = self.blockCount
        data['timestamp'] = self.timestamp
        data['signature'] = self.signature

        jsontransaction =[]
        for txn in self.transactions:
            jsontransaction.append(txn.toJson())
        
        data['transactions'] = jsontransaction

        return data
    
    def payload(self):
        jsonrepresentation = copy.deepcopy(self.toJson())
        jsonrepresentation['signature'] = ''
        return jsonrepresentation
    
    def sign(self,signature):
        self.signature = signature