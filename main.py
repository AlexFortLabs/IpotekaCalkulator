from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.uix.screenmanager import Screen
from kivymd.uix.datatables import MDDataTable
from kivy.metrics import dp
# Display Pixles

#from kivymd.uix.button import MDRectangleFlatButton


class MainApp(MDApp):
    def build(self):
        # Opredelim Screen
        screen = Screen()
        # Opredelim Tablizu
        table = MDDataTable(
            orientation="lr-tb",
            pos_hint = {'center_x': 0.5, 'center_y': 0.5},
            size_hint = (0.9, 0.6),
            check = True,
            column_data = [
                ("First Name", dp(30)),
                ("Last Name", dp(30)),
                ("Email", dp(30)),
                ("Phone", dp(30))
            ],
            row_data = [
                ("Jon", "Edler", "meil@test.de", "123/8888999"),
                ("Jon", "Edler", "meil@test.de", "123/8888999"),
                ("Jon", "Edler", "meil@test.de", "123/8888999")
            ]
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