### !challenge

* type: local-snippet
* language: javascript
* id: 99c43844-c828-47d6-a073-db33a9f9bfb7
* title: getLongestWordOfMixedElements*.md

### !question

Write a function called "getLongestWordOfMixedElements".

Given an array of mixed types, "getLongestWordOfMixedElements" returns the longest string in the given array.

Notes:
* If the array is empty, it should return an empty string ("").
* If the array contains no strings; it should return an empty string.

```
var output = getLongestWordOfMixedElements([3, 'word', 5, 'up', 3, 1]);
console.log(output); // --> 'word'
```

### !end-question

### !placeholder

```js
function getLongestWordOfMixedElements(arr) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("getLongestWordOfMixedElements", function() {
  it("should return a string", function() {
    expect(typeof getLongestWordOfMixedElements(["these", "are", "strings"])).to.deep.eq("string");
  });
  it("should return the longest string in an array", function() {
    expect(getLongestWordOfMixedElements([3, "word", 5, "up", 3, 1])).to.deep.eq("word");
  });
  it("should return the longest string in an array that appears first when there are ties", function() {
    expect(getLongestWordOfMixedElements(["word", 3, 5, 3, "bird", "up", 1, 5])).to.deep.eq("word");
  });
  it("should return an empty string when the array is empty", function() {
    expect(getLongestWordOfMixedElements([])).to.deep.eq("");
  });
  it("should return an empty string there are no strings", function() {
    expect(getLongestWordOfMixedElements([1, 2, 4])).to.deep.eq("");
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
