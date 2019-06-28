# Intro to Loops

## Key Takeaways

In this section, you will:
* Learn how to repeatedly execute code with loop and iteration fundamentals
* Explore working with JavaScript while and for loops
* Answer the question: “What is full stack engineering?”

## Explanation #1

Complete the fourth section of Udacity's JS101.

* [Complete Lesson 4: Loops](https://classroom.udacity.com/courses/ud803)

## Explanation #2

This is a video that describes [EVERY programming language](https://www.youtube.com/watch?v=duhDovqHbEs). It is an interesting video to watch, and provides an excellent introduction to programming for total beginners. 

## Vocabulary List
Some vocab words to add to your mental glossary:
* Back End
* Decrement operator
* For loop
* Front End
* Full stack
* Increment operator
* While loop

## Check For Understanding

<!--BEGIN CHALLENGE-->

### !challenge

* type: local-snippet
* language: javascript
* id: ae6de11e-934d-436b-8f34-fedc9dca79c1
* title: Countdown

### !question

Fill out the rest of the `while` loop so that the following sequence is logged to the console:

```
10
9
8
7
6
5
4
3
2
1
```

### !end-question

### !placeholder

```js
function myFunction () {
  // Replace each comment below

  var number = 10;

  while (/* add conditional */) {
    /* console.log number */
    /* change value of number */
  }

}
```

### !end-placeholder

### !tests

```js
describe('While loop', function() {

    it("Uses a While loop", function() {
      expect(myFunction.toString(), "While loop not found").to.match(/while \(/)
    })

    it('logs the numbers from 10-1', function() {
      var originalLogger = console.log;
      var capturedMessage = '';
      console.log = function(message) {
        capturedMessage += message;
      }

      myFunction();

      console.log = originalLogger;

      expect(capturedMessage).to.deep.eq('10987654321');
    });

})

```

### !end-tests

### !end-challenge

<!--END CHALLENGE-->

<!--BEGIN CHALLENGE-->

### !challenge

* type: local-snippet
* language: javascript
* id: 35d75756-d2a6-421e-b7c1-e872eec4d99e
* title: Multiples of Three

### !question

The code below counts the multiples of 3 between 1-100.

Rewrite the code to use a `for` loop instead of a `while` loop.

### !end-question

### !placeholder

```js
function myFunction(input) {

  // Rewrite the code below to use a `for` loop instead of a `while` loop.

  var multiplesOfThreeCount = 0;

  // loop through numbers 1-100, count multiples of 3
  var number = 1;
  while (number <= 100) {
    if (number % 3 === 0) {
      multiplesOfThreeCount++;
    }
    number++;
  }

  console.log('There are ' + multiplesOfThreeCount + ' multiples of 3 between 1 and 100.')

  /* NOTE: For this challenge to pass all tests, you will have to replace
  the entire `while` loop. Commenting out the `while` loop will not work. */

  return multiplesOfThreeCount;
}
```

### !end-placeholder

### !tests

```js


describe('Using a `for` loop', function() {

    it("counts the multiples of 3 between 1-100", function() {
      expect(myFunction(), "Expected count to be 33 (did you remove the increment in the while loop?)").to.deep.eq(33)
    })

    it("doesn't use a `while` loop", function() {
      expect(myFunction.toString(), "Should not contain a `while` loop (did you delete the while loop instead of commenting it out?)").to.not.match(/while \(/)
    })

    it("uses a `for` loop", function() {
      expect(myFunction.toString(), "Should contain a `for` loop").to.match(/for \(/)
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

<p><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSfN8i24kiZTJR_t7jcXBIG3fNKmUsB3LNTI5P4ppaeUAu7xig/viewform?embedded=true" width="700" height="720" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></p>
