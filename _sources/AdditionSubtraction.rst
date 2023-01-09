======================================================
Addition and Subtraction Principles
======================================================

The Addition Principle (AP) and Subtraction Principle (SP) are fundamental
principles in counting. In essence, the AP allows you to break a counting
problem into different cases that are easier to manage, and then count each
case separately. The SP is similar, but it allows us to remove (or "uncount") cases
that we have already counted but do not want in our final total.

The AP and SP are commonly used in more advanced problems, but they themselves are
fairly intuitive. We use them often when we solve counting problems, sometimes without
being aware that we are using them. We will start each section by asking a series
of questions meant to highlight the aspects of each principle before we give you
statements of the principles. Then, we will discuss how they can be used in counting
problems.

Addition Principle
=======================

Let's begin by solving the following problems.

.. mchoice:: Trial_1
    :correct: b
    :answer_a: 3
    :answer_b: 7
    :answer_c: 4
    :feedback_a: Incorrect
    :feedback_b: Correct
    :feedback_c: Incorrect

    You own three red cars, four blue cars, and no cars of other colors. How many cars do you own?

.. mchoice:: Trial_2
    :correct: a
    :answer_a: Yes
    :answer_b: No
    :feedback_a: Correct. Some of the cars may be in multiple categories.
    :feedback_b: Incorrect. What if a car can fit into multiple categories?

    Five of your cars are Toyotas, and three of your cars are red, and seven of your cars are vans. Can you
    own fewer than 15 cars?

.. mchoice:: Trial_3
    :correct: b
    :answer_a: No
    :answer_b: Yes
    :feedback_a: Incorrect. What if you have a blue car without ABS?
    :feedback_b: Correct.

    Three of your cars are red, and two of your cars have anti-lock braking systems (ABS).
    Can you own more than five cars?

How did you feel about those problems? Now let's look at statements of the Addition Principle.

Addition Principle Basic (AP)
----------------------------------------
  Suppose a set of events :math:`S` can be partitioned (or separated) into subsets
  of events :math:`A` or :math:`B` such that every event in :math:`S` belongs to one
  and exactly one of :math:`A` or :math:`B`. Then the number of events in :math:`S`
  is equal to the sum of the number of events in :math:`A` and the number of events
  in :math:`B`. Said another way, if we consider :math:`|A|` to be the number of
  elements in the set :math:`A` (also called the cardinality of :math:`A`), Then
  we have that :math:`|S| = |A| + |B|`.

Addition Principle Full (AP)
------------------------------
  Suppose a set of events, :math:`S` can be partitioned (or separated) into a number
  of subsets :math:`S_1, S_2, \ldots , S_k`, where every event in :math:`S` belongs
  to one and exactly one of these subsets. Then the total number of events in :math:`S`
  is the sum of the number of events in each subset :math:`S_1, S_2, \ldots , S_k`.
  Alternatively, :math:`|S| = |S_1| + |S_2| + \cdots + |S_k|`.

The way the AP statements are written may seem more detailed and intimidating than
how you might have been thinking about it. This is done with the primary reason of
intimidating you. Mathematicians bond over scaring their students, and they often
swap intimidation tactics at holiday parties.

All joking aside, the reason for wordy mathematical statements like the AP is so that
we can be precise. We will walk through the language of the AP to help you develop
a robust understanding of it. Informally, we might say that the addition principle
states, "if you can break down a set of events into different cases, then you can
add together the sizes of all the cases to find out the total number of events."

The word "partition" in the statements of the AP is actually doing a lot of work here.
While it is a familiar term, it actually has a specific definition when we are
talking about sets. In particular, a partition breaks a set into subset, but those
subsets have two important properties:
First, the subsets are disjoint, which means that any element of the set can only
belong to exactly one (and not more than one) subset of the partition.
Second, taken together, all of the subsets exactly form the set, which means that
any element of the set must be in exactly one (and not less than one) subset of
the partition.
Thus, when a partition is formed, we know that every element of the set is in exactly
one part (or subset) of partition. This is what allows us to sum as we do in our
statements of the AP.

