=========================================
The ABCDEs of Counting
=========================================

In this essay, we will use the Analysis Tool to investigate counting problems. The
analysis tool allows you to input a set of outcomes and count how many outcomes
start with or contain a sequence of characters. It also counts the total number of
outcomes.
Here, our focus will not be on determining how many outcomes there are. Instead,
we will focus on using the analysis tool to investigate regularity in the set of
outcomes, and how that regularity relates to ways of counting the outcomes.

All of the outcomes we discuss here will be constructed from three-letter combinations
of ``A, B, C, D, E``. First, let's demonstrate how to use the analysis tool.

Problem 1:
------------------

The code below will print all the ways to create a three-letter word from the letters
``A, B, C, D, E``, where letters can be repeated. The code is hidden, so you do not
need to write it yourself.

.. activecode:: WithRepeats
    :coach:

    # The hidden code will produce the outcomes.
    # Run this cell to print the outcomes.

    ====
    def NoSpaces(text):
        finalWord = str(text[0])
        for i in range(1,len(text)):
            finalWord += str(text[i])
        return finalWord

    letters = 'ABCDE'
    for i in letters:
        for j in letters:
            for k in letters:
                word = [i,j,k]
                print(NoSpaces(word))


After you run the above code, copy the printed list and paste it into the input
area in the analysis tool below.

.. analysistool:: WithRepeatsTool


After you paste the outcomes into the analysis tool, use the tool to verify there
are 125 outcomes. You can do this by pressing the button for count lines.

A mathematical expression that gives the number of outcomes is
:math:`5\times 5\times 5`. We will look about how regularity in the set of outcomes
relates to this expression.

.. fillintheblank:: WRQ1
    :casei:

    The number of outcomes that start with A is ``|blank|``.

    - :25: Correct
      :x: Incorrect. Try 25.

You can verify your answer using the "Count lines with prefix" button.

We can relate this question to the mathematical expression above by pointing out
how :math:`5\times 5\times 5` corresponds to five groups of five groups of five.
The list of outcomes is organized by which letter comes first. All outcomes starting
with an A are first, and all outcomes starting with an E are last. If we look only at
those outcome that start with A, we notice that they are organized by which letter
comes second. Within the outcomes starting with A, all the outcomes with second letter
A are listed first, and all the outcomes with second letter E are listed last. Finally,
if we specify the first two letters, say ``AA``, we see that the outcomes are listed
by the alphabetical order of the third letters. Hence, the outcomes really are
organized as five groups of five groups of five.

.. fillintheblank:: WRQ2
    :casei:

    The number of outcomes that start with B is ``|blank|``.

    - :25: Correct
      :x: Incorrect. Try 25.

.. fillintheblank:: WRQ3
    :casei:

    The number of outcomes that start with AA is ``|blank|``.

    - :5: Correct
      :x: Incorrect. Try 5.

.. fillintheblank:: WRQ4
    :casei:

    The number of outcomes that start with AB is ``|blank|``.

    - :5: Correct
      :x: Incorrect. Try 5.

.. fillintheblank:: WRQ5
    :casei:

    The number of outcomes that **contain** AB is ``|blank|``.

    - :10: Correct
      :x: Incorrect. Try 10.

.. fillintheblank:: WRQ6
    :casei:

    The number of outcomes that **contain** AA is ``|blank|``.

    - :9: Correct
      :x: Incorrect. Try 9.




Problem 2:
-----------------

The code below will print all the ways to create a three-letter word from
``A, B, C, D, E`` if no letter is repeated. Use the analysis tool to answer the
following questions.

.. activecode:: NoRepeats
    :coach:

    # Run this cell to print the outcomes.

    ====
    def NoSpaces(text):
        finalWord = str(text[0])
        for i in range(1,len(text)):
            finalWord += str(text[i])
        return finalWord

    letters = 'ABCDE'
    for i in letters:
        for j in letters:
            if j not in [i]:
                for k in letters:
                    if k not in [i,j]:
                        word = [i,j,k]
                        print(NoSpaces(word))




.. analysistool:: NoRepeatsTool

A mathematical expression for this set of outcomes :math:`5\times 4\times 3`.
Using a similar argument to the above question, answer the following.

.. fillintheblank:: NRQ1
    :casei:

    The outcomes can be organized into ``|blank|`` groups of ``|blank|``
    groups of ``|blank|``.

    - :5: Correct
      :x: Incorrect
    - :4: Correct
      :x: Incorrect
    - :3: Correct
      :x: Incorrect

.. fillintheblank:: NRQ2
    :casei:

    The number of outcomes that start with A is ``|blank|``.

    - :12: Correct
      :x: Incorrect

.. fillintheblank:: NRQ3
    :casei:

    The number of outcomes that start with AA is ``|blank|``.

    - :0: Correct
      :x: Incorrect

.. fillintheblank:: NRQ4
    :casei:

    The number of outcomes that start with AB is ``|blank|``.

    - :3: Correct
      :x: Incorrect

.. fillintheblank:: NRQ5
    :casei:

    The number of outcomes that **contain** AB is ``|blank|``.

    - :3: Correct
      :x: Incorrect

.. fillintheblank:: NRQ6
    :casei:

    The number of outcomes that **contain** AA is ``|blank|``.

    - :0: Correct
      :x: Incorrect


Problem 3:
----------------------

The code below will print all the ways to create a three-letter word from
``A, B, C, D, E`` if no letter is repeated and the letters appear in alphabetical
order (e.g. ``D`` will never come before ``A``).

