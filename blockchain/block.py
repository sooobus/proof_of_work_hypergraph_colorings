import numpy as np
import mining

# написать генерацию заголовка
# превращать семейство в хеш

s = 20 #50
n = 20 #50
k = 5 #16

def get_mask(n):
    return np.binary_repr(n)

class Block(object):
    def __init__(self, index, timestamp, data, prev_hash):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.prev_hash = prev_hash

    def __dict__(self):
        info = {}
        info['index'] = str(self.index)
        info['timestamp'] = str(self.timestamp)
        info['prev_hash'] = str(self.hash)
        info['hash'] = str(self.hash)
        info['data'] = str(self.data)
        return info
    
    def generate_header(self, n, k, s):
        prev_hash = self.info['prev_hash']
        set_size = ncr(ncr(n, k), s)
        res = mine_process(n, k, s, prev_hash, set_size)
