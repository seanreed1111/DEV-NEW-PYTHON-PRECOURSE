# Intro to Objects

## Key Takeaways

In this section, you will:
* Create JavaScript objects to represent complex data types

## Explanation #1

Complete the seventh (and final!) section of Udacity's JS101.

* [Complete Lesson 7: Objects](https://classroom.udacity.com/courses/ud803)

<!-- ## Explanation #2

Work on lessons 9 - 17 of Codecademy's [Arrays and Objects in JS](https://www.codecademy.com/en/courses/javascript-beginner-en-9Sgpi/0/1) module. -->

## Vocabulary List
Some vocab words to add to your mental glossary:
* Object
* Object literal
* Object methods
* Object.hasOwnProperty
* Object.keys
* Object.values

## Check For Understanding

<!--BEGIN CHALLENGE-->

### !challenge

* type: local-snippet
* language: javascript
* id: c12add77-9e7a-479f-8151-e0aa73bf9495
* title: Object Properties

### !question

Create an object called "person".

Set the following properties:
* firstName: the person's first name
* lastName: the person's last name
* ageInYears: the person's age in years

### !end-question

### !placeholder

```js
function myFunction() {

  // create the object described above

  return person;
}
```

### !end-placeholder

### !tests

```js


describe('person', function() {

    it("is an object", function() {
      expect(myFunction(), "Not an object").to.be.an("object")
    })

    it("has a firstName property", function() {
      expect(myFunction().firstName, "firstName property not a string").to.be.a("string")
    })

    it("has a lastName property", function() {
      expect(myFunction().lastName, "lastName property not a string").to.be.a("string")
    })

    it("has an ageInYears property", function() {
      expect(myFunction().ageInYears, " property not a number").to.be.a("number")
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
* id: 7a09f2d4-d88a-410b-b4b5-74c4c8346492
* title: addFullName

### !question

Fill out the code for the `addFullName` function. The function should:

* Take one input parameter, a `person` object.
* Add a property called `fullName` to the `person` object when called. The new `fullName` property is set to the string `'firstName lastName'` (one string, with a space between the two names)
* Modify the object passed in without returning anything.

### !end-question

### !placeholder

```js
// an example `person` object
var person = {
    firstName: 'Joseph',
    lastName: 'Magnolia',
    ageInYears: 34
}

function addFullName(personObj) {
  /* your code here */
}
```

### !end-placeholder

### !tests

```js

describe('person', function() {

    it("should set fullName property to 'Joseph Magnolia'", function() {
      let person = {
          firstName: 'Joseph',
          lastName: 'Magnolia',
          ageInYears: 34
      }
      addFullName(person);
      expect(person.fullName, "fullName does not equal 'Joseph Magnolia'").to.deep.eq('Joseph Magnolia');
    })

    it("should set fullName property to 'Michael Smith'", function() {
      let person = {
          firstName: 'Michael',
          lastName: 'Smith',
          ageInYears: 22
      }
      addFullName(person);
      expect(person.fullName, "fullName does not equal 'Michael Smith'").to.deep.eq('Michael Smith');
    })

})

```

### !end-tests

### !end-challenge

<!--END CHALLENGE-->

## Survey

These are optional, anonymous surveys that help us improve the course.

<p><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSe4AJnqQa8gbEQha5R93ghxwmPTOVmwPfCqugWLIZqSNVGn8w/viewform?embedded=true" width="700" height="720" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></p>
