from ._anvil_designer import Form1Template
from anvil import *
import anvil.js

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run when the form opens.

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    self.call_js("wg")


  def data(self, x, y):
    print(x,y)

