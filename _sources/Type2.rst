=======================================================
Type 2 - Arrangement without Repetition - Permutations
=======================================================

In this section, we present some tasks involving arrangement without repetition
problems. In our 2x2 grid, this is the cell in which repetition is not allowed,
and we are counting ordered outcomes (or arrangements). In problems like these,
we can employ multi-stage processes, where the number of options is reduced at
each stage, because repetition is not allowed.

For instance, consider the following problem: ::

  1. "How many arrangements are there of the numbers 1, 2, 3, and 4?"

Here, we have four positions, and we can employ a 4-stage process we consider
the number of options at each position. Note that once a number is selected
for the first position, that number now cannot be used again, so the number of
options for the second position is reduced by 1. The same is true for the third
and fourth positions. Because there is the same number of options no matter what
particular element was chosen at each stage, the number of options are
independent, and so we can use the multiplication principle. We get
:math:`4 \cdot 3 \cdot 2 \cdot 1 = 24` total outcomes.

Below is some code that generates all of the outcomes. The j != i is means j is
not equal to i. This ensures that the choice for the second position will not
be equal to the choice for the first position. Thus, these conditional statements
ensure that an element cannot be repeated.

Notice the outcomes themselves - repetition is not allowed (we do not get
something like 1 1 1 1 or 2 4 1 4), and we are counting ordered outcomes
(1 2 3 4 and 2 1 4 3 are listed as distinct outcomes).

Active Code
------------

.. activecode:: Type_2_CodeSample1
   :coach:
   :caption: Create some code

   Numbers = [1, 2, 3, 4]
   counter = 0

   for i in Numbers:
       for j in Numbers:
           if j != i:
               for k in Numbers:
                   if k != j and k != i:
                       for l in Numbers:
                           if l != k and l != j and l != i:
                               print(i,j,k,l)
                               counter += 1
   print(counter)

As another example, consider the following problem. ::

  2. How many ways are there to arrange three friends, John, Angel, and
  Dan in a row?

This is an arrangement without repetition problem because we are counting
ordered arrangements (John, Dan, Angel is a different arrangement than Angel,
Dan, John). And, once a friend is placed in a position, they cannot sit in
another position, and so repetition is not allowed. (That is, we will never
have an outcome like John, John, John, as that does not make sense in the
context of the problem.) How many arrangements are there of three friends?
What is a mathematical expression for this?

Below, remix code from the previous problem to write code that produces all possible
arrangements of your friends Angel, Dan, and John. Check to see if you get what you expect,
and look at the outcomes to see if the output makes sense.

Active Code
------------

.. activecode:: Type_2_CodeSample2
   :coach:


::

  3. How many ways are there to arrange the letters in the word ROCKET?

First, make a guess as to what you think the total will be. Write it here.

.. fillintheblank:: Type_2_fitb1
   :casei:

   I think that there are |blank| rearrangements of the letters in the word ROCKET

   -   :120: Correct.
       :x: Incorrect. The answer is 120.


Here is some code that will solve the problem. Do not run it, but answer questions
about it below.

Active Code
------------

.. activecode:: Type_2_CodeSample3
   :coach:
   :caption: Create some code

   Rocket = ['R', 'O', 'C', 'K', 'E', 'T']
   counter = 0

   for i in Rocket:
       for j in Rocket:
           if j != i:
               for k in Rocket:
                   if k != j and k != i:
                       for l in Rocket:
                           if l != k and l != j and l != i:
                               for m in Rocket:
                                   if m != l and m != k and m != j and m != i:
                                       for n in Rocket:
                                           if n != m and n != l and n != k and n != j and n != i:
                                               print(i,j,k,l,m,n)
                                               counter += 1
   print(counter)



Quick Check 1.1
----------------

.. mchoice:: Type_2_MC1_1
   :correct: b
   :answer_a: 6*6*6*6*6*6
   :answer_b: 6*5*4*3*2*1
   :answer_c: 6+5+4+3+2+1
   :feedback_a: Incorrect.
   :feedback_b: Correct.
   :feedback_c: Incorrect.

   What is an expression that is represented by the structure of the code and the structure of the output?

If you were to run the code above, think about what the output would be.

How many of the outcomes in the output of this code will start with "O" as the
first letter? How many will start with "ET"? Answer this question below.

