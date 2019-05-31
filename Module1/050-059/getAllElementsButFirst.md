### !challenge

* type: local-snippet
* language: javascript
* id: 879c0dc1-12a5-4dad-876a-5f698f0dbe05
* title: getAllElementsButFirst.md

### !question

Write a function called "getAllElementsButFirst".

Given an array, "getAllElementsButFirst" returns an array with all the elements but the first.

```
var input = [1, 2, 3, 4];
var output = getAllElementsButFirst(input);
console.log(output); // --> [2, 3, 4]
```

### !end-question

### !placeholder

```js
function getAllElementsButFirst(array) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getAllElementsButFirst", function() {
  it("should return an array", function() {
    expect(Array.isArray(getAllElementsButFirst([4, 5, 6]))).to.deep.eq(true);
  });
  it("should return an array with all the elements of the passed in array, except for the first", function() {
    expect(getAllElementsButFirst([4, 5, 6])).to.deep.eq([5, 6]);
  });
  it("should return an empty array when passed in a single element array", function() {
    expect(getAllElementsButFirst([4])).to.deep.eq([]);
  });
  it("should return an empty array when passed in an empty array", function() {
    expect(getAllElementsButFirst([])).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
