class MinStack:


    def __init__(self):
        self.__stack = []
        self.__mins = []

    def push(self, val: int) -> None:
        self.__stack.append(val)

        if not self.__mins or val <= self.__mins[-1]:
            self.__mins.append(val)

    def pop(self) -> None:
        value = self.__stack.pop()

        if value == self.__mins[-1]:
            self.__mins.pop()

    def top(self) -> int:
        return self.__stack[-1]

    def getMin(self) -> int:
        return self.__mins[-1]
        
