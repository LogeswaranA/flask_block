from Block import Block
from utils.BlockchainUtils import BlockchainUtils

class Blockchain():
    def __init__(self):
        self.blocks = [Block.genesis()]

    def addBlock(self,block):
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