# Methods

## Learning Objectives:
_By the end of this lesson, you will be able to:_  
* Define methods in user-defined classes
* Use `self` in methods that you define


### Defining Other Methods

Defining other methods within a class is exactly like defining the `__init__()` method. The only difference is how you access those methods from outside of an object. Whereas the `__init__()` method is called automatically when you instantiate an object, your code will have to explicitly call other methods that you define. As before, you'll call those other methods via dot notation. Take a look at defining another method within the `GalvanizeCourse` class.

```python
In [1]: class GalvanizeCourse:
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:
   ...:     def add_question(self, question):
   ...:         self.questions_asked.append(question)

In [2]: our_course = GalvanizeCourse('Intro Python', 'Boulder', 15)

In [3]: our_course.name, our_course.location, our_course.size
Out[3]: ('Intro Python', 'Boulder', 15)

In [4]: our_course.questions_asked
Out[4]: []

In [5]: our_course.add_question('Why Python?')

In [6]: our_course.questions_asked
Out[6]: ['Why Python?']

In [7]: our_course.add_question('Why not R?')

In [8]: our_course.questions_asked
Out[8]: ['Why Python?', 'Why not R?']
```

Here, another method within the class has been called, named `add_question()`. Notice that you call this method after you've created an instance of `GalvanizeCourse` (stored in the variable `our_course`), and you use dot notation to access it. This `add_question()` method takes a string (or anything, really) and appends it to the object's `questions_asked` attribute. But, how does `add_question()` know where to find the `questions_asked` attribute if it isn't passed as an argument? This is thanks to the `self` variable that is automatically assigned to the first parameter of the method. The `self` variable permits access to _any_ of the object's attributes, no matter where they were defined (typically, in the `__init__()` method). As long as the attribute was assigned via dot notation using `self`, then it will be accessible via `self` from any method of the class.

### Don't forget your self

You'll need to remember to specify `self` as the first parameter of methods that you define — Python won't do this for you.  In fact, a common mistake when first doing object-oriented programming in Python is to forget to specify `self`.  Here's what happens when you do:

```python
In [1]: class GalvanizeCourse:
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:
   ...:     def add_question(self, question):
   ...:         self.questions_asked.append(question)
   ...:
   ...:     def print_name():
   ...:         print(self.name)

In [2]: our_course = GalvanizeCourse('Intro Python', 'Boulder', 15)

In [3]: our_course.print_name()
---------------------------------------------------------------------------
TypeError                                 Traceback (most recent call last)
<ipython-input-28-317832e4d83b> in <module>()
----> 1 our_course.print_name()

TypeError: print_name() takes 0 positional arguments but 1 was given
```

As you can see, forgetting to specify `self` as an argument in methods you define can lead to some confusing error messages, such as "print_name() takes 0 positional arguments but 1 was given".  The first time you encounter an error like this, you might wonder why Python is complaining: the method expected zero arguments, you provided zero arguments, so what's the problem? The problem comes from the fact that Python passes the `self` argument automatically, but you forgot to receive it in your method parameters.  Whenever you are doing OOP in Python and see an odd error message about arguments not matching up, check to see that you specified a `self` parameter in all your methods.

### Using methods to modify attributes

Another thing to note is that any method within the class can modify attributes that are accessible via `self`. Above, the `add_question()` method was used to modify the `questions_asked` attribute. However, if you use a variable within a method instead of an attribute, then it won't be accessible from other methods of the class — it will be limited to the scope of that method only. Here's another example to illustrate this.

```python
In [1]: class GalvanizeCourse:
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:
   ...:     def add_question(self, question):
   ...:         self.questions_asked.append(question)
   ...:     
   ...:     def add_students(self, num):
   ...:         self.size += num
   ...:
   ...:         if self.size >= 20:
   ...:             print('Capacity Reached!!')
   ...:             at_capacity = True
   ...:
   ...:     def check_if_at_capacity(self):
   ...:         return self.at_capacity

In [2]: our_course = GalvanizeCourse('Intro Python', 'Boulder', 15)

In [3]: our_course.add_question("What's he going to show?")

In [4]: our_course.add_question('Do you know the answer?')

In [5]: our_course.questions_asked
Out[5]: ["What's he going to show?", 'Do you know the answer?']

In [6]: our_course.add_students(3)

In [7]: our_course.size
Out[7]: 18

In [8]: our_course.add_students(5)
Capacity Reached!!

In [9]: our_course.size
Out[9]: 23

In [10]: our_course.check_if_at_capacity()
______________________________________________________________________
NameError                           Traceback (most recent call last)
<ipython-input-21-bd556e9468f1> in <module>()
    > 1 our_course.check_if_at_capacity()

<ipython-input-9-f631bd9392f0> in check_if_at_capacity(self)
      18
      19     def check_if_at_capacity(self):
    > 20         return self.at_capacity

AttributeError: GalvanizeCourse instance has no attribute 'at_capacity'
```

