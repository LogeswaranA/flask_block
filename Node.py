from TransactionPool import TransactionPool
from Wallet import Wallet
from Blockchain import Blockchain
from SocketCommunication import SocketCommunication
from NodeAPI import NodeAPI
from utils.BlockchainUtils import BlockchainUtils

class Node():
    def __init__(self,ip,port):
        self.p2p = None
        self.ip = ip
        self.port = port
        self.transactionPool = TransactionPool()
        self.wallet = Wallet()
        self.blockchain = Blockchain()

    def startP2P(self):
        self.p2p = SocketCommunication(self.ip,self.port)
        self.p2p.startSocketCommunication()

    def startAPI(self):
        self.api = NodeAPI()
        self.api.injectNode(self)
        self.api.start()

    def handleTransaction(self,transaction):
        data = transaction.payload()
        signature = transaction.signature
        signersPublicKey = transaction.sender
        signatureValid = Wallet.signatureValid(data,signature,signersPublicKey)
        txnExists = self.transactionPool.isTransactionExists(transaction)
        if not txnExists and signatureValid:
            self.transactionPool.addTransaction(transaction)
