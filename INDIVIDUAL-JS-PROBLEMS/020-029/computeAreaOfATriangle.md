### !challenge

* type: local-snippet
* language: javascript
* id: bb88d243-fda0-4b49-ba45-f4a19ead5d03
* title: computeAreaOfATriangle.md

### !question

Write a function called "computeAreaOfATriangle".

Given the base and height of a triangle, "computeAreaOfATriangle" returns its area.

```
var output = computeAreaOfATriangle(4, 6);
console.log(output); // --> 12
```

### !end-question

### !placeholder

```js
function computeAreaOfATriangle(base, height) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("computeAreaOfATriangle", function() {
  it("should return a number", function() {
    expect(typeof computeAreaOfATriangle(6, 4)).to.deep.eq("number");
  });
  it("should return the area of a triangle", function() {
    expect(computeAreaOfATriangle(6, 4)).to.deep.eq(12);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
