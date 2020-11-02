# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 16:34:16 2020

@author: Zou Long
"""
import numpy as np
Nx = 101
Ny = 101
# 不同的x对应不同的列 
# 不同的y对应不同的行
phi = np.zeros((Nx,Ny))

for i in range(Nx):
    x = i/(Nx-1.0)*2.0 - 1.0
    for j in range(Ny):
        y = j/(Ny-1.0)*2.0 - 1.0
        # [x,y] --> theta = arctan(y/x)
        if y > 0:
            # x = 0 正轴
            if x == 0:
                theta = np.pi/2
            # 第一象限
            elif x>0:
                theta = np.arctan(y/x)
            # 第二象限
            elif x<0:
                theta = np.arctan(y/x) + np.pi
        else:
            # x = 0 负轴
            if x == 0:
                theta = np.pi*3/2
            # 第三象限
            elif x>0:
                theta = np.arctan(y/x) + 2*np.pi
            # 第四象限
            elif x<0:
                theta = np.arctan(y/x) + np.pi
        phi[j,i] = theta
import matplotlib.pyplot as plt
plt.pcolormesh(phi)
plt.colorbar()
# In[]
# Vortex light function
# Input arguments 
# L  : number of angular momentum
# Nx : number of grids of x axis
# Ny : number of grids of y axis
# lx  : box size along x axis
# ly  : box size along y axis
# Return 
# phi : shape =[Nx,Ny]
# representing the vortex phase at each grid points
def vortex_phase(L=1,Nx=501,Ny=501,,lx=2.0,ly=2.0):
    phi = np.zeros((Nx,Ny))
    for i in range(Nx):
        x = i/(Nx-1.0)*lx - lx/2.0
        for j in range(Ny):
            y = j/(Ny-1.0)*ly - ly/2.0
            # [x,y] --> theta = arctan(y/x)
            if y > 0:
                # x = 0 正轴
                if x == 0:
                    theta = np.pi/2
                # First quadrant -- 第一象限
                elif x>0:
                    theta = np.arctan(y/x)
                # Second quadrant -- 第二象限
                elif x<0:
                    theta = np.arctan(y/x) + np.pi
            else:
                # x = 0 负轴
                if x == 0:
                    theta = np.pi*3/2
                # Third quadrant -- 第三象限
                elif x>0:
                    theta = np.arctan(y/x) + 2*np.pi
                # Forth quadrant -- 第四象限
                elif x<0:
                    theta = np.arctan(y/x) + np.pi
            # Angular momentum & polar angle --> vortex phase
            if L == 1:
                phi[j,i] = theta
            else:
                phi[j,i] = np.mod(theta*L,2*np.pi)
    # Plot the vortex phase
    import matplotlib.pyplot as plt
    plt.figure()
    plt.pcolormesh(phi)
    plt.colorbar()
    plt.title('L = '+str(L))
    return phi
# Test of function
phi_2=vortex_phase(L=2)
# In[]
# Another way to get vortex phase
# Different in the definition of loop
import numpy as np
import matplotlib.pyplot as plt 


x0 = np.arange(-1,1,0.01)
y0 = np.arange(-1,1,0.01)

phase = np.zeros((x0.shape[0],y0.shape[0]))
L = 1#拓扑荷数
i = 0

for x in x0:
    j=0
    for y in y0:
        if y > 0:
            if x==0:
                theta = np.pi/2
            elif x>0:
                theta = np.arctan(y/x)
            elif x<0:
                theta = np.arctan(y/x)+np.pi
        else:
            if x==0:
                theta = np.pi*3/2
            elif x>0:
                theta = np.arctan(y/x)+2*np.pi
            elif x<0:
                theta = np.arctan(y/x)+np.pi     
        phase[j,i] = np.mod(theta*L,2*np.pi)
        j=j+1
    i=i+1

plt.figure()
plt.pcolormesh(phase)
plt.colorbar()
plt.title('L = '+str(L))
