
# coding: utf-8

# In[108]:


import numpy as np
import matplotlib.pyplot as plt
from scipy import misc


# In[ ]:


# image = misc.imread('x.png')


# In[120]:


class FullCon(object):
    pass
    
    def softmax(target, target_array):
        numerator = np.exp(target)
        denominator = sum(np.exp(target_array))

        prob = numerator / denominator
        return prob


# In[122]:


class Pooling(object):
    
    def __init__(self, input_arr, filter_size, stride):
        self.input_arr = input_arr
        self.filter_size = filter_size
        self.stride = stride
        
    def max_pool(input_arr, filter_size, stride=1):
        # height == width for square
        h, h, c = input_arr.shape
        pool_height = int((h - filter_size) / stride + 1)
        pool_array = np.zeros((pool_height, pool_height, c))
        i = j = 0
        while i + filter_size <= h:
            while j + filter_size <= h:
                region = return_patch(input_arr, filter_size, i, j)
                pool_array[i, j] = np.max(region)
                j += stride

            j = 0
            i += stride

        return pool_array
    
    def avg_pool(input_arr, filter_size, stride=1):
        # height == width for square
        h, h, c = input_arr.shape
        pool_height = int((h - filter_size) / stride + 1)
        pool_array = np.zeros((pool_height, pool_height, c))
        i = j = 0
        while i + filter_size <= h:
            while j + filter_size <= h:
                region = return_patch(input_arr, filter_size, i, j)
                pool_array[i, j] = np.average(region)
                j += stride

            j = 0
            i += stride

        return pool_array  


# In[121]:


class Dropout(object):
    def __init__(self, size, prob):
        self.size = size
        self.prob = prob
    
    def dropout(size, prob):
        return np.random.binomial(1, prob, size=size)


# In[116]:


#trial_input
a = np.resize(np.eye(3, 3), (3, 3, 1))
b = np.ones((2, 2, 1))


# In[62]:


#input_arr -- 3d, filter_arr -- 3d, stride -- 1d, num_filters = 1d
#output_shape = (num_filters, num_products, num_products, num_channels)


# In[118]:


class Conv2(object):
    def __init__(self, input_arr, filter_arr, num_filters, strides, weights, biases, is_dropout):
        self.input_arr = input_arr
        self.filter_arr = filter_arr
        self.num_filters = num_filters
        self.strides = strides
        self.weights = weights
        self.biases = biases
        self.is_dropout = is_dropout
        
    def return_patch(input_arr, dim, row, col):
        patch = input_arr[row: row + dim , col: col + dim]
        return patch
        
    def convolve(input_arr, filter_arr, num_filters, strides=1):
        output_height = int(((input_arr.shape[0] - filter_arr.shape[0]) / strides + 1 ))
        output = np.zeros((num_filters, output_height, output_height, input_arr.shape[2]))
        
        i = j = 0
        filter_num = 1ss
        filter_size = filter_arr.shape[0]
        h = input_arr.shape[0]
        biases = np.zeros(num_filters)

        while filter_num <= num_filters:
            while i + filter_size <= h:
                while j + filter_size <= h:
                    region = return_patch(input_arr, filter_size, i, j)
                    #print(region, filter_arr)
                    output[filter_num - 1, i, j] = np.sum(np.multiply(region, filter_arr)) + biases[num_filters - 1]
                    #print(output[filter_num - 1, i, j])
                    j += strides

                j = 0
                i += strides

            filter_num += 1

        return output
    
    def relu(x):
        return max(0, x)

        
    
    

