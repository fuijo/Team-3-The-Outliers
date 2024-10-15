# %%
#Dependencies and setup
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy.stats import linregress

# %%
#Define LinReg Function that will calculate the Linear Regression of 2 sets of data
#Input: takes 2 data series
#Output: an array of the slope, intercept, rvalue, pvalue,stderr,line to print and line equation
def LinReg(xs,ys):
    slope, intercept, rvalue, pvalue, stderr = linregress(xs,ys)
    regvalues = slope*xs+intercept
    line_eq = "y = " + str(round(slope,2)) + "x + " + str(round(intercept,2))
    linregs = [slope,intercept,rvalue,pvalue,stderr,regvalues,line_eq]
    return linregs

# %%
#Define ScatPlotandReg creates a scatter plot with a linear Regression show as well as an Rsquared value
#Inputs: takes 2 data series, your x and y coordinates, labels for  the axises and a title
#Output shows and saves a scatterplot
def ScatPlotandReg(xs,ys,xlab,ylab,title,filename):
    reginfo = LineReg(xs,ys)
    print(f"The r^2-value is: {reginfo[2]**2}")
    plt.scatter(xs,ys)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.plot(xs,reginfo[5],color = 'r')
    plt.annotate(reginfo[6],ha = 'left',va = 'top',fontsize=15,color="red")
    plt.savefig(f"Graphs/{filename}")
    plt.show()

# %%
#Define ScatPlotNoReg creates a scatter plot
#Inputs: takes 2 data series, your x and y coordinates, labels for  the axises and a title
#Output shows and saves a scatterplot
def ScatPlotNoReg(xs,ys,xlab,ylab,title,filename):
    plt.scatter(xs,ys)
    plt.xlabel(xlab)
    plt.ylabel(ylab)
    plt.title(title)
    plt.savefig(f"Graphs/{filename}")
    plt.show()


