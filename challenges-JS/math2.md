# Math 2

### !challenge

* type: local-snippet
* language: javascript
* id: 9ac26815-96c8-44bd-baac-960b874e4b32
* title: computeAreaOfARectangle

### !question

Write a function called "computeAreaOfARectangle".

Given the length and width of a rectangle, "computeAreaOfARectangle" returns its area.

```
var output = computeAreaOfARectangle(4, 8);
console.log(output); // --> 32
```

### !end-question

### !placeholder

```js
function computeAreaOfARectangle(length, width) {
  // your code here
  
}

```

### !end-placeholder

### !tests

```js

describe("computeAreaOfARectangle", function() {
  it("should return a number", function() {
    expect(typeof computeAreaOfARectangle(7, 6)).to.deep.eq("number");
  });
  it("should return the area of a rectangle", function() {
    expect(computeAreaOfARectangle(7, 6)).to.deep.eq(42);
  });
})

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 2fd97e96-08e0-4a67-a662-949acbf0e43c
* title: computePerimeterOfARectangle

### !question

Write a function called "computePerimeterOfARectangle".

Given a length and a width describing a rectangle, "computePerimeterOfARectangle" returns its perimter.

```
var output = computePerimeterOfARectangle(5, 2);
console.log(output); // --> 14
```

### !end-question

### !placeholder

```js
function computePerimeterOfARectangle(length, width) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("computePerimeterOfARectangle", function() {
  it("should return a number", function() {
    expect(typeof computePerimeterOfARectangle(5, 2)).to.deep.eq("number");
  });
  it("should return the perimeter of a rectangle", function() {
    expect(computePerimeterOfARectangle(5, 2)).to.deep.eq(14);
  });
})

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 349703e4-eba7-4566-9a0f-c81569733b84
* title: computePerimeterOfATriangle

### !question

Write a function called "computePerimeterOfATriangle".

Given 3 sides describing a triangle, "computePerimeterOfATriangle" returns its perimter.

```
var output = computePerimeterOfATriangle(6, 7, 10);
console.log(output); // --> 23
```

### !end-question

### !placeholder

```js
function computePerimeterOfATriangle(side1, side2, side3) {
  // your code here
  
}

```

### !end-placeholder

### !tests

```js


describe("computePerimeterOfATriangle", function() {
  it("should return a number", function() {
    expect(typeof computePerimeterOfATriangle(6, 7, 10)).to.deep.eq("number");
  });
  it("should return the perimeter of a triangle", function() {
    expect(computePerimeterOfATriangle(6, 7, 10)).to.deep.eq(23);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
