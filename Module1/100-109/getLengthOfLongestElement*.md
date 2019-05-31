### !challenge

* type: local-snippet
* language: javascript
* id: bed00f94-4f5c-4a82-8cfa-7eaf872368f5
* title: getLengthOfLongestElement*.md

### !question

Write a function called "getLengthOfLongestElement".

Given an array, "getLengthOfLongestElement" returns the length of the longest string in the given array.

Notes:
* It should return 0 if the array is empty.

```
var output = getLengthOfLongestElement(['one', 'two', 'three']);
console.log(output); // --> 5
```

### !end-question

### !placeholder

```js
function getLengthOfLongestElement(arr) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getLengthOfLongestElement", function() {
  it("should return a number", function() {
    expect(typeof getLengthOfLongestElement(["one", "two", "three"])).to.deep.eq("number");
  });
  it("should return the length of the longest element in an array", function() {
    expect(getLengthOfLongestElement(["one", "two", "three"])).to.deep.eq(5);
  });
  it("it should handle ties", function() {
    expect(getLengthOfLongestElement(["one", "two", "no"])).to.deep.eq(3);
  });
  it("it should return 0 when given an empty array", function() {
    expect(getLengthOfLongestElement([])).to.deep.eq(0);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
