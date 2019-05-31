### !challenge

* type: local-snippet
* language: javascript
* id: d89ba6ec-9149-4147-b78e-d449659e0661
* title: getLastElement.md

### !question

Write a function called "getLastElement".

Given an array, "getLastElement" returns the last element of the given array.

Notes:
* If the given array has a length of 0, it should return 'undefined'.

```
var output = getLastElement([1, 2, 3, 4]);
console.log(output); // --> 4
```

### !end-question

### !placeholder

```js
function getLastElement(array) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("getLastElement", function() {
  it("should return the last element of an array", function() {
    expect(getLastElement([1, 3, 5])).to.deep.eq(5);
  });
  it("should return undefined if the array is empty", function() {
    expect(getLastElement([])).to.deep.eq(undefined);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
