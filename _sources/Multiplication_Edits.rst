=======================================
The Multiplication Principle Edited
=======================================
..
  This edited document will include all changes that I think are appropriate.
  I have shortened the length of narratives, included quite a few more problems,
  and have written more questions meant to elicite connections between counting
  and computer programs.

  I will also include comments throughout the document for the changes to make
  when using Counting Sheets. Because many of the questions refer to code, there
  are quite a few of these changes.

  Anytime there is active code, there needs to be a corresponding code in Counting
  Sheets. However, I will mark any places where the code needs to be omitted
  instead of replaced.

The Multiplication Principle (MP) is a fundamental counting principle that helps us to
determine the number of ways that a multi-stage event can occur. When applying
the MP, we will be able to count the total number of events by multiplying the
number of ways each stage can occur. This principle
will help us to count problems like "how many ways are there to flip a coin five
times in a row," and "if five people are competing in a race, how many ways can
a gold, siver, and bronze trophy be awarded?" We will call each possible result
of a multi-stage event an outcome of those events.

In this essay, we will work through some problems that help to motivate the use
of the MP, as well as explain why it can be applied. After working through
problems, we will end with a formal statement of the multiplication principle.



Motivating Problem
---------------------

Let's examine our first problem. As you read through it, try to think about why
each outcome being counted has multiple stages, and try to determine what those
stages could be.

Problem 1: Outfits
~~~~~~~~~~~~~~~~~~~~~~
  You have four different tops (a tee, a sweater, a tank, and a blouse) and three different bottoms
  (shorts, capris, and jeans). How many different outfits are you able to make out
  of one top and one bottom?



To count the number of outfits, we can think about dressing as occuring in
two stages. First, we put on a top, and second we put on a bottom. If we wanted to
list every outcome, we could do so by first specifying a top, and then specifying a bottom.


To visualize these outcomes, consider the table below where we list every outcome:

+--------------+---------------------+------------------------+---------------------+
|              |        **Shorts**   |        **Capris**      |     **Jeans**       |
+--------------+---------------------+------------------------+---------------------+
| **Tee**      | (1) (Tee, Shorts)   |  (2) (Tee, Capris)     |  (3) (Tee, Jeans)   |
+--------------+---------------------+------------------------+---------------------+
| **Sweater**  |(4) (Sweater, Shorts)| (5) (Sweater, Capris)  | (6) (Sweater, Jeans)|
+--------------+---------------------+------------------------+---------------------+
| **Tank**     | (7) (Tank, Shorts)  | (8) (Tank, Capris)     | (9) (Tank, Jeans)   |
+--------------+---------------------+------------------------+---------------------+
| **Blouse**   |(10) (Blouse, Shorts)| (11) (Blouse, Capris)  | (12) (Blouse, Jeans)|
+--------------+---------------------+------------------------+---------------------+


This table neatly organizes the outcomes by using rows to distinguish between the tops,
and columns to distinguish between the bottoms. Since we can write the outcomes
so that they occupy each spot in a three-by-four table, the total number of
outcomes is :math:`4\times 3`.


Checkpoint 1:
~~~~~~~~~~~~~~~
  Why is the total number of outfits :math:`4\times 3`?

.. mchoice:: Checkpoint1_Edits
  :correct: d
  :answer_a: Every outfit fits into a three-by-four table
  :answer_b: You can pair each of the four tops with each of the three bottoms
  :answer_c: You can pair each of the three bottoms with each of the four tops
  :answer_d: All of the above
  :feedback_a: This is true, but are others true as well?
  :feedback_b: This is true, but are others true as well?
  :feedback_c: This is true, but are others true as well?

  Why is the total number of outfits :math:`4\times 3`?



You may notice that in any row
all the tops are the same, and in any column all the bottoms are the same. We could have
created this table one row at a time, where for every option of top we cycled through
every option of bottom. Let's do this process using computer code.


..
  Counting Sheets: Examine the computer code below. The first column corresponds
  to the tops, and the second column corresponds to the bottoms. After you
  run it, compare the printed output to the table above, and relate that
  output to the mathematical expression :math:`4\times 3`.

