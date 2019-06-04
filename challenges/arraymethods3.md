# Array Methods 3

### !challenge

* type: local-snippet
* language: javascript
* id: 14e62a93-6633-4448-bea5-14ab6d68995c
* title: joinArrays

### !question

Write a function called "joinArrays".

Given two arrays, "joinArrays" returns an array with the elements of "arr1" in order, followed by the elements in "arr2".

```
var output = joinArrays([1, 2], [3, 4]);
console.log(output); // --> [1, 2, 3, 4]
```

You should be familiar with the "concat" method for this problem.

### !end-question

### !placeholder

```js
function joinArrays(arr1, arr2) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("joinArrays", function() {
  it("should return an array", function() {
    expect(Array.isArray(joinArrays(['a', 'b'], [1, 3]))).to.deep.eq(true);
  });
  it("should return an array with the elements from the first and then the second array", function() {
    expect(joinArrays(['a', 'b'], [1, 3])).to.deep.eq(['a', 'b', 1, 3]);
  });
  it("should handle empty arrays in the first position", function() {
    expect(joinArrays([], [1, 3])).to.deep.eq([1, 3]);
  });
  it("should handle empty arrays in the second position", function() {
    expect(joinArrays(['a', 'b'], [])).to.deep.eq(['a', 'b']);
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
* id: 39177ecc-9a13-4ca6-83c2-495489bfa312
* title: getElementsAfter

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

### !challenge

* type: local-snippet
* language: javascript
* id: 41fe3188-d6e9-4f43-9c4a-a1313a61b407
* title: getElementsUpTo

### !question

Write a function called "getElementsUpTo".

Given an array and a index, "getElementsUpTo", returns an array with all the elements up until, but not including, the element at the given index.

Notes:
* In order to do this you should be familiar with the 'slice' method.

```
var output = getElementsUpTo(['a', 'b', 'c', 'd', 'e'], 3)
console.log(output); // --> ['a', 'b', 'c']
```

### !end-question

### !placeholder

```js
function getElementsUpTo(array, n) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("getElementsUpTo", function() {
  it("should return an array", function() {
    expect(Array.isArray(getElementsUpTo([4, 5, 6], 2))).to.deep.eq(true);
  });
  it("should return an array with all the elements of the passed in array up until the nth", function() {
    expect(getElementsUpTo([4, 5, 6], 2)).to.deep.eq([4, 5]);
  });
  it("should return an empty array when passed in a single element array", function() {
    expect(getElementsUpTo([4], 0)).to.deep.eq([]);
  });
  it("should return a mirror of the original array when passed an n out of range", function() {
    expect(getElementsUpTo([4], 10)).to.deep.eq([4]);
  });
  it("should return an empty array when passed in an empty array", function() {
    expect(getElementsUpTo([])).to.deep.eq([]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
