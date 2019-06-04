# Checkpoint

Try to complete all of the challenges and note the areas that you need additional study and practice.

#### !challenge

* type: code-snippet
* language: python3.6
* id: 3459d539-9aa2-4288-8b6f-1c9c9f30b801
* title: Practice with Functions 1

#### !question
Fill in the following function according to the doc string
#### !end-question

### !placeholder
```python
def get_divisors(n):
    '''
    This function calculates and returns all of the divisors of n, between 1 and
    n, inclusive.

    Parameters
    ----------
    n: {int}

    Returns
    -------
    divisors: {list} all divisors of n in order from smallest to largest
    '''
    pass
```
### !end-placeholder

### !tests
```python
import main
import random
import unittest


def make_examples():
    output = random.randint(20, 178)
    answer = [x for x in range(1, output + 1) if output % x == 0]
    return answer, output


class Test(unittest.TestCase):
    def test(self):
        for _ in range(10):
            result, test_case = make_examples()
            student_response = main.get_divisors(test_case)
            self.assertEqual(student_response, result)
```
### !end-tests

### !explanation

```python
def get_divisors(n):
    '''
    This function calculates and returns all of the divisors of n, between 1 and
    n, inclusive.

    Parameters
    ----------
    n: {int}

    Returns
    -------
    divisors: {list} all divisors of n in order from smallest to largest
    '''
    divisors = [1] # 1 divides all numbers
    stop = int(n / 2)
    for number in range(2, stop + 1):
        if n % number == 0:
            divisors.append(number)
    divisors.append(n) # all numbers divide themselves
    return divisors
```


### !end-explanation

#### !end-challenge

#### !challenge

* type: code-snippet
* language: python3.6
* id: 15254554-ce52-445f-8bce-4b619ac07b80
* title: Factorial again

#### !question
Fill in the following function according to the doc string
#### !end-question

### !placeholder
```python
def factorial(n):
    '''
    Returns the factorial of the input integer:
        n * (n - 1) * (n - 2) * ... * 2 * 1
    Parameters
    ----------
    n: {int} number to compute factorial of (must be greater than 0)

    Returns
    -------
    n!: {int} factorial of n

    '''
    pass
```
### !end-placeholder

### !tests
```python
import main
import random
import unittest
from math import factorial


def make_examples():
    output = random.randint(3, 20)
    answer = factorial(output)
    return answer, output


class Test(unittest.TestCase):
    def test(self):
        for _ in range(10):
            result, test_case = make_examples()
            student_response = main.factorial(test_case)
            self.assertEqual(student_response, result)
```
### !end-tests

### !explanation
There are a number of ways to do this, all with different advantages and
disadvantages. A fine way to calculate this is below (but if you did it another
way, great)

```python
def factorial(n):
    '''
    Returns the factorial of the input integer:
        n * (n - 1) * (n - 2) * ... * 2 * 1
    Parameters
    ----------
    n: {int} number to compute factorial of (must be greater than 0)

    Returns
    -------
    n!: {int} factorial of n

    '''
    output = 1
    for multiple in range(1, n + 1):
        output *= multiple
    return output
```

### !end-explanation

#### !end-challenge

<!-- Next Challenge -->

#### !challenge

* type: code-snippet
* language: python3.6
* id: 7f6f13ef-fd40-44f1-a1f1-500e7cfac9fb
* title: Is a number prime?

#### !question
Fill in the following function according to the doc string
#### !end-question

### !placeholder
```python
def is_prime(n):
    '''
    Return True if the input is prime, False otherwise
    Parameters
    ----------
    n: {int} input integer

    Returns
    -------
    is_prime: {bool} whether n is prime
    '''
    pass
```
### !end-placeholder

