# Array Methods 9

### !challenge

* type: local-snippet
* language: javascript
* id: f606fc41-1d59-4fa5-8d68-d95dfd88a02e
* title: filterOddLengthWords

### !question

Write a function called "filterOddLengthWords".

Given an array of string, "filterOddLengthWords" returns an array containing only the elements of the given array whose lengths are odd numbers.

```
var output = filterOddLengthWords(['there', 'it', 'is', 'now']);
console.log(output); // --> ['there', "now']
```

### !end-question

### !placeholder

```js
function filterOddLengthWords(words) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("filterOddLengthWords", function() {
  it("should return an array", function() {
    expect(Array.isArray(filterOddLengthWords(["there", "it", "is", "now"]))).to.deep.eq(true);
  });
  it("should return an array with odd lengthed words", function() {
    expect(filterOddLengthWords(["there", "it", "is", "now"])).to.deep.eq(["there", "now"]);
  });
  it("should return an empty array when passed an array with no odd lengthed words", function() {
    expect(filterOddLengthWords(["it", "cats"])).to.deep.eq([]);
  });
  it("should return an empty array when passed an empty array", function() {
    expect(filterOddLengthWords([])).to.deep.eq([]);
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
* id: 1beb59a5-644c-4508-922f-4d8b4910bf77
* title: filterEvenLengthWords

### !question

Write a function called "filterEvenLengthWords".

Given an array of strings, "filterEvenLengthWords" returns an array containing only the elements of the given array whose length is an even number.

```
var output = filterEvenLengthWords(['word', 'words', 'word', 'words']);
console.log(output); // --> ['word', 'word']
```

### !end-question

### !placeholder

```js
function filterEvenLengthWords(words) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("filterEvenLengthWords", function() {
  it("should return an array", function() {
    expect(Array.isArray(filterEvenLengthWords(["there", "it", "is", "now"]))).to.deep.eq(true);
  });
  it("should return an array with even lengthed words", function() {
    expect(filterEvenLengthWords(["there", "it", "is", "now"])).to.deep.eq(["it", "is"]);
  });
  it("should return an empty array when passed an array with no even lengthed words", function() {
    expect(filterEvenLengthWords(["there", "now"])).to.deep.eq([]);
  });
  it("should return an empty array when passed an empty array", function() {
    expect(filterEvenLengthWords([])).to.deep.eq([]);
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
* id: bed00f94-4f5c-4a82-8cfa-7eaf872368f5
* title: getLengthOfLongestElement

### !question

Write a function called "getLengthOfLongestElement".

Given an array, "getLengthOfLongestElement" returns the length of the longest string in the given array.

Notes:
* It should return 0 if the array is empty.

```
var output = getLengthOfLongestElement(['one', 'two', 'three']);
console.log(output); // --> 5
```

### !end-question

### !placeholder

```js
function getLengthOfLongestElement(arr) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("getLengthOfLongestElement", function() {
  it("should return a number", function() {
    expect(typeof getLengthOfLongestElement(["one", "two", "three"])).to.deep.eq("number");
  });
  it("should return the length of the longest element in an array", function() {
    expect(getLengthOfLongestElement(["one", "two", "three"])).to.deep.eq(5);
  });
  it("it should handle ties", function() {
    expect(getLengthOfLongestElement(["one", "two", "no"])).to.deep.eq(3);
  });
  it("it should return 0 when given an empty array", function() {
    expect(getLengthOfLongestElement([])).to.deep.eq(0);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
