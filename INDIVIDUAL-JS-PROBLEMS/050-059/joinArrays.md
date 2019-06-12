### !challenge

* type: local-snippet
* language: javascript
* id: 14e62a93-6633-4448-bea5-14ab6d68995c
* title: joinArrays.md

### !question

Write a function called "joinArrays".

Given two arrays, "joinArrays" returns an array with the elements of "arr1" in order, followed by the elementsin "arr2".

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
