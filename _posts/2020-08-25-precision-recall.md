---
layout: post
title: "Precision and Recall: A different perspective"
comments: true
author: Hashir Ahmad
tags: [machine-learning, deep-learning, philosophical]
---
How many times did you have to remember what precision and recall actually are? You might remember the expressions for their calculation but you don't find them very intuitive. At least I don't. I have to look up and see the examples to understand the relevance of each and their counter-balancing nature.

Both precision and recall are widely used metrics in Machine Learning. Let's look at the wikipedia definitions of each:

> Precision (also called positive predictive value) is the fraction of relevant instances among the retrieved instances, while recall (also known as sensitivity) is the fraction of the total amount of relevant instances that were actually retrieved.

It's not too complicated to understand but somehow, the words *relevant* and *retrieved* make a mess and mix the definitions when you try to remember them. It is bound to happen since both the sentences have a similar structure but our mind loves to identify patterns in order to distinguish one thing from another.

I have written a piece which might not make our understanding better but surely provide a lasting memory for these metrics. Before we begin, I would like to introduce the two characters in our story - *Professor* and *Student*. For the sake of simplicity, let's assume the professor and student do not have the Computer Science background. . I have enclosed in brackets the term which is being referred to in the dialogue. With that being said, let's get started:

> A student asks the Professor what is it that he really wants. The Professor is kind enough to answer in a philosophical way, teaching the student a deeper understanding of life and something which he is unaware of (precision and recall)

Student: Professor, how do I know what I want?

Professor: You don't. You take something and decide if you wanted it or not.

Student: OK. How about I take all that is offered? (high recall)

Professor: But then you also get the things that you don't want? (false positive, low precision)

Student: What if I don't want anything? (low precision, low recall)

Professor: Highly unlikely. Everybody needs something!

Student: Ummm, how about I take only a few things? (high precision)

Professor: Sure, but then you are missing out on the things you really want (false negative, low recall)

Student: OK. Then I take only the things I want. (high precision, high recall)

Professor: If only you know what you really want!

The professor made the student understand precision and recall without himself knowing anything about it. This is what makes the world a beautiful place. All the things that we discover and give fancy titles to have already been present naturally. I hope when you come across these metrics again in your life, you will recall this short story and it will all be natural to understand them precisely.

### References
* [Precision and recall (Wikipedia)](https://en.wikipedia.org/wiki/Precision_and_recall)