.. fillintheblank:: Type_2_fitb2
   :casei:

   |blank| of the outcomes will start with "O", and |blank| of the outcomes will start with "ET".

   -   :120: Correct.
       :x: Incorrect. The answer is 120.
   -   :24: Correct.
       :x: Incorrect. The answer is 24.


General formula for Arrangements without Repetition of all :math:`n` elements
------------------------------------------------------------------------------

In the problems above, we arranged all of the elements in a given set (all of
the numbers, all of the friends, all of the letters). When we are arranging all
:math:`n` elements in a set, there is a general formula that we can use. In general,
if we have :math:`n` distinct objects, and we are arranging all :math:`n` of them where repetition
is not allowed, there are :math:`n` choices for the first position, :math:`n-1`
for the second, :math:`n-2` for the third, etc. It is useful to think of this as
a product of :math:`n` terms, :math:`n \cdot (n-1) \cdot (n-2) \cdot \ldots \cdot
3 \cdot 2 \cdot 1`. This expression, the product of the positive integers from
:math:`1` to :math:`n` is written as :math:`n!`.

This is called ":math:`n` factorial," and it both represents the mathematical expression
of the product of positive integers from :math:`1` to :math:`n`, and the number of arrangements
of :math:`n` distinct objects. For example, then, there are :math:`20!` ways to arrange 20
different books in a row on a shelf, there are :math:`150!` ways to rank 150 restaurants
in a given city, and there are :math:`26!` arrangements of the letters in the alphabet.

While :math:`n!` gives the total number of arrangements of an entire set of :math:`n` elements,
sometimes we want to arrange SOME but not ALL of the elements in a set.
Consider the following problem.

::

  4. Nine horses compete in a race, and there will be a first, second, and third
  prize given (assume no ties). How many possibilities are there for how prizes are
  distributed to the horses?

Note in this case, we only want to count arrangements of 3 of the 9 horses.
Here we have a 3-stage process, and our number of options at each stage are
reduced by 1. In particular, we have 10 options for who receives first place, 9
options for second (because whichever horse placed first cannot also place second),
and 8 options for third. Our expression is :math:`9 \cdot 8 \cdot 7 = 504`.

Write some code to solve this problem (remixing code from previous problems if
you wish).

.. activecode:: Type_2_CodeSample4
   :coach:
   :caption: Create some code to answer the Horse Race problem



.. shortanswer:: short-ex1

   In the space below, explain how you know how many nested for loops your code
   should have.

::

  5. There are 8 possible class projects and four teams of students who will work on those
  projects. In how many ways can the projects be assigned to the students if
  each team works on one project, and no two teams can work on the same project?

We consider a four-stage process of assigning a project to each of four different
teams. There are 8 options for which project the first team gets, then 7 for the
second team since projects cannot be repeated, then 6 for the third and 5 for
the fourth. Thus our expression is :math:`8 * 7 * 6 * 5 = 1680`.

Solve the following Parson's problem to create code that generates all 1680 possibilities
for assigning projects to teams of students.


.. parsonsprob:: Type_2_Parson1
    :numbered: left

    Arrange the lines below to create code to print all the possible outcomes for
    assigning 8 possible projects to 4 teams of students.
    -----

    Projects = ['P1','P2','P3','P4','P5','P6','P7','P8']
    =====
    counter = 0
    =====
    for i in Projects:
        for j in Projects:
    =====
            if j!=i:
                for k in Projects:
    =====
                    if k!=j and k!=i:
                        for l in Projects:
    =====
                            if l!=k and l!=j and l!=i:
                                print(i,j,k,l)
                                counter += 1
    =====
    print(counter)


General Formula for Arrangements without Repetition
----------------------------------------------------

