# Array Methods 7

### !challenge

* type: local-snippet
* language: javascript
* id: d5349d84-2036-435e-a352-d996dffc92e3
* title: joinThreeArrays

### !question

Write a function called "joinThreeArrays".

Given three arrays, "joinThreeArrays" returns an array with the elements of "arr1" in order followed by the elements in "arr2" in order followed by the elements of "arr3" in order.

```
var output = joinThreeArrays([1, 2], [3, 4], [5, 6]);
console.log(output); // --> [1, 2, 3, 4, 5, 6]
```

You should be familiar with the "concat" method for this problem.


### !end-question

### !placeholder

```js
function joinThreeArrays(arr1, arr2, arr3) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("joinThreeArrays", function() {
  it("should return an array", function() {
    expect(Array.isArray(joinThreeArrays(['a', 'b'], [1, 3], [true, false]))).to.deep.eq(true);
  });
  it("should return an array with the elements from the first and then the second array", function() {
    expect(joinThreeArrays(['a', 'b'], [1, 3], [true, false])).to.deep.eq(['a', 'b', 1, 3, true, false]);
  });
  it("should handle empty arrays in the first position", function() {
    expect(joinThreeArrays([], [1, 3], [true, false])).to.deep.eq([1, 3, true, false]);
  });
  it("should handle empty arrays in the second position", function() {
    expect(joinThreeArrays(['a', 'b'], [], [true, false])).to.deep.eq(['a', 'b', true, false]);
  });
  it("should handle empty arrays in the third position", function() {
    expect(joinThreeArrays(['a', 'b'], [1, 3], [])).to.deep.eq(['a', 'b', 1, 3]);
  });
  it("should handle empty arrays in all positions", function() {
    expect(joinThreeArrays([], [], [])).to.deep.eq([]);
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
* id: a5d9e27b-ea2f-4134-ad30-ef9366b3c761
* title: addToFrontOfNew

### !question

Write a function called "addToFrontOfNew".

Given an array and an element, "addToFrontOfNew" returns a new array containing all the elements of the given array, with the given element added to the front.

Important: It should be a NEW array instance, not the original array instance.

```
var input = [1, 2];
var output = addToFrontOfNew(input, 3);
console.log(output); // --> [3, 1, 2];
console.log(input); --> [1, 2]
```

### !end-question

### !placeholder

```js
function addToFrontOfNew(arr, element) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("addToFrontOfNew", function() {
  it("should return an array", function() {
    expect(Array.isArray(addToFrontOfNew([1, 2], 3))).to.deep.eq(true);
  });
  it("should add an element to the end of an array", function() {
    expect(addToFrontOfNew([1, 2], 3)).to.deep.eq([3, 1, 2]);
  });
  it("should add an element to the end of an empty array", function() {
    expect(addToFrontOfNew([], 3)).to.deep.eq([3]);
  });
  it("should leave arr unmodified", function() {
    var originalArray = [1, 2];
    var newArray = addToFrontOfNew(originalArray, 3);
    expect(originalArray).to.deep.eq([1, 2]);
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
* id: 52e8002f-f926-4b68-b70b-c41fe566ba8c
* title: addToBackOfNew

### !question

Write a function called "addToBackNew".

Given an array and an element, "addToBackNew" returns a clone of the given array, with the given element added to the end.

Important: It should be a NEW array instance, not the original array instance.

```
var input = [1, 2];
var output = addToBackOfNew(input, 3);
console.log(input); // --> [1, 2]
console.log(output); // --> [1, 2, 3]
```

### !end-question

### !placeholder

```js
function addToBackOfNew(arr, element) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("addToBackOfNew", function() {
  it("should return an array", function() {
    expect(Array.isArray(addToBackOfNew([1, 2], 3))).to.deep.eq(true);
  });
  it("should add an element to the end of an array", function() {
    expect(addToBackOfNew([1, 2], 3)).to.deep.eq([1, 2, 3]);
  });
  it("should add an element to the end of an empty array", function() {
    expect(addToBackOfNew([], 3)).to.deep.eq([3]);
  });
  it("should leave arr unmodified", function() {
    var originalArray = [1, 2];
    var newArray = addToBackOfNew(originalArray, 3);
    expect(originalArray).to.deep.eq([1, 2]);
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
* id: dac91596-8674-4ea2-a348-db7120c0fe36
* title: getAllElementsButNth

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
