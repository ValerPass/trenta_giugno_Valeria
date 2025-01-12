import warnings

import flet as ft
from model.model import Model
from UI.view import View

class Controller:
    def __init__(self, view: View, model: Model):
        # the view, with the graphical elements of the UI
        self._view = view
        # the model, which implements the logic of the program and holds the data
        self._model = model


    def fillDD(self):
        self._model.buildGrafo()
        for i in list(self._model.grafo.nodes):
            self._view.ddLocalizzazione.options.append(ft.dropdown.Option(i))
        self._view.update_page()



    def handleStatistiche(self, e):
        self._view.txtOut.controls.clear()
        if self._view.ddLocalizzazione.value is None:
            warnings.warn("Deve selezionare una localizzazione")
            self._view.txtOut.controls.append(ft.Text(f"Deve selezionare una localizzazione"))
            self._view.update_page()
            return
        nNodes, nEdges = self._model.getDetails()
        self._view.txtOut.controls.append(ft.Text(f"Il grafo ha {nNodes} vertici e {nEdges} archi"))
        self.vicini = self._model.getStatistiche(self._view.ddLocalizzazione.value)
        self._view.txtOut.controls.append(ft.Text(f"Adiacenti a : {self._view.ddLocalizzazione.value}"))
        for v in self.vicini:
            self._view.txtOut.controls.append(ft.Text(f"{v[0]} ------- {v[1]}"))
        self._view.update_page()




    def handle_path(self, e):
        pass