Examine the code below. The nested lines ``for i in Tops:``
and ``for j in Bottoms:`` correspond to the process of cycling through every possible
Top, and for each Top cycling through every possible Bottom. After you run it,
compare the printed output to the table above and relate
the printed output to the mathematical expression :math:`4\times 3`.

Tops and Bottoms
~~~~~~~~~~~~~~~~~

.. activecode:: CodeSampleMult1_Edit
   :coach:
   :caption: Code that generates possible outfits

   Tops = ['tee', 'sweater','tank', 'blouse']
   Bottoms = ['shorts', 'capris', 'jeans']
   counter=0

   for i in Tops:
       for j in Bottoms:
           print(i,j)
           counter+=1
   print(counter)

.. shortanswer:: MP_Outfit_SA_Edit

  By referring to the code above, justify why the outfits can be broken into four groups of three.

..
  Counting Sheets: Change the above problem to "By referring to the printed
  output above,..." and include the rest of the question.

Problem 2: Outfits Part 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Suppose now you had 4 different tops, 3 different bottoms, and 3 different pairs of shoes.



The code below will list all possible outfits. Before you run it, predict how the printed
outcomes will be organized. Then, jot down your prediction for the first 5 outcomes that
will be printed.


.. shortanswer:: MP_TopsBottomsShoes_SA_Edit

  Read through the code below. Then, write dow your prediction for the first
  five outcomes that will be printed.


.. activeCode:: CodeSampleMult2_Edit
   :coach:
   :caption: Outfits including shoes

   Tops = ['tee', 'sweater','tank', 'blouse']
   Bottoms = ['shorts', 'capris', 'jeans']
   Shoes = ['sneakers', 'sandals', 'keds']
   counter=0

   for i in Tops:
       for j in Bottoms:
           for k in Shoes:
               print(i,j,k)
               counter+=1
   print(counter)


.. shortanswer:: short-mult1_Edit

  In the space below, describe if your predicted first 5 outcomes matched the first 5
  outcomes that were printed. If they were the same, tell us about your reasoning.
  If they were different, describe how they were different.

By creating an outfit out of four possible tops, three possible bottoms, and
three possible shoes, there are now :math:`4\times 3\times 3` possible outfits.
The reason we can multiply here is that there are three possible choices of shoes that can
be made for each of the :math:`4\times 3` outfits made from tops and bottoms.
That is, each of the 12 outfits we counted before can now be paired with 3 possible
shoes.

Checkpoint 2:
~~~~~~~~~~~~~~~~~~~
  Suppose you have four tops, three bottoms, three shoes, and two hats. How many
  possible outfits can you make?

.. mchoice:: Checkpoint2_Edits
  :correct: b
  :answer_a: 4*3*2
  :answer_b: 4*3*3*2
  :answer_c: 3*3*2
  :feedback_a: Incorrect
  :feedback_b: Correct
  :feedback_c: Incorrect

  Suppose you have four tops, three bottoms, three shoes, and two hats. How many
  possible outfits can you make?

..
  Counting Sheets: The following parson problem can be omitted, and replaced with
  a blank counting sheets accompanied with the description "Using the two above
  computer programs as guides, fill out the first four columns of the counting
  sheets so that it prints out all top-bottom-shoe-hat combinations."

Using the two above computer programs as guide, drag and drop the program components
below to create a computer program that prints all top-bottom-shoe-hat combinations.

.. parsonsprob:: MP_OutfitTBSH_Parson1_Edits
    :numbered: left

    Tops = ['tee', 'sweater','tank', 'blouse']
    Bottoms = ['shorts', 'capris', 'jeans']
    Shoes = ['sneakers', 'sandals', 'keds']
    Hats = ['ballcap', 'beanie']

    =====
    counter=0
    =====
    for i in Tops:
        for j in Bottoms:
    =====
            for k in Shoes:
                for l in Hats:
    =====
                    print(i,j,k,l)
                    counter+=1
    =====
    print(counter)

Point for pondering
~~~~~~~~~~~~~~~~~~~~~~
  Statements like `for i in Tops:` are called loops because the value of i will
  cycle through all entries of Tops. We say a loop is nested when it is indented
  inside another loop. Nesting one loop inside another will make the entire second loop
  happen for every value in the first loop.
  In the above code, the loop `for j in Bottoms:` is nested
  within the loop `for i in Tops:`, so for each value of i in Tops, j will take on
  every value in Bottoms.

