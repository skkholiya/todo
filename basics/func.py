#function is a block of statements, executed only when it's called.

#defining a function: Arbitrary arguments: when we don't know how many arguments that will be passed into our function.
def example1(*arg):
  print("oldest child is:",arg[0])
  
example1("emil","wasu","neera")

#Keyword arguments: send argument with key-value syntax.
def example(a,b,c):
#return value of the key.
  print(a,b,c);
  
example(a=1,b=2,c=3)

#Arbitray Keyword Arguments: if we don't know how many keyword arguments that will be passed into function
def framework(**args):
  print("java backend framework is:",args["java"])
  
framework(java="spring",python="django",javascript="node")

#Default parameter in function: by default it will return the specifed value
def front_end(language="javaScript"):
  print("Using",language,"as frontend");
  
front_end("react")
front_end("vue")
front_end("angular")
front_end()
