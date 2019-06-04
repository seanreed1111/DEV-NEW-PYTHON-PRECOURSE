# Math 4

### !challenge

* type: local-snippet
* language: javascript
* id: bf41eed3-a9de-4e31-9750-a645da0ab576
* title: computePower

### !question

Write a function called "computePower".

Given a number and an exponent, "computePower" returns the given number, raised to the given exponent.

```
var output = computePower(2, 3);
console.log(output); // --> 8
```

### !end-question

### !placeholder

```js
function computePower(num, exponent) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("computePower", function() {
  it("should return a number", function() {
    expect(typeof computePower(2, 4)).to.deep.eq("number");
  });
  it("should return a number raised to a given exponent", function() {
    expect(computePower(2, 4)).to.deep.eq(16);
  });
  it("should return a negative number raised to a given exponent", function() {
    expect(computePower(-2, 4)).to.deep.eq(16);
  });
  it("should return a number raised to 0", function() {
    expect(computePower(-2, 0)).to.deep.eq(1);
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
* id: d6959c6e-7921-4f3d-9b44-947c99fab887
* title: computeSquareRoot

### !question

Write a function called "computeSquareRoot".
Given a number, "computeSquareRoot" returns its square root.

```
var output = computeSquareRoot(9);
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function computeSquareRoot(num) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("computeSquareRoot", function() {
  it("should return a number", function() {
    expect(typeof computeSquareRoot(4)).to.deep.eq("number");
  });
  it("should return the square root of a number", function() {
    expect(computeSquareRoot(4)).to.deep.eq(2);
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
* id: e5a953a0-42f3-414c-bd77-c4247d272f7a
* title: doubleSquareRootOf

### !question

Write a function called "doubleSquareRootOf".
Given a number, "doubleSquareRootOf" returns double its square root.

```
var output = doubleSquareRootOf(121);
console.log(output); // --> 22
```

### !end-question

### !placeholder

```js
function doubleSquareRootOf(num) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("doubleSquareRootOf", function() {
  it("should return a number", function() {
    expect(typeof doubleSquareRootOf(9)).to.deep.eq("number");
  });
  it("should return the doubled square root of the passed in number", function() {
    expect(doubleSquareRootOf(9)).to.deep.eq(6);
  });
})

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
