
=========================================
Type 1 - Arrangement with Repetition
=========================================



In this section, we present some tasks involving arrangement with repetition
problems. In our 2x2 grid, this is the cell in which unrestricted repetition
is allowed, and we are counting ordered outcomes (or arrangements). In problems
like these, we can employ multi-stage processes, where we have the same number
of options at each stage because repetition is allowed.

For instance, consider the following problem: ::

  1. "How many length 5 binary strings are there?"

Here, we have five positions, and we can employ a five-stage process where we
consider the number of options at each position. Since there are 2 options
(0 or 1) at each position no matter the choice of any previous position, we
use the multiplication principle to yield :math:`2 \cdot 2 \cdot 2 \cdot 2 \cdot 2 = 2^5 = 32` total
outcomes.

Below is some code that generates all of the outcomes. Notice the nature of the
outcomes themselves - repetition is allowed (something like 0 0 0 0 0 is a valid
outcome), and we are counting ordered outcomes (outcomes like 1 0 0 0 0 and 0 0 0 0 1 are
listed as distinct outcomes).

Active Code 1
-------------

.. activecode:: Type_1_CodeSample1
   :coach:
   :caption: Code that generates length 5 binary strings

   Digits = [0,1]
   counter = 0
   for i in Digits:
       for j in Digits:
           for k in Digits:
               for l in Digits:
                   for m in Digits:
                       print(i,j,k,l,m)
                       counter += 1
   print(counter)

Now, answer the following questions about these outcomes You can use this analysis tool to answer them.

.. analysistool:: type1Analysis

Quick Check 1.1
----------------

.. mchoice:: QC1_1
   :correct: c
   :answer_a: 16 outcomes start with 01
   :answer_b: 4 outcomes start with 01
   :answer_c: 8 outcomes start with 01
   :feedback_a: Incorrect.
   :feedback_b: Incorrect.
   :feedback_c: Correct. 8 outcomes start with 01, as there are 8 possible outcomes for the remaining three positions once 0 and 1 are in the first positions.

   How many outcomes start with 01?

Quick Check 1.2
----------------

.. mchoice:: QC1_2
   :correct: b
   :answer_a: 10101
   :answer_b: 10110
   :answer_c: 11111
   :answer_d: 10111
   :feedback_a: Incorrect. 10101 is the 22nd outcome in the list.
   :feedback_b: Correct. 10110 is the 23rd outcome in the list.
   :feedback_c: Incorrect. 11111 is the 32nd outcome in the list.
   :feedback_d: Incorrect. 10111 is the 24th outcome in the list.

   Following the process that the code represents, what is the 23rd outcome
   in the list?


Let's look at a couple more examples. ::

  2. There are 12 people competing for three different prizes. The same person
  can win multiple prizes, but ties are not allowed. How many possible outcomes are
  there for how the 3 prizes can be distributed to the 12 people?

Note we can think of a three-stage process, where we give out a first,
second, and third prize. For each stage, any of the 12 people can win, no
matter who was picked previously. Thus, there are 12 choices for each of the
three prizes, so our answer is :math:`12 \cdot 12 \cdot 12 = 12^3 = 1728`.

Solve the Parson's problem below to create code that produces all the outcomes for
this problem.


.. parsonsprob:: Type_1_Parson1
    :numbered: left

    Arrange the lines below to create code to print all the possible outcomes for distributing 3 prizes to 12 people.
    -----

    People = ['A','B','C','D','E','F','G','H','I','J','K','L']
    =====
    counter = 0
    =====
    for i in People:
    =====
        for j in People:
    =====
            for k in People:
    =====
                print(i,j,k)
                counter += 1
    =====
    print(counter)

Now answer the following questions about this code.

Quick Check 2.1
----------------

.. mchoice:: QC1_3
   :correct: b
   :answer_a: Person A and Person G do not receive prizes
   :answer_b: Person A receives the first prize and the third prize, and Person G receives the second prize
   :answer_c: Person A receives the first prize, and Person G receives the second and third prizes
   :feedback_a: Incorrect.
   :feedback_b: Correct. The each term in the output shows who received each respective prize. Because people can receive multiple prizes, here A won two prizes (first and third) and G won the second prize.
   :feedback_c: Incorrect.

   What does the outcome AGA represent in the context of the problem?

Now, let's consider the following problem: ::

  3. I am going to roll a 6-sided dice four consecutive times. How many
  possible outcomes are there for that sequence of four rolls?

Quick Check 3.1
----------------

.. mchoice:: QC1_4
   :correct: d
   :answer_a: 4
   :answer_b: 24
   :answer_c: 10
   :answer_d: 6
   :feedback_a: Incorrect. We are rolling four times, but there are 6 options for what can occur on each roll.
   :feedback_b: Incorrect.
   :feedback_c: Incorrect.
   :feedback_d: Correct. There are 6 options for what will come up on a given roll, one for each face of the dice.

   If you were to write code to produce outcomes, how many elements would you
   have in your starting list?

