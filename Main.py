from Transaction import Transaction
from Wallet import Wallet
from TransactionPool import TransactionPool
from Block import Block
import pprint
from Blockchain import Blockchain
from utils.BlockchainUtils import BlockchainUtils
from AccountModel import AccountModel
from Node import Node
import sys

if __name__ == "__main__":
   ip = sys.argv[1]
   port = int(sys.argv[2])
   node = Node(ip,port)
   node.startP2P()
   node.startAPI()

#    if port == 10002:
#       node.p2p.connect_with_node('localhost',10001)
