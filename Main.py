from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import Blockchain
from utils.BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel

if __name__ == "__main__":
   
   blockchain = Blockchain()
   pool = TransactionPool()

   alice = Wallet()
   bob = Wallet()

   txn = alice.createTransaction(bob.publicKeyString(),5,"TRANSFER")

   if not pool.isTransactionExists(txn):
      pool.addTransaction(txn)
    
   coveredtxn = blockchain.getCoveredTransactionSet(pool.transactions)

   print(coveredtxn)