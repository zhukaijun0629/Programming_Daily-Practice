from collections import OrderedDict

class LRUCache():
    def __init__(self, N):
        self.size = N
        self.key_to_value = OrderedDict()
    
        
    def put(self, key, val):
        if key in self.key_to_value:
            del self.key_to_value[key]
        self.key_to_value[key] = val
        if self.size < len(self.key_to_value):
            self.key_to_value.popitem(last=False)
            
        
        
    def get(self, key):
        if key in self.key_to_value:
            val = self.key_to_value[key]
            self.key_to_value.move_to_end(key)
            return val
        return None


cache = LRUCache(3)
cache.put('key1','val1')
print(cache.get('key1'))
cache.put('key2','val2')
cache.put('key3','val3')
cache.put('key4','val4')
print(cache.get('key1'))
cache.put('key2','val22')
print(cache.get('key2'))
cache.put('key5','val5')
print(cache.get('key3'))
cache.put('key6','val6')
print(cache.get('key5'))


    
        