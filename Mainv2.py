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
   exchange = Wallet()
   forger = Wallet()

   txn = exchange.createTransaction(alice.publicKeyString(),10,"EXCHANGE")

   if not pool.isTransactionExists(txn):
      pool.addTransaction(txn)

   coveredtxn = blockchain.getCoveredTransactionSet(pool.transactions)
   lasthash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
   blockCount = blockchain.blocks[-1].blockCount + 1
#    blockOne = Block(coveredtxn,lasthash,forger.publicKeyString(),blockCount)
   blockOne = forger.createBlock(coveredtxn,lasthash,blockCount)
   blockchain.addBlock(blockOne)
   pool.removeFromPool(blockOne.transactions)

   txn = alice.createTransaction(bob.publicKeyString(),5,"TRANSFER")

   if not pool.isTransactionExists(txn):
      pool.addTransaction(txn)
   
   coveredtxn = blockchain.getCoveredTransactionSet(pool.transactions)
   lasthash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()
   blockCount = blockchain.blocks[-1].blockCount + 1
#    blockTwo = Block(coveredtxn,lasthash,forger.publicKeyString(),blockCount)
   blockTwo = forger.createBlock(coveredtxn,lasthash,blockCount)
   blockchain.addBlock(blockTwo)
   pool.removeFromPool(blockTwo.transactions)

   pprint.pprint(blockchain.toJson())