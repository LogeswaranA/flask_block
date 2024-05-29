from Crypto.PublicKey import RSA
from Crypto.Signature import PKCS1_v1_5
from utils.BlockchainUtils import BlockchainUtils
from Transaction import Transaction
from Block import Block

class Wallet():
    def __init__(self):
        self.keypair = RSA.generate(2048)

    def sign(self,data):
        datahash = BlockchainUtils.hash(data)
        print("datahash",datahash)
        signatureSchemaObject = PKCS1_v1_5.new(self.keypair)
        signature = signatureSchemaObject.sign(datahash).hex()
        return signature
    
    @staticmethod
    def signatureValid(data,signature,publicKeyString):
        signature = bytes.fromhex(signature)
        datahash = BlockchainUtils.hash(data)
        publicKey = RSA.importKey(publicKeyString)
        signatureSchemaObject = PKCS1_v1_5.new(publicKey)
        isValidSignature = signatureSchemaObject.verify(datahash,signature)
        return isValidSignature
    
    #this method will derive the PEM file of publickey from given keypair of a wallet
    def publicKeyString(self):
        publicKeyString = self.keypair.publickey().exportKey("PEM").decode('utf-8')
        return publicKeyString
    
    def createTransaction(self,receiver,amount,txnType):
        transaction = Transaction(self.publicKeyString(),receiver,amount,txnType)
        signature = self.sign(transaction.payload())
        transaction.sign(signature)
        return transaction

    def createBlock(self,transactions,lasthash,blockCount):
        block = Block(transactions,lasthash,self.publicKeyString(),blockCount)
        signature = self.sign(block.payload())
        block.sign(signature)
        return block
