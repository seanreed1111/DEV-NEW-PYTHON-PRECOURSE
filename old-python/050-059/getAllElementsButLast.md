### !challenge

* type: local-snippet
* language: javascript
* id: 1662f5c1-43d4-4cbe-8a0e-2c6866408de5
* title: getAllElementsButLast.md

### !question

Write a function called "getAllElementsButLast".

Given an array, "getAllElementsButLast" returns an array with all the elements but the last.

```
var input = [1, 2, 3, 4];
var output = getAllElementsButLast(input);
console.log(output); // --> [1, 2 , 3]
```

### !end-question

### !placeholder

```js
function getAllElementsButLast(array) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getAllElementsButLast", function() {
  it("should return an array", function() {
    expect(Array.isArray(getAllElementsButLast([4, 5, 6]))).to.deep.eq(true);
  });
  it("should return an array with all the elements of the passed in array, except for the last", function() {
    expect(getAllElementsButLast([4, 5, 6])).to.deep.eq([4, 5]);
  });
  it("should return an empty array when passed in a single element array", function() {
    expect(getAllElementsButLast([4])).to.deep.eq([]);
  });
  it("should return an empty array when passed in an empty array", function() {
    expect(getAllElementsButLast([])).to.deep.eq([]);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
