### !challenge

* type: local-snippet
* language: javascript
* id: a2e9ed27-c4b2-4aa9-bd99-afe1d3a8a68a
* title: computeAreaOfACircle.md

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
