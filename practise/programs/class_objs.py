'''Acces Three level class methods.'''

class ClassA(object):
	def __init__(self):
		self.varA = 'varA String'

	def do_nothing_in_a(self):
		print('print something in ClassA')


class ClassB(object):
	def __init__(self):
		self.varB = 'varB String'
		self.class_a_obj = ClassA()

	def do_nothing_in_b(self):
		print('print something in ClassB')


class ClassC(object):
	def __init__(self):
		self.varC = 'varC String'
		self.class_b_obj = ClassB()

	def do_nothing_in_c(self):
		print('print something in ClassC')
		self.class_b_obj.class_a_obj.do_nothing_in_a()


if __name__ == '__main__':
    print('Start.')
    class_c_obj = ClassC()
    class_c_obj.do_nothing_in_c()
    print('End.')