# Conditionals 4

### !challenge

* type: local-snippet
* language: javascript
* id: c13afed5-de19-458a-a3b9-65fc3d34f842
* title: isOdd

### !question

Write a function called "isOdd".
Given a number, "isOdd" returns whether the given number is odd.

```
var output = isOdd(9);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isOdd(num) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("isOdd", function() {
  it("should return a boolean", function() {
    expect(typeof isOdd(40)).to.deep.eq("boolean");
  });
  it("should return if the number is odd", function() {
    expect(isOdd(7)).to.deep.eq(true);
  });
  it("should return false if the number is 0", function() {
    expect(isOdd(0)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: d502830a-6d86-479d-9bd3-664e13d2a686
* title: isSameLength

### !question

Write a function called "isSameLength".

Given two words, "isSameLength" returns whether the given words have the same length.

```
var output = isSameLength('words', 'super');
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isSameLength(word1, word2) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("isSameLength", function() {
  it("should return a boolean", function() {
    expect(typeof isSameLength("hi", "there")).to.deep.eq("boolean");
  });
  it("should return true if the two words are the same length", function() {
    expect(isSameLength("yes", "you")).to.deep.eq(true);
  });
  it("should return false if the two words are not the same length", function() {
    expect(isSameLength("hi", "there")).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 2b052832-2dec-494d-9a24-090c8051db0a
* title: areBothOdd

### !question

Write a function called "areBothOdd".

Given 2 numbers, "areBothOdd" returns whether or not both of the given numbers are odd.

```
var output = areBothOdd(1, 3);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function areBothOdd(num1, num2) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("areBothOdd", function() {
  it("should return a boolean", function() {
    expect(typeof areBothOdd(40, 3)).to.deep.eq("boolean");
  });
  it("should return true if both numbers are odd", function() {
    expect(areBothOdd(41, 3)).to.deep.eq(true);
  });
  it("should return false if the first number is even", function() {
    expect(areBothOdd(4, 3)).to.deep.eq(false);
  });
  it("should return false if the second number is even", function() {
    expect(areBothOdd(5, 30)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 2aa4cdd8-0158-438d-8a53-b9c0283226c7
* title: isEitherEven

### !question

Write a function called "isEitherEven".

Given two numbers, "isEitherEven" returns whether or not either one of the given numbers is even.

```
var output = isEitherEven(1, 4);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isEitherEven(num1, num2) {
  // your code here
  
}

```

### !end-placeholder

### !tests

```js

describe("isEitherEven", function() {
  it("should return a boolean", function() {
    expect(typeof isEitherEven(40, 3)).to.deep.eq("boolean");
  });
  it("should return true if the first number is even", function() {
    expect(isEitherEven(4, 3)).to.deep.eq(true);
  });
  it("should return true if the second number is even", function() {
    expect(isEitherEven(7, 30)).to.deep.eq(true);
  });
  it("should return true if the both numbers are even", function() {
    expect(isEitherEven(70, 30)).to.deep.eq(true);
  });
  it("should return false if both numbers are odd", function() {
    expect(isEitherEven(71, 31)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
