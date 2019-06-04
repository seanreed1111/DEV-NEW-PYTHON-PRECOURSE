# Array Methods 1

### !challenge

* type: local-snippet
* language: javascript
* id: 95a46849-2478-44f2-8783-0729dd17eaae
* title: getNthElement

### !question

Write a function called "getNthElement".

Given an array and an integer, "getNthElement" returns the element at the given integer, within the given array.

Notes:
* If the array has a length of 0, it should return 'undefined'.

```
var output = getNthElement([1, 3, 5], 1);
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function getNthElement(array, n) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("getNthElement", function() {
  it("should return the nth element of an array", function() {
    expect(getNthElement([1, 3, 5], 1)).to.deep.eq(3);
  });
  it("should return undefined if the array is empty", function() {
    expect(getNthElement([], 1)).to.deep.eq(undefined);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: 7c720b84-05ae-44b5-ab40-5ef78db09bec
* title: getFirstElement

### !question

Write a function called "getFirstElement".

Given an array, "getFirstElement" returns the first element of the given array.

Notes:
* If the given array has a length of 0, it should return undefined.

```
var output = getFirstElement([1, 2, 3, 4, 5]);
console.log(output); // --> 1
```

### !end-question

### !placeholder

```js
function getFirstElement(array) {
  // your code here

}
```

### !end-placeholder

### !tests

```js


describe("getFirstElement", function() {
  it("should return the first element of an array", function() {
    expect(getFirstElement([1, 3, 5])).to.deep.eq(1);
  });
  it("should return undefined if the array is empty", function() {
    expect(getFirstElement([])).to.deep.eq(undefined);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge

### !challenge

* type: local-snippet
* language: javascript
* id: d89ba6ec-9149-4147-b78e-d449659e0661
* title: getLastElement

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
