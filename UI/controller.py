import flet as ft
from UI.view import View
from model.model import Model

'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view

        # Variabili per memorizzare le selezioni correnti
        self.biblioteca_selezionata = None
        self.genere_selezionato = None

    # POPOLA DROPDOWN
    # TODO

    # CALLBACKS DROPDOWN
    # TODO

    # AZIONE: MOSTRA LIBRI
    # TODO
    def handler_btn(self, e):
        print("Button clicked")
        result = self._model.get_libri_filtrati()
        # Prende quanto letto dal Model/Dao e lo mostra nella UI, all'interno della listview.
        self._view.list_view.controls.clear()
        self._view.list_view.controls.append(ft.Text(f"{len(result)}"))
        for libro in result:
            self._view.list_view.controls.append(ft.Text(f"{libro}"))


