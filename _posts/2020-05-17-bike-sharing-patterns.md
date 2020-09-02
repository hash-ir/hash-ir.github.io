---
layout: post
title: "Udacity Projects Series | Part 1: Predicting Bike Sharing Patterns" 
comments: true
mathjax: true
author: Hashir Ahmad
tags: [udacity, numpy, backpropagation, regression]
---
I have had a lot of fun doing Udacity's [Deep Learning Nanodegree](https://www.udacity.com/course/deep-learning-nanodegree--nd101) and would highly recommend enrolling in it. For me, the projects were the highlight of this nanodegree. From implementing a neural network from scratch in NumPy to deploying an entire model on Amazon Web Services, the projects provided a very good understanding of the different aspects of deep learning. As suggested by the fellows at Udacity and also by the seasoned individuals, I am making a habit to document my projects and learned skills. This 5 part series justifies that purpose where I write about my implementations of the projects. In the particular order, we discuss the following projects:

1. Predicting Bike Sharing Patterns
2. Dog Breed Classifier
3. Generate TV Scripts
4. Generate Faces
5. Deploying a Sentiment Analysis Model

In the first part (project), I built a neural network from scratch to carry out a prediction problem on the [Bike Sharing Dataset](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset). This project helped in understanding the concepts of forward pass, gradient descent, backpropagation and hyperparameter tuning from the ground up. It was essentially a predictive modeling problem where a 2-layer neural network (including the output layer) is used to predict (regress) future ridership data based on the historical data. The full implementation of the project is available [here](https://github.com/hash-ir/Predicting-Bike-Sharing-Patterns). This post is just for understanding the details.

## Dataset
This dataset has the number of riders for each hour of each day from January 1, 2011 to December 31, 2012. The number of riders is split between casual and registered, summed up in the *cnt* column. You can see the first few rows of the data below.

![data](/public/images/data.PNG)

The information about the different columns of the dataset can be viewed [here](https://archive.ics.uci.edu/ml/datasets/Bike+Sharing+Dataset#). For our purpose, the target columns are *cnt*, *casual* and *registered*. The rest of the columns serve as the input features. Some of the columns have categorical values like *weathersit*, *mnth*, *season*, *hr* and *weekday*. We convert these into one-hot representation using Pandas' `get_dummies()` method. We delete the respective columns and also some other columns which are not useful like *instant*, *dteday*, *atemp* and *workingday*.

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

The input has a mean of $0$ and standard deviation of $1$. If we choose the same statistics for the weight of a given node, the output of one product between input and weight $w_{ij}x_j$ would still have a mean of $0$ and standard deviation of $1$. This is helpful as further dot products in the network do not result in either vanishing or exploding products. Now the output is a sum of these products upto the number of nodes in the layer. Hence, the output will have a $0$ mean and a variance equal to the number of nodes $n$ or a standard deviation of $\sqrt{n}$. Hence, we initialize the weights with a normal distribution $\mathcal{N}(\mathbf{0},\sqrt{n}\mathbf{I})$

<script src="https://gist.github.com/hash-ir/fb794303db33cef14310ba689a842c4f.js"></script>

### Forward pass
The forward pass builds the computational graph in the following way:

1. $h^{\prime} = XW^{(1)}$
2. $h = \sigma(h^{\prime})$
3. $o = hW^{(2)}$
4. $L = \frac{1}{N}\sum_{i=0}^{N}(y_i-o_i)^2 = (Y - o)^T(Y - o)$

where $X$ is the input, $h^{\prime}$ is the pre-activated hidden output, $h$ is the activated hidden output, $W^{(1)}$ and $W^{(2)}$ are the weights of hidden and output layer respectively, $o$ is the final output and $L$ is the mean squared error between the grount truth $y$ and output $o$ for $N$ records. There is no activation at the output layer since we want real values for the number of riders. 

<script src="https://gist.github.com/hash-ir/21072d11b1a39f14305b6116c6a6e25c.js"></script>

### Backward pass
The backward pass calculates the gradients (partial derivates) at each layer to get the error w.r.t the different weights of the network. You might already know or have heard about the famous backpropagation algorithm. Here, we are going to see it in action. 

For smaller networks like ours, it is always suggested to work out the math in backpropagation on a piece of paper. It helps to understand how the information is flowing inside the network. Specifically, for this project, it was an essential part to implement it correctly. 

Before we dive in, there are two techniques by which you can calculate the gradients. There might be other techniques or algorithms but I am familiar with these two. The first is basically to compute the gradient using the product of partial derivatives (chain-rule). For example, with a compute graph like below:

$$ c = a + b $$

$$ d = c^2 $$

$$ e = d * f $$

the gradients $\frac{\partial e}{\partial a}$, $\frac{\partial e}{\partial b}$ and $\frac{\partial e}{\partial f}$ can be written as:

$$ \frac{\partial e}{\partial a} = \frac{\partial e}{\partial d} * \frac{\partial d}{\partial c} * \frac{\partial c}{\partial a} = f * 2c * 1$$

$$ \frac{\partial e}{\partial b} = \frac{\partial e}{\partial d} * \frac{\partial d}{\partial c} * \frac{\partial c}{\partial b} = f * 2c * 1$$

$$ \frac{\partial e}{\partial f} = \frac{\partial e}{\partial f} * \frac{\partial f}{\partial f} = d * 1$$

This has no symbolic meaning with the network and you just need the chain-rule to get the particular gradient. However, neural networks usually have similar operations repeated in multiple layers. Each layer is characterized by matrix multiplications and an activation. It is, therefore, helpful to utilize this structure. From the Udacity Nanodegree:
> Since the output of a layer is determined by the weights between layers, the error resulting from units is scaled by the weights going forward through the network. Since we know the error at the output, we can use the weights to work backwards to hidden layers.

The error at the output is simply the gradient of the loss $L$ w.r.t the output $o$. Similarly, the hidden error is the gradient of $L$ w.r.t $h$. The general algorithm used here is as follows:
1. Calculate the error in the output unit, $\delta^o = (y - y^{\prime})f^{\prime}(z)$ where $y^{\prime}$ is the output, $f^{\prime}(z)$ is the gradient of the activation function and $z = \sum_jW_ja_j$ is the input to the output unit (pre-activated hidden output).
2. Propagate the error to each hidden unit, $\delta^h_{j} = \delta^oW_jf^{\prime}(h_j)$ where $W_j$ is the weight between the output layer $j$ and the input layer $j-1$.

Now, let's use these steps to compute the gradients of our network. Using the notation in the forward pass, from step 1, we have:

$$\delta^o = (Y - o)\frac{\partial{f(o)}}{\partial o} = (Y - o)\frac{\partial o}{\partial o} = (Y - o)$$

since there is no (or identity) activation at the output.

Since we have only one hidden layer, we denote its error term by $\delta^h$. From step 2, we have:

$$
\delta^h = \delta^oW^{(2)}f^{\prime}(h^{\prime}) = (Y - o)W^{(2)}\sigma(h^{\prime})(1 - \sigma(h^{\prime})) 
$$

$$\delta^h = (Y - o)W^{(2)}h(1-h)$$



<script src="https://gist.github.com/hash-ir/b9be1c98cf9f0a75cfcd9ccf51e8bd7e.js"></script>

### Update weights
After calculating the error terms at the output and hidden units, we can compute the gradients w.r.t weights and update these weights. The gradients are simply the error terms scaled by the input of the corresponding layer:

$$\nabla_{W^{(1)}}{L} = \frac{\partial L}{\partial{W^{(1)}}} = \delta^h\frac{\partial{h^{\prime}}}{\partial{W^{(1)}}} = \delta^hX$$

$$\nabla_{W^{(2)}}{L} = \frac{\partial L}{\partial{W^{(2)}}} = \delta^o\frac{\partial o}{\partial{W^{(2)}}} = \delta^oh$$

Now that we have the gradients, we can update the weights using the update step ($\eta$ is the learning rate):

$$W^{(1)} = W^{(1)} + \eta \cdot \frac{\nabla_{W^{(1)}}{L}} {N}$$

$$W^{(2)} = W^{(2)} + \eta \cdot \frac{\nabla_{W^{(2)}}{L}} {N}$$

There are two things to note here. The first is there is a $+$ instead of $-$. This is still the gradient descent because the negative sign is accomodated in the output error term $\delta^o$. Secondly, the loss is a mean over the records. This is why the gradient is downscaled by the factor $N$. In the case of batch training, $N$ is replaced by $m$ (batchsize).  

<script src="https://gist.github.com/hash-ir/f4baf6ba61f95f9f3046d8e5dd7387dc.js"></script>

### Training
We have all the pieces of the puzzle and now it's time to put everything together. We divide the training data into batches, do the forward pass, backpropagate to get the gradients and update the weights. 

<script src="https://gist.github.com/hash-ir/e37509a7cca23a9e51d07b2719cc0c7a.js"></script>

### Hyperparameter tuning
We can tune the hyperparameters to improve the training performance. This can be done simply by changing the values and training to check the performance increase or decrease like below:

<script src="https://gist.github.com/hash-ir/2a4b106264cb6ecd8f9268217123befb.js"></script>

This can take a lot of time since we have no idea how to select the best configuration locally if we are trying out random values. Further, since these hyperparameters jointly determine the training performance, it is very hard to determine the optimal values. Instead, we use Grid Search to span over a range of values for each hyperparameter and train separately.

<script src="https://gist.github.com/hash-ir/81b773a36014409b80eade58d0e236fe.js"></script>








