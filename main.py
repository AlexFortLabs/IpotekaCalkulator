from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
# Display Pixles

#from kivymd.uix.button import MDRectangleFlatButton

tabelka = [
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Jon", "Edler", "my@test.br", "123/8888999"),
                ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
                ("Inga", "Mendel", "inga.mendel@test.de", "+49 123 / 888 899 9")
            ]

class MainApp(MDApp):
    title = "Ipoteka Kalkulator"
    by_who = "Author Alexander Fortowski"

    def build(self):
        # Opredelim Screen
        screen = Screen()
        # Opredelim Tablizu
        table = MDDataTable(
            #orientation="lr-tb",
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.6),
            check = True,
            use_pagination = True,
            rows_num = 3,
            pagination_menu_height = '240dp',
            pagination_menu_pos = "auto",   # center
            #background_color = [1,0,0,.5],   # [r,g,b,transparensy]
            column_data = [
                ("Vorname", dp(30)),
                ("Nachname", dp(30)),
                ("Email", dp(25)),
                ("Phone", dp(25))
            ],
            row_data = tabelka
            #[
            #    ("Jon", "Edler", "my@test.br", "123/8888999"),
            #    ("Paul", "Louvat", "p.louvat@test.fr", "123/8888999"),
            #    ("Inga", "Mendel", "inga.mendel@test.de", "+49 123 / 888 899 9")
            #]
        )
        # Bind the table
        table.bind()
        table.bind(on_check_press=self.checked)
        table.bind(on_row_press=self.row_checked)

        self.theme_cls.theme_style = "Light"
        self.theme_cls.primary_palette = "BlueGray"
        # Dobawim Widget-Tablizu
        screen.add_widget(table)
        #screen.add_widget(
        #    MDRectangleFlatButton(
        #        text="Hello, World",
        #        pos_hint={"center_x": 0.5, "center_y": 0.5},
        #    )
        #)
        return screen

    # objavim obe funkzii
    def checked(self, instance_table, curent_row):
        print(instance_table, curent_row)

    def row_checked(self, instance_table, instance_row):
        print(instance_table, instance_row)

if __name__ == "__main__":
    MainApp().run()