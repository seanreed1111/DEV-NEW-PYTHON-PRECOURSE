### !challenge

* type: local-snippet
* language: javascript
* id: bc301ebb-2394-447c-a893-a41007246e59
* title: computeAverageOfNumbers*.md

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
