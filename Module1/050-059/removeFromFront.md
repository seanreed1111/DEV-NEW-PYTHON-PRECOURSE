### !challenge

* type: local-snippet
* language: javascript
* id: 94f66a0e-795b-439b-bb69-c12c78b475b0
* title: removeFromFront.md

### !question

Write a function called "removeFromFront".

Given an array, "removeFromFront" returns the given array with its first element removed.

Notes:
* You should be familiar with the method 'shift'.

```
var output = removeFromFront([1, 2, 3]);
console.log(output); // --> [2, 3]
```

### !end-question

### !placeholder

```js
function removeFromFront(arr) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeFromFront", function() {
  it("should return an array", function() {
    expect(Array.isArray(removeFromFront([1, 2, 3]))).to.deep.eq(true);
  });
  it("should return the array with the first element removed", function() {
    expect(removeFromFront([1, 2])).to.deep.eq([2]);
  });
  it("should handle an empty array", function() {
    expect(removeFromFront([])).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
