### !challenge

* type: local-snippet
* language: javascript
* id: 4912dcc3-714b-405d-a1c6-9d4668195528
* title: computeTripledAreaOfARectangle.md

### !question

Write a function called "computeTripledAreaOfARectangle".

Given a length and width of a rectangle, "computeTripledAreaOfARectangle" returns the rectangle's area, multiplied by 3.

```
var output = computeTripledAreaOfARectangle(2, 4);
console.log(output); // --> 24
```

### !end-question

### !placeholder

```js
function computeTripledAreaOfARectangle(length, width) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("computeTripledAreaOfARectangle", function() {
  it("should return a number", function() {
    expect(typeof computeTripledAreaOfARectangle(7, 6)).to.deep.eq("number");
  });
  it("should return the area of a rectangle", function() {
    expect(computeTripledAreaOfARectangle(7, 6)).to.deep.eq(126);
  });
})

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
