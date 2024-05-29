import uuid
import time
import copy

class Transaction():
    def __init__(self,sender,receiver,amount,txnType):
        self.sender = sender
        self.receiver = receiver
        self.amount = amount
        self.txnType = txnType
        self.id = uuid.uuid1().hex
        self.timestamp = time.time()
        self.signature = ''

    def toJson(self):
        return self.__dict__
        
    def sign(self,signature):
        self.signature = signature

    def payload(self):
        jsonrepresentation = copy.deepcopy(self.toJson())
        jsonrepresentation['signature'] = ''
        return jsonrepresentation
    
    def equals(self,transaction):
        if self.id == transaction.id:
            return True
        else:
            return False