Notice that there is a commonality among the mathematical expressions that solve
this particular kind of problem. In general, if we have :math:`n` distinct objects, and
we are arranging :math:`r` of them where repetition is not allowed, there are :math:`n` choices
for the first position, :math:`n-1` for the second, :math:`n-2` for the third, etc. It is
useful to think of this as a product of :math:`r` terms, :math:`n \cdot (n-1) \cdot (n-2)
\cdot \ldots \cdot (n-r+1)`. This expression is sometimes denoted as :math:`P(n,r)`` or
:math:`_nP_r`, where :math:`P` stands for permutation. Note that this product can
be rewritten efficiently as a ratio of two factorials, because as terms cancel we
get the desired product: :math:`\frac{n!}{(n-r)!}`

In terms of coding problems like these, notice that we can have :math:`n` elements in
our initial list, and we have :math:`r` nested for loops with the restriction that
elements cannot be repeated. These correspond to the :math:`r` stages in our counting
process, where at each stage we are cycling through all :math:`n` options in our list,
excluding elements that cannot be repeated as we go.

As is often the case, most problems will not be only a direct application of this
formula, but rather they will involve or incorporate that formula in some way
into a broader problem. Here we offer some examples of how this formula might
arise or be used in problems.

::

  6. How many arrangements of the letters in the word CATTLE have the Ts together
  at the beginning or the end of the word?

Here we have two cases - when the Ts are at the beginning of the word and when
the Ts are at the end of the word. If the Ts are at the beginning, there are 4!
ways to arrange the rest of the letters, and if the Ts are at the end, there are
4! ways to arrange the rest of the letters. We can add these two distinct cases,
so we get a final expression of :math:`4! + 4! = 48`. The program below lists these
outcomes.

.. activecode:: Cattle
    :coach:

    letters = ['C','A','L','E']
    counter=0

    for i in letters:
        for j in letters:
            if j!=i:
                for k in letters:
                    if k!=i and k!=j:
                        for l in letters:
                            if l!=i and l!=j and l!=k:
                                print('T','T',i,j,k,l)
                                counter+=1
    for a in letters:
        for b in letters:
            if b!=a:
                for c in letters:
                    if c!=a and c!=b:
                        for d in letters:
                            if d!=a and d!=b and d!=c:
                                print(a,b,c,d,'T','T')
                                counter+=1
    print(counter)


::

  7. You have 10 different hardcover books and 8 different paperback books.
  How many ways are there to arrange 3 hardback books and 5 paperback books if
  each kind of book has to be in a block together?



.. parsonsprob:: PP_books
   :numbered: left

   Solve the following Parson's Problem for this question.
   -----

   Hardcover = ['H1','H2','H3','H4','H5','H6','H7','H8','H9','H10']
   Paperback = ['P1','P2','P3','P4','P5','P6','P7','P8']

   =====
   counter = 0
   =====
   for i in Hardcover:
       for j in Hardcover:
           if j != i:
   =====
               for k in Hardocver:
                   if k!=j and k!= i:
   =====
                       for l in Paperback:
                           for m in Paperback:
                               if m!= l:
   =====
                                   for n in Paperback:
                                       if n != m and n!= l:

   =====
                                           print(i,j,k,l,m,n)
                                           counter +=1
   =====
   for i in Paperback:
       for j in Paperback:
           if j != i:
   =====
               for k in Paperback:
                   if k!=j and k!= i:
   =====
                       for l in Hardcover:
                           for m in Hardcover:
                               if m!= l:
   =====
                                   for n in Hardcover:
                                       if n != m and n!= l:
   =====
                                           print(i,j,k,l,m,n)
                                           counter +=1
   =====
   print(counter)


Here we have two cases - either the hardcover books are first, or the paperback
books are first. In the first case, we have a two-stage counting process of first
arranging the three hardcover books (there are :math:`\frac{10!}{(10-3)!}` such
arrangements) and then arranging the paperback books (there are :math:`\frac{8!}{(8-5)!}`
such arrangements). Because for each of those stages, the number of choices is
independent, we can use the multiplication principle. Thus, the number of arrangements
with hardcover then paperback books is :math:`P(10,3)\cdot P(8,5)`, or :math:`\frac{10!}{(10-3)!}
\cdot \frac{8!}{(8-5)!}.`

The second case is similar - first we arrange paperback books (:math:`\frac{8!}{(8-5)!}`),
then we arrange hardcover books :math:`\frac{10!}{(10-3)}!`. Again we use the
multiplication principle, so the number of arrangements with paperback then
hardcover books is :math:`P(8,5) \cdot P(10,3)`, or :math:`\frac{8!}{(8-5)!} \cdot \frac{10!}{(10-3)!}.`

For the total, we add both cases, so our total is :math:`\frac{10!}{(10-3)!} \cdot
\frac{8!}{(8-5)!} + \frac{8!}{(8-5)!} \cdot \frac{10!}{(10-3)!} = 483840.`