### !tests
```python
import main
import random
import unittest

def is_prime(n):
    if n == 2:
        return True
    for div in range(2, n // 2):
        if n % div == 0:
            return False
    return True

def make_examples():
    output = random.randint(2, 187)
    answer = is_prime(output)
    return answer, output


class Test(unittest.TestCase):
    def test(self):
        # test n=2 explicitly
        msg = "Remember that 2 is a prime number, is_prime should handle this edge case."
        self.assertEqual(main.is_prime(2), True, msg=msg)
        for _ in range(10):
            result, test_case = make_examples()
            student_response = main.is_prime(test_case)
            self.assertEqual(student_response, result)
```
### !end-tests

### !explanation

```python
def is_prime(n):
    '''
    Return True if the input is prime, False otherwise
    Parameters
    ----------
    n: {int} input integer

    Returns
    -------
    is_prime: {bool} whether n is prime
    '''
    if n == 2:
        return True
    for check in range(2, n // 2):
        if n % check == 0:
            return False
    return True
```

### !end-explanation

#### !end-challenge

<!-- Next Challenge -->

#### !challenge

* type: code-snippet
* language: python3.6
* id: febc112b-7c13-4555-872b-2adf35b071f3
* title: Next Perfect Square

#### !question

As you write your own functions you will often call other functions from within
them. Your task here is complete the function `next_perfect_square`.

A number is a perfect square if it is the square of an integer, e.g. 9 = 3 * 3.
For the following question, you have access to the function `is_perfect_square`,
which returns True if the number is a perfect square, and False if it is not.
Use this function to fill out the code stub below.

You do not have to write the `is_perfect_square` function, it exists in the
environment for you already.

#### !end-question

### !placeholder
```python
def next_perfect_square(number):
    '''
    Returns the next perfect square of the input number, if the input number
    is not a perfect square, returns -1.
    Ex:
    next_perfect_square(10)
    >>> -1
    next_perfect_square(9)
    >>> 16
    next_perfect_square(25)
    >>> 36
    next_perfect_square(37)
    >>> -1

    Parameters
    ----------
    number: {int}

    Returns
    -------
    next_perfect: {int} the next perfect square, or -1 if number is not a
    perfect square
    '''
    is_perfect_square(number)
```
### !end-placeholder

### !tests
```python
import main
import random
import unittest

def is_perfect_square(number):
    sqrt_num = number ** 0.5
    return sqrt_num == int(sqrt_num)

main.is_perfect_square = is_perfect_square

def make_examples():
    output = random.randint(5, 13984) ** 2
    if random.random() < 0.2:
        output = output + 1
    if not is_perfect_square(output):
        answer = -1
    else:
        answer = (output ** 0.5 + 1) ** 2
    return answer, output


class Test(unittest.TestCase):
    def test(self):
        for _ in range(15):
            result, test_case = make_examples()
            student_response = main.next_perfect_square(test_case)
            self.assertEqual(student_response, result)
```
### !end-tests

### !explanation

```python
def next_perfect_square(number):
    '''
    Returns the next perfect square of the input number, if the input number
    is not a perfect square, returns -1.
    Ex:
    next_perfect_square(10)
    >>> -1
    next_perfect_square(9)
    >>> 16
    next_perfect_square(25)
    >>> 36
    next_perfect_square(37)
    >>> -1

    Parameters
    ----------
    number: {int}

    Returns
    -------
    next_perfect: {int} the next perfect square, or -1 if number is not a
    perfect square
    '''
    if not is_perfect_square(number):
        return -1
    return (number ** 0.5 + 1) ** 2
```

### !end-explanation

#### !end-challenge


#### !challenge

* type: code-snippet
* language: python3.6
* id: d11b2e04-0959-4c75-b370-adf868f3af64
* title: Simulate coin flips

#### !question
Data scientists often encounter situations that can be thought of as random processes and it can be useful to simulate these processes to help confirm that things are working as expected (more on this in the unit on Probability). In this challenge you will simulate one of the simplest random processes: flipping a (biased) coin.

Fill in the following function according to the doc string. 

