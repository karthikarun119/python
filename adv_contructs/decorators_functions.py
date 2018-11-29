def simple_decorator(function1):
    print("decorating the functions")
    return function1
@simple_decorator
def function1():
    print("inside the functions")
function1()
def replacing_decorator_with_arguments(arg):
  print("defining the decorator")
  def _decorator(function):
      # in this inner function, arg is available too
        print("doing decoration, %s" % arg)
        def _wrapper(*args,**kwargs):
            print("Inside the wrapper %r %r"% (args,kwargs) )
            return function(*args,*kwargs)
        return _wrapper
        
  return _decorator
@replacing_decorator_with_arguments("abc")
def function(*args,**kwargs):
    print("Inside the function %r %r"%(args,kwargs))
function(11,12)