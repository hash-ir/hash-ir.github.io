---
title: "Precision and Recall: A different perspective"
comments: true
categories:
    - Blog
tags: 
    - machine-learning
    - deep-learning
    - philosophical
---
![precision-recall](https://images.unsplash.com/photo-1550985543-49bee3167284?ixlib=rb-1.2.1&auto=format&fit=crop&w=1267&q=80)

How many times did you have to remember what precision and recall actually are? You might know the formulation but agree with me, they are not very intuitive. Personally, I have see an example every time to understand them and their counter-balancing nature.

<!--more-->

Both precision and recall are widely used metrics in Machine Learning. On a quick search, this is what defines precision and recall:

> Precision (also called positive predictive value) is the fraction of relevant instances among the retrieved instances, while recall (also known as sensitivity) is the fraction of the total amount of relevant instances that were actually retrieved.

It's not as complicated as it seems from the definitions but somehow, the words *relevant* and *retrieved* make a mess. If you try to apply these metrics using their textual definitions, it might occur that you have to double check or see an example. This makes sense since both the definitions have a similar structure but our brain is wired to identify patterns to distinguish one thing from another.

I have written a dialogue which may not make our understanding better but surely provides an intuitive perspective on these metrics. Before we begin, I would like to introduce the two characters in our dialogue - *Professor* and *Student*. For the sake of simplicity, let's assume the professor and student are not from the Computer Science background. When you read through the dialogue, there are some lines which depict the metrics - precision and recall and their relative degree. It's important to read the dialogue without wondering about the depiction. Later, you can ponder and connect the lines with the metrics. With that being said, let's get started.

> A student asks the Professor what is it that he really wants. The Professor is kind enough to answer in a philosophical way, teaching the student a deeper understanding of life and something which he is unaware of (precision and recall)

"Professor, how do I know what I want?", asked a curious student.

Professor said, "You don't. You take something you come across and decide if you want it or not."

"OK. How about I take all that is offered to me?", the student inquired. *(high recall)* 

"Fine. But then you also take the things that you don't want.", the Professor explained. *(false positive, low precision)*

The student still unsure further asked, "What if I don't want anything?" *(low precision, low recall)*

Encouragingly, the Professor replied, "Highly unlikely. Everybody needs something!"

"Ummm, how about I take only a few things?", said the student being careful. *(high precision)*

"Sure, but then you are missing out on the things you really want.", the wise Professor said. *(false negative, low recall)*

The student thinking he figured out his life, replied, "OK. Then I take only the things I want." *(high precision, high recall)*

The Professor paused for a moment and then whispered, "If only you know what you really want!"

The professor, having no idea about precision and recall, made the student understand their counter-balancing nature. It is wonderful to realize the things that we formalize have already been present naturally since the start of time. This is what makes the world a beautiful place. I hope when you come across these metrics again in your life, you will *recall* this piece and apply them *precisely*.

### References
* Photo by [William Warby](https://unsplash.com/@wwarby) on [Unsplash](https://unsplash.com/)
* [Precision and recall (Wikipedia)](https://en.wikipedia.org/wiki/Precision_and_recall)