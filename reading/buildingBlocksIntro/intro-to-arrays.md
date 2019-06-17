# Intro to Arrays

## Key Takeaways

In this section, you will:
* Store collections of data in arrays
* Manipulate arrays using common properties and methods

## Explanation #1

Complete the sixth section of Udacity's JS101.

* [Complete Lesson 6: Arrays](https://classroom.udacity.com/courses/ud803)

<!-- ## Explanation #2

Work on the first 8 lessons Codecademy's [Arrays and Objects in JS](https://www.codecademy.com/en/courses/javascript-beginner-en-9Sgpi/0/1) module. If you're having trouble, the page links some past exercises you can review. -->

## Vocabulary List
Some vocab words to add to your mental glossary:
* Array
* Array element
* Array methods
* Array properties
* Array.forEach
* Array.length
* Array.map
* Array.pop
* Array.push
* Array.splice

## Check For Understanding

<!--BEGIN CHALLENGE-->

### !challenge

* type: local-snippet
* language: javascript
* id: 08dd0954-dd19-498b-b3a8-2986930bd9e2
* title: Even or Odd

### !question

Complete the `isLastEvenOdd` function below. The function should:
* Take one input parameter, an array of numbers.
* Return the string `'even'` or `'odd'` based on whether the last item in the array is even or odd.

### !end-question

### !placeholder

```js
function isLastEvenOdd(numArray) {

}
```

### !end-placeholder

### !tests

```js

describe('isLastEvenOdd', function(numArray) {

    it("works for an even positive number", function() {
      expect(isLastEvenOdd([1, 2, 3, 4]), "Failed [1, 2, 3, 4]").to.deep.eq('even')
    })

    it("works for an odd negative number", function() {
      expect(isLastEvenOdd([1, 3, 5, 7, -9]), "Failed [1, 3, 5, 7, -9]").to.deep.eq('odd')
    })

})

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

<!--END CHALLENGE-->

## Survey

These are optional, anonymous surveys that help us improve the course.

<p><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeZQrmqZeupBGMHFZ1uIKxbGI4vAbpnfwHyctxBB9-9HjMjBA/viewform?embedded=true" width="700" height="720" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></p>
