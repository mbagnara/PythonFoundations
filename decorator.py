
def DecoratorFunction(fn):

	import time	
	def wrapper():
		print("Internal wrapper function: Initiating...")
		time.sleep(1)
		t1 = time.time()
		result = fn()
		t2 = time.time()
		print("Internal wrapper function: Initiating...")
		print(f"function took {t2-t1} to run")
	return wrapper
		
	


@DecoratorFunction
def PrintMessage():
	print("Hola")





