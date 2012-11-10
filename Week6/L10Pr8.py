class Queue(object):
    def __init__(self):
        self.vals = []
        
    def insert(self, e):
        self.vals.append(e)
     
    def remove(self):
        try: 
            element = self.vals[0]
            self.vals.remove(self.vals[0])
        except:
            raise ValueError()
        return element
