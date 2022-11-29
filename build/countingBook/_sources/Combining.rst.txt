=================================================
Coordinating Fundamentals of Counting Problems
=================================================

We can solve a large number of counting problems by combining what we know
about permutations, combinations, multiplication, and addition/subtraction.
Let's review how we typically use these four things.

.. dragndrop:: mixnmatch
   :feedback: Not quite
   :match_1: Number of ways to order m of n distinct objects|||P(n,m)
   :match_2: Operator for multi-step processes|||Multiplication
   :match_3: Number of ways to select m of n distinct objects|||C(n,m)
   :match_4: Operator for multi-case processes|||Addition/Subtraction

   Drag the description to the terms used to describe them.

For this essay, we have included some functions to help you coordinate multiple
types of common counting objects in a single problem.

New Functions for Counting
--------------------------------

When coordinating fundamentals of counting problems, permutations of characters
and combinations of characters become important building blocks. To make the process
of writing a computer program to solve a counting problem easier, we introduce
three new functions.

The function ``Prod(Characters, Number)`` takes two inputs and returns arrangements where
repetition is allowed. The input ``Characters`` are the objects that are to be arranged,
and ``Number`` is the number of objects we are arranging. For example, if
``Characters = [1,2]`` and ``Number = 2``, then this would return the outcomes
``(1,1), (1,2), (2,1), (2,2)``.

The function ``Perms(Characters, Number)`` takes two inputs and returns permutations.
The two inputs are ``Characters``, which is a list of the objects being permuted, and
``Number``, which is the number of these objects we want to permute. For example, if
``Characters = [1,2]`` and ``Number = 2``, then this would return the outcomes ``(1,2), (2,1)``.

The function ``Combs(Characters, Number)`` takes two inputs and returns combinations.
The two inputs are ``Characters``, which is a list of the objects used to make combinations,
and ``Number``, which is the number of objects in each combination. For example, if
``Characters = [1,2]`` and ``Number = 2``, then this would return the outcome ``(1,2)``.

Run the following three blocks of code, and predict what each will do.

.. activecode:: Coordinating0
    :coach:
    :include: Function-Creations

    Letters = 'ABCDE'

    Product = Prod(Letters, 3)
    Show(Product,125)

.. activecode:: Coordinating1
    :coach:
    :include: Function-Creations

    Letters = 'ABCDE'

    Permutations = Perms(Letters,3)
    Show(Permutations,60)

.. activecode:: Coordinating2
    :coach:
    :include: Function-Creations

    Letters = 'ABCDE'

    Combinations = Combs(Letters,3)
    Show(Combinations,10)

Because the counting problems we will be solving in this essay have large numerical
answers, we will not print every outcome. Instead, we have included the function
``Show(Problem, number)``. This function takes in ``Problem``, which is a generator
that generates all the outcomes of the counting problem (more on this later). It also
takes in ``number``, which is the number of outcomes that will be printed off.

Example Problem
~~~~~~~~~~~~~~~~~~~~~~~~
You are buying coffee and doughnuts for your friends. The deli you go to has 5 different
types of doughnuts and 4 different types of coffee. How many ways are there to choose
2 types of doughnuts and 2 types of coffee to buy? (You do not need to account
for the number of each type you are buying.)

Examine the code below, and determine if it solves the problem.

.. activecode:: CoffeeDoughnuts
    :coach:
    :include: Function-Creations

    def CoffeeDoughnuts(): # A generator for the outcomes
        Doughnuts = [1,2,3,4,5]
        Coffee = [1,2,3,4]

        for i in Combs(Doughnuts, 2):
            for j in Combs(Coffee, 2):
                yield (i,j)

    Show(CoffeeDoughnuts(), 10)
    Count(CoffeeDoughnuts)

In the above example, we have defined a generator ``CoffeeDoughnuts()`` that creates
all outcomes of the problem. The function ``Count(Generator)`` takes in a generator
and counts everything it generates.

