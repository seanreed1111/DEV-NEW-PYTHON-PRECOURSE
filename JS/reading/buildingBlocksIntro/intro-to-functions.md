# Intro to Functions

## Key Takeaways

In this section, you will:
* Organize your code by declaring functions and writing function expressions
* Demystify tricky JavaScript behavior by learning about scope and hoisting

## Explanation #1

Complete the fifth section of Udacity's JS101.

* [Complete Lesson 5: Functions](https://classroom.udacity.com/courses/ud803/)

<!-- ## Explanation #2

Complete the 13 lessons in Codecademy's [Intro to Functions](https://www.codecademy.com/courses/javascript-beginner-en-6LzGd/0/1). These lessons do a good job tying in elements from the conditionals section. -->

## Explanation #2
Read [this article](https://stackoverflow.com/questions/336859/var-functionname-function-vs-function-functionname) explaining the difference between function declarations and expressions.

## Vocabulary List
Some vocab words to add to your mental glossary:
* D.R.Y.
* Function declaration
* Function expression
* Global variable
* Hoisting (this word will appear at some point in a future job interview. Be able to explain what this means)
* Local variable
* Return keyword
* Scope

## Check For Understanding

<!--BEGIN CHALLENGE-->

### !challenge

* type: local-snippet
* language: javascript
* id: 50f9b860-eaf5-4d45-8111-654fb0dfde57
* title: addThreeNumbers()

### !question

Write a function called addThreeNumbers. The function should:
- Take 3 input parameters, all numbers.
- Return the sum of all 3 numbers.

### !end-question

### !placeholder

```js
// Write a function called addThreeNumbers.
```

### !end-placeholder

### !tests

```js

describe('addThreeNumbers', function(a, b, c) {

    it("declares a function called addThreeNumbers()", function() {
      expect(addThreeNumbers, "addThreeNumbers() not declared as a function").to.be.a("function")
    })

    it("adds 1, 2, and 3", function() {
      expect(addThreeNumbers(1, 2, 3), "Didn't add 1+2+3=6").to.deep.eq(6)
    })

    it("adds 7, 8, and 9", function() {
      expect(addThreeNumbers(7, 8, 9), "Didn't add 7+8+9=24").to.deep.eq(24)
    })

})

```

### !end-tests

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: local-snippet
* language: javascript
* id: 0156bed7-60a6-456d-86f7-d85b25501f52
* title: sayHello

### !question

Write a function called sayHello. The function should:

* Take one input parameter, the language.
* Return a greeting in that language.
  * If the language is 'English', return 'Hello'
  * If the language is 'French', return 'Bonjour'
  * If the language is 'Spanish', return 'Hola'
  * If the language is anything else, return 'Sorry, I do not speak [language].'

### !end-question

### !placeholder

```js
// Write a function called sayHello.
// sayHello takes one input parameter, the language for the greeting.
// sayHello returns a greeting following the rules defined above.

```

### !end-placeholder

### !tests

```js

describe('sayHello', function() {

    it("declares a function called sayHello", function() {
      expect(sayHello, "sayHello() not declared").to.be.a("function")
    })

    it("Says Hello in English", function() {
      expect(sayHello('English'), "Didn't say Hello in English").to.deep.eq('Hello')
    })

    it("Says Bonjour in French", function() {
      expect(sayHello('French'), "Didn't say Bonjour in French").to.deep.eq('Bonjour')
    })

    it("Says Hola in Spanish", function() {
      expect(sayHello('Spanish'), "Didn't say Hola in Spanish").to.deep.eq('Hola')
    })

    it("Doesn't speak other languages", function() {
      expect(sayHello('German'), "Didn't warn for unsupported languages").to.deep.eq('Sorry, I do not speak German.')
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

<p><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSeUl0LhpGUBHznNt0nlQD4Cf6-UMyhajITm9arh6e07pt7EaQ/viewform?embedded=true" width="700" height="720" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></p>
