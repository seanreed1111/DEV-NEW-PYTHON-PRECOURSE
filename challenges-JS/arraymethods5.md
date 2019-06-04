# Array Methods 5

### !challenge

* type: local-snippet
* language: javascript
* id: 241a37de-4069-418a-8f8d-64a40cc74f49
* title: removeFromBackOfNew

### !question

Write a function called "removeFromBackOfNew".

Given an array, "removeFromBackOfNew" returns a new array containing all but the last element of the given array.

Notes:
* You should be familiar with the 'slice' method.

```
var arr = [1, 2, 3];
var output = removeFromBackOfNew(arr);
console.log(output); // --> [1, 2]
console.log(arr); // --> [1, 2, 3]
```

### !end-question

### !placeholder

```js
function removeFromBackOfNew(arr) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("removeFromBackOfNew", function() {
  it("should return an array", function() {
    expect(Array.isArray(removeFromBackOfNew([1, 2], 3))).to.deep.eq(true);
  });
  it("should return an array with the last element of the passed in array removed", function() {
    expect(removeFromBackOfNew([1, 2])).to.deep.eq([1]);
  });
  it("should handle an empty array", function() {
    expect(removeFromBackOfNew([])).to.deep.eq([]);
  });
  it("should leave arr unmodified", function() {
    var originalArray = [1, 2];
    var newArray = removeFromBackOfNew(originalArray);
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
* id: 8a97c37b-54f3-4db0-845f-d2e7901e4244
* title: removeFromFrontOfNew

### !question

Write a function called "removeFromFrontOfNew".

Given an array, "removeFromFrontOfNew" returns a new array containing all but the first element of the given array.

Notes:
* You should be familiar with the 'slice' method.

```
var arr = [1, 2, 3];
var output = removeFromFrontOfNew(arr);
console.log(output); // --> [2, 3]
console.log(arr); // --> [1, 2, 3]
```

### !end-question

### !placeholder

```js
function removeFromFrontOfNew(arr) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("removeFromFrontOfNew", function() {
  it("should return an array", function() {
    expect(Array.isArray(removeFromFrontOfNew([1, 2]))).to.deep.eq(true);
  });
  it("should remove an element from the front of an array", function() {
    expect(removeFromFrontOfNew([1, 2])).to.deep.eq([2]);
  });
  it("should handle an empty array", function() {
    expect(removeFromFrontOfNew([])).to.deep.eq([]);
  });
  it("should leave arr unmodified", function() {
    var originalArray = [1, 2];
    var newArray = removeFromFrontOfNew(originalArray);
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
* id: a3d52d99-9784-457b-8201-1210a097d449
* title: countCharacter

### !question

Write a function called "countCharacter".

Given a string input and a character, "countCharacter" returns the number of occurences of a given character in the given string.

```
var output = countCharacter('I am a hacker', 'a');
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function countCharacter(str, char) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("countCharacter", function() {
  it("should return a number", function() {
    expect(typeof countCharacter("say what!?", "a")).to.deep.eq("number");
  });
  it("should return the number of occurences of a character in a string when the character exists", function() {
    expect(countCharacter("say what!?", "a")).to.deep.eq(2);
  });
  it("should return the number of occurences of a character in a string when the character does not exist", function() {
    expect(countCharacter("say what!?", "x")).to.deep.eq(0);
  });
  it("should return the number of occurences of a non-alphanumeric character in a string when the character exists", function() {
    expect(countCharacter("say what!?", " ")).to.deep.eq(1);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