A note on generators--We will create and use generators in this essay because the problems
we are counting are large. Generators will create the outcomes one at a time, and won't store
them in memory. If a counting problem has 10 million outcomes, this means that
we won't need to store 10 million outcomes in memory. To create a generator, you
can mimic the example above. You start by defining the name of your generator, like
``def CoffeeDoughnuts():`` and inside that definition you write the process to create
the outcomes. Rather than printing the outcome, you will use the word ``yield``. To count the
number of outcomes, you use the function ``Count(Generator)``, where ``Generator`` is the
name of your generator. Syntax is important with the ``Count`` function. A statement like
``Count(Generator())`` will return an error. If you include parameters in the
definition of your generator, then you can add the parameters after the name of
the generator. For example, if we changed the definition of CoffeeDoughnuts so that
we inputed the number of coffee and donuts (e.g. ``CoffeeDoughnuts(4,5)``), we
would write ``Count(CoffeeDoughnuts, 4, 5)``.

Generator Practice: Books
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this problem, we will practice writing a generator to solve a simple problem.
Suppose you have 10 books. How many ways are there for you to arrange three of them on
a shelf. Write a generator that will produce these outcomes. Then, use the ``Show``
function to print the first 10 outcomes, and use the ``Count`` function to count
the total number of outcomes.

.. activecode:: Books1
    :coach:
    :include: Function-Creations

    # Include your code here

Generator Practice: License Plates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

In this problem, we will practice using the ``Perms`` function in a generator. Suppose
a license plate consists of three letters (from the English alphabet) followed by
three digits (from 0 to 9). How many license plates are there with no repeated letters,
and where the numbers are in increasing order? Write a generator to create the outcomes, then use the ``Show``
function two print the first 20 outcomes, and use the ``Count`` function to determine
the total number of outcomes.

.. activecode:: License-Plate
    :coach:
    :include: Function-Creations

    # I plan on erasing this code before this goes live

    def LicensePlates():

        Letters = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        Numbers = '0123456789'

        for i in Perms(Letters,3):
            for j in Combs(Numbers,3):
                yield (i,j)

    Show(LicensePlates(),20)
    Count(LicensePlates)

Example Problem 0:
--------------------
  Suppose you have eight friends. If you have three unique hats and three identical
  t-shirts, how many ways can you distribute the hats and t-shirts to your friends
  if nobody can get multiple t-shirts or hats, but they can get both a t-shirt
  and a hat?

We can think about a solution where we first distribute the hats to our friends,
and then we distribute the t-shirts to our friends. There are :math:`P(8,3)` ways
to distribute the hats, and there are :math:`C(8,3)` ways to distribute the t-shirts.
Hence, there are :math:`P(8,3)\times C(8,3)` ways to distribute the hats and
t-shirts.

Write some code that will generate these outcomes.



.. activecode:: HatsShirts0
    :coach:
    :include: Function-Creations

    # I would remove this code before this goes live
    def HatsShirts():
        Friends = [1,2,3,4,5,6,7,8]

        for i in Perms(Friends,3):
            for j in Combs(Friends, 3):
                yield (i,j)

    Show(HatsShirts(),10)
    Count(HatsShirts)


Example Problem 1:
----------------------
  Suppose you have eight friends. If you have three unique hats, and three identical
  t-shirts, how many ways can you distribute the hats and t-shirts to your friends
  if nobody receives both a hat and a t-shirt?

We can think about a solution where we first distribute the hats to our friends,
and then we distribute the t-shirts to those friends who didn't receive a hat. There
are :math:`P(8,3)` ways to distribute the hats to our friends, because the hats
are distinct. When we select friends that will receive the t-shirts, we must remove
those friends that received the hats from consideration.
No matter which friends we give the hats to, there will be five friends
who don't receive one. Hence, there are :math:`C(5,3)` ways to distribute the t-shirts
to our friends **for each way** to distribute the hats. Therefore, the total number
of ways to distribute the hats and t-shirts is :math:`P(8,3)\times C(5,3) = 3360`.

We can code these possibilities too. Examine the code below, predict what line
5 accomplishes in relation to the above counting process.

.. activecode:: HatsShirts
    :coach:
    :include: Function-Creations


    def HatsShirts():
        Friends = [1,2,3,4,5,6,7,8]

        for Get_Hats in Perms(Friends, 3):            # Ways to distribute the hats
            Unchosen = Remove(Friends, Get_Hats)      # Create set of friends who didn't receive a hat
            for Get_Tshirts in Combs(Unchosen,3):     # Ways to distribute the t-shirts
                yield (Get_Hats, Get_Tshirts)         # This is a long list
    Show(HatsShirts(),10)
    Count(HatsShirts)



