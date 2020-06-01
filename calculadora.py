import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout

class LayoutCalculadora(GridLayout):

    def resultado(self, valor):
        if valor:
            try:
                self.display.text = str(eval(valor))
            except Exception:
                self.display.text = 'Erro ao calcular! Tente Novamente!'

class CalculadoraApp(App):

    def build(self):
        return LayoutCalculadora()

if __name__ == "__main__":
    CalculadoraApp().run()