..
  Counting Sheets: This Point for Pondering can be replaced with "You may have noticed
  that every data entry in a column is repeated for every data entry in a previous column.
  For example, when there is data in two columns, the data in the second column is
  cycled through for every entry in the first column."

.. shortanswer:: MP_PointPondering_1_Edit

  Based on what you have seen so far, are there any connections between nested loops
  and multiplication? If so, explain the connections you see.

..
  Counting Sheets: The short answer above can be replaced with "Based on what you
  have seen so far, are there any connections between the data entries in each
  column and multiplication? If so, explain the connections you see."

Now that we have seen examples of applying the MP, let's formalize one scenario
where it can be applied.

Counting Cartesian Products
---------------------------------

Given two sets of objects, :math:`X` and :math:`Y`, we call the set of all pairs
of objects from :math:`X` and :math:`Y` the Cartesian product of :math:`X` and
:math:`Y`, denoted :math:`X \times Y`.
For example, if we denote the set of all tops as :math:`T`, and the set of all bottoms as
:math:`B`, then the Cartesian product :math:`T\times B` is all pairs of a top with
a bottom.

We can also find the Cartesian product of more than two sets. For example, the code
below will create all elements of the Cartesian product between the set of Tops,
the set of Bottoms, and the set of Shoes. We denote this set as :math:`T\times B \times S`.

.. activeCode:: CodeSampleMult2_Edit_2
   :coach:
   :caption: Outfits including shoes

   Tops = ['tee', 'sweater','tank', 'blouse']
   Bottoms = ['shorts', 'capris', 'jeans']
   Shoes = ['sneakers', 'sandals', 'keds']
   counter=0

   for i in Tops:
       for j in Bottoms:
           for k in Shoes:
               print(i,j,k)
               counter+=1
   print(counter)

The size (also called cardinality) of a Cartesian product can be found by multiplying
the sizes of the individual sets in the product. In the above computer program,
there are :math:`36` total outfits because there are :math:`4` tops, :math:`3` bottoms,
:math:`3` shoes, and :math:`36 = 4\times 3\times 3`.

.. shortanswer:: MP_CartProd_Edit

  The above code has three nested loops. What is a correspondance between each of the
  three nested loops and each of the three terms in the expression :math:`4\times 3 \times 3`?
  How might nesting the loops correspond to multiplication?

Let's solve some more Cartesian Product Problems.

Problem 3: Coin, Dice, Letter
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How many ways are there to first flip a fair coin, then roll a 6-sided die, and
  then pick a letter from the alphabet?

.. shortanswer:: shortmult2_Edit

  Explain why problem 3 is a Cartesian Product Problem. Then,
  describe how you will find the total number of outcomes.

The code below generates the outcomes of problem 3. Predict the first
five outcomes of the code before you run it.

.. activecode:: CodeSampleMult3_Edit
  :coach:

  Coin = ['H', 'T']
  Dice = range(1,7)
  Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
  counter = 0

  for i in Coin:
      for j in Dice:
          for k in Letters:
              print(i,j,k)
              counter+=1
  print(counter)

..
  Editing this now, I forget how to provide feedback to students after they
  have finished a short answer prompt. If possible, I would like to return the
  feeback "There are 6*26=156 outcomes that start with T, and an equal number that start with H. "

As you scroll through the output of the above code, you may notice that the outcomes
are split into two groups: those that start with "T" and those that start with "H".

.. shortanswer:: shortmult3_Edit

  How many outcomes start with H? How many start with T? Are you able to use the MP to solve this?


Problem 4: Pants
~~~~~~~~~~~~~~~~~~~~
    A store carries 8 styles of pants. For each style, there are 10 different
    possible waist sizes, 6 pant lengths, and 4 color choices. Rearrange the
    code below so that it creates all possible types of Pants.

..
  Counting Sheets: I think problem 4 can be omitted, and the rest of the problems renumbered.



Drag and drop the following blocks of code to create a computer program that will list
every possible outcome.



