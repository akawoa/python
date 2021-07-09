class MathDojo:
    def __init__(self):
        self.result = 0

    def add(self, num, *nums):
        self.result += num
        for a in nums:
            self.result += int(a)
        return self
    def subtract(self, num, *nums):
        self.result -= num
        for a in nums:
            self.result -= int(a)
        return self
        
        # create an instance:
md = MathDojo()

x = md.add(2).add(2, 5, 1).subtract(3, 2).result
print(x)  # should print 5
# run each of the methods a few more times and check the result!


# Create a MathDojo class

# Write the add method and test it by calling it 3 times, with different numbers of arguments each time

# Write the subtract method and test it by calling it 3 times, with different numbers of arguments each time

# Make sure you are able to chain methods as demonstrated above