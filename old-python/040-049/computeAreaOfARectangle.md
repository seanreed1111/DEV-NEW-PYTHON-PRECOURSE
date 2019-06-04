### !challenge

* type: local-snippet
* language: javascript
* id: 9ac26815-96c8-44bd-baac-960b874e4b32
* title: computeAreaOfARectangle.md

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