.. parsonsprob:: MP_Pants_Edit
    :numbered: left

    Styles = range(1,9)
    Waists = range(1,11)
    Lengths = range(1,7)
    Colors = range(1,4)
    =====
    counter = 0
    =====
    for s in Styles:
    =====
        for w in Waists:
    =====
            for l in Lengths:
    =====
                for c in Colors:
    =====
                    counter+=1
                    print(s,w,l,c)
    =====
    print(counter)

Problem 5: Tea Shop
~~~~~~~~~~~~~~~~~~~~
    A tea shop offers four types of tea, and three types of scones. Write a computer
    program below that lists every combination of tea and scone. How many should there be?

.. activecode:: Multiplication_Prob5_Edit
    :coach:
    :Caption: Hint: You can use the above programs as reference.

    Teas = []
    Scones = []
    counter=0

    #Fill in code

.. mchoice:: MP_TeaShop_Edit
  :correct:
  :answer_a: 4*3
  :answer_b: 4^3
  :answer_c: 3^4
  :answer_d: 4+3

  How many tea and scone combinations are there?

Problem 6: Coin Flips
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How many ways are there to flip a coin 4 times in a row?

.. mchoice:: Coin_Flips_FA_Edit
    :correct: c
    :answer_a: 8
    :answer_b: 12
    :answer_c: 16
    :feedback_a: Incorrect
    :feedback_b: Incorrect
    :feedback_c: Correct

    How many ways are there to flip a coin 4 times in a row?

.. shortanswer:: Coin_Flips_SA_Edit

  Using your own words, why can we use multiplication to find the total number of outcomes?

Examine the code below. Will it produce every possible outcome?

..
  Counting Sheets: Replace this with a counting sheet that has H, T in the four
  columns

.. activecode:: Coin_Flips_AC_Edit
    :coach:
    :Caption: Every combination of four coin flips?

    flip1 = ['H','T']
    flip2 = ['H','T']
    flip3 = ['H','T']
    flip4 = ['H','T']

    counter = 0

    for i in flip1:
        for j in flip2:
            for k in flip3:
                for l in flip4:
                    counter+=1
                    print(i,j,k,l)



.. mchoice:: Coin_Flips_MC2_Edit
    :correct: a
    :answer_a: Yes
    :answer_b: No
    :feedback_a: Correct
    :feedback_b: Incorrect

    Does the code above produce every combination of coin flips?

Examine the code below. Will it produce every possible outcome?

..
  Counting Sheets: Replace this one with a counting sheet that has H, T
  in the first column, and =data1 in columns 2, 3, and 4.

.. activecode:: Coin_Flips_AC2_Edit
    :coach:
    :Caption: Every combination of four coin flips?

    flips = ['H','T']
    counter = 0

    for i in flips:
        for j in flips:
            for k in flips:
                for l in flips:
                    counter+=1
                    print(i,j,k,l)



.. mchoice:: Coin_Flips_MC3_Edit
    :correct: a
    :answer_a: Yes
    :answer_b: No
    :feedback_a: Correct
    :feedback_b: Incorrect

    Does the code above produce every combination of coin flips?

.. shortanswer:: Coin_Flips_2_MC2_Edit

  The two computer programs above produced the exact same output. What was
  different about how the programs were written? Why did they produce the same
  output?



Problem 7: Quiz Questions
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  On a quiz, there are 6 True/False questions. How many ways can a student
  finish the quiz, if they put an answer for every question?

For the problem above, write some code that prints the possible outcomes.

..
  Counting Sheets: Replace this with a blank counting sheet.

.. activecode:: CodeSampleMult5_Edit
  :coach:
  :caption: Ways to finish a 6-question T/F quiz

  Answers = ['T', 'F']
  counter = 0

  %Finish the code here

.. mchoice:: MP_Quiz_Edit
    :correct: c
    :answer_a: 8
    :answer_b: 12
    :answer_c: 2^6
    :answer_d: 6^2

    How many ways can the student finish the quiz?

Problem 8: 3-digit sequences
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How many 3-digit sequences can we make using the letters {a, b, c, d, e, f}? Letters
  may be repeated.

For the problem above above, write some code that prints the possible outcomes.

.. activecode:: CodeSampleMult6_Edit
  :coach:
  :caption: Possible 3-letter sequences

  Letters = ['a','b','c','d','e','f']
  counter = 0

  %Finish the code here

