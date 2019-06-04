### !challenge

* type: local-snippet
* language: javascript
* id: 39177ecc-9a13-4ca6-83c2-495489bfa312
* title: getElementsAfter.md

### !question

Write a function called "getElementsAfter".

Given an array and an index, "getElementsAfter" returns a new array with all the elements after (but not including) the given index.

```
var output = getElementsAfter(['a', 'b', 'c', 'd', 'e'], 2);
console.log(output); // --> ['d', 'e']
```

### !end-question

### !placeholder

```js
function getElementsAfter(array, n) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getElementsAfter", function() {
  it("should return an array", function() {
    expect(Array.isArray(getElementsAfter([4, 5, 6], 2))).to.deep.eq(true);
  });
  it("should return an array with all the elements of the passed in array getElementsAfter the nth", function() {
    expect(getElementsAfter([4, 5, 6, 7, 8, 9], 3)).to.deep.eq([8, 9]);
  });
  it("should return an empty array when passed in a single element array", function() {
    expect(getElementsAfter([4], 0)).to.deep.eq([]);
  });
  it("should return an empty array when passed an n out of range", function() {
    expect(getElementsAfter([4], 11)).to.deep.eq([]);
  });
  it("should return an empty array when passed in an empty array", function() {
    expect(getElementsAfter([])).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
