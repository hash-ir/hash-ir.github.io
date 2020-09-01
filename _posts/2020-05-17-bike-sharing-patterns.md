---
layout: post
title: "Udacity Projects Series | Part 1: Predicting Bike Sharing Patterns" 
comments: true
mathjax: true
author: Hashir Ahmad
tags: [udacity, numpy, backpropagation, regression]
---
I have had a lot of fun doing Udacity's [Deep Learning Nanodegree](https://www.udacity.com/course/deep-learning-nanodegree--nd101) and would highly recommend enrolling in it. For me, the projects were the highlight of this nanodegree. From implementing a neural network from scratch in NumPy to deploying an entire model on Amazon Web Services, the projects provided a very good understanding of the different aspects of deep learning. As suggested by the fellows at Udacity and also by the seasoned individuals, I am making a habit to document my projects and learned skills. This 5 part series justifies that purpose where I write about my implementations of the Nanodegree's projects. In the particular order, we discuss the following projects:

1. Predicting Bike Sharing Patterns
2. Dog Breed Classifier
3. Generate TV Scripts
4. Generate Faces
5. Deploying a Sentiment Analysis Model

In the first part (project), I built a neural network from scratch to carry out a prediction problem on the [Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset). This project helped in understanding the concepts of forward pass, gradient descent, backpropagation and hyperparameter tuning from the ground up. It was essentially a predictive modeling problem where a 2-layer neural network (including the output layer) is used to predict (regress) future ridership data based on the historical data. The full implementation of the project is available [here](https://github.com/hash-ir/Predicting-Bike-Sharing-Patterns). This post is just for understanding the details.

## Dataset
This dataset has the number of riders for each hour of each day from January 1, 2011 to December 31, 2012. The number of riders is split between casual and registered, summed up in the *cnt* column. You can see the first few rows of the data below.

![data](/public/images/data.PNG)

The information about the different columns of the dataset can be viewed [here](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset#). For our purpose, the target columns are *cnt*, *casual* and *registered*. The rest of the columns serve as the input features. Some of the columns have categorical values like *weathersit*, *month*, *season*, *hours* and *weekday*. We convert these into one-hot representation using Pandas' `get_dummies()` method. We delete the respective columns and also some other columns which are not useful like *instant*, *dteday*, *atemp*, *workingday*.

<script src="https://gist.github.com/hash-ir/53a768e4c5bdf3e8ac3af72945471a64.js"></script>

Since the continuous variables have different scales, we need to normalize them to make the training easier. We shift and scale the variables such that they have $0$ mean and a standard deviation of $1$. For making the predictions, we store the means and standard deviations in a dictionary to reverse the normalization.

<script src="https://gist.github.com/hash-ir/14c16db4d42960f9058eb7901dcabb66.js"></script>

Finally, we separate the data into training, validation and test sets. We'll save the data for the last approximately 21 days to use as a test set after we've trained the network. The rest of the data is divided into training and validation. Since this is time series data, we'll train on historical data, then try to predict on future data (the validation set).

## Network
Now we look into the structure of the network and how it is built to train on our dataset.

### Initialization
We create a 2-layer neural network using NumPy. Of course, the network can have more depth but this is just for the sake of creating the network from scratch. To do this, we create a class and initialize it with all the necessary information - input nodes, hidden nodes, output nodes, learning rate, weight initialization. 

The number of unique features we have after dropping the columns *instant*, *dteday*, *atemp* and *workingday* is 10. The one-hot representation separates the categorical columns *weathersit*, *month*, *season*, *hours* and *weekday* into their respective columns resulting in 56 features. This is the number of `input nodes`. The `output_nodes` is just 1 which is the number of riders. The `hidden_nodes` is a hyperparameter which usually lies between `input_nodes` and `output_nodes`.

We initialize the weights of the layers with a normal distribution. Good initialization results in efficient training. Here, we are using the fact that the output of a layer is a dot product between the input and weights (followed by activation):

$$ y_i = \sum_{j=0}^{n-1}w_{ij}x_j$$

The input has a mean of $0$ and standard deviation of $1$. If we choose the same statistics for the weight of a given node, the output of one product between input and weight $w_{ij}x_j$ would still have a mean of $0$ and standard deviation of $1$. This is helpful as further dot products in the network do not result in either vanishing or exploding products. Now the output is a sum of these products upto the number of nodes in the layer. Hence, the output will have a $0$ mean and a variance equal to the number of nodes $n$ or a standard deviation of $\sqrt{n}$. 

<script src="https://gist.github.com/hash-ir/fb794303db33cef14310ba689a842c4f.js"></script>

### Forward pass
The forward pass builds the computational graph in the following way:

1. $h^{\prime} = XW^{(1)}$
2. $h = \text{sigmoid}(h^{\prime})$
3. $o = hW^{(2)}$
4. $L = \frac{1}{N}\sum_{i=0}^{N}(y_i-o_i)^2$

where $X$ is the input, $h^{\prime}$ is the pre-activated hidden output, $h$ is the activated hidden output, $W^{(1)}$ and $W^{(2)}$ are the weights of hidden and output layer respectively, $o$ is the final output and $L$ is the mean squared error between the grount truth $y$ and output $o$ for $N$ records. There is no activation at the output layer since we want real values for the number of riders. 

<script src="https://gist.github.com/hash-ir/21072d11b1a39f14305b6116c6a6e25c.js"></script>

### Backward pass
The backward pass calculates the gradients (partial derivates) at every layer to get the error w.r.t the different weights of the network. 

<script src="https://gist.github.com/hash-ir/b9be1c98cf9f0a75cfcd9ccf51e8bd7e.js"></script>
<script src="https://gist.github.com/hash-ir/f4baf6ba61f95f9f3046d8e5dd7387dc.js"></script>
<script src="https://gist.github.com/hash-ir/e37509a7cca23a9e51d07b2719cc0c7a.js"></script>

### Hyperparameter tuning
We can tune the hyperparameters to improve the training performance. This can be done simply by changing the values and training to check the performance increase or decrease like below:

<script src="https://gist.github.com/hash-ir/2a4b106264cb6ecd8f9268217123befb.js"></script>

This can take a lot of time since we have no idea how to select the best configuration locally if we are trying out random values. Further, since these hyperparameters jointly determine the training performance, it is very hard to determine the optimal values. Instead, we use Grid Search to span over a range of values for each hyperparameter and train separately.

<script src="https://gist.github.com/hash-ir/81b773a36014409b80eade58d0e236fe.js"></script>