.. mchoice:: MP2_3_digit_Edit
  :correct: b
  :answer_a: 6^6
  :answer_b: 6^3
  :answer_c: 3^3
  :answer_d: 3^6

  How many 3-digit sequences can we make using the letters {a, b, c, d, e, f}? Letters
  may be repeated.

Point for Pondering
~~~~~~~~~~~~~~~~~~~~~

..
  Counting Sheet: Replace the question below with "Suppose a counting sheet had
  data in three columns. How could you find the number of outputs from that counting
  sheet before you ran it?"

.. shortanswer:: MP2_3_digit_SA_Edit

  If a loop such as `for i in Letters:` corresponds to cycling through all possible
  values in Letters, what does nesting the loops correspond to?

Applying multiplication and the MP to other types of problems
-------------------------------------------------------------------

While we have worked through counting Cartesian products by using multiplication,
we can also solve other types of problems by using multiplication. We start
with some examples.


Problem 10: Small lottery
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You have placed slips of paper with the numbers 1 through 5 in a baseball cap,
  with one sheet of paper per number. How many ways are there to draw three slips of paper
  from the hat, one at a time, if you don't replace the pieces of paper?



Here is one way to list all such outcomes:

::

  123
  124
  125
  132
  134
  135
  142
  143
  145
  152
  153
  154
  213
  .
  .
  .
  541
  542
  543


Checkpoint:
~~~~~~~~~~~~~~~~~~~~

.. mchoice:: MP2_Lottery_Edit
  :correct: b
  :answer_a: Yes
  :answer_b: No
  :feedback_a: Incorrect. The slips of paper are not returned to the hat, so you cannot draw 4 twice.
  :feedback_b: Correct. The slips of paper are not returned to the hat, so you cannot draw 4 twice.

  Is 434 a possible way to draw the slips of paper?



.. mchoice:: MP2_Lottery_Edit_2
  :correct: b
  :answer_a: Yes
  :answer_b: No
  :feedback_a: Incorrect. The Cartesian product would include outcomes like 434, which we do not want to count.
  :feedback_b: Correct. The Cartesian product would include outcomes like 434, which we do not want to count.

  If :math:`S = \{1,2,3,4,5\}`, are we counting :math:`S\times S\times S`?


The following computer program lists these outcomes.

.. activeCode:: MP_Lottery_Edit
  :coach:
  :Caption: All possible lottery draws

  Numbers = [1,2,3,4,5]
  counter = 0

  for i in Numbers:
      for j in Numbers:
          if j!=i:
              for k in Numbers:
                  if k!=i and k!=j:
                      print(i,j,k)
                      counter +=1

.. shortanswer:: MP_Lottery_SA_Edit

  In Python, the symbols '!=' mean 'not equal to,' which is equivalent to :math:`\neq`.
  What do you think the lines 'if j!=i:' and 'if k!=i and k!=j' do in the code?

..
  Counting Sheets: Replace the above question with "In the second column, '=col1 minus item 1' means that
  the entries iterated through in the second position will be all data in the first
  column except the current occupant of the first position. How do you think this
  affects the output of the program?"

Problem 11: The ABCDEs
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How many ways are there to arrange three letters from A, B, C, D, E if no
  letter is repeated?




.. mchoice:: MP2_ABCDE_Edit
  :correct: b
  :answer_a: Yes
  :answer_b: No
  :feedback_a: Incorrect. We are only counting arrangements where no letters are repeated.
  :feedback_b: Correct. We are only counting arrangements where no letters are repeated.

  Is ADA one of the arrangements we are trying to count?



.. mchoice:: MP2_ABCDE_2_Edit
  :correct: b
  :answer_a: Yes
  :answer_b: No
  :feedback_a: Incorrect. The Cartesian product would include arrangements like ADA and CDD.
  :feedback_b: Correct. The Cartesian product would include arrangements like ADA and CDD.

  If :math:`S=\{A, B, C, D, E\}`, are we counting :math:`S\times S\times S`?

Consider the code below.

..
  Counting Sheets: Replace this code with a counting sheet.

.. activecode:: MP_ABCDE_Code_Edit
  :coach:
  :Caption: Arrangements of letters from A, B, C, D, E without repetition.

  Letters = ['A','B','C','D','E']
  counter = 0

  for i in Letters:
      for j in Letters:
          if j!=i:
              for k in Letters:
                  if k!=i and k!=j:
                      print(i,j,k)
                      counter+=1
  #print(counter)



