Go back and finish Module 1. 
## Writing Code Well

At this point, your proverbial "axe" should be nice and sharpened. Excellent work! A sharp axe is only effective if it strikes consistently. Wild, unintentional swings will likely cause some damage, but a uniform approach will surely win the day. 

## The Goal

This module consists of a handful of harder problems that begin to realistically reflect the kinds of problems you are asked in admissions interviews. They also begin to reflect the kinds of problems that come up in the core immersive curriculum.

As you solve these problems, you will learn concepts and techniques that will help you code much more cleanly and professionally. 

The real benefit in this module will happen **after** you get the automated tests working. I would suggest you revisit and refactor your code after each problem. Do so by following the suggestions outlined in the [Coding Style Guide](https://learn.makerpass.com/groups/freeprep00/courses/reactorcore/course.free-prep?id=coding-style-guide). This is one of the best ways to ensure a successful interview. To fail with one curly brace out of order would be the height of tragedy. However, if your style and organization are precise, you can contend with the real challenges facing you in the interview.

Additionally, please read these articles as they are exceedingly helpful:
 
* [How to Think about Memory](https://learn.makerpass.com/groups/freeprep00/courses/reactorcore/course.free-prep?id=memory)
* [Outlining and Stubs](https://learn.makerpass.com/groups/freeprep00/courses/reactorcore/course.free-prep?id=outlining-and-stubs)
* [Testing](https://learn.makerpass.com/groups/freeprep00/courses/reactorcore/course.free-prep?id=testing)
* [Test Driven Development](https://learn.makerpass.com/groups/freeprep00/courses/reactorcore/course.free-prep?id=test-driven-development)
* [Functions and Reliable Systems](https://learn.makerpass.com/groups/freeprep00/courses/reactorcore/course.free-prep?id=functions-and-reliable-systems)





## Sample of Clean Code Structure



```
function isOne(val) {
  return val === 1;
}

function assertTrue(actual, testName) {
  if (actual === true) {
    console.log('passed');
  } else {
    console.log('FAILED [' + testName + '] Expected "true", but got "' + actual  + '"';
  }
}

var willPassTest = isOne(1);
assertTrue(willPassTest, 'should pass when input is one');

var willNotPassTest = isOne(2);
assertTrue(willNotPassTest, 'this fails on purpose');
```

Please take careful note of the spacing, indentation, and consistency of the code. Run this code in a console to get a sense of what is going on. The second test is included for demonstrative purpses; in general, you do not want to include failing tests. 

## Sections
  * [Variable Assignments](https://learn.makerpass.com/groups/freeprep00/courses/reactorcore/course.free-prep?id=variableassignments)
  * [Testing Problems](https://learn.makerpass.com/groups/freeprep00/courses/reactorcore/course.free-prep?id=testingproblems)
  * [Full Problems](https://learn.makerpass.com/groups/freeprep00/courses/reactorcore/course.free-prep?id=fullproblems)











