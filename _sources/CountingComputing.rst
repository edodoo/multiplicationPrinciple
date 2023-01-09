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

.. activecode:: Outfits1a
    :coach:

    Shirts = ['tee', 'polo', 'sweater']
    Pants = ['jeans', 'khakis']
    counter=0

    for i in Shirts:
        for j in Pants:
            print(i,j)
            counter+=1
    print(counter)

To see the importance of connecting counting processes and sets of outcomes, we
can consider a slightly different question. What if, now, we wanted to change the
code in the previous example to print pants-shirts outfits instead?

Suppose that two students had two different ideas for how to solve this problem.
One student suggests that we can simply change the i and the j in the print statement,
yielding the following code in lines ? to ?.

On the other hand, another student suggests that we can instead switch the order of
the loops, making first a Pants loop followed by a Shirts loop. This is seen in the
following code in lines ? to ?.

Both of these answers are correct, in the sense that they do print pant-shirt outfits.
And, they both give the total of 6. However, the two programs produce differently-
ordered lists of outcomes.
Run the program below, and now the different ways in which the six outcomes are organized.

.. activecode:: Outfits1b
    :coach:

    Shirts = ['tee', 'polo', 'sweater']
    Pants = ['jeans', 'khakis']
    counter = 0

    for i in Shirts:
        for j in Pants:
            print(j,i)
            counter+=1
    print(counter)

    Shirts = ['tee', 'polo', 'sweater']
    Pants = ['jeans', 'khakis']
    counter = 0

    for i in Pants:
        for j in Shirts:
            print(i,j)
            counter+=1
    print(counter)

The different computer programs help us see what different counting process might
entail.


Example 2:

As a more complicated example, we can consider the following problem: Suppose we
flip a coin 6 times in a row. How many possible outcomes are there?


.. activecode:: CoinFlips
    :coach:

    Coins = ['H','T']
    counter = 0

    for i in Coins:
        for j in Coins:
            for k in Coins:
                for l in Coins:
                    for m in Coins:
                        for n in Coins:
                            print(i,j,k,l,m,n)
                            counter += 1
    print(counter)

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
