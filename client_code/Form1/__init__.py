from ._anvil_designer import Form1Template
from anvil import *
import anvil.js

class Form1(Form1Template):

  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    self.canvas_1.set_event_handler("x-gaze", self.canvas_gaze)

  def start_tracking_click(self, **event_args):
    
    # This function is implemented in the Native Libraries section of the app.
    self.call_js("startGazeTracking")


  def canvas_gaze(self, x, y, **event_args):
    self.canvas_1.fill_style = "theme:Primary 500"
    self.canvas_1.fill_rect(x,y,1,1)