Let's return to the previous car examples. In the first questions, we said that you
owned three red cars, four blue cars, and no cars of other color. Because cars cannot
both be red and blue, then there are no cars that fall into both of those categories.
Further, we specified that every car fits into one of those categories. Hence,
the two categories together make up all of your cars, and each car falls into exactly
one category. This exactly satisfies the requirements of the partition, as describe
above. From this, then, we can gather that the total number cars you own is the
sum of each of the size of the categories.

.. mchoice:: AP_1
    :correct: c
    :answer_a: Electric, Diesel
    :answer_b: Red, Toyota, neither Red nor Toyota
    :answer_c: Toyota, Hyundai, neither Toyota nor Hyundai
    :feedback_a: Incorrect, there are cars that are neither electric nor diesel.
    :feedback_b: Incorrect, red Toyotas would fit into multiple categories.
    :feedback_c: Correct!

    Thinking about buying a car, you try to determine which type of car you want.
    Which of the below ways to categorize cars would account for all cars, so that each
    car fits into exactly one of the categories?


Lets's review with a simple example. I want to pick out a shirt to wear. I own 8
different cat shirts and 6 different Rocket Raccoon shirts. I might ask how
many ways I can pick a single shirt to wear. Because I can partition each choice
of which shirt to wear into either choosing a cat shirt or a Rocket shirt,
then the total number of ways to choose a shirt is the sum of ways to pick a
Cat shirt and ways to pick a Rocket shirt. Hence, there are :math:`8+6=14` ways I
can pick a shirt to wear.

There are a couple of characteristics of this example to point out. The first is that
every choice of shirt can be categorized as choosing a Cat or a Rocket shirt. This
makes sure that we are are not missing outcomes. The second is that there are no
t-shirts that are both Cat and Rocket shirts (although that would be amazing). This
makes sure that we are not counting a shirt more than once. Thus, we are counting
all of our shirts, and we are only counting a shirt once.

The AP is typically used for problems where the set of outcomes or events can be
categorized into sets that are easier to count. Consider the following problem.


We can consider what it might look like to write a program to list outcomes so as
to leverage the addition principle. Consider a problem like the following.

Problem: Username
~~~~~~~~~~~~~~~~~~~~~

  You are deciding on a username for social media. To keep things simple, you decide
  that it will have two letters and two numbers, where either the numbers come first
  (such as 79HI) or the letters come first (such as HI79). How many ways are there to
  create such a username?

Here, we can break the usernames into two cases, based on whether or not the numbers
come first. If the numbers come first, then there are :math:`10^2\times 26^2` ways to
create a username. If the letters come first, then there are :math:`26^2 \times 10^2`
ways to create a username. Hence, there are :math:`10^2\times26^2 + 26^2\times 10^2`
total ways to create a username.

The code below is meant to reflect this process and this case breakdown. In particular,
the two successive sets of nested for loops correspond to the two cases. In the
first set of loops, we compute the usernames that consist of numbers followed by
letters. In the second set of loops, we compute the usernames that consist of
letters followed by numbers.

Look at the code below. Before you run it, answer the following multiple choice
question.

.. mchoice:: AP_2
    :correct: c
    :answer_a: 135200
    :answer_b: 67600
    :answer_c: First 67600 then 135200
    :feedback_a: Incorrect.
    :feedback_b: Incorrect.
    :feedback_c: Correct.

    What do you expect the output of the code to be, when you run it?


.. activecode:: Usernames
    :coach:

    Numbers = [0,1,2,3,4,5,6,7,8,9]
    Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    counter=0

    for i in Numbers:
        for ii in Numbers:
            for j in Letters:
                for jj in Letters:
                    counter+=1
    print(counter)

    for k in Letters:
        for kk in Letters:
            for l in Numbers:
                for ll in Numbers:
                    counter+=1
    print(counter)


