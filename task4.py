# -*- coding: utf-8 -*-
"""
Created on Wed Jan 20 11:17:58 2021

@author: amina
"""


import numpy as np
import copy
import cv2
import matplotlib.pyplot as plt

class Forest:
    def __init__(self, height, width, prob_deer_init, prob_fox_init, k, p1, p2, p3, num_runs, fps):
        self.height = height
        self.width = width
        self.k = k
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.num_runs = num_runs
        self.fps = fps

        self.empty = 2
        self.prey = 1
        self.predator = 0
        self.cell_types = [self.empty, self.prey, self.predator]

        self.data = np.random.choice(self.cell_types,
                                     (height, width),
                                     p=[1 - prob_fox_init - prob_deer_init, prob_deer_init, prob_fox_init])

        self.num_foxes = [np.count_nonzero(self.data == self.predator)]
        self.num_deers = [np.count_nonzero(self.data == self.prey)]

    def find_neighbours(self, row_number, column_number):
        neighbours = set()
        for i in range(row_number - 1 - self.k + 1, row_number + self.k + 1):
            for j in range(column_number - 1 - self.k + 1, column_number + self.k + 1):
                if 0 <= i < len(self.data) and 0 <= j < len(self.data[0]):
                    neighbours.add((self.data[i][j], (i, j)))
        neighbours.remove((self.data[row_number][column_number], (row_number, column_number)))
        return neighbours

    def get_random_neighbouring_cell(self, row_number, column_number):
        neighbours = list(self.find_neighbours(row_number, column_number))
        return neighbours[np.random.randint(0, len(neighbours))]

    def update_forest_cell(self, row_number, column_number):
        updated_forest = copy.deepcopy(self.data)

        if updated_forest[row_number][column_number] == self.empty:
            neighbouring_cell = self.get_random_neighbouring_cell(row_number, column_number)
            if neighbouring_cell[0] == self.prey:
                if np.random.random() < self.p1:
                    updated_forest[row_number][column_number] = self.prey
                    self.num_deers[-1] += 1

        elif self.data[row_number][column_number] == self.prey:
            neighbouring_cell = self.get_random_neighbouring_cell(row_number, column_number)
            if neighbouring_cell[0] == self.predator:
                if np.random.random() < self.p2:
                    updated_forest[row_number][column_number] = self.predator
                    self.num_deers[-1] -= 1
                    self.num_foxes[-1] += 1

        elif updated_forest[row_number][column_number] == self.predator:
            if np.random.random() < self.p3:
                updated_forest[row_number][column_number] = self.empty
                self.num_foxes[-1] -= 1

        return updated_forest

    def update_forest(self):
        updated_forest = copy.deepcopy(self.data)
        self.num_foxes.append(self.num_foxes[-1])
        self.num_deers.append(self.num_deers[-1])
        for i in range(self.height):
            for j in range(self.width):
                updated_forest[i][j] = self.update_forest_cell(i, j)[i][j]

        self.data = updated_forest

    def run(self):
        cv2.namedWindow("Visualization", cv2.WINDOW_NORMAL)
        cv2.resizeWindow("Visualization", self.width * 10, self.height * 10)
        vis = cv2.applyColorMap(np.array(self.data * 127, dtype=np.uint8), cv2.COLORMAP_HOT)
        cv2.imshow("Visualization", vis)
        cv2.waitKey(0)
        for run in range(self.num_runs):
            self.update_forest()
            vis = cv2.applyColorMap(np.array(self.data * 127, dtype=np.uint8), cv2.COLORMAP_HOT)
            cv2.imshow("Visualization", vis)
            cv2.waitKey(int(1000/self.fps))

    def plot(self):
        plt.figure(figsize=(12, 9))
        plt.plot(list(range(self.num_runs + 1)), self.num_foxes, label="foxes")
        plt.plot(list(range(self.num_runs + 1)), self.num_deers, label="deers")
        plt.legend()
        plt.title("height={},width={}".format(self.height,self.width))
        plt.show()


h = np.array([1,2,4,5,10,20,25,50,100])
w = np.array([100,50,25,20,10,5,4,2,1])


if __name__ == '__main__':
    for i in range(len(h)):
        np.random.seed(1)
        forest = Forest(height=h[i], width=w[i],
                                prob_fox_init=0.1, prob_deer_init=0.4,
                                k=5, p1=0.2, p2=0.5, p3=5e-9,
                                num_runs=20, fps=1000)
        forest.run()
        forest.plot()
    
  
            
            

