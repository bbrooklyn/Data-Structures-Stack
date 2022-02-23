'''
This is a Python representation of the low level functionality that a stack would follow.
Data cannot be removed from memory, it can only be overwritten or put out of scope; this functionality is
replicated in the code.
'''

class Stack:
    def __init__(self, size: int):
        self.stack = [None for b in range(size)] # Allocates memory with the size of [size] values.
        self.SIZE = size
        self.pointer = 0

    def __simulate_memory(self): # Simulates fixed sized memory; unable to do so in Python by default.
        if self.pointer <= self.SIZE: # Checks whether the size of the stack is within the size of allocated memory.
            if not self.pointer >= 0: # Checks whether the memory is out of reach, resulting in a stack underflow.
                raise MemoryError('STACK UNDERFLOW')
        else:
            raise MemoryError('STACK OVERFLOW')
                
    def is_empty(self):
        if self.pointer == 0:  # If the size of the stack is the same as allocated memory.
            return True
        else:
            return False

    def is_full(self):
        if self.pointer == self.SIZE: # If the size of the stack is the same as allocated memory.
            return True
        else:
            return False
        
    def push(self,value):
        # The value being pushed is being assigned to the position after the last value.
        self.pointer = self.pointer + 1
        self.__simulate_memory()
        self.stack[self.pointer] = value # End of the stack.

        
    def pop(self):
        self.pointer = self.pointer-1 # Moves the pointer below the last item/value, rendering it out of scope, the value can then be overwritten or ignored.
        self.__simulate_memory()
        
    def peek(self):
        return self.stack[self.pointer]
    
            