Problem: Book Genres
~~~~~~~~~~~~~~~~~~~~~~~~

  You are traveling on vacation and you decide to bring two books with you. Your
  three favorite series are Harry Potter (there are 7 HP books), Game of Thrones
  (there are 5 GoT books), and Lord of the Rings (there are 3 LOTR books). How many
  possibilities are there for which two books you take with you on vacation, if
  the books must be from different series?

.. mchoice:: AP_3
    :correct: a
    :answer_a: 7*5 + 7*3 + 5*3
    :answer_b: (7*5)^2 + (7*3)^2 + (5*3)^2
    :answer_c: 7*5*3
    :feedback_a: Correct
    :feedback_b: Incorrect. Your solution accounts for multiple orderings of the two books.
    :feedback_c: Incorrect. Your solution counts the way to order three books.

    Which of the following expressions counts the number of ways to bring two
    books from different genres with you?


.. parsonsprob:: AS_Parson1
    :numbered: left

    Arrange the lines below to create code to print all the ways to bring the books
    with you on vacation, so that the order of the books corresponds to the order of
    terms in 7*5 + 7*3 + 5*3.
    -----

    HP = ['HP1', 'HP2', 'HP3', 'HP4', 'HP5', 'HP6', 'HP7']
    GoT = ['GoT1', 'GoT2', 'GoT3', 'GoT4', 'GoT5']
    LOTR = ['LOTR1', 'LOTR2', 'LOTR3']
    =====
    for i in HP:
    =====
        for ii in GoT:
    =====
            print(i,ii)
    =====
    for j in HP:
    =====
        for jj in LOTR:
    =====
            print(j,jj)
    =====
    for k in GoT:
    =====
        for kk in LOTR:
    =====
            print(k,kk)



Subtraction Principle
==========================

Technically, we can think of the Subtraction Principle (SP) as an application of the
Addition Principle (AP). Just like you can do algebra on the expression :math:`y = x+3`
to find that :math:`y-3 = x`, we can subtract off outcomes or events that we don't want to count.
Try it for yourself.

.. mchoice:: SP_1
    :correct: b
    :answer_a: 60
    :answer_b: 18
    :answer_c: There is not enough information given in the problem
    :feedback_a: Incorrect, this is the number of non-face pairs.
    :feedback_b: Correct.
    :feedback_c: Incorrect, if a pair is not non-face, must they be a face pair?

    There are 78 possible pairs in a standard deck of cards (e.g. two 5s). Of these,
    60 are non-face pairs. How many face pairs are there?


.. mchoice:: SP_2
    :correct: a
    :answer_a: Yes
    :answer_b: No
    :feedback_a: Correct
    :feedback_b: Incorrect, what if two of your Toyotas are red?

    Suppose you have seven cars. Three of your cars are Toyotas, and two of your cars
    are red. Is it possible that you own three blue Hyundais?


.. mchoice:: SP_3
    :correct: c
    :answer_a: 62
    :answer_b: 61
    :answer_c: 60
    :answer_d: 59
    :feedback_a: Incorrect
    :feedback_b: Incorrect
    :feedback_c: Correct
    :feedback_d: Incorrect

    How many xs are there in the following table?

    == == == == == == == ==
    x  x  x  x  x  x  x  x
    x  OO x  x  x  x  x  x
    x  x  x  x  x  OO x  x
    OO x  x  x  x  x  x  x
    x  x  x  x  x  x  x  x
    x  x  x  x  x  x  OO x
    x  x  x  x  x  x  x  x
    x  x  x  x  x  x  x  x
    == == == == == == == ==

Did you count number of xs one by one? Probably not. Although that would work, an easier
method is to recognize that there are 8 rows and 8 columns, so there are 64
total entries. Plus, you know that there are only four entries that are not xs. How
many does this leave that are xs?

