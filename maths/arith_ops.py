
  
class ArithOps:

  def add(self, a, b):
    return a+b

  def sub(self, a, b):
   return a-b

  def mul(self, a, b):
    return a*b


if __name__ == '__main__':
  arith_ops_obj = ArithOps()
  print(arith_ops_obj.add(5, 4))