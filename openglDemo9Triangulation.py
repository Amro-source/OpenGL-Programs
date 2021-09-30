# -*- coding: utf-8 -*-
"""
Created on Fri Jul 30 01:29:03 2021

@author: Zikantika
"""

import numpy as np
import scipy.spatial

P = np.random.uniform(-1.0, 1.0, (100,2))
P = P[scipy.spatial.ConvexHull(P).vertices]


def triangulate(vertices):
    n = len(vertices)
    segments = (np.repeat(np.arange(n+1),2)[1:-1]) % n
    T = triangle.triangulate({'vertices': vertices,
                              'segments': segments}, "p")
    return T["vertices"], T["triangles"]



def on_draw(dt):
    window.clear()
    polygon.draw(gl.GL_TRIANGLE_FAN)