Let's state the Subtraction Principle so we have it on record.

Subtraction Principle Basic (SP)
-----------------------------------
  Suppose a set of events :math:`S` can be partitioned into two subsets of events
  :math:`A` and :math:`B` so that every event in :math:`S` belongs to either :math:`A`
  or :math:`B`, but not both. Then the number of events in :math:`B` is equal to the number of
  events in :math:`S` minus the number of events in :math:`A`.
  Alternatively, :math:`|S| - |A| = |B|`.

Let's unpack this statement using the x and OO example. We can partition the number
of entries in the table (the set :math:`S`) into those that are xs (the set :math:`B`)
and those that are OOs (the set :math:`A`). If we want to
count the number of xs (:math:`|B|`), we can do so by subtracting the number of
OOs from the total number of entries (:math:`|S|-|A|`).

Subtraction Principle Full (SP)
-----------------------------------
  Suppose a set of events :math:`S` can be partitioned into subsets
  :math:`S_1, S_2, \ldots , S_k`, where every event in :math:`S` belongs to exactly
  one of the subsets. Then the number of events in :math:`S_k` is the number of
  events in :math:`S` minus the number of events in all other subsets.
  Alternatively, :math:`|S|-|S_1| -|S_2| - \cdots - |S_{k-1}| = |S_k|`.

This sounds much more difficult than how the SP is applied in practice. The basic premise
is that we can overcount, and then 'uncount' the outcomes we don't want in our final tally.
Try the following problem.

This is how the subtraction principle is usually applied. You count a larger number
of events because it is easy (or familiar), and then you subtract, or "uncount",
the unwanted events.

Problem: Hotel
~~~~~~~~~~~~~~~~~~~~~~~~~~
  Steve and Royce arrive at a hotel that has 10 available rooms. They decide to book
  rooms so that they don't share a room. Examine the following code.

  .. activecode:: HotelCode_1
      :coach:

      Rooms = [1,2,3,4,5,6,7,8,9,10]
      counter=0

      for Steve in Rooms:
          for Royce in Rooms:
              if Steve!=Royce:
                  print(Steve, Royce)
                  counter+=1
      print(counter)

  .. mchoice:: H_1
      :correct: a
      :answer_a: Yes
      :answer_b: No
      :feedback_a: Correct.
      :feedback_b: Incorrect.

      Does the above code list and count all of the ways Steve and Royce can book
      rooms if they do not share a room?

Look at the list of outcomes when you run the code above. Some combinations of
numbers are missing. Which numbers are missing, and why does that make sense?
What would a missing number correspond to in terms of Steve and Royce booking a room?

.. mchoice:: H_2
    :correct: b
    :answer_a: Doubles, such as 11, 22, 33, etc. are missing. A double would mean that Royce is staying in two rooms.
    :answer_b: Doubles, such as 11, 22, 33, etc. are missing. A double would mean that both Royce and Steve are in the same room.
    :answer_c: Numbers like 01, 02, 03, etc. are missing. Such numbers would mean that no one is staying at the hotel.
    :feedback_a: Correct.
    :feedback_b: Incorrect.
    :feedback_c: Incorrect.

    Which numbers are missing from the list of all possible combinations, and what do they correspond to?

Let's use the SP to count the number of ways that Steve and Royce can book rooms if they
do not share a room. First, we note that there are :math:`10^2` ways for them to book
rooms. Steve has 10 different rooms he can be in, and for any room Steve is in
Royce also has 10 different rooms he can be in. Thus, there are :math:`10\times 10`
ways that they can be placed in hotel rooms. However, these choices also include
the options where they share a hotel room, which we do not want to count. There are
:math:`10` ways they can share a hotel room (1 way per available room). Hence, there
are :math:`10^2-10` ways that they can be booked into the hotel, if they don't want
to share a room.

