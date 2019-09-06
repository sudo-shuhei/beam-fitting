import numpy as np
from PIL import Image as pil
import matplotlib.pyplot as plt
from scipy.optimize import curve_fit

data = np.array(pil.open("original.bmp"))
data = data/np.max(data)

x,y=np.meshgrid(np.linspace(0,data.shape[1],data.shape[1]),np.linspace(0,data.shape[0],data.shape[0]))

def twoDgaussian(X,wx,wy,x0,y0):
    x,y=X
    z=np.exp(-(x-x0)**2/wx**2-(y-y0)**2/wy**2)
    return z

initial=(50,50,500,500)

popt,pcov=curve_fit(twoDgaussian,(x,y),data,initial)