New Counting Function: Remove
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Many solutions to counting problems involve breaking a process into steps, such as
first distributing hats and then distributing t-shirts. In some of these solutions,
the choices in the first step are removed from the possible choices in later steps.
We have created the function ``Remove(BigList, SmallList)`` which takes in two lists (or tuples),
and returns the set difference of the lists. Specifically, ``Remove(BigList, SmallList)``
will return a list that contains everything in ``BigList`` that is not also in ``SmallList``.
Run the following code to see an example.

.. activecode:: Remove
    :coach:
    :include: Function-Creations

    A = [1,2,3,4,5,6,7,8,9,10]
    B = [2,5,7,8]

    print(Remove(A,B))



Example Problem 2:
--------------------------
  In how many ways can we create a 3-letter password from the letters A, B, C, D, and E if
  the password must contain at least one E?

Examine the solutions below. Which one(s) is/are correct?

Solution 1:
~~~~~~~~~~~~~~~~

  Since the password must contain at least one E, we can start by choosing if the first,
  second, or third character must be an E. There are three ways to make this choice.
  By selecting which character must be an E, then our password will contain an E
  no matter the choices we make for the other characters. Hence, there are 5 possible choices
  for each of the two remaining positions. Therefore, there are :math:`3\times 5^2` ways
  to create these passwords.

  .. activecode:: EPasswords1
      :coach:
      :include: Function-Creations

      # I really need to go back and make this code easier to parse
      def E_Passwords():
          positions = [0,1,2]
          Letters = ['A', 'B', 'C', 'D', 'E']

          for i in positions:
              for j in Letters:
                  for k in Letters:
                      password = ['','','']
                      other_positions = Remove(positions,[i])
                      password[i] = 'E'
                      password[other_positions[0]] = j
                      password[other_positions[1]] = k
                      yield(password)
      Show(E_Passwords(),10)
      Count(E_Passwords)

Solution 2:
~~~~~~~~~~~~~~~~~

  Since the passwords contain at least one E, we can break the outcomes into cases
  that depend on the number of Es. If the password contains exactly one E, then there
  are 3 ways to choose the position of the E, and for every position of the E there
  are :math:`4^2` ways to choose the remaining letters. Hence, there are :math:`3\times 4^2`
  ways to choose passwords that contain exactly one E. Similarly, for passwords that contain
  two Es there are 3 ways to choose which positions contain an E, and there are 4 ways to choose
  the remaining letter. Thus, there are :math:`3\times 4` ways to create a password with
  exactly two Es. Finally, there is only one way to create a password that contains
  exactly three Es. Therefore, there are :math:`3\times 4^2 + 3\times 4 + 1` ways to create the
  passwords.

  .. activecode:: EPasswords2
      :coach:
      :include: Function-Creations

      # wow this code is a mess, and I plan on cleaning it up
      def E_Passwords():
          positions = [0,1,2]
          Letters_No_E = ['A', 'B', 'C', 'D']

          for i in [1,2,3]:
              for j in Combs(positions, i):
                  for k in Prod(Letters_No_E, 3-i):
                      password = ['','','']
                      Non_E_Positions = Remove(positions, j)
                      for E_place in j:
                          password[E_place] = 'E'
                      for x in range(len(Non_E_Positions)):
                          password[Non_E_Positions[x]] = k[x]
                      yield(password)
      Show(E_Passwords(),10)
      Count(E_Passwords)

Solution 3:
~~~~~~~~~~~~~~~~
  To find all the passwords with at least one E, we count all the passwords that
  may or may not have an E, and then subtract the number of passwords that don't
  contain an E. There are :math:`5^3` ways to create a password without a restriction
  on the number of Es. There are :math:`4^3` ways to create a password without an E. Hence,
  there are :math:`5^3 - 4^3` total passwords that contain at least one E.

  .. activecode:: EPasswords 3
      :coach:
      :include: Function-Creations

      # I need to clean up this code too
      Letters = ['A', 'B', 'C', 'D', 'E']
      Letters_No_E = ['A', 'B', 'C', 'D']

      All_Passwords = []
      for i in Prod(Letters,3):
          All_Passwords.append(i)

      No_E_Passwords = []
      for j in Prod(Letters_No_E,3):
          No_E_Passwords.append(j)

      E_Passwords = Remove(All_Passwords, No_E_Passwords)

      print(len(E_Passwords))



