from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import Blockchain
from utils.BlockchainUtils import BlockchainUtils

if __name__ == "__main__":
    receiver = "receiver"
    amount = 100
    txnType = "TRANSFER"
    
    wallet = Wallet()
    pool = TransactionPool()
    transaction = wallet.createTransaction(receiver,amount,txnType)

    if pool.isTransactionExists(transaction) == False:
        pool.addTransaction(transaction)

    # #let's try one more time to see if the txn is getting added,, expected result it should not add
    # if pool.isTransactionExists(transaction) == False:
    #     pool.addTransaction(transaction)

    blockchain = Blockchain()
    lastblockhash = BlockchainUtils.hash(blockchain.blocks[-1].payload()).hexdigest()

    blockCount = blockchain.blocks[-1].blockCount + 1
    block = wallet.createBlock(pool.transactions,lastblockhash,blockCount)

    if not blockchain.lastBlockHashValid(block):
        print("not a valid blockhash")

    if not blockchain.blockCountValid(block):
        print("not a valid blockcount")

    if blockchain.blockCountValid(block) & blockchain.lastBlockHashValid(block):
        blockchain.addBlock(block)
        
    pprint.pprint(blockchain.toJson())

    # pprint.pprint(block.toJson())
    # #to verify the signatureValid is working fine, passing original public key with original transaction, and it should return true
    # isSignaturevalid = Wallet.signatureValid(block.payload(),block.signature,wallet.publicKeyString())
    # print(isSignaturevalid)
    # print(transaction.toJson())

    # #to verify the signatureValid is working fine, passing original public key with original transaction, and it should return true
    # isSignaturevalid = Wallet.signatureValid(transaction.payload(),transaction.signature,wallet.publicKeyString())
    # print(isSignaturevalid)

    # #to verify the signatureValid is working fine, passing new public key with original transaction, and it should return false
    # fraudWallet = Wallet()
    # isSignaturevalid = Wallet.signatureValid(transaction.payload(),transaction.signature,fraudWallet.publicKeyString())
    # print(isSignaturevalid)