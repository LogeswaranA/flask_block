

class TransactionPool():

    def __init__(self):
        self.transactions = []

    def addTransaction(self,transaction):
        self.transactions.append(transaction)

    def isTransactionExists(self,transaction):
        # Check if txn exists
        for pool in self.transactions:
            if pool.equals(transaction):
                return True
        return False