Example Problem 3:
----------------------
  (Adapted from **Introduction to Combinatorics** by Wallis and George, 2011) A popular
  portable gaming console comes in six different colors. In how many ways can we buy three
  consoles, if any consoles of the same color are considered the same?

.. mchoice:: Video-James
    :correct: b
    :answer_a: Solution 1
    :answer_b: Solution 2
    :answer_c: Both are correct
    :feedback_a: Incorrect
    :feedback_b: Correct
    :feedback_c: Incorrect

    Read the solutions below. Which solution(s) is/are correct?


Solution 1:
  We can solve this by pretending different arrangements of the consoles are distinct,
  and then dividing by the number of ways to arrange the consoles. If the consoles
  were distinct, then there would be :math:`6^3` ways to create an arrangement (six
  colors for each console). However, for any three consoles there are :math:`3!` to arrange
  them. Thus, the expression :math:`6^3` counts each choice exactly :math:`3!` times,
  so we can divide by this number to make sure we only count each choice once.
  Therefore, there are :math:`\frac{6^3}{3!}` ways to select three consoles.

[Do we want to use a different incorrect solution? I'm not sure the students
will have thought deeply about the division principle, and I don't want their first
example of it be an inappropriate usage]

Solution 2:
  We can solve this by breaking the outcomes into the number of colors we buy. If we
  buy three consoles of the same color, there are only 6 ways to choose that color.
  If we buy two consoles of the same color, and one of a different color, then there
  are 6 ways to select the color for the pair and 5 ways to select the color of the
  other console, for a total of :math:`6\times 5` ways. If we have three consoles all
  of different color, then there are :math:`{6\choose 3}` ways to select the colors. Thus,
  there are a total of :math:`6 + 6\times 5 + {6\choose 3}` ways to select consoles.

[Insert discussion of these solutions, and the ways the outcomes are encoded]

[Insert computer programs]


Encoding Outcomes
----------------------------

A helpful first step when solving counting problems is to determine how the outcomes to be
counted might be encoded. What we mean by this is essentially how might we
write an outcome on a piece of paper. What will they look like? What are some
possible outcomes? What are some things that are not outcomes?

Consider this example.

Encoding Practice: Books
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
  Suppose I have 5 books, and I am thinking about bringing
  some of these books with me on vacation. How many ways are there to take some, or none,
  of my books with me?

  One way to encode these outcomes is to label my books as the numbers :math:`\{ 1,2,3,4,5\}`,
  and then take any subset (including the empty subset and the whole set) as the
  outcomes. This way, the outcome :math:`\{ 2, 4\}` represents taking books 2 and 4,
  and the outcome :math:`\{ 3, 4, 5\}` represents taking books 3, 4, and 5. If I wanted
  to count the total number of outcomes, I could break the outcomes into cases that
  depend on the number of books being taken, and then count each case separately. In
  this case, this expression would be
  :math:`{5\choose 0} + {5\choose 1} +{5\choose 2} +{5\choose 3} +{5\choose 4} +{5\choose 5} = 32`.
  The code below counts these outcomes.

  .. activecode:: BooksEx1
      :coach:
      :include: Function-Creations

      def Books():
          books = [1,2,3,4,5]

          for i in range(5+1): # Determine number of books taken
              for j in Combs(books,i): # Which books are taken
                  yield(j)

      Show(Books(),20) # Print the first 20 outcomes
      Count(Books)

  This is a perfectly reasonable way to count all the way to bring books on vacation,
  but calculating the total number of ways by hand becomes progressively more
  difficult the more books we have. Consider another way of encoding the outcomes.

  Another way of encoding an outcomes would be as a string of five 0s and 1s, such as
  01010. Here, each position represents a book, and a 0 represents leaving the book and
  a 1 represents taking the book with you. So, the outcome 01010 is the same as
  the outcome :math:`\{ 2,4\}`, and the outcome 00111 is the same as the outcome
  :math:`\{ 3,4,5\}`. This new method of encoding is a bit easier to count. We
  have five position, and each position can be occupied by one of two characters.
  Thus, there are :math:`2^5 = 32` possible outcomes.

  The code below counts these outcomes.

  .. activecode:: BooksEx2
      :coach:
      :include: Function-Creations

      def Books():
          NoYes = [0,1]

          for i in NoYes:
              for j in NoYes:
                  for k in NoYes:
                      for l in NoYes:
                          for m in NoYes:
                              yield(i,j,k,l,m)
      Show(Books(),20)
      Count(Books)

