# List Comprehensions

## Learning Objective
_By the end of this lesson you will be able to:_

* Read and create list comprehensions


## List Comprehensions

The last topic covered in this unit is a different way to construct lists. Up to this point you have built lists by first initializing them then taking advantage of their mutability to build them up one element at a time. However, there is a more succinct way to accomplish this task.

Before diving into the specifics about how this new tool (called _list comprehensions_) works, let's look at an example.

Imagine that you have the list `[1, 5, 9, 33]` stored in the variable `my_list`. Now, assume that you want to make a new list containing the squares of all the values in `my_list` and call it `my_squares`. With the tools you've learned so far, you might write:

```python
my_squares = []
for num in my_list:
    my_squares.append(num ** 2)
```

This produces the list `my_squares` as follows: `[1, 25, 81, 1089]`. To create `my_squares`, you specified the things that you wanted to add to the end of the `my_squares` list, using the elements in `my_list`.  If we were to write this code in more generic terms, we might say something like the following:

```python
list_result = []
for thing in iterable:
    list_result.append(transform(thing))
```
(The above is an example of [_pseudocode_](https://en.wikipedia.org/wiki/Pseudocode). Pseudocode is simply a high-level description of an algorithm that omits -- for the sake of readability -- some of the details needed for the code to actually run. In this case, `iterable` is a stand-in for `my_list`, `list_result` stands in for `my_squares`, and `transform()` takes the place of `num ** 2`.)

Now, believe it or not, you can use the following syntax to accomplish the very same task of building up a generic list:

```python
list_result = [transform(thing) for thing in iterable]
```

This one line of code does the exact same thing as the three lines before! Here, the thing that you would pass to the `append()` method, `transform(thing)`, comes at the beginning of the statement between the square brackets (`[]`).  The square brackets signal that the thing assigned to the variable `list_result` will be of type `list`. Then, the `for` loop statement that you had written is at the end. This is the basic syntax of a Python [list comprehension](https://en.wikipedia.org/wiki/List_comprehension).

In real Python code, you can use a list comprehension to build your `my_squares` list as follows:

```python
my_squares = [num ** 2 for num in my_list]
```

But wait, there's more! Suppose that you want to build a list containing only even-valued integers.  Previously, you would have accomplished this by using an `if` statement within a loop to check if each number is even before appending it to your list. Well, you can also accomplish this by using a list comprehension and specifying a condition that must be satisfied for an element to be included in the resulting list. Take a look:

```python
# Old way of constructing list of evens
evens = []
for num in range(10):
    if num % 2 == 0:
        evens.append(num)

# Old way in pseudocode
list_were_building = []
for thing in iterable:
    if condition:
        list_were_building.append(transform(thing))

# List comprehension way in pseudocode
list_were_building = [transform(thing) for thing in iterable if condition]

# List comprehension way of constructing list of evens
evens = [num for num in range(10) if num % 2 == 0]
```

Note: the way `transform()` was called in the above examples -- as though it were a function -- is an option when writing list comprehensions. For example, the `my_squares` example could be accomplished in the same way with:

```python
def square(num):
    return num ** 2

my_squares = [square(num) for num in my_list]
```

This example might seem silly, since you could just write `num ** 2` directly in the list comprehension as you did above. However, calling a function from a list comprehension can be powerful when you want to transform your list elements in a more complex way.




### !challenge

* type: code-snippet
* language: python3.6
* id: 6198d29e-ceb8-4f89-9a37-4b5a4299d4ad
* title: Challenge 1

### !question
One common task in data science is to lowercase strings so that they are more directly comparable. We may not care that one user says 'SPAM' and another says 'spam', and yet a third says 'Spam', for example; they're all arguably talking about the same thing.

Write a one-liner that takes in a list of words like ['SPAM', 'Spam', 'spam'] and outputs a list with the lowercase version of each word. Use a list comprehension, do not use a for loop!

### !end-question

### !placeholder

```python
in_list = ['SPAM', 'Spam', 'spam']
answer = None  # change this to not be None
```

### !end-placeholder

### !tests

```python

import unittest
import main



class TestScript(unittest.TestCase):

    def test_output(self):
        student_answer = main.answer
        expected_answer = ['spam', 'spam', 'spam']
        self.assertEqual(student_answer, expected_answer)



```

### !end-tests

### !explanation

You can lowercase each string in a list with:
```python
answer = [s.lower() for s in in_list]
```


### !end-explanation

### !end-challenge







### !challenge

* type: multiple-choice
* id: ab035b3b-9fc2-4f49-a214-4964232b1291
* title: Challenge 2
##### !question

Another common task in data science involves filtering out the most commonly used words in English, referred to as stop words, because they typically don't provide much information about the content of text.

Consider the code below, which shows a (simplified) process for removing stop words.

```python
stop_words_list = ['a', 'an', 'and', 'in', 'is',
                   'of', 'or', 'that', 'the', 'to']


text = """Data science is an interdisciplinary field of scientific
methods, processes, algorithms and systems to extract knowledge or
insights from data in various forms, either structured or unstructured,
similar to data mining."""
text_list = text.lower().split()

no_stops_list = []
for word in text_list:
    if word not in stop_words_list:
        no_stops_list.append(word)
```        

In which of the following options is `no_stops_list` the same as defined above?
##### !end-question

##### !options

* `no_stops_list = [w for w in text_list]`
* `no_stops_list = [w for w in text_list + stop_words_list]`
* `no_stops_list = [w for w in text_list if w in stop_words_list]`
* `no_stops_list = [w for w in text_list if w not in stop_words_list]`

##### !end-options

##### !answer

`no_stops_list = [w for w in text_list if w not in stop_words_list]`

##### !end-answer

##### !explanation

The code:

```python
no_stops_list = []
for word in text_list:
    if word not in stop_words_list:
        no_stops_list.append(word)
```

can be rewritten as a list comprehension as:

```python
no_stops_list = [w for w in text_list if w not in stop_words_list]
```

##### !end-explanation

### !end-challenge
