#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/2 13:50
# @Author  : jianqiugao
# @File    : ceshi.py
# @email: 985040320@qq.com
from fipy import CellVariable, Grid2D, Viewer, TransientTerm, DiffusionTerm,ConvectionTerm,FaceVariable
import numpy as np

nx = 200
ny = nx
dx = 1./nx
dy = dx
L = dx * nx

mesh = Grid2D(dx=dx, dy=dy, nx=nx, ny=ny)

phi = CellVariable(name = "level set ",
                   mesh = mesh,
                   value = 0.,hasOld = 1
                   ) # 定义水平集变量
D = 0
X, Y = mesh.cellCenters
# 定义初始水平集
xo = 0.3
yo = 0.5
R = 0.2

inner = ((X-xo)**2+(Y-yo)**2 < R**2)
outer = ((X-xo)**2+(Y-yo)**2 > R**2)
# 设定初始值
phi.value[inner] = -1
phi.value[outer] = 1

# 设置固定的边界
# phi.constrain(-1, inner)
# phi.constrain(1, outer)  # 设置水平集的初始条件

# 定义
X, Y = mesh.faceCenters  # 拿到网格面，用于设置面上的速度
ux = (np.sin(np.pi*X)**2)*np.sin(2*np.pi*Y)
uy = -(np.sin(np.pi*Y)**2)*np.sin(2*np.pi*X)

velocity = FaceVariable(mesh=mesh, rank=1)  # 定义面上的速度
velocity[0] = ux
velocity[1] = uy
advEqn = TransientTerm() + ConvectionTerm(velocity) #== DiffusionTerm(coeff=D) #

if __name__ == '__main__':
    viewer = Viewer(vars=phi,
                    xmin=0., xmax=1., ymin=0., ymax=1., colorbar='vertical', scale=20,datamin=-2, datamax=2)
    timeStepDuration = 0.02
    steps = 50
    for step in range(steps):
        phi.updateOld()
        advEqn.solve(var=phi,dt=timeStepDuration)
        if __name__ == '__main__':
            viewer.plot()