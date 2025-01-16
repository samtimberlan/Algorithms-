

class Stack:
    def __init__(self):
        self.data = []

    def push(self, data):
        self.data.append(data)

    def pop(self, data):
        return self.data.pop()

    def peek(self, data):
        return self.data[-1]
    
    def is_empty(self):
        return len(self.data) == 0
    

class SetOfStacks:
    def __init__(self, threshold) -> None:
        self.threshold = threshold
        self.stack_set = [[]]

    def push(self, data):
        if len(self.stack_set[-1]) < self.threshold:
            self.stack_set[-1].append(data)
        else:
            self.stack_set.append([data])

    def pop(self):
        if len(self.stack_set[-1]) >= 1:
            data = self.stack_set[-1].pop()
            if len(self.stack_set[-1]) == 0:
                self.stack_set.pop()
        return data
    
    # 1, 5 idx % threshold
    # [[0,2], [1,3,5]]
    def pop_at(idx):
    
set = SetOfStacks(threshold = 5)
for i in range(10):
    set.push(i)
print(set)

for i in range(5):
    set.pop()
print(set)

    