_Note_: Unlike most functions where a given input always yields the same output, using `random.random()` means that the output from this function varies, even when the input is the same. Consequently, it is impossible to know that your function is correct (in that it satisfies the doc string) without testing it many times. Therefore, the tests will check that _on average_ over many trials the number of heads and tails returned is as expected.
#### !end-question

### !placeholder
```python
def flip_coin(p=0.5):
    '''
    Using random.random() simulate flipping a coin where the probability of
    flipping a head is p.

    Parameters
    ----------
    p: {float} probability of flipping a head (must be between 0 and 1)

    Returns
    -------
    flip: {str} "H" if coin is heads, otherwise "T"
    '''
    pass

```
### !end-placeholder

### !tests
```python
import main
import random
import unittest


def make_examples():
    output = random.random()
    answer = None
    return answer, output


class Test(unittest.TestCase):
    def test(self):
        for _ in range(3):
            _, heads_prob = make_examples()
            heads = 0
            num_trials = 200000
            for _ in range(num_trials):
                flip = main.flip_coin(heads_prob)
                self.assertIn(flip, {'H', 'T'}, msg='result other than H or T returned')
                if flip == 'H':
                    heads += 1
            student_average = heads / num_trials
            msg = "Proportion of heads over {} trials is: {}. Expected: {}"
            self.assertAlmostEqual(student_average, heads_prob, places=2,
                                   msg = msg.format(num_trials, student_average, heads_prob))
```
### !end-tests

### !explanation
```python
import random

def flip_coin(p=0.5):
    '''
    Using random.random() simulate flipping a coin where the probability of
    flipping a head is p.

    Parameters
    ----------
    p: {float} probability of flipping a head (must be between 0 and 1)

    Returns
    -------
    flip: {str} "H" if coin is heads, otherwise "T"
    '''
    return 'H' if random.random() <= p else 'T'

```
### !end-explanation

#### !end-challenge

<!-- next challenge -->

#### !challenge

* type: code-snippet
* language: python3.6
* id: 3a3ea66d-4018-4416-bd62-9b399e251fac
* title: Sum to number

#### !question
Write a function which calculates how many pairs of numbers sum to a user
inputted value (default of 0).

Note: numbers are not consumed when included in a pair, so if you gave
the input `count_pair_sums([1, -1, 1], 0)` the answer would be 2. Both the
first 1 and the -1, and then the -1 with the second 1 contribute one pair
summing to zero. However, `count_pair_sums([1, 1, 0], 0)` would give 0, as
there is no pair which sums to zero. Some more examples are listed below
`count_pair_sums([1, 1, 0, 0], 0)`: 1
`count_pair_sums([7, 7, 8, 8], 15)`: 4
`count_pair_sums([1, 1, 1, 1], 2)`: 6
`count_pair_sums([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11)`: 9

#### !end-question

### !placeholder
```python
def count_pair_sums(arr, number=0):
    '''
    Given an array, find the count of how many pairs of numbers in the array sum
    to the input number

    Parameters
    ----------
    arr: {list} list of integers (positive and negative)
    number: number to see if pairs sum to (default 0)

    Returns
    -------
    {int} the number of pairs found that sum to given number
    '''
    pass
```
### !end-placeholder

### !tests
```python
import main
import random
import unittest

def count_pair_sums(arr, number=0):
    possibles = {}
    for num in arr:
        if num not in possibles:
            possibles[num] = 0
        possibles[num] += 1

    count = 0
    for num in arr:
        if number - num in possibles:
            count += possibles[number - num]

        if (number - num) == num:
            count -= 1

    return count // 2


def make_examples(n):
    pairs = [(([1, -1, 1], 0), 2),
             (([1, 1, 0], 0), 0),
             (([1, 1, 0, 0], 0), 1),
             (([7, 7, 8, 8], 15), 4),
             (([1, 1, 1, 1], 2), 6),
             (([10, 12, 10, 15, -1, 7, 6, 5, 4, 2, 1, 1, 1], 11), 9)]
    for example, answer in pairs:
        yield example, answer

    for _ in range(n):
        example = ([random.randint(-50, 50) for _ in range(25)],
                  random.randint(-50, 50))
        answer = count_pair_sums(*example)
        yield example, answer


class Test(unittest.TestCase):
    def test(self):
        for example, answer in make_examples(10):
            student_response = main.count_pair_sums(*example)
            self.assertEqual(student_response, answer)
```
### !end-tests

