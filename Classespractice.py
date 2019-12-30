# Luke Reed


print("welcome to the area calculator")
print("______________________________________________________________________________________")


# 'here we make a class '

class Area:
    # 'for and for anyone who is wondering the __init__ is a way of telling python that'
    # 'you are making a class that you want to (initialize) attributes to'
    # 'the attributes we are passing to the initialized class are length and width'
    # 'that's why if you just makes a class and pass stuff to you'll get the Error: '
    # '(Name_of_class takes no arguments) because you haven't yet initialized the class... hope this helps :)'

    def __init__(self, length, width):
        self.length = length
        self.width = width
# 'calculate area and return it'

    def calculate(self):
        area = self.length * self.width
        print("The total area is {}".format(area))


a = input("Enter the length of the rectangle: ")
b = input("Enter the width of the rectangle: ")

# 'here we type cast (a) and (b) because when python takes in data it does everything is a string and'
# 'two strings cannot be multiplied together'

a = int(a)
b = int(b)

a1 = Area(a, b)
# 'calling the calculate function in the class Area'
a1.calculate()
