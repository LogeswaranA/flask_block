from Block import Block
from utils.BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

class Blockchain():
    def __init__(self):
        self.blocks = [Block.genesis()]
        self.accountModel = AccountModel()

    def addBlock(self,block):
        self.executeTransactions(block.transactions)
        self.blocks.append(block)

    def toJson(self):
        data = {}
        jsonblocks =[]
        for block in self.blocks:
            jsonblocks.append(block.toJson())
        data['blocks']=jsonblocks
        return data
    
    def blockCountValid(self,block):
        if self.blocks[-1].blockCount == block.blockCount - 1:
            return True
        else:
            return False
        
    def lastBlockHashValid(self,block):
        latestblocklasthash = BlockchainUtils.hash(self.blocks[-1].payload()).hexdigest()
        if latestblocklasthash == block.lasthash:
            return True
        else:
            return False
        
    def getCoveredTransactionSet(self,transactions):
        coveredTransactions=[]
        for txn in transactions:
            if self.transactionCovered(txn):
                coveredTransactions.append(txn)
            else:
                print("Transaction is not covered by sender")
        return coveredTransactions
        
    def transactionCovered(self,transaction):
        if transaction.txnType=="EXCHANGE":
            return True
        senderbalance = self.accountModel.getBalance(transaction.sender)
        if senderbalance >= transaction.amount:
            return True
        else:
            return False
        
    def executeTransactions(self,transactions):
        for txn in transactions:
            self.executeTransaction(txn)


    def executeTransaction(self,transaction):
        sender = transaction.sender
        receiver = transaction.receiver
        amount = transaction.amount
        self.accountModel.updateBalance(sender,-amount)
        self.accountModel.updateBalance(receiver,amount)


