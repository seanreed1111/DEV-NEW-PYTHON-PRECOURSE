# Data Types & Variables

## Key Takeaways

In this section, you will:
* Use a variety of data types to represent data in your code
* Learn how to store data using variables
* Start to understand _how not to learn_

<div class='alert alert-info'><strong>Reminder</strong><br>Skip ahead to the questions at the bottom of this page if you already feel comfortable with the lesson topics. You can do this for any lesson!</div>

## Explanation #1

Complete the second section of Udacity's JS101.

* [Complete Lesson 2: Data Types & Variables](https://classroom.udacity.com/courses/ud803)

## Vocabulary List
Some vocab words to add to your mental glossary:
* Boolean
* Concatenation
* Data type
* Number
* String
* String index
* Variables

## Check For Understanding

<!--BEGIN CHALLENGE-->

### !challenge

* type: multiple-choice
* id: 90a03e39-ff5b-4c49-b09c-a911016a59c1
* title: Boolean

##### !question

Which of the following evaluates to `false`?

##### !end-question

##### !options

* 3 == '3'
* 'java'+'Script' === 'javaScript'
* 'Galvanize'+10*100 === 'Galvanize1000'
* All of the above
* None of the above

##### !end-options

##### !answer

None of the above

##### !end-answer

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: local-snippet
* language: javascript
* id: adafdf02-13d1-4b1c-9180-c30d34694951
* title: Data Types

### !question

Set a value to each variable as described in the comments.

### !end-question

### !placeholder

```js
function myFunction() {
  // Give each of the following variables a value of the type described.
  // Don't change the variable names.

  // set to any Number
  var number

  // set to any String
  var string

  // set to any Boolean
  var boolean

  // set to null
  var nullVar

  // set to undefined
  var undefinedVar

  return [number, string, boolean, nullVar, undefinedVar];
}
```

### !end-placeholder

### !tests

```js

describe('Data types', function() {

    it("has a Number in the 'number' variable", function() {
      expect(myFunction()[0], "Number variable is not a Number").to.be.a('number');
    })

    it("has a String in the 'string' variable", function() {
      expect(myFunction()[1], "String variable is not a String").to.be.a('string');
    })

    it("has a Boolean in the 'boolean' variable", function() {
      expect(myFunction()[2], "Boolean variable is not a Boolean").to.be.a('boolean');
    })

    it("has a null in the 'nullVar' variable", function() {
      expect(myFunction()[3], "nullVar variable is not null").to.be.a('null');
    })

    it("has an undefined in the 'undefinedVar' variable", function() {
      expect(myFunction()[4], "undefinedVar variable is not a Boolean").to.be.an('undefined');
    })

})

```

### !end-tests

### !end-challenge

<!--END CHALLENGE-->
