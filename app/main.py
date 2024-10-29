from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.textinput import TextImport
import datetime

class MusubiApp(App):
    def build(self):
        self.sales_log = []
        self.total_sold = 0
        self.total_revenue = 0

        layout = BoxLayout(orientation='vertical')

        #label to display profit
        self.profit_label = Label(text="Total Profit: $0")
        layout.add_widget(self.profit_label)

        #button to log a sale
        log_button = Button(text="Log Sale")
        log_button.bind(on_press=self.log_sale)
        layout.add_widget(log_button)

        #button to calculate profit
        profit_button = Button(text="Calculate Profit")
        profit_button.bind(on_press=self.calculate_profit)
        layout.add_widget(profit_button)

        #input for sale amount
        self.sale_input = TextInput(hint_text="Enter amount sold")
        layout.add_widget(self.sale_input)

        return layout

def log_sale(self, instance):
    try:
        quantity_sold = int(self.sale_input.text)
        price_per_musubi = 5.0 
        revenue = quantity_sold * price_per_musubi
        timestamp = datetime.datetime.now()

        self.sales_log.append({'timestamp': timestamp, 'quantity_sold': quantity_sold, 'revenue': revenue})
        self.total_sold += quantity_sold
        self.total_revenue += revenue

        self.sale_input.text = ''
        print(f"Sale logged: {quantity_sold} musubi(s) at {timestamp}, Revenue: ${revenue:.2f}")
    except ValueError:
        print("Invalid input for quantity sold")

        
def calculate_profit(self, instance):
    ingredient_cost_per_musubi = 3.0 #assume fixed cost for now, will change later when costs are known
    total_cost = self.total_sold * ingredient_cost_per_musubi
    profit = self.total_revenue - total_cost
    self.profit_label.text = f"Total Profit: ${profit:.2f}"

if __name__ == '__main__' :
    MusubiApp().run()