# Array Methods 10

### !challenge

* type: local-snippet
* language: javascript
* id: 89972114-2f9f-47da-aae3-8df266ff32b7
* title: squareElements

### !question

Write a function called "squareElements".
Given an array of numbers, "squareElements" should return a new array where each element is the square of the element of the given array.
```
var output = squareElements([1, 2, 3]);
console.log(output); // --> [1, 4, 9]
```

### !end-question

### !placeholder

```js
function squareElements(arr) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("squareElements", function() {
  it("should return an array", function() {
    expect(Array.isArray(squareElements([1, 2, 3]))).to.deep.eq(true);
  });
  it("should return an array with the elements of the passed in array, squared", function() {
    expect(squareElements([1, 2, 3])).to.deep.eq([1, 4, 9]);
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
* id: bc26b616-3099-4e47-ad75-5670968a8ed1
* title: filterOddElements

### !question

Write a function called "filterOddElements".

Given an array of numbers, "filterOddElements" returns an array containing only the odd numbers of the given array.
```
var output = filterOddElements([1, 2, 3, 4, 5]);
console.log(output); // --> [1, 3, 5]
```

### !end-question

### !placeholder

```js
function filterOddElements(arr) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("filterOddElements", function() {
  it("should return an array", function() {
    expect(Array.isArray(filterOddElements([1, 2, 3, 4]))).to.deep.eq(true);
  });
  it("should return an array with the odd elements from the passed in array", function() {
    expect(filterOddElements([1, 2, 3, 4, 5])).to.deep.eq([1, 3, 5]);
  });
  it("should return an array if there are no odd numbers", function() {
    expect(filterOddElements([2, 4, 6])).to.deep.eq([]);
  });
  it("should return an array if given an emtpy array", function() {
    expect(filterOddElements([])).to.deep.eq([]);
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
* id: e2f51369-1a84-42dc-8613-2ccd23f46bc2
* title: computeProductOfAllElements

### !question

Write a function called "computeProductOfAllElements".

Given an array of numbers, "computeProductOfAllElements" returns the products of all the elements in the given array.

Notes:
* If given array is empty, it should return 0.

```
var output = computeProductOfAllElements([2, 5, 6]);
console.log(output); // --> 60
```

### !end-question

### !placeholder

```js
function computeProductOfAllElements(arr) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("computeProductOfAllElements", function() {
  it("should return a number", function() {
    expect(typeof computeProductOfAllElements([1, 2, 4])).to.deep.eq("number");
  });
  it("return the product of all elements", function() {
    expect(computeProductOfAllElements([1, 2, 4])).to.deep.eq(8);
  });
  it("return 0 if the passed in array is empty", function() {
    expect(computeProductOfAllElements([])).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
