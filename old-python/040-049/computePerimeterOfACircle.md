### !challenge

* type: local-snippet
* language: javascript
* id: a4c9be25-3121-4933-a4b5-e6099ca26ec6
* title: computePerimeterOfACircle.md

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
