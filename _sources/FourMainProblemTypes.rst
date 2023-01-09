=========================================
Combinatorics - Four Basic Problem Types
=========================================

In this essay, we give an overview of four kinds of problems that are common in
introductory combinatorics. The goal here is to highlight some interesting ways in
which these problems relate and to think of an overall structure for how to organize
these main problem types.

There are more details and examples provided in separate essays on Type 1, Type 2,
Type 3, and Type 4 problems, but here we offer an overview.

The table below shows the number of ways to arrange or select :math:`r` objects
from :math:`n` items (adapted from Tucker (2002)).

========================= =========================== =============================
          *                 Arrangement (ordered)       Selection (unordered)
------------------------- --------------------------- -----------------------------
Unrestricted Repetition    :math:`n^r`                 :math:`{n+r-1} \choose {r}`
No Repetition              :math:`\frac{n!}{(n-r)!}`   :math:`n \choose r`
========================= =========================== =============================

We offer canonical examples of these four problem types, and for each problem
type we describe a similar problem and offer some active code. The point is to
draw some similarities and differences between these problem types by focusing on
similar problems and contexts. Note, too, similarities and differences among the
code that generates outcomes for each type. We will discuss this later in the essay.
(Note, the following is adapted from Lockwood & De Chenne, 2020).

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type 1 Problems (Arrangement with repetition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
In the upper left of the two-by-two grid, we have arrangement with unrestricted repetition
problems, which we call Type 1 problems. An example is, `How many 3-character strings can
be made from the numbers 1 through 5, where repetition of characters is allowed?`
Here repetition is allowed, so an outcome like 222 is allowed, and order matters
because a string such as 123 is considered different from 213.

The code below produces all of the 3-character strings that can be made from the numbers
1 to 5 (answering the counting problem above). Run it to see the kinds of outcomes that
are produced, and to see what the total is.

Arrangements with repetition - Type 1 code sample
---------------------------------------------------

.. activecode:: FourPT_Type1_Code1
   :coach:
   :caption: 3-character strings, repetition allowed

   Numbers = [1,2,3,4,5]
   Counter = 0

   for i in Numbers:
       for j in Numbers:
           for k in Numbers:
               print(i,j,k)
               Counter = Counter + 1
   print(Counter)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type 2 Problems (Arrangement without repetition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, in the bottom left we have permutation problems, which we call Type 2 problems.
An example is, `How many 3-character strings can be made from the numbers 1 through 5,
where repetition of characters is not allowed?` Here order matters, as we are counting
strings of numbers, but the problem states that repetition is not allowed. Thus, we would
count strings like both 123 and 213, but not 223. Note, a problem involving arranging all
elements of a set (How many ways are there to arrange the numbers 1 through 5?) is a special
case of this kind of problem.

The code below produces all of the 3-character strings that can be made from the numbers
1 to 5, where repetition is not allowed (answering the counting problem above). Run it
to see the kinds of outcomes that are produced, and to see what the total is.

Arrangements without repetition - Type 2 code sample
-----------------------------------------------------

.. activecode:: FourPT_Type2_Code1
   :coach:
   :caption: 3-character strings, repetition not allowed

   Numbers = [1,2,3,4,5]
   Counter = 0

   for i in Numbers:
       for j in Numbers:
           if j != i:
               for k in Numbers:
                   if k != j and k != i:
                       print(i,j,k)
                       Counter = Counter + 1
   print(Counter)

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type 3 Problems (Selection without repetition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Next, in the bottom right we have combination, or selection, problems, which we
call Type 3 problems. An example of such a problem is, `How many 3-element subsets
can be made from the numbers 1 through 5?` Here order does not matter because we
are counting subsets (and order is irrelevant in sets), and repetition again is
not allowed. So, we would count {1,2,3} and {2,4,5}, but not {1,1,1} and also not both
{1,2,3} and {2,1,3}.

The code below produces all of the 3-character subsets that can be made from the numbers
1 to 5, where repetition is not allowed (answering the counting problem above). Run it
to see the kinds of outcomes that are produced, and to see what the total is.

Arrangements without repetition - Type 3 code sample
-----------------------------------------------------

.. activecode:: FourPT_Type3_Code1
   :coach:
   :caption: 3-character subsets, repetition not allowed

   Numbers = [1,2,3,4,5]
   Counter = 0

   for i in Numbers:
       for j in Numbers:
           if j > i:
               for k in Numbers:
                   if k > j:
                       print(i,j,k)
                       Counter = Counter + 1
   print(Counter)


~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Type 4 Problems (Selection with repetition)
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Finally, in the top right we have selection with repetition problems, which we call Type
4 problems. Here, order does not matter but repetition is allowed. An example of such
a problem is, `How many non-decreasing 3-character sequences can be formed from
the numbers 1 through 5, where repetition of characters is allowed?` Here since
repetition is allowed, we count outcomes like 111 and 222. However, because the sequences
are non-decreasing, while we would count 123 and 233, we would not also count 321 and 332.

The code below produces all of the 3-character multisets that can be made from the numbers
1 to 5, where repetition is allowed (answering the counting problem above). Run it
to see the kinds of outcomes that are produced, and to see what the total is.

Arrangements without repetition - Type 4 code sample
-----------------------------------------------------

.. activecode:: FourPT_Type4_Code1
   :coach:
   :caption: 3-character subsets, repetition not allowed

   Numbers = [1,2,3,4,5]
   Counter = 0

   for i in Numbers:
       for j in Numbers:
           if j >= i:
               for k in Numbers:
                   if k >= j:
                       print(i,j,k)
                       Counter = Counter + 1
   print(Counter)


We note further that for each of these four problem types, there tend to be corresponding
canonical types of outcomes – for example, permutations tend to count strings or
sequences, while combinations tend to count subsets. Problem types thus articulate
certain counting problems that satisfy certain constraints, and outcomes types represent
the actual outcomes that those problems tend to count.
Similarly, the slight variations in which conditional statements we use in the code
correspond to different kinds of outcomes we are counting. We have attempted to articulate
this fact in these examples and in the table below, which highlights corresponding
conditional statements with the outcomes that are being counted in each type of problem.


+--------------+---------------------+------------------------+
|              |       Arrangement   |       Selection        |
+--------------+---------------------+------------------------+
| Repetition   | nested for loops,   | nested for loops,      |
|              |  no restriction     |  j >= i                |
+--------------+---------------------+------------------------+
| No           | nested for loops,   | nested for loops,      |
| Repetition   |  j != i             |  j > i                 |
+--------------+---------------------+------------------------+

--------------------
Some More Practice
--------------------
In the following sections, we have some additional examples that highlight distinctions
between these problem types. As noted, more details are available in other separate
essays on Type 1, 2, 3, and 4.

.. dragndrop:: mixnmatch1
   :feedback:
   :match_1: How many outcomes are there if I flip a coin 5 times in a row? ||| Nested loops, No restriction
   :match_2: How many arrangements are there of the letters in the word ATOM?||| Nested loops, j != i
   :match_3: How many ways are there to pick three of 10 students to serve on a committee?||| Nested loops, j > i
   :match_4: how many ways are there to pick four donuts from six types of donuts||| Nested loops, j >= i

   Drag the description to the terms used to describe them.

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Differences between Type 1 and Type 2
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In distinguishing between Type 1 and Type 2 problems, it is important to keep in
mind what outcomes we are trying to count.

Consider the following two problems:

Problem A:
  We are going to give three different prizes to 8 students, where a student
  can win more than one prize. How many possible outcomes are there for the prizes
  to be distributed to the students?

Problem B:
  We are going to give a first, second, and third prize to 8 students, where
  student can win at most one prize. How many possible outcomes are there for the prizes
  to be distributed to the students?


A. Students can win more than one prize
----------------------------------------
Complete the code below to list all of the possibilities for Problem A above.

.. activecode:: FourPT_Type1_Code2
   :coach:
   :caption: Students can win more than one prize

   Students = [1,2,3,4,5,6,7,8]
   Counter = 0


B. Students can win at most one prize
--------------------------------------
Complete the code below to list all of the possibilities for Problem B above.

.. activecode:: FourPT_Type2_Code2
  :coach:
  :caption: Students can win at most one prize

  Students = [1,2,3,4,5,6,7,8]
  Counter = 0

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Differences between Type 2 and Type 3
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In distinguishing between Type 2 and Type 3 problems, it is again important to
keep in mind what outcomes we are trying to count. These problems are well known
as `permutations` (Type 2) and `combinations` (Type 3). For permutations, different
orders of elements in a given outcome result in distinct outcomes (so, something
like 123 is considered different than 132). For combinations, different orders of
elements in a given outcome do not result in distinct outcomes (so, something
like 123 is NOT considered different than 132). The problems below highlight this
distinction. As you write and run the code, look at the differences in outcomes.

Consider the following two problems:

Problem C:
  There are ten athletes competing in an Olympic event. How many ways can the
  athletes be awarded gold, silver, and bronze medals?

Problem D:
  There are ten athletes competing in an Olympic event. How many possibilities
  are there for which three athletes can end up with medals?

C. Athletes receiving gold, silver, and bronze medals
------------------------------------------------------
Complete the code below to list all of the possibilities for Problem C above.

.. activecode:: FourPT_Type2_Code3
   :coach:
   :caption: Athletes receive gold, silver, or bronze medals

   Students = [1,2,3,4,5,6,7,8,9,10]
   Counter = 0


D. Athletes receiving any medal
--------------------------------------
Complete the code below to list all of the possibilities for Problem 1 above.

.. activecode:: FourPT_Type3_Code2
  :coach:
  :caption: Athletes receive a medal

  Students = [1,2,3,4,5,6,7,8,9, 10]
  Counter = 0

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
Differences between Type 3 and Type 4
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In distinguishing between Type 3 and Type 4 problems, it is again important to
keep in mind what outcomes we are trying to count. In both of these cases, we
are selecting and not arranging, and so different orders of elements of an outcome
do not result in distinct outcomes. Here, the key difference is in whether or not
repetition is allowed. In Type 3 we are counting sets (where elements are not
repeated), and in Type 4 we are counting multisets (where elements are repeated).

Consider the following two problems:

Problem E:
  There are six different donuts remaining at the store, and I want to buy three of them.
  In how many ways can I do this?

Problem F:
  There are six different kinds of donuts at the store, and I want to buy three of them.
  In how many ways can I do this?

E. Donuts from last six remaining
------------------------------------------------------
Complete the code below to list all of the possibilities for Problem C above.

.. activecode:: FourPT_Type3_Code3
 :coach:
 :caption: Choosing donuts

 Students = [1,2,3,4,5,6]
 Counter = 0

F. Donuts from six kinds remaining
--------------------------------------
Complete the code below to list all of the possibilities for Problem 1 above.

.. activecode:: FourPT_Type4_Code2
   :coach:
   :caption: Choosing from types of donuts

   Students = [1,2,3,4,5,6]
   Counter = 0