The point of this example is to show that any method can access any attribute that is assigned via `self`. You see this in two of the methods above: `add_question()` is able to modify the `questions_asked` attribute (just as before), and `add_students()` is able to modify `size`. Both of these attributes are accessed via `self`. The method `check_if_at_capacity()`, though, tries to access `at_capacity`, which was never made an attribute (using `self`), and so you receive an error.  The way this code is written, `at_capacity` is only ever set and accessible within the `add_students()` method. You can fix this by assigning it via `self` and see what happens.

```python
In [1]: class GalvanizeCourse:
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:
   ...:     def add_question(self, question):
   ...:         self.questions_asked.append(question)
   ...:     
   ...:     def add_students(self, num):
   ...:         self.size += num
   ...:
   ...:         if self.size >= 20:
   ...:             print('Capacity Reached!!')
   ...:             self.at_capacity = True
   ...:
   ...:     def check_if_at_capacity(self):
   ...:         return self.at_capacity

In [2]: our_course = GalvanizeCourse('Intro Python', 'Platte', 15)

In [3]: our_course.add_students(5)
Capacity Reached!!

In [4]: our_course.at_capacity
Out[4]: True

In [5]: our_course.check_if_at_capacity()
Out[5]: True
```

Here you see that it is not only possible to create attributes in the `__init__()` method, but in other methods as well. Before the line `our_course.add_students(5)` was called, there was no `at_capacity` attribute on the `our_course` object. Afterward, there was. This is because `at_capacity` was created in the `if` block within the `add_students()` method. Furthermore, because it was assigned via `self`, the `at_capacity` attribute was accessible in the `check_if_at_capacity()` method when it was called.

### Initialize all attributes in `__init__()`

Although Python permits you to create attributes in methods other than  `__init__()`, in general this is not considered good practice. To see why, imagine what would have happened if you had called the `check_if_at_capacity()` method before `self.at_capacity` was set. It would have thrown an error. Typically, you want to define all of the attributes that will ever be accessed on the object in the `__init__()` method. You can give that attribute a default value, or you can simply assign `None` to it. This is actually what should have happened with the `at_capacity` attribute above. Take a look at the next example to see this done right.

```python
In [1]: class GalvanizeCourse:
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:         if self.size >= 20:
   ...:             self.at_capacity = True
   ...:         else:
   ...:             self.at_capacity = False
   ...:
   ...:     def add_question(self, question):
   ...:         self.questions_asked.append(question)
   ...:     
   ...:     def add_students(self, num):
   ...:         self.size += num
   ...:
   ...:         if self.size >= 20:
   ...:             print('Capacity Reached!!')
   ...:             self.at_capacity = True
   ...:
   ...:     def check_if_at_capacity(self):
   ...:         return self.at_capacity

In [2]: our_course = GalvanizeCourse('Intro Python', 'Platte', 15)

In [3]: our_course.check_if_at_capacity()
Out[3]: False

In [4]: our_course.add_students(3)

In [5]: our_course.size
Out[5]: 18

In [6]: our_course.check_if_at_capacity()
Out[6]: False

In [7]: our_course.add_students(5)
Capacity Reached!!

In [8]: our_course.size
Out[8]: 23

In [9]: our_course.check_if_at_capacity()
Out[9]: True
```

Now, you won't get any errors no matter when you try to access `self.at_capacity`.  Hopefully, this is a solid illustration of why it is important to initialize all of your attributes in the `__init__()` method.

### Maintain consistent state

Related to the importance of complete initialization is the importance of maintaining consistent object state.  As you'll recall, an object's _state_ is the collection of all the data represented by its attributes. Any method that modifies an attribute should make sure that it introduces no contradictions in state.  Consider the following example.

