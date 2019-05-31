### !challenge

* type: local-snippet
* language: javascript
* id: 89972114-2f9f-47da-aae3-8df266ff32b7
* title: squareElements*.md

### !question

Write a function called "squareElements".
Given an array of numbers, "squareElements" should return a new array where each element is the square of the element of the given array.
```
var output = squareElements([1, 2, 3]);
console.log(output); // --> [1, 4, 9]
```

### !end-question

### !placeholder

```js
function squareElements(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("squareElements", function() {
  it("should return an array", function() {
    expect(Array.isArray(squareElements([1, 2, 3]))).to.deep.eq(true);
  });
  it("should return an array with the elements of the passed in array, squared", function() {
    expect(squareElements([1, 2, 3])).to.deep.eq([1, 4, 9]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