.. mchoice:: MP2_ABCDE_3_Edit
  :correct: b
  :answer_a: 3
  :answer_b: 4
  :answer_c: 5
  :feedback_a: Incorrect. Only one of the five possibilities has been removed.
  :feedback_b: Correct. One of the five possibilities has been removed.
  :feedback_c: Incorrect. One of the five possibilities has been removed.

  In the code above, the line 'if j!=i:' eliminates the possibility that the value of
  j can be equal to the value of i. For each value of i, how many possible values for j are there?

..
  Counting Sheet: Replace the above question with "In the above code, the '=col1 minus item 1'
  eliminates the possibility of the second position being equal to the first position. For
  each value in the first position, how many possible values are there for the second position?"

.. mchoice:: MP2_ABCDE_4_Edit
  :correct: a
  :answer_a: 3
  :answer_b: 4
  :answer_c: 5
  :feedback_a: Correct. Two of the five possibilities have been removed.
  :feedback_b: Incorrect. Two of the five possibilities have been removed.
  :feedback_c: Incorrect. Two of the five possibilities have been removed.

  In the code above, the line 'if k!=i and k!=j:' eliminates the possibility that the value of
  k can be equal to the value of i or the value of j. If we have already chosen values for i and j, how many possible values for k are there?

..
  Counting Sheets: Replace the above question with "In the above code, the '=col1 minus item 1 minus item 2'
  eliminates the possibility of the second position being equal to the first or second position. For
  each value in the first and second position, how many possible values are there for the third position?"

The above two problems point out that for each of the five possible choices for
the first letter, there are four possible choices for the second letter, and for each possible
choice of the first and second letter there are three possible choices for the third letter.

.. shortanswer:: MP2_ABCDE_SA_Edit

  Explain why there might be :math:`5\times 4\times 3` total ways to arrange three
  of the letters from A, B, C, D, E, if no letter is repeated.

We will return to these types of problems in a later module.

When the MP doesn't quite work
-----------------------------------

Multiplication can be used to solve every problem we have discussed so far. A rough characterization
of the MP can be stated as "If we can break an event into multiple stages, and the number
of ways each stage can occur is fixed, then we can multiply the number of possible outcomes
at each stage to find the total number of events." However, there are some sequential events for
which this won't work, and it is key to be able to identify why multiplication doesn't work.
This can happen when the number of possible outcomes at each stage are not independent
of the other stages.

Consider the following problem:

Problem 9: Face Card, Heart Card
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How many ways are there to make a two-card hand, where the first card is a face
  card and the second card is a heart? The order of the cards in your hand
  matters, but you must have two distinct cards (e.g. you cannot have two Jacks of Hearts).


.. mchoice:: MP2_FaceHeart_1_Edit
  :correct: c
  :answer_a: 3
  :answer_b: 9
  :answer_c: 12
  :feedback_a: Incorrect. There are three face cards per suit.
  :feedback_b: Incorrect. There are three face cards per suit.
  :feedback_c: Correct. There are three face cards per suit.

  How many face cards are there?


.. mchoice:: MP2_FaceHeart_2_Edit
  :correct: d
  :answer_a: 10
  :answer_b: 11
  :answer_c: 12
  :answer_d: 13
  :feedback_a: Incorrect.
  :feedback_b: Incorrect.
  :feedback_c: Incorrect.
  :feedback_d: Correct.

  How many heart cards are there?

.. shortanswer:: MP2_FaceHeart_SA_Edit

  If :math:`F` is the set of all Face cards, and :math:`H` is the set
  of all Heart cards, are there any elements of :math:`F\times H` that we don't
  want to count?


Consider the following code.

.. activecode:: MP2_FaceHeart_AC_Edit
  :coach:
  :Caption: Face and Heart combinations?

  Faces = ['JackSpade','QueenSpade','KingSpade','JackClub','QueenClub','KingClub', \
          'JackHeart','QueenHeart','KingHeart','JackDiamond','QueenDiamond','KingDiamond']
  Hearts = ['AceHeart','OneHeart','TwoHeart','ThreeHeart','FourHeart','FiveHeart','SixHeart', \
          'SevenHeart','EightHeart','NineHeart','TenHeart','JackHeart','QueenHeart','KingHeart']
  counter=0

  for i in Faces:
      for j in Hearts:
          print(i,j)
          counter+=1

