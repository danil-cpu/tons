#translation of number systems

class Tons:
	def __init__(self, number, notation_one, notation_two):
		
		self.number = number
		self.notation_one = notation_one # max 32
		self.notation_two = notation_two # max 32 
		
		self.literals = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
		self.result = self.convert_base()
		
	def convert_base(self, to_base=None):
		result = ''
		if isinstance(self.number, str):
			if self.notation_one < 33:
				n = int(self.number, self.notation_one)
			else:
				literals = {b: a for a, b in enumerate(list(self.literals))}
				translation_result = list()
				nu = len(self.number)-1
				for i in self.number:
					translation_result.append(literals.get(i, i)*self.notation_one**nu)
					nu-=1
				n = sum(translation_result)
		else:
			n = int(self.number)
		self.result_10 = n
		while n > 0:
			n, m = divmod(n, self.notation_two if to_base is None else to_base)
			result += self.literals[m]
		return result[::-1]
	
	def __eq__(self, other):
		if isinstance(other, Tons):
			return self.result_10 == other.result_10
		elif isinstance(other, int):
			return self.result_10 == other
			
"""
example:
tons = Tons('AABC', 16, 10)
result = tons.result
print(result)

$ Tons('AAA', 16, 10) == Tons('AAA', 16, 10)
>> True
$ Tons('AAA', 16, 10) == Tons('AAB', 16, 10)
>> False
"""
