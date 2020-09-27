# -*- coding: utf-8 -*-
"""
Created on Sun Sep 27 13:36:38 2020

@author: spand
"""

import numpy as np
import matplotlib.pyplot as plt

P = 100
Ao = 10
L = 100
E = 200000

#lets create a class which stores the numbered position of spring and in general total number of springs in the system
class Spring:
    def __init__(self, area_no, tot_num_of_springs):
        self.no = area_no
        self.tot = tot_num_of_springs
        #area_no is that numbered partition and tot_num_of_springs is the number of partitions made of bar
        
    def area(self):
        return 3*Ao - 2*Ao*(self.no + 0.5)/self.tot
    
    def stiffness(self):
        return (E*self.area()*self.tot)/L
    

       
def solution(n):
    #n is the number of springs(i.e elements)
    number_of_nodes = n+1 #only in this case of springs(in series) not for general questions
    stiffness_matrix = np.zeros((number_of_nodes, number_of_nodes))
    force = np.zeros(number_of_nodes)
    force[-1] = P
    #note we are keeping force[0] i.e. reaction force at hinge(R1) to be zero but that is not true. We have not calculated it
    #nor we do need to calculate it as displacement can be found out with the help of other equations of matrix
    #we will leave it as it is as we are not actually using it
    for i in range(n):
        ith_spring = Spring(i,n)
        stiffness_matrix[i][i] += ith_spring.stiffness()
        stiffness_matrix[i+1][i+1]+= ith_spring.stiffness()
        stiffness_matrix[i][i+1]-= ith_spring.stiffness()
        stiffness_matrix[i+1][i]-= ith_spring.stiffness()
              
    x = np.linalg.solve(stiffness_matrix[1:,1:], force[1:]) #I sliced the matrix i.e removed complete 1st row and 1st column as they were of
    #no need as R1 was unknown and u1 is zero(hinged)
    #x here is the solution of u2,u3,u4 till un
    return x[-1]  #last un term which we need to find
        
array = [2,4,6,8,10]
disp_for_array=[solution(g) for g in array]
print(disp_for_array)  #answer to c and the plot is answer to d

num = np.linspace(1,100,100,dtype=int) #for n=1 to n=100
sol = np.array([solution(i) for i in num])
plt.plot(num,sol)