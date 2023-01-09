
=====================================================
Type 3 - Selection Without Repetition - Combinations
=====================================================



In this section, we present some tasks involving selection without repetition problems.
In our 2x2 grid, this is the cell in which repetition is not allowed, and we are
counting unordered outcomes (or combinations). In problems like these, we can again
employ multi-stage processes, where the number of options is reduced at each stage,
because repetition is not allowed. However, in addition, we must avoid duplicate
outcomes, as we do not want to count ordered outcomes, but rather unordered outcomes.
For instance, in counting ordered outcomes, we might count 123, 132, 213, 231, 312,
and 321 as distinct outcomes. In counting UNordered outcomes, we do not consider
those as distinct; they are all the same set {1, 2, 3}. Thus, we need to account
for duplicates when we count combinations.

There are a couple of ways in which we handle this. One way we can do this is to
leverage division and equivalence in order to "uncount" all the repeated outcomes.
This can be most easily seen in Type 2 problems - arrangements without repetition, also called permutations.

For instance, suppose we want to select, but not arrange, 3 objects from 5 objects.
That is, we want to count unordered outcomes of 3 objects chosen from 5 objects.
To do this, let us first consider arranging objects, which we know can be done
in :math:`5 \cdot 4 \cdot 3 = \frac{5!}{2!} = 60` ways.

If we look at the outcomes of this process, notice that we get outcomes like 123,
132, 312, and 321. Run the next bit of code to check that we generated ordered outcomes.

Active Code 1
--------------

.. activecode:: Type_3_CodeSample1
   :coach:
   :caption: Create some code

   Numbers = [1, 2, 3, 4, 5]
   counter = 0

   for i in Numbers:
       for j in Numbers:
           if j != i:
               for k in Numbers:
                   if k != j and k != i:
                       print(i,j,k,)
                       counter += 1
   print(counter)

In the above problem, note that for any given set of digits, such as {1, 2, 3},
there are 6 total outcomes in the list of ordered outcomes that contain these three digits.
These are, specifically, 123, 132, 213, 231, 312, and 321. It makes sense that
there are 6 such outcomes, as there are :math:`3! = 3 \cdot 2 \cdot 1 = 6` arrangements
of three distinct digits. Thus, for every set of numbers, there are 6 times as many
ordered outcomes as there are unordered outcomes. For every 6, we want to count
one outcome. Answer the following question:

Quick Check 1.1
----------------

.. mchoice:: Type_3_MC1_1
   :correct: c
   :answer_a: There are 3 outcomes that contain 2, 4, and 5.
   :answer_b: There are 5 outcomes that contain 2, 4, and 5.
   :answer_c: There are 6 outcomes that contain 2, 4, and 5.
   :feedback_a: Incorrect.
   :feedback_b: Incorrect.
   :feedback_c: Correct.

   Scroll through the outcomes above and convince yourself that this is the case.
   Consider a set like {2, 4, 5}. In the output of the code above, how many outcomes
   contain a 2, 4, and 5?

General formula for Selection without Repetition
----------------------------------------------------
In general, if we are arranging :math:`r` elements from :math:`n` distinct elements,
there will always be :math:`r!` arrangements of any given :math:`r` elements. So,
if we want to count unordered rather than ordered outcomes, there will be :math:`r!`
times more ordered outcomes than unordered outcomes. We thus have the following
general relationship for selecting :math:`r` elements from :math:`n` distinct elements:

In particular, we get that :math:`(\text{Number of unordered outcomes})\cdot (\text{Number of ways to arrange } r \text{ elements} ) = (\text{Number of ordered outcomes})`,
which we know to be the following:

:math:`(\text{Number of unordered outcomes}) \cdot r! = \frac{n!}{(n-r)!}`.

Thus, the total :math:`(\text{Number of unordered outcomes}) = \frac{n!}{(n-r)!\cdot r!}.`

This is often denoted as :math:`C(n,r)` and, more commonly as :math:`{n \choose r}`,
which is said ":math:`n` choose :math:`r`." So, :math:`{n \choose r} = \frac{n!}{(n-r)!\cdot r!}`.


For example, consider the problem below. ::

  1. Nine horses compete in a beauty competition, and there will three identical
  prizes given. How many possibilities are there for which three horses receive prizes?

