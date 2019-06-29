import time
import csv
import math

class Vertice:
	def __init__(self, n):
		self.nome = n
		self.adjacentes = list()
		self.cor = 'null'
	
	def add_adjacente(self, v):
		if v not in self.adjacentes:
			self.adjacentes.append(v)
			#self.adjacentes.sort()

class Grafo:
	vertices = {}

	def add_vertice(self, vertice):
		if isinstance(vertice, Vertice) and vertice.nome not in self.vertices:
			self.vertices[vertice.nome] = vertice
			return True
		else:
			return False
			
	
	def add_aresta(self, u, v):
		if u in self.vertices and v in self.vertices:
			self.vertices[u].add_adjacente(v)
			self.vertices[v].add_adjacente(u)
			return True
		else:
			return False
			
	def max_len(self):
		max = 0
		vert = ''
		for u in self.vertices:
			leng = len(list(self.vertices[u].adjacentes))
			if leng >= max:
			    max = leng
			    vert = u
		return vert

	def res_max(self):
		max = 0
		for u in self.vertices:
			leng = len(list(self.vertices[u].adjacentes))
			if leng >= max:
			    max = leng
		return max

	def res_med(self):
		soma = 0
		med = 0
		for u in self.vertices:
			leng = len(list(self.vertices[u].adjacentes))
			soma += leng
		med = (soma/len(self.vertices))
		return med

	def res_min(self):
		min = 100000
		for u in self.vertices:
			leng = len(list(self.vertices[u].adjacentes))
			if leng <= min:
			    min = leng
		return min

	def res_desvio(self):
		num = 0
		desv = 0
		for u in self.vertices:
			leng = len(list(self.vertices[u].adjacentes))
			num += ((leng-(self.res_med())) ** 2)
		desv = math.sqrt((num/((len(self.vertices)))))
		return desv
		        
	def max_adj(self, u):
		max = 0
		vert = ''
		for p in self.vertices[u].adjacentes:
			leng = len(list(self.vertices[p].adjacentes))
			if leng >= max and self.vertices[p].cor == 'null':
				max = leng
				vert = p
		if vert == '':
			for j in self.vertices:
				leng = len(list(self.vertices[j].adjacentes))
				if leng >= max and self.vertices[j] == 'null':
					max = leng
					vert = j
		return vert
	
	def todosColoridos(self):
		for vertice in self.vertices:
			if self.vertices[vertice].cor == 'null':
				return False
		return True
	
	def verif(self, vert, cor):
		for u in self.vertices[vert].adjacentes:
			if self.vertices[u].cor == cor:
				return False    
		return True
	

	def pintar(self, vert):
		colors = []
		for i in range(65, 65+len(self.vertices)):
			colors.append(chr(i))
		if vert == '':
			return True	
		for i in colors:
			if self.verif(vert, i) and self.vertices[vert].cor == 'null':
				self.vertices[vert].cor = i
				self.pintar(self.max_adj(vert))
		self.pintar(self.max_adj(vert))
		return True

	
		            
	def mostrar_grafo(self):
		for key in list(self.vertices.keys()):
			print(key + ' ' + str(self.vertices[key].cor) + ' ' + str(self.vertices[key].adjacentes))

# MAIN

start = time.time()

g = Grafo()

arestas = []

# PARA LER O ARQUIVO CSV

with open('grafocert.csv', newline='') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',', skipinitialspace=True, quotechar="'")
	csv_reader = list(csv_reader)
	
	for coluna in csv_reader:
		g.add_vertice(Vertice(coluna[0]))
	
	loop = int(len(g.vertices))

	for i in range(loop):
		for col in csv_reader[i][1:]:
			g.add_aresta(list(g.vertices)[i], col)

g.mostrar_grafo()
print('')
g.pintar(g.max_len())
print('')
g.mostrar_grafo()

print('')
print('Maior grau: ', g.res_max())
print('')
print('Menor grau: ', g.res_min())
print('')
print('Media: ', g.res_med())
print('')
print('Desvio Padrão: ', g.res_desvio())

# PARA ESCREVER O ARQUIVO CSV

vertices = []
cores = []

loop = len(g.vertices)

for i in range(loop):
	vertices.append(list(g.vertices)[i])

for i in range(65, 65+loop):
			cores.append(chr(i))

rows = zip(vertices, cores)

with open('resultadocert.csv', 'w') as f:
	csv_writer = csv.writer(f, delimiter=',')	

	for row in rows:
		csv_writer.writerow(row)

end = time.time()
time = end - start
print('')
print ('Tempo de execução: ', time)
