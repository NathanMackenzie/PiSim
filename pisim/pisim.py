# pisim.py
__version__ = '0.5.0'

from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)

import numpy as np
import helpers as hp

class PiSim:
  
    def __init__(self):
        # Define window
        self.window = Tk()
        self.window.title("Monte Carlo Pi Simulation")
        self.window.geometry("500x550")
        # Add plot to window
        self.add_plot()
        # Add start button 
        plot_button = Button(master = self.window, command = self.run_sim, height = 2, width = 10, text = "Run") 
        plot_button.pack(padx=5, pady=10, side = LEFT)
        # create a StringVar class 
        self.my_string_var = StringVar() 
  
        # create a label widget 
        self.my_label = Label(self.window, textvariable = self.my_string_var, font=("Arial", 24)) 
        self.my_label.pack(side = LEFT)
        # Show window
        self.window.mainloop()

    def add_plot(self):
         # the figure that will contain the plot 
        fig = Figure(figsize = (5, 5), dpi = 100) 
        
        # Coordinates of the points
        self.x_coords = []
        self.y_coords = []
  
        # adding the subplot 
        self.plt = fig.add_subplot(111) 
        self.plt.axis([-1, 1, -1, 1])
        
        theta = np.linspace( 0 , 2 * np.pi , 150 ) 
  
        radius = 1
  
        a = radius * np.cos( theta ) 
        b = radius * np.sin( theta ) 
        
        

        self.animated_plot = self.plt.plot(self.x_coords, self.y_coords, 'bo')[0]
        
        self.plt.plot( a, b ) 

        # creating the Tkinter canvas containing the Matplotlib figure 
        self.canvas = FigureCanvasTkAgg(fig, master = self.window)   
        self.canvas.draw() 
  
        # placing the canvas on the Tkinter window 
        self.canvas.get_tk_widget().pack() 

  
    def run_sim(self):
        radius = 1
        in_count = 0
        n = 0

        # Perform monte carlo simulation
        for i in range(1000):
            n = i # number of iterations

            # get random point coordinates
            x = hp.get_random()
            y = hp.get_random()

            self.x_coords.append(x)
            self.y_coords.append(y)

            self.animated_plot.set_xdata(self.x_coords[0:i])
            self.animated_plot.set_ydata(self.y_coords[0:i])
            self.canvas.draw()
            
            # calculate points distances from origin
            dist = hp.pythag(x, y)

            # check if point is witin the circle
            if dist <= 1:
                 in_count += 1

            if n > 0:
                temp = "Pi: {:.5f}"
                self.my_string_var.set(temp.format(hp.monte_carlo_sim(1, in_count, n)))
            self.window.after(50)

            
                
#-----------------------------------------------
# Main Code
#-----------------------------------------------

PiSim()