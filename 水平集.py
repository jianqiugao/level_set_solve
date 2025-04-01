#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2025/4/1 16:35
# @Author  : jianqiugao
# @File    : 水平集.py
# @email: 985040320@qq.com
import numpy as np
import matplotlib.pyplot as plt
x_num = 350
y_num = 350
x = np.linspace(0,1,x_num)
y = np.linspace(0,1,y_num)
mesh_x, mesh_y = np.meshgrid(x,y)
mesh = np.concatenate([mesh_x[:,:,np.newaxis],mesh_y[:,:,np.newaxis]],axis=-1)
sdf = np.zeros(mesh.reshape(-1,2).shape[0])
xo = 0.7
yo = 0.5
R = 0.2
cond = (np.sqrt(np.power(mesh[:,:,0]-xo,2)+np.power(mesh[:,:,1]-yo,2))-R).reshape(-1)

sdf[np.where(cond<0)] = -1
sdf[np.where(cond>0)] = 1

sdf = sdf.reshape(x_num,y_num)

ux = (np.sin(np.pi*mesh_x)**2)*np.sin(2*np.pi*mesh_y)
uy = -(np.sin(np.pi*mesh_y)**2)*np.sin(2*np.pi*mesh_x)

plt.streamplot(mesh_x,mesh_y,ux,uy)

# plt.contourf(mesh_x,mesh_y,sdf)
plt.show()

