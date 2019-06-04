# Array Methods 14

### !challenge

* type: local-snippet
* language: javascript
* id: a67d49da-9135-4b9b-96be-37a1accc9b5f
* title: joinArraysOfArrays

### !question

Write a function called "joinArrayOfArrays".

Given an array of arrays, "joinArrayOfArrays" returns a single array containing the elements of the nested arrays.

```
var output = joinArrayOfArrays([[1, 4], [true, false], ['x', 'y']]);
console.log(output); // --> [1, 4, true, false, 'x', 'y']
```

You should be familiar with the "concat" method for this problem.

### !end-question

### !placeholder

```js
function joinArrayOfArrays(arr) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js


describe("joinArrayOfArrays", function() {
  it("should return an array", function() {
    expect(Array.isArray(joinArrayOfArrays([['a', 'b'], [1, 3], [true, false]]))).to.deep.eq(true);
  });
  it("should return an array with the elements from all the nested arrays", function() {
    expect(joinArrayOfArrays([['a', 'b'], [1, 3], [true, false]])).to.deep.eq(['a', 'b', 1, 3, true, false]);
  });
  it("should handle empty arrays in the first position", function() {
    expect(joinArrayOfArrays([[], [1, 3], [true, false]])).to.deep.eq([1, 3, true, false]);
  });
  it("should handle empty arrays in the second position", function() {
    expect(joinArrayOfArrays([['a', 'b'], [], [true, false]])).to.deep.eq(['a', 'b', true, false]);
  });
  it("should handle empty arrays in the third position", function() {
    expect(joinArrayOfArrays([['a', 'b'], [1, 3], []])).to.deep.eq(['a', 'b', 1, 3]);
  });
  it("should handle empty arrays in all positions", function() {
    expect(joinArrayOfArrays([[], [], []])).to.deep.eq([]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
