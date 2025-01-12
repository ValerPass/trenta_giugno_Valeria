import copy

import networkx as nx

from database.DAO import DAO


class Model:
    def __init__(self):
        self.grafo = nx.Graph()

    def buildGrafo(self):
        self.grafo.clear()
        self.grafo.add_nodes_from(self.getLocalizzazioni())
        self.grafo.add_edges_from(self.getArchi())
        for a in self.grafo.edges:
            a1 = a[0]
            a2 = a[1]
            peso = DAO.getPesi(a1, a2)
            self.grafo[a1][a2]["weight"] = peso

    def getStatistiche(self, loc):
        res = []
        for l in self.grafo.neighbors(loc):
            res.append((l, self.grafo[loc][l]["weight"]))
        res.sort(key=lambda x: x[1], reverse=True)
        return res





    def getLocalizzazioni(self):
        return list(DAO.getLocalizzazioni())

    def getArchi(self):
        return list(DAO.getArchi())

    def getDetails(self):
        return len(self.grafo.nodes), len(self.grafo.edges)