..
  Counting Sheets: When replaceing the above code, it is okay if we change the name of each data point.
  I can also give a different question if putting it into counting sheets is troublesome.

.. shortanswer:: MP2_FaceHeart_SA2_Edit

  Does the above code count any outcomes that we don't want to count? If so, why, and which ones? If not, why not?

The reason that we cannot use multiplication in this problem is that the number of ways to choose the
second card (the heart card) depends on the choice of the first card, the face card.
If the Jack, Queen, or King of Hearts is chosen as the first card, then there are only 12 ways to choose the second
card because the two cards cannot be the same. On the other hand, if the Jack, Queen, or King
of Hearts is not chosen as the first card, then there are 13 possible ways to choose the
second card.

This scenario demonstrates what we call **independence**. In a multi-stage process,
we can use multiplication to count events if the **number** of outcomes
at any stage is independent of the choices at any of the prior stages.

Consider the following code. This code will show all choices from the previous
code where the choices for i and j are the same.

..
  Counting Sheets: If possible, can the code below be replaced with something
  where the second column still iterates through all of the data, but only prints
  something if the first and second column are equal?

.. activecode:: MP2_FaceHeart_AC2_Edit
  :coach:
  :Caption: Face and Heart combinations?

  Faces = ['JackSpade','QueenSpade','KingSpade','JackClub','QueenClub','KingClub', \
          'JackHeart','QueenHeart','KingHeart','JackDiamond','QueenDiamond','KingDiamond']
  Hearts = ['AceHeart','OneHeart','TwoHeart','ThreeHeart','FourHeart','FiveHeart','SixHeart', \
          'SevenHeart','EightHeart','NineHeart','TenHeart','JackHeart','QueenHeart','KingHeart']
  counter=0

  for i in Faces:
      for j in Hearts:
          if i==j:
              print('Both same card: ', i, j)
          else:
              #print(i,j)
              counter+=1



.. mchoice:: MP2_FaceHeart_3_Edit
  :correct: c
  :answer_a: 2
  :answer_b: 3
  :answer_c: 6
  :answer_d: 12
  :feedback_a: Incorrect.
  :feedback_b: Incorrect.
  :feedback_c: Correct.
  :feedback_d: Incorrect.

  How many incorrect events did the original code create?

.. mchoice:: MP2_FaceHeart_4_Edit
  :correct: c
  :answer_a: 12*13 - 2
  :answer_b: 12*13 - 3
  :answer_c: 12*13 - 6
  :answer_d: 12*13 - 12
  :feedback_a: Incorrect. The expression 12*13 includes the three options where the two cards are identical.
  :feedback_b: Incorrect. The expression 12*13 includes the three options where the two cards are identical.
  :feedback_c: Correct. The expression 12*13 includes the three options where the two cards are identical.
  :feedback_d: Incorrect. The expression 12*13 includes the three options where the two cards are identical.

  How many correct hands are there?

Can you modify the code above so that it only prints the outcomes where the first and second card are not identical?
How would you check your code to verify that it is correct?

.. activecode:: MP2_FaceHeart_AC3_Edit
  :coach:
  :Caption: Modify this code to only print outcomes where the two cards are different

  Faces = ['JackSpade','QueenSpade','KingSpade','JackClub',\
          'QueenClub','KingClub', 'JackHeart','QueenHeart',\
          'KingHeart','JackDiamond','QueenDiamond','KingDiamond']
  Hearts = ['AceHeart','OneHeart','TwoHeart','ThreeHeart',\
          'FourHeart','FiveHeart','SixHeart', 'SevenHeart',\
          'EightHeart','NineHeart','TenHeart','JackHeart','QueenHeart','KingHeart']
  counter=0

  for i in Faces:
      for j in Hearts:
          if i==j:
              print('Both same card: ', i, j)
          else:
              #print(i,j)
              counter+=1



Formal Statement of the MP
-----------------------------

We now provide a formal statement of the multiplication principle.

