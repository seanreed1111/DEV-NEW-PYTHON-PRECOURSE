# Conditionals 6

### !challenge

* type: local-snippet
* language: javascript
* id: 17849d44-37ff-4fde-a81f-884838cdb8f5
* title: or

### !question

Write a function called "or".

Given 2 boolean expressions, "or" returns true or false, corresponding to the '||' operator.
Notes:
* Do not use the || operator.
* Use ! and && operators instead.

```
var output = or(true, false);
console.log(output); // --> true;
```

### !end-question

### !placeholder

```js
function or(expression1, expression2) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("or", function() {
  it("should not use the logical OR operator", function() {
    var body = or.toString()
    expect(/\|\|/.test(body)).to.deep.eq(false);
  });
  it("should return a boolean", function() {
    expect(typeof or(true, true)).to.deep.eq("boolean");
  });
  it("should return true if the first value is true", function() {
    expect(or(true, false)).to.deep.eq(true);
  });
  it("should return true if the second value is true", function() {
    expect(or(false, true)).to.deep.eq(true);
  });
  it("should return true both values are true", function() {
    expect(or(true, true)).to.deep.eq(true);
  });
  it("should return false both values are false", function() {
    expect(or(false, false)).to.deep.eq(false);
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
* id: 1f440059-2dd7-472c-8106-c56fa9f75029
* title: isEitherEvenOrAreBoth7

### !question

Write a function called "isEitherEvenOrAreBoth7".

Given two numbers, 'isEitherEvenOrAreBoth7' returns whether at least one of them is even, or, both of them are 7.

```
var output = isEitherEvenOrAreBoth7(3, 7);
console.log(output); // --> false

var output = isEitherEvenOrAreBoth7(2, 3);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isEitherEvenOrAreBoth7(num1, num2) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("isEitherEvenOrAreBoth7", function() {
  it("should return a boolean", function() {
    expect(typeof isEitherEvenOrAreBoth7(40, 3)).to.deep.eq("boolean");
  });
  it("should return true if the first number is even", function() {
    expect(isEitherEvenOrAreBoth7(4, 3)).to.deep.eq(true);
  });
  it("should return true if the second number is even", function() {
    expect(isEitherEvenOrAreBoth7(7, 8)).to.deep.eq(true);
  });
  it("should return true if the both numbers are even", function() {
    expect(isEitherEvenOrAreBoth7(2, 4)).to.deep.eq(true);
  });
  it("should return true if the both numbers are 7", function() {
    expect(isEitherEvenOrAreBoth7(7, 7)).to.deep.eq(true);
  });
  it("should return false if the both numbers are odd and not both 7", function() {
    expect(isEitherEvenOrAreBoth7(7, 3)).to.deep.eq(false);
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
* id: 45e91a10-4d74-4f10-83ef-b7b065d45830
* title: isEitherEvenAndLessThan9

### !question

Write a function called "isEitherEvenAndLessThan9".

Given two numbers, 'isEitherEvenAndLessThan9' returns whether at least one of them is even, and, both of them are less than 9.

```
var output = isEitherEvenAndLessThan9(2, 4);
console.log(output); // --> true

var output = isEitherEvenAndLessThan9(72, 2);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isEitherEvenAndLessThan9(num1, num2) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("isEitherEvenAndLessThan9", function() {
  it("should return a boolean", function() {
    expect(typeof isEitherEvenAndLessThan9(40, 3)).to.deep.eq("boolean");
  });
  it("should return true if the first number is even and both are less than 9", function() {
    expect(isEitherEvenAndLessThan9(4, 3)).to.deep.eq(true);
  });
  it("should return true if the second number is even and both are less than 9", function() {
    expect(isEitherEvenAndLessThan9(7, 8)).to.deep.eq(true);
  });
  it("should return true if the both numbers are even and both are less than 9", function() {
    expect(isEitherEvenAndLessThan9(2, 4)).to.deep.eq(true);
  });
  it("should return false if the both numbers are greater than 9", function() {
    expect(isEitherEvenAndLessThan9(72, 32)).to.deep.eq(false);
  });
  it("should return false if the first number is greater than 9", function() {
    expect(isEitherEvenAndLessThan9(72, 2)).to.deep.eq(false);
  });
  it("should return false if the second number is greater than 9", function() {
    expect(isEitherEvenAndLessThan9(2, 20)).to.deep.eq(false);
  });
  it("should return false if neither is even", function() {
    expect(isEitherEvenAndLessThan9(3, 5)).to.deep.eq(false);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
