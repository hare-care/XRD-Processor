# XRD-Processor
Code to proceed XRD data in the lab so I don't have to do manual calculations for my superlattice(SL) samples.
Version 0.2

## Requirements:
Python 3.x | Packages: math, sys

## How to use:
Obtain angle values via some other tool.
Navigate to repo and run main.py with values, example shown below:
```
python3 main.py 1 2 3 4
```
Results will be printed to terminal.
4 arguments must be included; the first left peak, the main peak, the substrate peak, and first right peak




## What is this for?
I dont want to do the same calculations all the time, so we automate. 
In my lab we use XRD (X-ray Diffraction) to verify structural information about our sample. The xrd machine outputs a .X01 data file and then it connects to some very old computer. We then use it to find the different peaks like the SL peak, substrate peak, and the n = -1, +1 peaks. From there we want the lattice constants for the SL and the substrate, lattice mismatch, and SL thickness.

This version requires some previous analysis to work which is not ideal. So it is still in testing phases but it gets the job done for me, 
as in it will give me the calculations. Right now it is a glorified calculator, just uses some equations based off the inputs. 
The inputs are the various theta values for the the peaks. You can also input the other values like lambda or hkl, but we dont change those in my lab. So I just keep it the same. 

## Methods

### Calculations: 
lattice constant:
To calculate this you need the angle for the n=0 peak of the SL and the peak of the substrate
d = (n*lambda)/(2*sind(theta)); // d is the atomic spacing
a = d*(sqrt(h^2+k^2+l^2));      // a is the lattice constant

### Mismatch:
To calculate the mismatch, you need the substrate lattice constant and SL lattice constant
mismatch = abs((suba-SLa)/suba);   // suba is the substrate lattice constant. SLa is the SL lattice constant

### SL thickness:
to calculate the thickness, you need the wavelength of the xray (lambda), theta of the SL-0 peak, and theta of the SL-1 or SL+1 peak
thickness = abs(-lambda/(2*(sind(sl1p)-sind(sl0))));   // sind is sin() but in degrees rather than radians


## Future Development:
I want to just input the file produced by the XRD machine and have the code find the peaks, angles, and values I need.
If possible I'd also love to graph it and then label it appropriately, but I have a feeling MATLAB cant do that effectively.
I might change this to a python project, depending on how it goes. 









