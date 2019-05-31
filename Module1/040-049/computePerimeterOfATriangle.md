### !challenge

* type: local-snippet
* language: javascript
* id: 349703e4-eba7-4566-9a0f-c81569733b84
* title: computePerimeterOfATriangle.md

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