If we want to select a set of three horses from a field of 9 horses to win a prize,
we can take the number of ordered outcomes (which we know to be :math:`9 \cdot 8 \cdot 7 =
\frac{9!}{6!}`) and divide it by the number of ways to arrange three horses, which
is :math:`3!`. Thus, the total number of unordered outcomes is :math:`\frac{9 \cdot 8 \cdot 7}{3!}
= \frac{9!}{6!\cdot 3!} = {9 \choose 3} = 84`.

Check your knowledge on the following problem.

.. mchoice:: QC_3_1
   :correct: b
   :answer_a: 5!/3!
   :answer_b: (5*4)/(2*1)
   :answer_c: 5!/2!
   :feedback_a: Incorrect.
   :feedback_b: Correct.
   :feedback_c: Incorrect.

   If you have five types of vegetables, what is an expression that counts the number of ways to put two types of vegetables in a stew?

Combinations as Sums of Sums
--------------------------------

There is another way to think about this kind of problem that does not involve
thinking about division and equivalence, and it lends itself well to using a
computer program. In particular, let us consider the following problem: ::

  2. Write out a list of unordered sets of two numbers from the numbers
  {1, 2, 3, 4, 5, 6}. How many are there?

If we were to list these outcomes, we could start with the number 1, and pair it with 2
through 6, yielding 12, 13, 14, 15, 16. (Note, we do not write 11, because repetition
is not allowed). Then, we could move to the number 2, and pair it with numbers.
We do not pair it with 21, because we already wrote 12, and we want unordered outcomes
(so we do not want to count both 12 and 21). We also don't want to write 22, as
repetition is not allowed. So, we write 23, 24, 25, 26. Similar, we would list 34,
35, 36, then 45, 46, and finally 56. An expression for the number of outcomes is
thus :math:`5+4+3+2+1 = 15`. This is reflected in the process of pairing 1 with any of
the 5 numbers greater than it, then pairing 2 with any of the 4 numbers greater
than it, and proceeding in that fashion.


12, 23, 34, 45, 56

13, 24, 35, 46

14, 25, 36

15, 26

16

This answer of 15 is the same value as if we had used our other process of
:math:`\frac{5!}{3!\cdot 2!} = {5 \choose 2}`.

For any unordered sequence of distinct numbers, there is only one way to write
them in increasing number. By choosing to create sequences of
numbers in increasing order, we are ensuring that we will never produce the same
outcome twice. The program below will generate exactly the
combinations we want, which are strictly increasing sequences of numbers. The use
of the if statement using :math:`j > i` ensures that the numbers in a given position will
be greater than the values in all of the previous positions, and this means that we
have strictly increasing sequences.


Reflect on the outcomes of the program below, which answers the question "How many
unordered sets of two numbers are there from the numbers {1, 2, 3, 4, 5, 6}?" Are you
convinced that the output is giving you what you want it to? Why or why not? Do you
see a structure of :math:`5+4+3+2+1` in the outcomes?

Active Code 2
--------------

.. activecode:: Type_3_CodeSample2
   :coach:
   :caption: Create some code

   Numbers = [1, 2, 3, 4, 5, 6]
   counter = 0

   for i in Numbers:
       for j in Numbers:
           if j > i:
               print(i,j)
               counter += 1
   print(counter)

Let us try to extend this idea by answering the following question: ::

  3. How many combinations of size 3 are there from the numbers {1, 2, 3, 4, 5, 6}?

Here again we can consider a process of writing down outcomes. We can start with the
number 1, and then pair it with 2, and then, since 1 and 2 have been used, we can
pair 12 with 3, 4, 5, and 6. Then, we can pair 1 with 3, and then pair 13 with 4,
5, and 6. Once we have exhausted all of the options starting with 1, we can move to 2,
and start with 23 paired with 4, 5, and 6. We can proceed in this manner, again
essentially creating 3-digit sequences that are strictly increasing.

Note that there are :math:`4+3+2+1` sets that start with 1, then :math:`3+2+1` that
start with 2, :math:`2+1` that start with 3, and :math:`1` that start with 4. Thus
the overall expression that reflects this process is :math:`(4+3+2+1)+(3+2+1)+(2+1)+(1) = 20.`

The program below executes this idea. Note again that the conditional statements
ensure the sequences will be strictly increasing. In the outcomes, we see
this expression reflected in the structure of the outcomes.

Active Code 3
--------------

