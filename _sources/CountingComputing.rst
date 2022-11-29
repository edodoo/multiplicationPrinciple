======================================================
An Introduction to Counting via Computing
======================================================

In this introductory essay, we highlight some of the motivation behind solving
counting problems in a computational environment.

While we acknowledge that students can solve counting problems without using the
computer, we have several reasons for leveraging the computer in this way.

The importance of connecting counting processes and sets of outcomes
----------------------------------------------------------------------

As an example, we consider the following problem: Suppose we have the set of Shirts
= ['tee', 'polo', 'sweater'], and a set of Pants = ['jeans','khakis']. How many
Shirt-Pants outfits can we make?

The code below reflects a particular process by which we can generate shirt-pant
outfits. In particular, by using nested for loops, we first hold a shirt constant
and then cycle through the options for pants; then, we move to the next shirt, hold
it constant, and cycle through the pants for that shirt. We continue in this way
until we have exhausted all of our shirts. This is reflective of what is known as
an `odometer` strategy (English, 1991), as the process is reminiscent of how an
automobile odometer keeps track of mileage.

When we run the code below, we can see that we do in fact generate a set of outcomes
that are organized as we described.

.. countingsheet:: Outfits01a
    :ncols: 2
    :col1: tee,polo,sweater
    :col2: jeans


To see the importance of connecting counting processes and sets of outcomes, we
can consider a slightly different question. What if, now, we wanted to change the
code in the previous example to print pants-shirts outfits instead?

One student suggests that we can simply swap the first and second columns  - shorthanded as col1 and col2.
Run the program below, and now note the different ways in which the six outcomes are organized.

.. countingsheet:: Outfits01b
    :ncols: 2
    :col1: jeans
    :col2: tee,polo,sweater

The different computer programs help us see what different counting process might
entail.


Example 2:

As a more complicated example, we can consider the following problem: Suppose we
flip a coin 6 times in a row. How many possible outcomes are there?


.. countingsheet:: Outfits02
    :ncols: 6
    :col1: heads,tails
    :col2: =data1
    :col3: =data1
    :col4: =data1
    :col5: =data1
    :col6: =data1


What is the answer? Why do we get this as an answer?


Affording prediction and reflection:
=====================================




Let's begin by solving the following problems.

.. mchoice:: Trial_x
    :correct: b
    :answer_a: 3
    :answer_b: 7
    :answer_c: 4
    :feedback_a: Incorrect
    :feedback_b: Correct
    :feedback_c: Incorrect

    You own three red cars, four blue cars, and no cars of other colors. How many cars do you own?