Encoding Outcomes Problems
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Problem 1:
++++++++++++++++++
  How many ways are there to arrange the letters in the word BANANA? Can you
  write a computer program to list these outcomes?

  .. activecode:: BANANA
      :coach:
      :include: Function-Creations

      # I would remove this code before it goes live

      def Banana():
          positions = [1,2,3,4,5,6]

          for a_positions in Combs(positions, 3):
              non_a_positions = Remove(positions, a_positions)
              for n_positions in Combs(non_a_positions, 2):
                  non_n_positions = Remove(non_a_positions, n_positions)
                  for b_position in Combs(non_n_positions, 1):
                      yield (a_positions, n_positions, b_position)
      Show(Banana(), 10)
      Count(Banana)

Problem 2: Coffee Run
~~~~~~~~~~~~~~~~~~~~~~~~~~
  Amy, Brady, and Carl are going to get some coffee. They invite their coworkers,
  Xander, Yan, and Zach to go with them. However, Xander, Yan, and Zach may decide
  not to get coffee, and they make this choice individually. If the coffee shop offers
  5 types of coffee, how many ways are there for people to get coffee?

  Consider the two solution methods below. Do both of them solve the problem?

  Solution 1:
    We can solve this problem in two stages: first, decide on which coffees Amy, Brady,
    and Carl receive, and second decide on who accompanies them and what coffees
    they get. Because these stages are independent, we can multiply the number of outcomes
    for each stage to get our final answer. Amy, Brady, and Carl can get coffees in
    :math:`5^3` ways. For the second stage, we can break into cases based on how many
    people get coffee, and for each stage determine which coffees the people get.
    We can encode these outcomes as a tuple that determines which people get coffee,
    followed by a tuple that determines which coffees they receive. For example,
    :math:`(Xander, Zach)(2,3)` could represent Xander getting coffee option 2 and Zach
    getting coffee option 3, and Yan deciding not to get a coffee. We can order the
    first tuple by the first letter of their names so that we do not overcount outcomes.
    There is one way for no people to get coffee. If one person gets
    coffee, then there are :math:`{3\choose 1}` ways to choose the person, and 5 ways for
    this person to get a coffee (:math:`{3\choose 1}\times 5` total ways). If two people
    get coffee, there is :math:`{3\choose 2}\times 5^2` ways to determine the people
    getting the coffee and which coffees they get. Finally, if all three people go there
    are :math:`{3\choose 3}\times 5^3` ways to decide which people get coffee, and which coffee
    they get. Hence, there are
    :math:`5^3\left( 1 + {3\choose 1}\times 5^1 + {3\choose 2}\times 5^2  + {3\choose 3}\times 5^3 \right)`
    ways to get coffee.

  Solution 2:
    Like before, our solution will have two stages. However, we will encode the second
    stage differently. In addition to the five coffee options, we can add the "no coffee" option,
    for a total of 6 options. For example, :math:`(2,0,3)` could represent Xander getting
    option 2, Yen not getting coffee, and Zach getting coffee 3. Hence, each person has 6 options
    in the second stage, and so there are :math:`5^3\times 6^3` ways to get coffee.


  Examine the codes below. How might you take the outcomes produced in the first code and
  turn them into outcomes produced in the second code? What about vice-versa?

  .. activecode:: CoffeeRun1
      :coach:
      :include: Function-Creations

      def CoffeeRun():
          CoffeeChoices = [1,2,3,4,5]
          People = ['Xander', 'Yan', 'Zach']

          for i in Prod(CoffeeChoices,3):
              for num in [0,1,2,3]:
                  for j in Combs(People, num):
                      for k in Prod(CoffeeChoices, num):
                          yield(i,j,k)

      Show(CoffeeRun(),20)
      Count(CoffeeRun)

  .. activecode:: CoffeeRun2
      :coach:
      :include: Function-Creations

      def CoffeeRun():
          CoffeeChoices = [1,2,3,4,5]
          CoffeeChoicesAddZero = [0,1,2,3,4,5]

          for i in Prod(CoffeeChoices,3):
              for j in Prod(CoffeeChoicesAddZero,3):
                  yield(i,j)

      Show(CoffeeRun(),20)
      Count(CoffeeRun)