The Multiplication Principle (MP)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Suppose an event can be broken up into :math:`n` discrete stages. Let :math:`r_1`
  be the number of ways that stage :math:`1` can occur, :math:`r_2` be the number of
  ways that stage :math:`2` can occur, and more generally :math:`r_i` be the number
  of ways that stage :math:`i` can occur. If the number of ways each stage can occur
  is independent of the choices at any of the other stages, and each composite event is distinct,
  then the total number of events is equal to
  :math:`r_1\times r_2\times r_3\times \cdots\times r_i \times \cdots \times r_n`.

To apply the multiplication principle, three things must occur. First, the events we
are counting need to be broken into distinct stages. Second, the number of ways
each stage can occur must be independent of the other stages. Third, each composite
event--that is, the event composed of what occurs at each stage--must be distinct.

Restatement: Outfit Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You have four different tops (a tee, a sweater, a tank, and a blouse) and three different bottoms
  (shorts, capris, and jeans). How many different outfits are you able to make out
  of one top and one bottom?

.. mchoice:: MP_Restatement_Outfit_1_Edit
  :answer_a: 1
  :answer_b: 2
  :answer_c: 3
  :answer_d: Cannot be broken into separate events
  :correct: b

  How many stages can this event be broken into?

.. mchoice:: MP_Restatement_Outfit_2_Edit
  :answer_a: Yes
  :answer_b: No
  :answer_c: Cannot say
  :correct: a
  :feedback_a: Correct
  :feedback_b: Incorrect. The number of ways that a shirt can be chosen is independent of what pants are chosen, or vice versa.
  :feedback_c: Incorrect. The number of ways that a shirt can be chosen is independent of what pants are chosen, or vice versa.

  Is the number of ways each stage can occur independent of the choices made at other stages?

.. mchoice:: MP_Restatement_Outfit_3_Edit
  :answer_a: Yes
  :answer_b: No
  :answer_c: Cannot say
  :correct: a
  :feedback_b: Incorrect. Any two pairings are distinct so long as they either have a different shirt or a different pair of pants.
  :feedback_c: Incorrect. Any two pairings are distinct so long as they either have a different shirt or a different pair of pants.

  Is each composite event distinct?

.. mchoice:: MP_Restatement_Outfit_4_Edit
  :answer_a: Yes
  :answer_b: No
  :answer_c: Cannot say
  :correct: a

  Can the multiplication principle be applied?

Restatement: Small Lottery Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  You have placed slips of paper with the numbers 1 through 5 in a baseball cap,
  with one sheet of paper per number. How many ways are there to draw three slips of paper
  from the hat, one at a time, if you don't replace the pieces of paper?

.. mchoice:: MP_Restatement_Lottery_1_Edit
  :answer_a: 1
  :answer_b: 2
  :answer_c: 3
  :answer_d: Cannot be broken into separate events
  :correct: c

  How many stages can this event be broken into?

.. mchoice:: MP_Restatement_Lottery_2_Edit
  :answer_a: Yes
  :answer_b: No
  :answer_c: Cannot say
  :correct: a
  :feedback_a: Correct
  :feedback_b: Incorrect. The number of choices is independent, even if the possible choices change.
  :feedback_c: Incorrect. The number of choices is independent, even if the possible choices change.

  Is the number of ways each stage can occur independent of the choices made at other stages?

.. mchoice:: MP_Restatement_Lottery_3_Edit
  :answer_a: Yes
  :answer_b: No
  :answer_c: Cannot say
  :correct: a
  :feedback_b: Incorrect. The order of the numbers matters.
  :feedback_c: Incorrect. The order of the numbers matters.

  Is each composite event distinct?

.. mchoice:: MP_Restatement_Lottery_4_Edit
  :answer_a: Yes
  :answer_b: No
  :answer_c: Cannot say
  :correct: a

  Can the multiplication principle be applied?

Restatement: Small Lottery Problem
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  How many ways are there to make a two-card hand, where the first card is a face
  card and the second card is a heart? The order of the cards in your hand
  matters, but you must have two distinct cards (e.g. you cannot have two Jacks of Hearts).

.. shortanswer:: MP_Restatement_FaceHearts_Edit

  The multiplication principle cannot be applied in this problem. In your own words, describe
  why the MP cannot be applied by referencing independence or composite events.
