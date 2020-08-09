---
layout: post
title: Model deployment using Amazon SageMaker | Part 1
comments: true
author: Hashir Ahmad
---

Model deployment is an essential skill that every Machine Learning enthusiast should have in his bucket. We train and test deep learning models all the time. The predictions or the final result, however, are limited to the Jupyter Notebooks or the IDEs that we use. It's not much helpful to show someone the real values or the predicted classes. And definitely not helpful to let someone try out your fancy neural network, especially when they don't know anything about it. In such scenarios, it is better to abstract away the model and provide an easy to use interface to communicate with the model. This is known as model deployment. It is surprising to see that many people know about building, training and evaluating deep learning models but have little to no idea about deploying these models.  


In this four part series, we will look into the steps involved in deploying a model using Amazon Web Services (AWS). I have divided the full content into separate parts: 

* **Part 1: Machine Learning workflow and Amazon SageMaker**
* **Part 2: How to use Jupyter Notebooks in SageMaker and Amazon S3 buckets for storage?**
* **Part 3: Training, Validation, Hyperparamter tuning and Updating a model**
* **Part 4: Deployment using Amazon Lambda and API Gateway**

If you have some prior knowledge about AWS, feel free to skip to the later parts. Without further ado, let's get right into the first part.

 


