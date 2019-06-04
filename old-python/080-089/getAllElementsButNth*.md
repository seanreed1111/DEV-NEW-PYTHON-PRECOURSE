### !challenge

* type: local-snippet
* language: javascript
* id: dac91596-8674-4ea2-a348-db7120c0fe36
* title: getAllElementsButNth*.md

### !question

Write a function called "getAllElementsButNth".

Given an array and an index, "getAllElementsButNth" returns an array with all the elements but the nth.

```
var output = getAllElementsButNth(['a', 'b', 'c'], 1);
console.log(output); // --> ['a', 'c']
```

### !end-question

### !placeholder

```js
function getAllElementsButNth(array, n) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getAllElementsButNth", function() {
  it("should return an array", function() {
    expect(Array.isArray(getAllElementsButNth([4, 5, 6], 2))).to.deep.eq(true);
  });
  it("should return an array with all the elements of the passed in array, except for the nth", function() {
    expect(getAllElementsButNth([4, 5, 6], 0)).to.deep.eq([5, 6]);
  });
  it("should return an empty array when passed in a single element array", function() {
    expect(getAllElementsButNth([4], 0)).to.deep.eq([]);
  });
  it("should return a mirror of the original array when passed an n out of range", function() {
    expect(getAllElementsButNth([4], 10)).to.deep.eq([4]);
  });
  it("should return an empty array when passed in an empty array", function() {
    expect(getAllElementsButNth([])).to.deep.eq([]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