.. shortanswer:: short-AS1

  In the space below, explain why expression :math:`10^2-10` makes sense in terms
  of the the code and the output of the code.

The SP can also be used in a more sophisticated way. Suppose we have two group of objects,
group A and group B, but there are some objects that are in both groups. If we wanted
to count the number of objects that are in either group A or group B, we can start
by adding the number of objects in A to the number of objects in B. However, this will
count anything that is both in A and in B twice because we count them once when we
count group A and a second time when we count group B. However, we can compensate
for this by subtracting the number of things that are in both A and B.

Problem: Cars, Revisited
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

  .. mchoice:: Car_1
      :correct: c
      :answer_a: 12.
      :answer_b: 35.
      :answer_c: 10.
      :feedback_a: Incorrect.
      :feedback_b: Incorrect.
      :feedback_c: Correct.

      Suppose you own seven Hondas and five red cars. If two of your Hondas are red, how many cars do you own that are either Hondas or are red?

Problem: Division
~~~~~~~~~~~~~~~~~~~~~~~
  How many of the numbers from 1 to 20 are divisible by 2 or 3?

  Solution:

    We notice that the numbers divisible by 2 are :math:`{2,4,6,8,10,12,14,16,18,20}`
    and the numbers divisible by 3 are :math:`{3,6,9,12,15,18}`. Thus, there are :math:`10`
    numbers divisible by 2 and :math:`6` numbers divisble by 3. However, we can't
    just add :math:`10 + 6` to find our final answer because some numbers are divisible by
    both 2 and 3. Hence, we need to subtract all numbers that are divisible by both
    2 and 3. Whenever a number is divisible by 2 and 3, it is a multiple of 6. Hence,
    the numbers divisible by 2 and 3 are :math:`{6,12,18}`. Thus, three numbers are divisible
    by 6 so there are :math:`10+6-3 = 13` numbers divisible by either 2 or 3.

Coordinating the AP and the SP:
----------------------------------

Problem: Wayside Hotel
~~~~~~~~~~~~~~~~~~~~~~~~~~~
  The Wayside Hotel is an infinitely tall hotel where the number of rooms on
  each floor is equal to the floor number (e.g. the 5th floor has 5 rooms and the 18th floor
  has 18 rooms).

  .. fillintheblank:: Hotel_1

      How many rooms are on or are below the 5th floor?

      - :15: Correct
        :x: Incorrect


  .. fillintheblank:: Hotel_2

      There are :math:`\frac{n(n+1)}{2}` rooms on or below the nth floor (this is a
      fact, you do not need to verify it). How many rooms are between the 7th and 12th
      floors, including the rooms on the 7th and 12th floors?

      - :57: Correct
        :x: Incorrect

  .. fillintheblank:: Hotel_3

      How many rooms are there on or below floor 20 whose floor numbers are
      divisible by either 2 or 3? Feel free to use the cell below to write a computer
      program that answers the question.

      - :137: Correct
        :x: Incorrect

  .. activecode:: Hotel_Code_1
      :coach:

      Rooms = range(21) # a list of the numbers from 1 to 20

      # feel free to add code


  .. fillintheblank:: Hotel_4

   The number of rooms on the even-numbered floors between floors 1 and :math:`2m`,
   inclusive, is :math:`m(m+1)`. The number of rooms that are on the odd-numbered floors
   between floors 1 and 20, including those on floor 1, is |blank|. Feel free to use the
   space below to write code to answer the question.

   - :100: Correct
     :x: Incorrect

  .. activecode:: Hotel_Code_2
      :coach:

      Rooms = range(21) # a list of the numbers from 1 to 20

      # feel free to add code

A Preview of Inclusion/Exclusion
----------------------------------
In these problems, we can use addition and subtraction together. We will talk about
this strategy later in a section on the Principle of Inclusion/Exclusion, which
uses this coordination of addition and subtraction more formally. 
