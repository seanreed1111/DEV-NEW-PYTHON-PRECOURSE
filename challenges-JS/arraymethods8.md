# Array Methods 8

### !challenge

* type: local-snippet
* language: javascript
* id: 5fc75a18-76e2-4e35-afac-e8433908ea84
* title: removeElement

### !question

Write a function called "removeElement".

Given an array of elements, and a "discarder" parameter, "removeElement" returns an array containing the items in the given array that do not match the "discarder" parameter.

Notes:
* If all the elements match, it should return an empty array.
* If an empty array is passed in, it should return an empty array.

```
var output = removeElement([1, 2, 3, 2, 1], 2);
console.log(output); // --> [1, 3, 1]
```

### !end-question

### !placeholder

```js
function removeElement(array, discarder) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("removeElement", function() {
  it("should return an array", function() {
    expect(Array.isArray(removeElement(["there", "it", "is", "there"]))).to.deep.eq(true);
  });
  it("return an array with all strings not matching 'discarder'", function() {
    expect(removeElement(["there", "it", "is", "there"], "there")).to.deep.eq(["it", "is"]);
  });
  it("return an array with all numbers not matching 'discarder'", function() {
    expect(removeElement([1, 2, 4, 3, 1, 4], 4)).to.deep.eq([1, 2, 3, 1]);
  });
  it("return an array with all booleans not matching 'discarder'", function() {
    expect(removeElement([true, true, true, false, true], true)).to.deep.eq([false]);
  });
  it("return an emtpy array when all elements match 'discarder'", function() {
    expect(removeElement([true, true, true, true], true)).to.deep.eq([]);
  });
  it("return an emtpy array when given an empty array", function() {
    expect(removeElement([], 4)).to.deep.eq([]);
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
* id: 93c14e61-6f43-4158-848c-268271807a39
* title: keep

### !question

Write a function called "keep".

Given an array and a keeper element, "keep" returns an array containing the items that match the given keeper element.

Notes:
* If no elements match, "keep" should return an empty array.

```
var output = keep([1, 2, 3, 2, 1], 2)
console.log(output); --> [2, 2]
```

### !end-question

### !placeholder

```js
function keep(array, keeper) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("keep", function() {
  it("should return an array", function() {
    expect(Array.isArray(keep(["there", "it", "is", "there"]))).to.deep.eq(true);
  });
  it("returns an array with all strings matching 'kept'", function() {
    expect(keep(["there", "it", "is", "there"], "there")).to.deep.eq(["there", "there"]);
  });
  it("returns an array with all numbers matching 'kept'", function() {
    expect(keep([1, 2, 4, 3, 1, 4], 4)).to.deep.eq([4, 4]);
  });
  it("returns an array with all booleans matching 'kept'", function() {
    expect(keep([true, true, true, false, true], true)).to.deep.eq([true, true, true, true]);
  });
  it("returns an emtpy array when no elements match 'kept'", function() {
    expect(keep([true, true, true, false, true], 4)).to.deep.eq([]);
  });
  it("returns an emtpy array when given an empty array", function() {
    expect(keep([], 4)).to.deep.eq([]);
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
* id: bc301ebb-2394-447c-a893-a41007246e59
* title: computeAverageOfNumbers

### !question

Write a function called "computeAverageOfNumbers".

Given an array of numbers, "computeAverageOfNumbers" returns their average.

Notes:
* If given an empty array, it should return 0.

```
var input = [1,2,3,4,5];
var output = computeAverageOfNumbers(input);
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function computeAverageOfNumbers(nums) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("computeAverageOfNumbers", function() {
  it("should return a number", function() {
    expect(typeof(computeAverageOfNumbers([6, 8, 10]))).to.deep.eq("number");
  });
  it("should return the average of the numbers in the given array", function() {
    expect(computeAverageOfNumbers([6, 8, 10])).to.deep.eq(8);
  });
  it("should return the average of negative numbers in the given array", function() {
    expect(computeAverageOfNumbers([-6, -8, -10])).to.deep.eq(-8);
  });
  it("should return 0 if given an empty array", function() {
    expect(computeAverageOfNumbers([])).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
