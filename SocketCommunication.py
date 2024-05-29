from p2pnetwork.node import Node

class SocketCommunication(Node):

    def __init__(self,ip,port):
        super(SocketCommunication,self).__init__(ip,port,None)

    def startSocketCommunication(self):
        self.start()
    
    def inbound_node_connected(self, node):
        print("inbound connection")
        self.send_to_node(node,"I am the node, you connected to")
        return super().inbound_node_connected(node)
    
    def outbound_node_connected(self, node):
        print("outbound connection")
        self.send_to_node(node,"I am the node, who initialized the connection")
        return super().outbound_node_connected(node)
    
    def node_message(self, node, data):
        print("message:::",data)
        return super().node_message(node, data)

