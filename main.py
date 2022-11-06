#importing libraries
import numpy as np
import matplotlib.pyplot as plt
import cv2
from keras.models import Sequential
from keras.layers import Dense, Flatten, Conv2D, MaxPool2D, Dropout
from keras.optimizers import SGD, Adam
from keras.callbacks import ReduceLROnPlateau, EarlyStopping
from keras.utils import to_categorical
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.utils import shuffle
from sklearn.datasets import load_digits
import os
from sklearn.model_selection import train_test_split
from sklearn.utils import shuffle
from keras.models import load_model
from statistics import mean
from sympy import sympify
from time import sleep
from sympy import Symbol, sympify, factor, plot, solve, sin, Limit, Derivative, init_printing
from sympy import Integral, log
from collections import deque
from predict import predictions





if __name__ == "__main__":

    image_path=input("Enter image path")
    image = cv2.imread(image_path)
    Result = predictions(image)
    Print(Result)
