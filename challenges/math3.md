# Math 3

### !challenge

* type: local-snippet
* language: javascript
* id: 4912dcc3-714b-405d-a1c6-9d4668195528
* title: computeTripledAreaOfARectangle

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

### !challenge

* type: local-snippet
* language: javascript
* id: a4c9be25-3121-4933-a4b5-e6099ca26ec6
* title: computePerimeterOfACircle

### !question

Write a function called "computePerimeterOfACircle".

Given the radius of a circle, "computePerimeterOfACircle" returns its perimeter.

Notes:
* `Math.PI` can be used for pi.

```
var output = computePerimeterOfACircle(4);
console.log(output); // --> 25.132741228718345
```

Reference:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/PI

### !end-question

### !placeholder

```js
function computePerimeterOfACircle(radius) {
  // your code here
  
}

```

### !end-placeholder

### !tests

```js

describe("computePerimeterOfACircle", function() {
  it("should return a number", function() {
    expect(typeof computePerimeterOfACircle(4)).to.deep.eq("number");
  });
  it("should return the perimeter of a circle", function() {
    expect(computePerimeterOfACircle(4)).to.deep.eq(25.132741228718345);
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
* id: a2e9ed27-c4b2-4aa9-bd99-afe1d3a8a68a
* title: computeAreaOfACircle

### !question

Write a function called "computeAreaOfACircle".

Given the radius of a circle, "computeAreaOfACircle" returns its area.

Notes:
* `Math.PI` can be used for pi.

```
var output = computeAreaOfACircle(4);
console.log(output); // --> 50.26548245743669
```


Reference:
https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Global_Objects/Math/PI

### !end-question

### !placeholder

```js
function computeAreaOfACircle(radius) {
  // your code here
  
}

```

### !end-placeholder

### !tests

```js

describe("computeAreaOfACircle", function() {
  it("should return a number", function() {
    expect(typeof computeAreaOfACircle(4)).to.deep.eq("number");
  });
  it("should return the area of a circle", function() {
    expect(computeAreaOfACircle(4)).to.deep.eq(50.26548245743669);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
