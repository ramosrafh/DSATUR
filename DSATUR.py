import csv

class Vertice:
	def __init__(self, n):
		self.nome = n
		self.adjacentes = list()
		self.cor = -1
	
	def add_adjacente(self, v):
		if v not in self.adjacentes:
			self.adjacentes.append(v)
			self.adjacentes.sort()

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

		        
	def max_adj(self, u):
		max = 0
		vert = ''
		for p in self.vertices[u].adjacentes:
			leng = len(list(self.vertices[p].adjacentes))
			if leng >= max and self.vertices[p].cor == -1:
				max = leng
				vert = p
		if vert == '':
			for j in self.vertices:
				leng = len(list(self.vertices[j].adjacentes))
				if leng >= max and self.vertices[j] == -1:
					max = leng
					vert = j
		return vert
	
	def todosColoridos(self):
		for vertice in self.vertices:
			if self.vertices[vertice].cor == -1:
				return False
		return True
	
	def verif(self, vert, cor):
		for u in self.vertices[vert].adjacentes:
			if self.vertices[u].cor == cor:
				return False    
		return True
	

	def pintar(self, vert):
		colors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
		if vert == '':
			return True
		while not self.todosColoridos():
			for i in colors:
				if self.verif(vert, i) and self.vertices[vert].cor == -1:
					self.vertices[vert].cor = i
					self.pintar(self.max_adj(vert))
			self.pintar(self.max_adj(vert))
			self.pintar(self.max_adj(vert))
			self.pintar(self.max_adj(vert))
			break

	
		            
	def mostrar_grafo(self):
		for key in sorted(list(self.vertices.keys())):
			print(key + ' ' + str(self.vertices[key].cor) + ' ' + str(self.vertices[key].adjacentes))

# MAIN



g = Grafo()
#for i in range(ord('A'), ord('K')):
#	g.add_vertice(Vertice(chr(i)))

arestas = []


with open('grafo.csv', newline='') as csvfile:
	csv_reader = csv.reader(csvfile, delimiter=',')
	csv_reader = list(csv_reader)

	#print(csv_reader[0][3])
	
	for coluna in csv_reader:
		g.add_vertice(Vertice(coluna[0]))
	
	loop = int(len(g.vertices))

	for i in range(loop):
		for col in csv_reader[i][1:]:
			arestas.append(col)
			i += 1


#arestas = ['AB', 'AC', 'AJ', 'BC', 'BG', 'BD', 'BJ', 'JD', 'JG', 'GH', 'IG', 'IH', 'ID', 'IC', 'FC', 'FE', 'FG', 'GE', 'EC', 'HJ', 'HI', 'DC']

for aresta in arestas:
	g.add_aresta(aresta[:1], aresta[1:])

g.mostrar_grafo()
print('')
g.pintar(g.max_len())
print('')
g.mostrar_grafo()