.. activecode:: Type_3_CodeSample3
   :coach:
   :caption: Create some code

   Numbers = [1, 2, 3, 4, 5, 6]
   counter = 0

   for i in Numbers:
       for j in Numbers:
           if j > i:
               for k in Numbers:
                   if k > j:
                       print(i,j,k,)
                       counter += 1
   print(counter)


Check your knowledge using the problem below:

.. fillintheblank:: Type_3_6choose3
   :casei:

   I think that |blank| of the outcomes will start with "3", and |blank| of the outcomes will start with "3 4".

   -   :3: Correct.
       :x: Incorrect. The answer is 3=2+1.
   -   :1: Correct.
       :x: Incorrect. The answer is 1.

Some Practice Problems
-----------------------

::

  4. There are 20 professors in a department, and a 4-person Graduate Committee
  must be formed. How many possibilities are there for who can be on the committee?

Notice, a committee is an unordered outcome because all that matters for determining
a committee is who is on the committee - different orders or arrangements of the
committee members do not make distinct outcomes. So, we are counting 4-combinations
chosen from 20 people.

We can employ our general formula to get :math:`{20 \choose 4} = \frac{20!}{16!\cdot4!} = 4,845.`

We can check our work by running a program, as seen below.

Active Code 4
--------------

.. activecode:: Type_3_CodeSample4
   :coach:
   :caption: Create some code

   People = range(1,21)
   counter = 0

   for i in People:
       for j in People:
           if j > i:
               for k in People:
                   if k > j:
                       for l in People:
                           if l > k:
                               #print(i,j,k,l)
                               counter += 1
   print(counter)

::

  5. A Poker hand consists of a set of 5 cards from a standard 52-card deck.
  How many possible Poker hands are there?

Here we must just choose 5 cards from 52 cards, so we get :math:`{52 \choose 5} =
\frac{52!}{47!\cdot5!} = 2,598,960.`

The following code yields this same result.

Active Code 5
--------------

.. activecode:: Type_3_CodeSample5
   :coach:
   :caption: Create some code

   Cards = range(1,53)
   counter = 0

   for i in Cards:
       for j in Cards:
           if j > i:
               for k in Cards:
                   if k > j:
                       for l in Cards:
                           if l > k:
                               for m in Cards:
                                   if m > l:
                                       #print(i,j,k,l)
                                       counter += 1
   print(counter)

Many problems will not be only a direct application of this formula, but rather
they will involve or incorporate the formula in some way into a broader problem.
Here we offer some examples of how this formula might arise or be used in problems.

::

  5. I have 12 books. I want to give three of them away to my friend John, and I
  want to give six of them away to my friend Craig. How many possible outcomes are
  there for giving my books away?

This counting process has a two-stage process. Note that I can first pick 3 of
the 12 books to give to John. There are then 9 books left, and I can pick 6 of them
to give to Craig. Since the number of outcomes at each stage is independent of
previous choices, I can employ the Multiplication Principle. Thus I get that my
answer is :math:`{12 \choose 3} \cdot {9 \choose 6} = 18,480`.


::

  6. We have 6 Moms, 6 Dads, and 8 children to choose from. We need to make a
  committee of size 7, with exactly 2 Dads, 3 Moms, and 2 children. How many ways
  are there to do this?

Solve the following Parson's problem to create code that solves this problem.

.. parsonsprob:: Type_3_Parson1
    :numbered: left

    Arrange the lines below to create code to count the number of ways to make the committee specified in the problem.
    -----

    Dads = [1, 2, 3, 4, 5, 6]
    Moms = [1, 2, 3, 4, 5, 6]
    Kids = [1, 2, 3, 4, 5, 6, 7, 8]
    =====
    counter = 0
    =====
    for i in Dads:
        for j in Dads:
            if j > i:
    =====
                for k in Moms:
                    for l in Moms:
                        if l > k:
    =====
                            for m in Moms:
                                if m > l:
    =====
                                    for n in Kids:
                                        for o in Kids:
                                            if o > n:
    =====
                                                #print(i,j,k,l,m,n,o)
                                                counter += 1
    ======
    print(counter)


We can first pick 2 of the 6 Dads, then 3 of the 6 Moms, then 2 of the 8 children.
Since the number of options at each stage is independent of any particular choice,
we can employ the multiplication principle. We get an expression of
:math:`{6 \choose 2} \cdot {6 \choose 3} \cdot {8 \choose 2} = 8,400`.
