### !challenge

* type: local-snippet
* language: javascript
* id: c910016d-56a3-4e65-88d8-01111d85a609
* title: getLongestElement*.md

### !question

Write a function called "getLongestElement".

Given an array, "getLongestElement" returns the longest string in the given array.

Notes:
* If there are ties, it returns the first element to appear.
* If the array is empty, it should return an empty string.

```
var output = getLongestElement(['one', 'two', 'three']);
console.log(output); // --> 'three'
```

### !end-question

### !placeholder

```js
function getLongestElement(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("getLongestElement", function() {
  it("should return a string", function() {
    expect(typeof(getLongestElement(["one", "two", "three"]))).to.deep.eq("string");
  });
  it("should return the longest element in an array", function() {
    expect(getLongestElement(["one", "two", "three"])).to.deep.eq("three");
  });
  it("should return the first longest element in an array when there are ties", function() {
    expect(getLongestElement(["one", "two", "one"])).to.deep.eq("one");
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
