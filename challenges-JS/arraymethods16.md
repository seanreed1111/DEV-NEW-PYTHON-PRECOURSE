# Array Methods 16

### !challenge

* type: local-snippet
* language: javascript
* id: 99c43844-c828-47d6-a073-db33a9f9bfb7
* title: getLongestWordOfMixedElements

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

### !challenge

* type: local-snippet
* language: javascript
* id: c73e353f-8655-42e8-8f6b-7e342182ca9c
* title: getLargestNumberAmongMixedElements

### !question

Write a function called "getLargestNumberAmongMixedElements".

Given any array, "getLargestNumberAmongMixedElements" returns the largest number in the given array.

Notes:
* The array might contain values of a type other than numbers.
* If the array is empty, it should return 0.
* If the array contains no numbers, it should return 0.

```
var output = getLargestNumberAmongMixedElements([3, 'word', 5, 'up', 3, 1]);
console.log(output); // --> 5
```

### !end-question

### !placeholder

```js
function getLargestNumberAmongMixedElements(arr) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("getLargestNumberAmongMixedElements", function() {
  it("should return a number", function() {
    expect(typeof getLargestNumberAmongMixedElements([3, 5, 3, 1])).to.deep.eq("number");
  });
  it("should return the largest element in an array", function() {
    expect(getLargestNumberAmongMixedElements([3, "word", 5, "up", 3, 1])).to.deep.eq(5);
  });
  it("should return the largest element in an array when there are ties", function() {
    expect(getLargestNumberAmongMixedElements(["word", 3, 5, 3, "wordy", "up", 1, 5])).to.deep.eq(5);
  });
  it("should return the largest element in an array when they are all negative", function() {
    expect(getLargestNumberAmongMixedElements([-1, -5, "word", -3])).to.deep.eq(-1);
  });
  it("should return 0 when the array is empty", function() {
    expect(getLargestNumberAmongMixedElements([])).to.deep.eq(0);
  });
  it("should return 0 when there are no numbers", function() {
    expect(getLargestNumberAmongMixedElements(["word", "up"])).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
