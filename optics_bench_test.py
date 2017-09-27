from vpython import *
from math import sin,cos,pi


#This iteration projects rays from a sphere projecting to the surface of a larger spheroid.



spikeball = sphere(pos = vector(0, 0, 0), radius = 0.01, color = color.white)
r = curve(pos = [vec(0,0,0), vec(0,0,0)])

r.aa = curve(pos = [vec(0,0,0),vec(1, 0, 0)], color = color.yellow) #Set of rays along each axis
r.ab = curve(pos = [vec(0,0,0),vec(-1, 0, 0)], color = color.yellow)
r.ac = curve(pos = [vec(0,0,0),vec(0, 1, 0)], color = color.yellow)
r.ad = curve(pos = [vec(0,0,0),vec(0, -1, 0)], color = color.yellow)
r.ae = curve(pos = [vec(0,0,0),vec(0, 0, 1)], color = color.yellow)
r.af = curve(pos = [vec(0,0,0),vec(0, 0, -1)], color = color.yellow)

r.ba = curve(pos = [vec(0,0,0),vec(100/141.421, 100/141.421, 0)], color = color.yellow) #Set of rays in 2D planes of two coordinate axes
r.bb = curve(pos = [vec(0,0,0),vec(-100/141.421, 100/141.421, 0)], color = color.yellow)
r.bc = curve(pos = [vec(0,0,0),vec(100/141.421, -100/141.421, 0)], color = color.yellow)
r.bd = curve(pos = [vec(0,0,0),vec(-100/141.421, -100/141.421, 0)], color = color.yellow)
r.be = curve(pos = [vec(0,0,0),vec(100/141.421, 0, 100/141.421)], color = color.yellow)
r.bf = curve(pos = [vec(0,0,0),vec(-100/141.421, 0, 100/141.421)], color = color.yellow)
r.bg = curve(pos = [vec(0,0,0),vec(100/141.421, 0, -100/141.421)], color = color.yellow)
r.bh = curve(pos = [vec(0,0,0),vec(-100/141.421, 0, -100/141.421)], color = color.yellow)
r.bi = curve(pos = [vec(0,0,0),vec(0, 100/141.421, 100/141.421)], color = color.yellow)
r.bj = curve(pos = [vec(0,0,0),vec(0, -100/141.421, 100/141.421)], color = color.yellow)
r.bk = curve(pos = [vec(0,0,0),vec(0, 100/141.421, -100/141.421)], color = color.yellow)
r.bl = curve(pos = [vec(0,0,0),vec(0, -100/141.421, -100/141.421)], color = color.yellow)

r.m = curve(pos = [vec(0,0,0), vec(100/173.205081,100/173.205081,100/173.205081)], color = color.yellow) #Set of rays along no explicit axis
r.n = curve(pos = [vec(0,0,0), vec(-100/173.205081,100/173.205081,100/173.205081)], color = color.yellow)
r.o = curve(pos = [vec(0,0,0), vec(100/173.205081,-100/173.205081,100/173.205081)], color = color.yellow)
r.p = curve(pos = [vec(0,0,0), vec(100/173.205081,100/173.205081,-100/173.205081)], color = color.yellow)
r.q = curve(pos = [vec(0,0,0), vec(-100/173.205081,-100/173.205081,100/173.205081)], color = color.yellow)
r.r = curve(pos = [vec(0,0,0), vec(-100/173.205081,-100/173.205081,-100/173.205081)], color = color.yellow)
r.s = curve(pos = [vec(0,0,0), vec(100/173.205081,-100/173.205081,-100/173.205081)], color = color.yellow)
r.t = curve(pos = [vec(0,0,0), vec(-100/173.205081,100/173.205081,-100/173.205081)], color = color.yellow)

list_of_rays=[]  # Create an empty list named 'list_of_rays'
L=1  #Define a length for the rays
for i in range(0,pi,.1):
    x=L*cos(i)
    y=L*sin(i)
    new_curve=curve(pos=[vec(0,0,0),vec(x,y,0)], color=color.red)
    list_of_rays.append(new_curve)