### !challenge

* type: local-snippet
* language: javascript
* id: 0c0a6c72-d8a0-488e-a0c7-c3a8df27630f
* title: getLengthOfShortestElement*.md

### !question

Write a function called "getLengthOfShortestElement".

Given an array, "getLengthOfShortestElement" returns the length of the shortest string in the given array.

Notes:
* It should return 0 if the array is empty.

```
var output = getLengthOfShortestElement(['one', 'two', 'three']);
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function getLengthOfShortestElement(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("getLengthOfShortestElement", function() {
  it("should return a number", function() {
    expect(typeof getLengthOfShortestElement(["one", "two", "three"])).to.deep.eq("number");
  });
  it("should return the length of the shortest element in an array", function() {
    expect(getLengthOfShortestElement(["one", "four", "three"])).to.deep.eq(3);
  });
  it("it should handle ties", function() {
    expect(getLengthOfShortestElement(["one", "to", "no"])).to.deep.eq(2);
  });
  it("it should return 0 when given an empty array", function() {
    expect(getLengthOfShortestElement([])).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