.. activecode:: Greater
    :coach:

    # Run this cell to print the outcomes.

    ====
    def NoSpaces(text):
        finalWord = str(text[0])
        for i in range(1,len(text)):
            finalWord += str(text[i])
        return finalWord

    letters = 'ABCDE'
    for i in range(5):
        for j in range(i+1,5):
            for k in range(j+1,5):
                word = [letters[i],letters[j],letters[k]]
                print(NoSpaces(word))




.. analysistool:: GreaterTool

A typical mathematical expression to count these outcomes is
:math:`\frac{5\times 4\times 3}{3\times 2 \times 1}`. However, we argue that as
they are listed here the outcomes are better represented by a different expression.
Answer the following questions.

.. fillintheblank:: GTQ1
    :casei:

    The number of outcomes that start with AB is ``|blank|``,
    the number of outcomes that start with AC is ``|blank|``, and
    the number of outcomes that start with AC is ``|blank|``.

    - :3: Correct
      :x: Incorrect
    - :2: Correct
      :x: Incorrect
    - :1: Correct
      :x: Incorrect

.. fillintheblank:: GTQ2
    :casei:

    An expression for the number of outcomes **that start with A** is
    ``|blank|`` + ``|blank|`` + ``|blank``.

    - :3: Correct
      :x: Incorrect
    - :2: Correct
      :x: Incorrect
    - :1: Correct
      :x: Incorrect

.. fillintheblank:: GTQ3
    :casei:

    Similar to above, an expression for the number of outcomes **that start with B** is
    ``|blank|`` + ``|blank|``.

    - :2: Correct
      :x: Incorrect
    - :1: Correct
      :x: Incorrect

.. fillintheblank:: GTQ4
    :casei:

    Similar to above, an expression for the number of outcomes **that start with C** is
    ``|blank|``.

    - :1: Correct
      :x: Incorrect


.. fillintheblank:: GTQ5
    :casei:

    Combining the answers from the above questions, a mathematical expression that
    represents the outcomes is
    ``|blank|`` + ``|blank|`` + ``|blank|``. (The first blank is an expression
    for the outcomes
    starting with A, the second blank is for those starting with B, and the third
    blank is for those starting with C)

    - :3\+2\+1: Correct
      :x: Incorrect. Try 3+2+1.
    - :2\+1: Correct
      :x: Incorrect. Try 2+1.
    - :1: Correct
      :x: Incorrect. Try 1.

Problem 4:
-----------------------

The code below will print all the ways to create a three-letter word from
``A, B, C, D, E`` where the letters appear in alphabetical order (e.g. ``AAB``
can appear but ``BAA`` cannot).

.. activecode:: GreaterEq
    :coach:

    # Run this cell to print the outcomes.

    ====
    def NoSpaces(text):
        finalWord = str(text[0])
        for i in range(1,len(text)):
            finalWord += str(text[i])
        return finalWord

    letters = 'ABCDE'
    for i in range(5):
        for j in range(i,5):
            for k in range(j,5):
                word = [letters[i],letters[j],letters[k]]
                print(NoSpaces(word))




.. analysistool:: GreaterEqTool

We can find a mathematical expression for this problem in a similarly to how
we found an expression for the previous problem. We will focus on finding smaller
expressions for the outcomes that start with each letter.

.. fillintheblank:: GEQ1
    :casei:

    We can find an expression to count the outcomes that start with A by counting
    the number of outcomes for each second letter. This expression is
    ``|blank|`` + ``|blank|`` + ``|blank|`` + ``|blank|`` + ``|blank|``.

    - :5: Correct
      :x: Incorrect
    - :4: Correct
      :x: Incorrect
    - :3: Correct
      :x: Incorrect
    - :2: Correct
      :x: Incorrect
    - :1: Correct
      :x: Incorrect

.. fillintheblank:: GEQ2
    :casei:

    We can find an expression to count the outcomes that start with B by counting
    the number of outcomes for each second letter. This expression is
    ``|blank|`` + ``|blank|`` + ``|blank|`` + ``|blank|``.

    - :4: Correct
      :x: Incorrect
    - :3: Correct
      :x: Incorrect
    - :2: Correct
      :x: Incorrect
    - :1: Correct
      :x: Incorrect

.. fillintheblank:: GEQ3
    :casei:

    We can find an expression to count the outcomes that start with C by counting
    the number of outcomes for each second letter. This expression is
    ``|blank|`` + ``|blank|`` + ``|blank|`` .

    - :3: Correct
      :x: Incorrect
    - :2: Correct
      :x: Incorrect
    - :1: Correct
      :x: Incorrect

.. fillintheblank:: GEQ4
    :casei:

    We can find an expression to count the outcomes that start with D by counting
    the number of outcomes for each second letter. This expression is
    ``|blank|`` + ``|blank|``.

    - :2: Correct
      :x: Incorrect
    - :1: Correct
      :x: Incorrect

.. fillintheblank:: GEQ5
    :casei:

    We can find an expression to count the outcomes that start with A by counting
    the number of outcomes for each second letter. This expression is
    ``|blank|``.

    - :1: Correct
      :x: Incorrect

.. fillintheblank:: GEQ6
    :casei:

    Combining all of these expressions, an expression that counts all the outcomes is
    ``|blank|`` + ``|blank|`` + ``|blank|`` + ``|blank|`` + ``|blank|``.

    - :5\+4\+3\+2\+1: Correct
      :x: Incorrect
    - :4\+3\+2\+1: Correct
      :x: Incorrect
    - :3\+2\+1: Correct
      :x: Incorrect
    - :2\+1: Correct
      :x: Incorrect
    - :1: Correct
      :x: Incorrect
