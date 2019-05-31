### !challenge

* type: local-snippet
* language: javascript
* id: d5349d84-2036-435e-a352-d996dffc92e3
* title: joinThreeArrays.md

### !question

Write a function called "joinThreeArrays".

Given three arrays, "joinThreeArrays" returns an array with the elements of "arr1" in order followed by the elements in "arr2" in order followed by the elements of "arr3" in order.

```
var output = joinThreeArrays([1, 2], [3, 4], [5, 6]);
console.log(output); // --> [1, 2, 3, 4, 5, 6]
```

You should be familiar with the "concat" method for this problem.


### !end-question

### !placeholder

```js
function joinThreeArrays(arr1, arr2, arr3) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("joinThreeArrays", function() {
  it("should return an array", function() {
    expect(Array.isArray(joinThreeArrays(['a', 'b'], [1, 3], [true, false]))).to.deep.eq(true);
  });
  it("should return an array with the elements from the first and then the second array", function() {
    expect(joinThreeArrays(['a', 'b'], [1, 3], [true, false])).to.deep.eq(['a', 'b', 1, 3, true, false]);
  });
  it("should handle empty arrays in the first position", function() {
    expect(joinThreeArrays([], [1, 3], [true, false])).to.deep.eq([1, 3, true, false]);
  });
  it("should handle empty arrays in the second position", function() {
    expect(joinThreeArrays(['a', 'b'], [], [true, false])).to.deep.eq(['a', 'b', true, false]);
  });
  it("should handle empty arrays in the third position", function() {
    expect(joinThreeArrays(['a', 'b'], [1, 3], [])).to.deep.eq(['a', 'b', 1, 3]);
  });
  it("should handle empty arrays in all positions", function() {
    expect(joinThreeArrays([], [], [])).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
