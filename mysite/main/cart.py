from .models import *
class Cart():
	def __init__(self, request):
		self.session = request.session
		cart = self.session.get('session_key')
		if 'session_key' not in request.session:
			cart = self.session['session_key'] = {}
		self.cart = cart
		
	def add(self, proizvod):
		id_proizvod= str(proizvod.id)
		if id_proizvod in self.cart:
			pass
		else:
			self.cart[id_proizvod] = {'price': str(proizvod.cijena_proizvoda)}
		self.session.modified = True
		
	def cart_total(self):
		id_proizvod = self.cart.keys()
		proizvod = Proizvod.objects.filter(id__in=id_proizvod)
		
		totals = self.cart
		total=0
		for key, value in totals.items():
			key= int(key)
			for pro in proizvod:
				if pro.id ==key:
					total = total + (pro.cijena_proizvoda)
		return total
		
		

	def __len__ (self):
		return len(self.cart)
	
	def get_prods(self):
		product_ids = self.cart.keys()
		proizvod = Proizvod.objects.filter(id__in =product_ids)
		return proizvod
	def delete(self, proizvod):
		id_proizvod = str(proizvod)
		if id_proizvod in self.cart:
			del self.cart[id_proizvod]
		self.session.modified = True
		
	def clear(self):
		self.cart = {}
		self.session.modified = True
	

