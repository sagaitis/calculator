class Calculator:
    def __init__(self):
        """
        Starts our calculator with a remembered number of zero.
        """
        self.memory = 0

    def add(self, number):
        """
        Adds a number to our remembered number.

        number: How much to add. (float)
        Returns the new total. (float)
        """
        self.memory += number
        return self.memory

    def subtract(self, number):
        """
       Takes away a number from what we remember.

       number: How much to take away. (float)
       Returns the remainder. (float)
       """
        self.memory -= number
        return self.memory

    def multiply(self, number):
        """
        Makes our remembered number bigger by multiplying it.

        number: What to multiply by. (float)
        Returns the new bigger number. (float)
        """
        self.memory *= number
        return self.memory

    def divide(self, number):
        """
        Splits our remembered number by another number.
        If you try to split by zero, it says you can't.

        number: What to split by. Can't be zero. (float)
        Returns the split number or nothing if we tried zero. (float/None)
        """
        if number == 0:
            print("Oops! Divided by zero. Math Police alerted. They're bringing pie. Not the yummy kind!")

            return None
        self.memory /= number
        return self.memory

    def root(self, n):
        """
        Finds the root of our remembered number.
        It's like asking what number times itself a few times makes our number.
        Can't use zero or negative numbers.

        n: How many times the number multiplies itself. (float)
        Returns the root or nothing if we did something wrong. (float/None)
        """
        if n <= 0:
            print("Oops! Only positive numbers, please.")
            return None
        self.memory **= 1/n
        return self.memory

    def reset(self):
        """
        Forgets the number we remembered and goes back to zero.
        Returns zero because we forgot everything else.
        """
        self.memory = 0
        return self.memory
