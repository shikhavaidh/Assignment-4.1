
# coding: utf-8

# In[4]:

#Assignment 4.1 (A)
# Write a Python Program(with class concepts) to find the area of the triangle using the below formula.
# area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
# Function to take the length of the sides of triangle from user should be defined in the parent
# class and function to calculate the area should be defined in subclass.

class Polygon:
    def __init__(self, a, b, c): # a,b,c are the length of sides    
        self.a = a
        self.b = b
        self.c = c
        
    def sideCount(self):
        return(self.a, self.b, self.c)
        
    def showName(self):  
        
        print("Triangle Side Size: - " ) 
        print(self.a, self.b, self.c) 
 
class Triangle(Polygon):
    area=0
    s=0 #Semi parameter s = (a + b + c) / 2
    def __init__(self, a, b, c):
        Polygon.__init__(self, a, b, c)
    
    def getArea(self):  
        s = (self.a+self.b+self.c) / 2
        area = (s*(s-self.a)*(s-self.a)*(s-self.a)) ** 0.5
        print("Area of Triangle: ")
        print(area)  #returns the value of student id

        
#obj = Polygon(3, 4, 5)
#obj.showName()  #Line: 41

objchild = Triangle(2,1,3)
objchild.showName()
objchild.getArea()



# In[5]:

#4.1 (B)
# Write a function filter_long_words() that takes a list of words and an integer n and returns the list of words that are longer than n.
def long_words(n, str):
    word_len = []
    txt = str.split(" ")
    for x in txt:
        if len(x) > n:
            word_len.append(x)
    return word_len	
print(long_words(5, "The quick brown fox jumps over the lazy dog helloworld"))


# In[ ]:




# In[ ]:



