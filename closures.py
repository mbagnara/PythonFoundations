"""
	In programming languages, a closure, also lexical closure or function closure, is a technique for implementing lexically scoped name binding in a language with first-class functions. Operationally, a closure is a record storing a function[a] together with an environment.[1] The environment is a mapping associating each free variable of the function (variables that are used locally, but defined in an enclosing scope) with the value or reference to which the name was bound when the closure was created.[b] Unlike a plain function, a closure allows the function to access those captured variables through the closure's copies of their values or references, even when the function is invoked outside their scope. 

	The term closure is often used as a synonym for anonymous function, though strictly, an anonymous function is a function literal without a name, while a closure is an instance of a function, a value, whose non-local variables have been bound either to values or to storage locations 
	
	Ref: https://en.wikipedia.org/wiki/Closure_(computer_programming)
"""

def outer_function(fn):

	def inner_function():
		result = n()
	return inner_function
	

#@outer_function
def Display():
	print("Hello")

a = Display # will only assign the function
a() # executes the function


