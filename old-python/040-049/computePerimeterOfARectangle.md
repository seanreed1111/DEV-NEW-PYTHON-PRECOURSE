### !challenge

* type: local-snippet
* language: javascript
* id: 2fd97e96-08e0-4a67-a662-949acbf0e43c
* title: computePerimeterOfARectangle.md

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