Quick Check 3.2
----------------

.. mchoice:: QC1_5
   :correct: b
   :answer_a: 6
   :answer_b: 4
   :answer_c: 10
   :answer_d: 24
   :feedback_a: Incorrect. You have six options per roll, but you are rolling the dice four times.
   :feedback_b: Correct. You are rolling four times, and each roll represents a stage in the counting process.
   :feedback_c: Incorrect.
   :feedback_d: Incorrect.

   If you were to write code to produce outcomes, how many for loops
   would you have?

Quick Check 3.3
----------------

.. mchoice:: QC1_6
  :correct: a
  :answer_a: 6 * 6 * 6 * 6
  :answer_b: 4 * 4 * 4 * 4 * 4 * 4
  :answer_c: 6 * 4
  :answer_d: 6 + 6 + 6 + 6
  :feedback_a: Correct. Each time you flip, you have 6 possible outcomes (no matter what was rolled previously); as you are rolling 4 times, using the multiplication principle we yield 6*6*6*6.
  :feedback_b: Incorrect.
  :feedback_c: Incorrect.
  :feedback_d: Incorrect.

  Which of the following is a mathematical expression that gives the total
  number of outcomes?

If you want more practice and want to check your work, in the space below, write
code that generates all possible outcomes for rolling a 6-sided dice four consecutive times.

Active Code
-------------

.. activecode:: CodeSample3
   :coach:
   :caption: Code that counts four consecutive dice rolls



Now, consider a couple of variations on this problem. ::

   4. Suppose now I want to roll a 6-sided dice 8 consecutive times. What
   is a mathematical expression for the number of outcomes?

Quick Check 4.1
----------------

.. mchoice:: QC1_7
  :correct: c
  :answer_a: 6 + 6 + 6 + 6 + 6 + 6 + 6 + 6
  :answer_b: 8 * 8 * 8 * 8
  :answer_c: 6 ^ 8
  :answer_d: 8 * 8 * 8 * 8 * 8 * 8
  :feedback_a: Incorrect.
  :feedback_b: Incorrect.
  :feedback_c: Correct. There are eight dice rolls, each of which has 6 options; using the multiplication principle we get 6*6*6*6*6*6*6*6 = 6^8.
  :feedback_d: Incorrect.

  Which of the following is a mathematical expression that gives the total
  number of outcomes for this problem?

::

    5. How many outcomes are there for rolling a 4-sided dice six consecutive
    times? What is a mathematical expression for the number of outcomes?

Quick Check 5.1
----------------

.. mchoice:: QC1_8
  :correct: b
  :answer_a: 6 + 6 + 6 + 6
  :answer_b: 4 * 4 * 4 * 4 * 4 * 4
  :answer_c: 6 ^ 4
  :answer_d: 4 + 4 + 4 + 4 + 4 + 4
  :feedback_a: Incorrect.
  :feedback_b: Correct. We roll the dice six times, and there are four options at each stage in the process.
  :feedback_c: Incorrect
  :feedback_d: Incorrect.

  Which of the following is a mathematical expression that gives the total
  number of outcomes for this problem?

::

   6. How many outcomes are there for rolling a 20-sided dice three times? Remix
   code from above to write code that would generate all possible outcomes. Then,
   select the correct answer in the multiple choice problem below.


Active Code 4
--------------

.. activecode:: Codesample4
  :coach:
  :caption: Code that generates outcomes of rolling a 20-sided dice three times.

  Quick Check 5.1
  ----------------

.. mchoice:: QC1_9
  :correct: c
  :answer_a: 20 + 20 + 20 + 20
  :answer_b: 3^20
  :answer_c: 20^3
  :answer_d: 3*20
  :feedback_a: Incorrect.
  :feedback_b: Incorrect.
  :feedback_c: Correct. We roll the dice 3 times, and there are 20 options at each stage in the process.
  :feedback_d: Incorrect.

  Which of the following is a mathematical expression that gives the total
  number of outcomes for this problem?

General formula for Arrangements with Repetition
-------------------------------------------------

We now discuss a general formula for these kinds of problems.

Notice that there is a commonality among the mathematical expressions that
solve this particular kind of problem. In general, if we have :math:`n` distinct
objects, and we are arranging :math:`r` of them, where repetition is allowed, there
are :math:`n^r` total outcomes.

To see why this works, note that if we are arranging :math:`r` elements, we can
think of :math:`r` stages in our counting process, and at each stage we consider how
many options there are at that stage. Since repetition is allowed, we have :math:`n`
options at each stage. These are independent choices at each stage, and using
the multiplication principle, we multiply :math:`n` together :math:`r` times, giving
us :math:`n^r`.

