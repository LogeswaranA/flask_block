

class Blockchain():
    def __init__(self):
        self.blocks = []

    def addBlock(self,block):
        self.blocks.append(block)

    def toJson(self):
        data = {}
        jsonblocks =[]
        for block in self.blocks:
            jsonblocks.append(block.toJson())
        data['blocks']=jsonblocks
        return data