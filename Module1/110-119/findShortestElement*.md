### !challenge

* type: local-snippet
* language: javascript
* id: 3a3527f5-84ad-4d59-8ba5-5e774661e37e
* title: findShortestElement*.md

### !question

Write a function called "findShortestElement".

Given an array, "findShortestElement" returns the shortest string within the given array.

Notes:
* If there are ties, it should return the first element to appear.
* If the given array is empty, it should return an empty string.

```
var output = findShortestElement(['a', 'two', 'three']);
console.log(output); // --> 'a'
```

### !end-question

### !placeholder

```js
function findShortestElement(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("findShortestElement", function() {
  it("should return a string", function() {
    expect(typeof(findShortestElement(["one", "two", "three"]))).to.deep.eq("string");
  });
  it("should return the shortest element in an array", function() {
    expect(findShortestElement(["a", "two", "three"])).to.deep.eq("a");
  });
  it("should return the first shortest element in an array when there are ties", function() {
    expect(findShortestElement(["one", "to", "no"])).to.deep.eq("to");
  });
  it("should return an empty string if the array is empty", function() {
    expect(findShortestElement([])).to.deep.eq("");
  })
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