Practice Problems:
-------------------------

Below are a number of practice problems. We have included space to write code if
you wish to do so.

1:
  You are hosting a barbeque, and six of your friends came. If you cooked two hamburgers,
  two hotdogs, and two veggie burgers, how many ways can you distribute these to your
  friends so that no friend receives more than one item?

  .. activecode:: P1
      :coach:
      :include: Function-Creations

      # Feel free to put code here

2:
  You are hosting a barbeque, and six of your friends came. If you cooked two hamburgers,
  two hotdogs, and two veggie burgers, how many ways can you distribute these to your
  friends so that no friend receives more than one item, and your vegetarian friend
  gets a veggie burger?

  .. activecode:: P2
      :coach:
      :include: Function-Creations

      # Feel free to put code here

3:
  In a standard deck of cards, the denominations are 2, 3, 4, 5, 6, 7, 8, 9, 10, Jack,
  Queen, King, and Ace. You are playing poker, where your hand has five cards in it.
  You have a 'pair' if exactly two of your cards are the same denomination.
  How many ways are there to have a pair?

  .. activecode:: P3
      :coach:
      :include: Function-Creations

      # Feel free to put code here

4:
  In poker, a three of a kind is where your hand has exactly three cards of the
  same denomination, and no other pairs. How many ways are there to get a three
  of a kind?

  .. activecode:: P4
      :coach:
      :include: Function-Creations

      # Feel free to put code here

5:
  How many ways are there to arrange the letters in the word SLEEPING?

  .. activecode:: P5
      :coach:
      :include: Function-Creations

      # Feel free to put code here

6:
  How many ways are there to arrange the letters in the phrase TACO CAT IN SLEEPY STEEPLE?

  .. activecode:: P6
      :coach:
      :include: Function-Creations

      # Feel free to put code here

7:
  You are friends with three pairs of twins. How many ways are there to choose three friends
  to go to lunch with you, if you are unable to distinguish between twins?

  .. activecode:: P7
      :coach:
      :include: Function-Creations

      # Feel free to put code here

End of Essay
--------------

.. activecode:: Function-Creations
    :coach:

    This area defines some functions that we are going to be using. No need to
    understand what is going on.
    ~~~~

    import itertools

    def Perms(Objects, Nums):
        return itertools.permutations(Objects, Nums)

    def Combs(Objects, Nums):
        return itertools.combinations(Objects,Nums)

    def Prod(Objects, Nums):
        return itertools.product(Objects, repeat=Nums)

    def Remove(A, B):
        # Creates a list that is essentially A\B in set theory
        return [i for i in A if i not in B]

    def isTrue(input):
    # Only used by the Show function
        return True

    def Show(GenFun, val1, val2=0, List=False, Condition=isTrue):
        Outcomes = []
        for i in range(max(val1, val2)):
            temp = list(next(GenFun))
            if i>=min(val1, val2) and Condition(temp) is True:
                Outcomes+=[temp]
        if List is False:
            for i in Outcomes:
                print(i)
        elif List is True:
            return(Outcomes)

    def Count(GenFun,*N):
        Object = GenFun(*N)
        print('Size: ', sum(1 for _ in Object))


