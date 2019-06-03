# Array Methods 6

### !challenge

* type: local-snippet
* language: javascript
* id: 8e828b4d-ff6f-4fed-9bab-7d7a1b4b0c1e
* title: removeFromBack

### !question

Write a function called "removeFromBack".

Given an array, "removeFromBack" returns the given array with its last element removed.

Notes:
* You should be familiar with the method 'pop'.

```
var output = removeFromBack([1, 2, 3]);
console.log(output); // --> [1, 2]
```

### !end-question

### !placeholder

```js
function removeFromBack(arr) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("removeFromBack", function() {
  it("should return an array", function() {
    expect(Array.isArray(removeFromBack([1, 2, 3]))).to.deep.eq(true);
  });
  it("should remove the last element from a 3-element array", function() {
    expect(removeFromBack([1, 2, 3])).to.deep.eq([1, 2]);
  });
  it("should remove the last element from a 2-element array", function() {
    expect(removeFromBack([1, 2])).to.deep.eq([1]);
  });
  it("should handle an empty array", function() {
    expect(removeFromBack([])).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