In terms of coding problems like this, notice that we can have :math:`n` elements in
our initial list, and we can have :math:`r` nested for loops cycling through these elements without restriction. These
correspond to the :math:`r` stages in our counting process, where at each stage we
are cycling through all :math:`n` options in our list. ::

  7. How many different license plate are there that consist of three letters,
  followed by three numbers?


.. parsonsprob:: PP_licenseplates
   :numbered: left

   Solve the following Parson's Problem for this question.
   -----

   Numbers = [0,1,2,3,4,5,6,7,8,9]
   Letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
   'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   =====
   counter = 0
   =====
   for i in Letters:
   =====
       for j in Letters:
   =====
           for k in Letters:
   =====
               for l in Numbers:
   =====
                   for m in Numbers:
   =====
                       for n in Numbers:
   =====
                           print(i,j,k,l,m,n)
                           print(counter)
   =====
   print(counter)


Coordinating multiple applications of this formula
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

As is often the case, most problems will not be only a direct application of
this formula, :math:`n^r`, but rather they will involve or incorporate it in some
way into a broader problem. Here we offer some examples of how this formula
might arise or be used in problems. ::

  7. How many different license plates involving three letters and three digits
  are there if the three letters appear together, either at the beginning or the end of the license plate?

Notice here that there are two cases, each of which involves our formula. In
both cases we are considering 26 options for each letter and 10 options for
each digit; the multiplication principle applies in each case.

In one case, the three letters are at the beginning of the license plate. Then
there are :math:`26 \cdot 26 \cdot 26 \cdot 10 \cdot 10 \cdot 10` or :math:`26^3 \cdot 10^3 = 17,576,000` total
license plates.

In the other case, the three letters are at the end of the license plate. Then
there are :math:`10 \cdot 10 \cdot 10 \cdot 26 \cdot 26 \cdot 26` or :math:`10^3 \cdot 26^3 = 17,576,000` total
license plates.

These are distinct cases, so we can add the total together, so our total number
of license plates is :math:`26^3 \cdot 10^3 + 10^3 \cdot 26^3 = 35,152,000`.

.. parsonsprob:: PP_licenseplates2
   :numbered: left

   Solve the following Parson's Problem for this question.
   -----

   Numbers = [0,1,2,3,4,5,6,7,8,9]
   Letters = ['A','B','C','D','E','F','G','H','I','J','K','L',
   'M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z']
   =====
   counter = 0
   =====
   for i in Letters:
       for j in Letters:
           for k in Letters:
   =====
               for l in Numbers:
                   for m in Numbers:
                       for n in Numbers:
   =====
                           print(i,j,k,l,m,n)
                           counter += 1
   =====
   for a in Numbers:
       for b in Numbers:
           for c in Numbers:
   =====
               for d in Letters:
                   for e in Letters:
                       for f in Letters:
   =====
                           print(a,b,c,d,e,f,g)
                           counter +1 =
   =====
   print(counter)


Now let's try another problem. ::

  8. At my bank, a PIN consists of 4 digits (from 0 to 9). How many PINs
  are there with no consecutive digits?

Note, here, we can apply our formula. We can think of a 4-stage process, where
in each stage we consider the number of options for each respective digit
(first, second, third, and fourth). In the first stage we can choose any number,
so there are 10 options. In the second stage, we can choose any number except
what was chosen first, so there are 9 options. In the third stage, we can choose
any number except what was chosen directly previously, so again there are 9
options. In the fourth stage, again we have 9 options.

So, our final answer is :math:`10 \cdot 9^3 = 7,290`.

To code this, note that for our later stages we include a conditional statement
that doesn't allow for the previous letter to be included. Run the code and
examine the output.

Active Code 5
--------------

.. activecode:: CodeSample5
   :coach:
   :caption: Code that counts PIN numbers with no consecutive digits.

   Digits = [0,1,2,3,4,5,6,7,8,9]
   counter = 0

   for i in Digits:
       for j in Digits:
           if j != i:
               for k in Digits:
                   if k != j:
                       for l in Digits:
                           if l != k:
                               print(i,j,k,l)
                               counter += 1
   print(counter)


Quick Check 8.1
----------------

.. mchoice:: QC1_10
  :correct: c
  :answer_a: It makes sure the second digit is not the same as the first digit.
  :answer_b: It makes sure the third digit is not the same as the first digit.
  :answer_c: It makes sure the third digit is not the same as the second digit.
  :answer_d: It makes sure the third digit is not the same as either of the first two digits.
  :feedback_a: Incorrect.
  :feedback_b: Incorrect.
  :feedback_c: Correct. All we need for this problem to ensure non-consecutivity is to have each digit not be equal to the digit directly preceding it. Thus, "if k != j" ensures the third digit is not the same as the second digit.
  :feedback_d: Incorrect.

  What does the conditional statement "if k != j" accomplish?
