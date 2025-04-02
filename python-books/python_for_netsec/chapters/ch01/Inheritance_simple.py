class BaseClass:
    def __init__(self, property):
        self.property = property
    def message(self):
        print('Welcome to Base Class')
    def message_base_class(self):
        print('This is a message from Base Class')

class ChildClass(BaseClass):
    def __init__(self, property):
        BaseClass.__init__(self, property)
    def message(self):
        print('Welcome to ChildClass')
        print('This is inherited from BaseClass')