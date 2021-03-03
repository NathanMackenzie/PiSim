# pisim.py
__version__ = '0.4.0'
from tkinter import *
from matplotlib.figure import Figure 
from matplotlib.backends.backend_tkagg import (FigureCanvasTkAgg,  NavigationToolbar2Tk)
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
        # button that displays the plot 
        plot_button = Button(master = self.window, command = self.run_sim, height = 2, width = 10, text = "Run") 
        plot_button.pack()

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
        self.plt.axis([-1.2, 1.2, -1.2, 1.2])
        #.ion() # turn interactive mode on
        self.animated_plot = self.plt.plot(self.x_coords, self.y_coords, 'ro')[0]

        self.x_coords.append(.1)
        self.y_coords.append(.1)

        


        # creating the Tkinter canvas 
        # containing the Matplotlib figure 
        self.canvas = FigureCanvasTkAgg(fig, master = self.window)   
        self.canvas.draw() 
  
        # placing the canvas on the Tkinter window 
        self.canvas.get_tk_widget().pack() 

  
    def run_sim(self):
        radius = 1
        in_count = 0
        n = 0

        # Perform monte carlo simulation
        for i in range(500):
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

        print("The estimated value of pi is...")
        print(hp.monte_carlo_sim(1, in_count, n))

        
        

        
        
#-----------------------------------------------
# Main Code
#-----------------------------------------------

PiSim()