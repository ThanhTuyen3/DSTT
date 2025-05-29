import numpy as np
from numpy import * 
vec1 = np.array([1., 3., 5.])
kq = vec1 * 2
print(kq)
kq = vec1 * vec1
print(kq)
vec1 /2 
print(vec1 + vec1) 
vec2 = array([2., 4., 8.]) 
kq = vec1 + vec2
print(kq) # lý do không thể cộng 2 vec khác kích thước vì vậy thêm số để bằng kích thước
vec3 = array([2., 4., 6.])
kq = vec1 + vec3
print(kq) 
kq = 2* vec1 + 5* vec3 
print(kq)
print(vec3[2]) 
vec4 = np.linspace(0, 20, 5) 
print(vec4) 
vec5 = np.zeros(5) 
print(vec5)
vec6 = np.ones(5)
print(vec6)
vec7 = np.empty(5) 
print(vec7)
vec8 = np.random.random(5)
print(vec8)

v = np.array([1., 3., 5.]) 
np.sum(v)
v.shape
v.transpose() 
v1 = v[:2]
print(v1)
v[0] = 5 
print(v)
print(v1) 
v1[:2] = [1., 2] 
print(v)
v3 = 2 * v[:2] + v1 * 3
print(v3)
v1 = [4, 6] 
print(v3)
print(v)
v + 10.0 
np.sqrt(v)
np.cos(v) 
np.sin(v)
print(np.dot(v1, v3)) 
print(v1.dot(v3))
print(v3.dot(v1))