from Wallet import Wallet
from utils.BlockchainUtils import BlockchainUtils
import requests

if __name__ == "__main__":
    alice = Wallet()
    bob = Wallet()
    exchange = Wallet()

    transaction = exchange.createTransaction(alice.publicKeyString(),10,"EXCHANGE")

    url = "http://localhost:8001/transaction"
    payload = {"transaction":BlockchainUtils.encode(transaction)}
    response = requests.post(url,json=payload)
    print(response.text)