Maybe include this problem:
(Adapted from **Introduction to Combinatorics** by Wallis and George, 2011) A student
wants to celebrate with two of her friends by going out to a restaurant. She has four
friends total, and one of these friends is under the age of 21. Of the seven restaurants
she could go to, only four of them permit people under the age of 21. In how many ways
could she select two friends and go to a restaurant.

  .. mchoice:: Restaurant
      :correct: a
      :answer_a: Yes
      :answer_b: No
      :feedback_a: Correct
      :feedback_b: Incorrect

      Examine the codes below. Will they both solve the above problem by listing
      all the ways to bring two friends to a restaurant (even if the outcomes may
      look different or be in a different order)? Feel free to run the code.

  .. activecode:: Restaurant1
      :coach:
      :include: Function-Creations

      # Friend 1 is underage
      # Under-age restaurants are 1,2,3,4

      def FriendsRestaurant():
          Friends = [1,2,3,4]
          Restaurants = [1,2,3,4,5,6,7]


          for group in Combs(Friends,2):
              for j in Restaurants:
                  if not (1 in group and j>4):
                      yield(group,j)
      Show(FriendsRestaurant(),10)
      Count(FriendsRestaurant)

  .. activecode:: Restaurant_Test
      :coach:
      :include: Function-Creations

      # This needs a bit of work
      # Intended to show the subtraction principle as literally subtracting one
      #       list from another, rather than using an if statement. Is this
      #       worth it? For the addition principle, we generally are adding two
      #       cases that are adjacent, but for the subtraction principle we
      #       use an if statement. What better aligns with combinatorics?

      def AllCombs():
          Friends = [1,2,3,4]
          Restaurants = [1,2,3,4,5,6,7]

          for group in Combs(Friends,2):
              for Restaurant in Restaurants:
                  yield (group, Restaurant)
      def BadCombs():
          Friends = [1,2,3,4]
          Restaurants = [1,2,3,4,5,6,7]

          for group in Combs(Friends,2):
              for Restaurant in Restaurants:
                  if 1 in group and Restaurant > 4:
                      yield (group, Restaurant)
      GoodCombs = Remove(AllCombs(), BadCombs())
      for i in range(10):
          print(GoodCombs[i])       #Show() and Count() only work with generators
      print(len(GoodCombs))

  .. activecode:: Restaurant2
      :coach:
      :include: Function-Creations

      Friends = [1,2,3,4]
      Restaurants = [1,2,3,4,5,6,7]
      Older_Friends = [2,3,4]
      Under_Age_Restaurants = [1,2,3,4]


      # If underage friend goes
      for i in Older_Friends:
          for j in Under_Age_Restaurants:
              print('Friends 1 and ', i, 'Restaurant', j)


      # If underage friend does not go
      for j in Combs(Older_Friends,2):
          for j in Restaurants:
              print('Friends', i, 'Restaurant', j)

  Consider the two solutions below. Do you think both are right?

  Jan's Solution:
    We can use the addition principle to solve this problem. Because friend 1 cannot
    go to certain restaurants, then we can split all the outcomes into whether or not
    friend is included. If friend 1 is included, there are 3 ways to select another
    friend. For each of these ways, there are 4 restaurants they could go to. Hence, there
    are :math:`3\times 4` ways to bring along friend 1. If friend 1 isn't included, then
    there are :math:`{3\choose 2}` ways to select two friends. For each of these ways,
    there are 7 restaurants they could go to. Hence, there are :math:`{3 \choose 2} \times 7`
    ways to go to a restaurant if friend 1 is not included. Therefore, there are
    :math:`3\times 4 + {3\choose 2}\times 7` ways to go to a restaurant.

  Jamie's Solution:
    We can use the subtraction principle for this problem. If we first count
    all the ways to bring two friends to the restaurant as if there were no restrictions,
    then we would only need to subtract the number of ways where friend 1 is brought
    to a restaurant that doesn't serve minors. If there were no restrictions, then there
    would be :math:`{4\choose 2}` ways to pick two friends, and for each choice there would
    be 7 restaurants to go to. Hence, there would be :math:`{4\choose 2}\times 7` ways to
    go to a restaurant. However, of these ways, there are :math:`3` ways to bring along friend 1,
    and for each of these options there are :math:`3` ways to bring friend 1 to a restaurant
    that doesn't serve minors. Thus, there are :math:`3\times 3` ways to bring friend 1 to a
    restaurant that doesn't serve minors. Therefore, there are :math:`{4\choose 2}\times 7 - 3\times 3`
    ways to go to a restaurant.

  [Insert a discussion about the way these outcomes are encoded]
