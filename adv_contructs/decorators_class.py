class replacing_decorator_class(object):
  def __init__(self, arg):
      # this method is called in the decorator expression
      print("in decorator init, %s" % arg)
      self.arg = arg
  def __call__(self, function):
      # this method is called to do the job
      print("in decorator call, %s" % self.arg)
      self.function = function
      return self._wrapper
  def _wrapper(self, *args, **kwargs):
      print("in the wrapper, %s %s" % (args, kwargs))
      return self.function(*args, **kwargs)
deco_instance = replacing_decorator_class('foo')
@deco_instance
def function(*args, **kwargs):
  print("in function, %s %s" % (args, kwargs))
function(11,12)