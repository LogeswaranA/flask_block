import time
import threading
from Message import Message
from utils.BlockchainUtils import BlockchainUtils

class PeerDiscoveryHandler():
    def __init__(self,node):
        self.socketCommunication = node

    def start(self):
        statusThread = threading.Thread(target=self.status,args={})
        statusThread.start()
        discoveryThread = threading.Thread(target=self.discovery,args={})
        discoveryThread.start()

    def discovery(self):
        while True:
            handShakeMessage = self.handShakeMessage()
            self.socketCommunication.broadCast(handShakeMessage)
            time.sleep(10)

    def status(self):
        while True:
            print("Connected To:::")
            for peer in self.socketCommunication.peers:
                print(str(peer.ip) + ":" + str(peer.port))
            time.sleep(10)
    
    def handShake(self,connected_node):
        handShakeMessage = self.handShakeMessage()
        self.socketCommunication.send(connected_node,handShakeMessage)
                
    def handleMessage(self,message):
        peersSocketConnector = message.senderConnector
        peersPeerList = message.data
        newPeer = True
        for peer in self.socketCommunication.peers:
            if peer.equals(peersSocketConnector):
                newPeer = False
        if newPeer:
            self.socketCommunication.peers.append(peersSocketConnector)
        
        for peersPeer in peersPeerList:
            peerKnown = False
            for peer in self.socketCommunication.peers:
                if peer.equals(peersPeer):
                    peerKnown=True
            if not peerKnown and not peersPeer.equals(self.socketCommunication.socketConnector):
                self.socketCommunication.connect_with_node(peersPeer.ip,peersPeer.port)


    def handShakeMessage(self):
        ownConnector = self.socketCommunication.socketConnector
        ownPeers = self.socketCommunication.peers
        data = ownPeers
        messageType = "DISCOVERY"
        message = Message(ownConnector,messageType,data)
        encodedMessage = BlockchainUtils.encode(message)
        return encodedMessage