```python
In [1]: class GalvanizeCourse:
   ...:     
   ...:     def __init__(self, name, location, size=0):
   ...:         self.name = name
   ...:         self.location = location
   ...:         self.size = size
   ...:         self.questions_asked = []
   ...:         if self.size >= 20:
   ...:             self.at_capacity = True
   ...:         else:
   ...:             self.at_capacity = False
   ...:
   ...:     def add_question(self, question):
   ...:         self.questions_asked.append(question)
   ...:     
   ...:     def add_students(self, num):
   ...:         self.size += num
   ...:
   ...:         if self.size >= 20:
   ...:             print('Capacity Reached!!')
   ...:             self.at_capacity = True
   ...:
   ...:     def check_if_at_capacity(self):
   ...:         return self.at_capacity

In [2]: our_course = GalvanizeCourse('Intro Python', 'Platte', 15)

In [3]: our_course.check_if_at_capacity()
Out[3]: False

In [4]: our_course.add_students(25)

In [5]: our_course.size
Out[5]: 40

In [6]: our_course.check_if_at_capacity()
Out[6]: True

In [7]: our_course.add_students(-25)

In [8]: our_course.size
Out[8]: 15

In [9]: our_course.check_if_at_capacity()
Out[9]: True
```

Here, 25 students were added to cause the course to be over capacity.  Then 25 students were subtracted (by calling `add_students()` with a negative number), reducing the course size to 15.  But the `check_if_at_capacity()` method still returns `True` — which is incorrect.  This bug happened because the `add_students()` method didn't properly handle the case where the `self.size` is reduced below the capacity threshold, and so caused the object state to become inconsistent. Instead, the `add_students()` method should set the `at_capacity` attribute back to `False` when `self.size` is less than 20.

### Tab completion on objects

As a final note, you can also perform tab completion on objects you create within the IPython console. If you were to tab-complete the last instance of `GalvanizeCourse` from directly above, you would see this:

```python
In [10]: our_course.
our_course.add_class_memebers    our_course.location
our_course.add_question          our_course.name
our_course.at_capacity           our_course.questions_asked
our_course.check_if_at_capacity  our_course.size
```
----
## Challenges

<!-- BEGIN ### !include challenges/challenge-05-1.md -->
### !challenge

* type: code-snippet
* language: python3.6
* id: 4b3d3f97-b8db-418a-89ca-270776ec45fa
* title: Challenge 1


### !question

Add a method to the `Person` class below called `is_teen()` that returns `True` if the `age` attribute is the range 13 to 19, inclusive.

Your submission will be tested with code similar to the following to make sure that `is_teen()` works properly.

```python
p = Person("Bob", 14)
p.is_teen()
```

### !end-question

### !placeholder

```python

class Person:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

```

### !end-placeholder
### !tests
```python

import unittest
import runpy
import sys

class TestScript(unittest.TestCase):

    def test1(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Mary")
        is_teen = person_object.is_teen()
        self.assertFalse(is_teen)

    def test2(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Mary", 12)
        is_teen = person_object.is_teen()
        self.assertFalse(is_teen)

    def test3(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Mary", 15)
        is_teen = person_object.is_teen()
        self.assertTrue(is_teen)

    def test4(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Mary", 20)
        is_teen = person_object.is_teen()
        self.assertFalse(is_teen)
```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge
<!-- END ### !include challenges/challenge-05-1.md -->
<!-- BEGIN ### !include challenges/challenge-05-2.md -->
### !challenge

* type: code-snippet
* language: python3.6
* id: c8618a98-7bd4-4981-baaf-6f09dbbf644c
* title: Challenge 2


### !question

The code below has a bug. Fix it so that it works.

Your submission will be tested with code similar to the following to make sure that it works properly.

```python
s = Student("Mary")
s.name
```

### !end-question

### !placeholder

```python
class Student:
    def __init__(name):
        self.name = name
```

### !end-placeholder
### !tests
```python

import unittest
import runpy
import sys

class TestScript(unittest.TestCase):

    def test1(self):
        main_globals = runpy.run_module('main')
        student_class = main_globals['Student']
        self.assertIsNotNone(student_class)

    def test2(self):
        main_globals = runpy.run_module('main')
        student_object = main_globals['Student']("Mary")
        self.assertIsNotNone(student_object)

    def test3(self):
        main_globals = runpy.run_module('main')
        student_object = main_globals['Student']("Mary")
        name = student_object.name
        self.assertEqual(name, "Mary")
```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge
<!-- END ### !include challenges/challenge-05-2.md -->
<!-- BEGIN ### !include challenges/challenge-05-3.md -->
### !challenge

