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
# Nx : number of grids of x axis
# Ny : number of grids of y axis
# L  : number of angular momentum
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
# Test of function
phi_2=vortex_phase(L=2)