### !explanation
This problem has many possible solutions, but two will be discussed in detail to
give examples of improving on code. The most basic way to solve this problem
is to iterate over the array and then for each value iterate over the array
again and see if the values add to the input:

*Note: I will not include the function definition or doc string to make this easier to read*

```python
count = 0
for num in arr:
    for num2 in arr:
        if num + num2 == number:
            count += 1
return count
```
However this will give the wrong answer. For example, in the first example
`[1, -1, 1], 0`:  
you get for `(num, num2)`:  
    `(1, 1), (1, -1), (1, 1), (-1, 1), (-1, -1), (-1, 1), (1, 1), (1, -1), (1, 1)`
4 of these pairs sum to zero, so you get 4 when the answer is 2. You are double
counting (basically looking at both `(num, num2)` and `(num2, num)`). This
problem is compounded when the sum is twice an entry, as some of the pairs you
are getting are actually `(num, num)`. You can resolve this in the following
way:

```python
count = 0
for index, num in enumerate(arr):
    for index2, num2 in enumerate(arr):
        if index == index2:
            continue
        if num + num2 == number:
            count += 1
return count // 2
```
Now skip the entries where it is the same value twice, and then return half
the sum. This will give the correct answer for all test cases. However it is
doing unnecessary work; you can remove the double counting, and lessen how
many steps it takes, by using `index` to only iterate over the remaining entries
of `arr` in each nested loop, this has the added advantage of eliminating the
double count.

```python
count = 0
for index, num in enumerate(arr):
    for num2 in arr[index + 1:]:
        if num + num2 == number:
            count += 1
return count
```

This is a reasonable solution, however, it is still iterating over the array
in a nested manner. This means that if the array is length `n` you will be
performing ~`n^2` operations. This is very slow for large arrays. You can
do much better by using dictionaries to do this with 2 non-nested loops:

```python
possibles = {}
for num in arr:
    if num not in possibles:
        possibles[num] = 0
    possibles[num] += 1

double_count = 0
for num in arr:
    if number - num in possibles:
        double_count += possibles[number - num]

    if (number - num) == num:
        double_count -= 1

return double_count // 2
```
Here you're using a dictionary to store the count of each number, so for
`[1, 5, 8, 7, 1, 7, 1]` you would have a possibles dictionary of:
`{1: 3, 5: 1, 8: 1, 7: 2}`
Now you go through our array again and look for entries that are `number - num` in
the dictionary. Because dictionaries have constant time lookup, you can do this
quickly. You then add the count of those entries to our total. This solution
suffers from both of the problems in our original double loop solution. However,
you can fix both of them. You can eliminate the same entry problems by lowering
the count when `(number - num) == num`. You can then address the double counting
by returning half the count. While this is not as satisfying as removing the
double counting, the efficiency gains of having this run in `2n` steps rather
than ~`n^2` steps more than makes up for it.


### !end-explanation

#### !end-challenge

<div class='bg-info' style='padding:8px;border-style:solid;border-width:2px;border-color:#00BFFF'>
<strong>Aside:</strong><br>
Remember: You can ask your instructor and peers questions in your cohort’s Slack channel. 
And if you encounter problems with the curriculum or software, email details and a screenshot of the issue to datasciencehelp@galvanize.com or  via our intercom system in Learn, which you can access by clicking on the teal chat icon in the lower right-hand corner of Learn (responses can take up to three business days).
</div>