* type: code-snippet
* language: python3.6
* id: 4fcc1e2f-acc8-417a-9043-8ed137e9501a
* title: Challenge 3


### !question

The code below has a bug. Fix it so that it works.

Your submission will be tested with code similar to the following to make sure that it works properly.

```python
s = Student("Chauncey", True, True)
s.is_continuing_ed()
```

### !end-question

### !placeholder

```python
class Student:
    def __init__(self, name, enrolled, alumni):
        self.name = name
        self.enrolled = enrolled
        self.alumni = alumni

        if enrolled and alumni:
            continuing_ed = True

    def is_continuing_ed(self):
        return self.continuing_ed
```

### !end-placeholder
### !tests
```python

import unittest
import runpy
import sys

class TestScript(unittest.TestCase):

    def test1(self):
        main_globals = runpy.run_module('main')
        student_object = main_globals['Student']("Mary", True, True)
        is_continuing_ed = student_object.is_continuing_ed()
        self.assertTrue(is_continuing_ed)

    def test2(self):
        main_globals = runpy.run_module('main')
        student_object = main_globals['Student']("Mary", False, True)
        is_continuing_ed = student_object.is_continuing_ed()
        self.assertFalse(is_continuing_ed)

    def test3(self):
        main_globals = runpy.run_module('main')
        student_object = main_globals['Student']("Mary", True, False)
        is_continuing_ed = student_object.is_continuing_ed()
        self.assertFalse(is_continuing_ed)

```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge
<!-- END ### !include challenges/challenge-05-3.md -->
<!-- BEGIN ### !include challenges/challenge-05-4.md -->
### !challenge

* type: code-snippet
* language: python3.6
* id: 48e0da92-a2fc-40de-a9ed-68044a012ab9
* title: Challenge 4


### !question

The code below has a bug. Fix it so that it works.

Your submission will be tested with code similar to the following to make sure that it works properly.  Note that the attribute `adult` should be `True` when the `Person` is 18 or older.

```python
p = Person("Frank", 17)
p.adult
p.happy_birthday()
p.adult
```

### !end-question

### !placeholder

```python

class Person:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

        if age > 17:
            self.adult = True
        else:
            self.adult = False

    def happy_birthday(self):
        self.age += 1
```

### !end-placeholder
### !tests
```python

import unittest
import runpy
import sys

class TestScript(unittest.TestCase):

    def test1(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Frank", 17)
        adult = person_object.adult
        self.assertFalse(adult)

    def test2(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Frank", 18)
        adult = person_object.adult
        self.assertTrue(adult)

    def test3(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Frank", 17)
        person_object.happy_birthday()
        adult = person_object.adult
        self.assertTrue(adult)
```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge
<!-- END ### !include challenges/challenge-05-4.md -->
<!-- BEGIN ### !include challenges/challenge-05-5.md -->
### !challenge

* type: code-snippet
* language: python3.6
* id: fe1f108a-7f66-45f9-afec-899961ca332a
* title: Challenge 5


### !question

The code below has a bug. Fix it so that it works.  Note that the method `can_vote()` should return `True` when the `Person` is 18 or older.

Your submission will be tested with code similar to the following to make sure that it works properly.

```python
p = Person("Adam", 17)
p.can_vote()
p.happy_birthday()
p.can_vote()
```

### !end-question

### !placeholder

```python

class Person:

    def __init__(self, name, age=0):
        self.name = name
        self.age = age

    def can_vote(self):
        return self.voting_age

    def happy_birthday(self):
        self.age += 1

        if self.age >= 18:
            self.voting_age = True
```

### !end-placeholder
### !tests
```python

import unittest
import runpy
import sys

class TestScript(unittest.TestCase):

    def test1(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Frank", 17)
        can_vote = person_object.can_vote()
        self.assertFalse(can_vote)

    def test2(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Frank", 18)
        can_vote = person_object.can_vote()
        self.assertTrue(can_vote)

    def test3(self):
        main_globals = runpy.run_module('main')
        person_object = main_globals['Person']("Frank", 17)
        person_object.happy_birthday()
        can_vote = person_object.can_vote()
        self.assertTrue(can_vote)
```
### !end-tests

### !explanation

### !end-explanation

### !end-challenge
<!-- END ### !include challenges/challenge-05-5.md -->
