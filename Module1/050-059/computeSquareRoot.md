### !challenge

* type: local-snippet
* language: javascript
* id: d6959c6e-7921-4f3d-9b44-947c99fab887
* title: computeSquareRoot.md

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
