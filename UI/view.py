import flet as ft
from UI.alert import AlertManager

'''
    VIEW:
    - Rappresenta l'interfaccia utente
    - Riceve i dati dal MODELLO e li presenta senza modificarli
'''

class View:
    def __init__(self, page: ft.Page):
        # Page
        self.page = page
        self.page.title = "Lab07"
        self.page.horizontal_alignment = "center"
        self.page.theme_mode = ft.ThemeMode.DARK

        # Alert
        self.alert = AlertManager(page)

        # Controller
        self.controller = None

        # LIST VIEW (AGGIUNTA DA ME)
        self.list_view = None

    def show_alert(self, messaggio):
        self.alert.show_alert(messaggio)

    def set_controller(self, controller):
        self.controller = controller

    def update(self):
        self.page.update()

    def load_interface(self):
        """ Crea e aggiunge gli elementi di UI alla pagina e la aggiorna. """
        # --- Sezione 1: Intestazione ---
        self.txt_titolo = ft.Text(value="Biblioteche di Torino", size=38, weight=ft.FontWeight.BOLD)

        # --- Sezione 2: Filtraggio ---
        # TODO
        self.dd_biblioteca = ft.Dropdown(label="Biblioteca", width=300)
        self.dd_biblioteca.options.append(
            ft.DropdownOption(key="Biblioteca civica Italo Calvino", text="Biblioteca civica Italo Calvino"))
        self.dd_biblioteca.options.append(
            ft.DropdownOption(key="Biblioteca civica Francesco Cognasso", text="Biblioteca civica Francesco Cognasso"))
        self.dd_biblioteca.options.append(
            ft.DropdownOption(key="Biblioteca civica Cesare Pavese", text="Biblioteca civica Cesare Pavese"))
        self.dd_biblioteca.options.append(
            ft.DropdownOption(key="Biblioteca musicale Andrea Della Corte", text="Biblioteca musicale Andrea Della Corte"))
        self.dd_biblioteca.options.append(
            ft.DropdownOption(key="Biblioteca del Centro interculturale", text="Biblioteca del Centro interculturale"))
        self.dd_biblioteca.options.append(
            ft.DropdownOption(key="Biblioteca civica Dietrich Bonhoeffer", text="Biblioteca civica Dietrich Bonhoeffer"))
        self.dd_biblioteca.options.append(
            ft.DropdownOption(key="Biblioteca civica Don Lorenzo Milani", text="Biblioteca civica Don Lorenzo Milani"))
        self.dd_biblioteca.options.append(
            ft.DropdownOption(key="Biblioteca civica Primo Levi", text="Biblioteca civica Primo Levi"))
        self.dd_biblioteca.options.append(
            ft.DropdownOption(key="Biblioteca civica Luigi Carluccio", text="Biblioteca civica Luigi Carluccio"))

        self.dd_genere = ft.Dropdown(label="Genere", width=200)
        Fantascienza
        Fantasy
        Fumetto
        Giallo
        Poesia
        Racconti
        Ragazzi
        Romanzo
        Saggio
        Storia
        Horror

        # Sezione 3: Libri
        # TODO
        btn = ft.Button(content="Mostra Libri",
                        on_click=self.controller.handler_btn)

        # --- Toggle Tema ---
        self.toggle_cambia_tema = ft.Switch(label="Tema scuro", value=True, on_change=self.cambia_tema)

        # --- Layout della pagina ---
        self.page.add(
            self.toggle_cambia_tema,

            # Sezione 1
            self.txt_titolo,
            ft.Divider(),

            # Sezione 2: Filtraggio
            # TODO
            ft.Row(controls=[self.dd_biblioteca, self.dd_genere],
                   spacing=50,
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.Divider(),

            # Sezione 3: Libri
            # TODO
            ft.Row(controls=[btn],
                   alignment=ft.MainAxisAlignment.CENTER),
            ft.ListView(expand=True,
                        spacing=10)

        )

        self.page.scroll = "adaptive"
        self.page.update()

    def cambia_tema(self, e):
        """ Cambia tema scuro/chiaro """
        self.page.theme_mode = ft.ThemeMode.DARK if self.toggle_cambia_tema.value else ft.ThemeMode.LIGHT
        self.toggle_cambia_tema.label = "Tema scuro" if self.toggle_cambia_tema.value else "Tema chiaro"
        self.page.update()
