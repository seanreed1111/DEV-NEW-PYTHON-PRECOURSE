# Conditionals 7

### !challenge

* type: local-snippet
* language: javascript
* id: b99bc1a5-bc3a-42c5-9372-745bcbea92a7
* title: areValidCredentials

### !question

Write a function called "areValidCredentials".

Given a name and a password, "areValidCredentials", returns true if the name is longer than 3 characters, AND, the password is at least 8 characters long. Otherwise it returns false.

```
var output = areValidCredentials('Ritu', 'mylongpassword')
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function areValidCredentials(name, password) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("areValidCredentials", function() {
  it("should return a boolean", function() {
    expect(typeof areValidCredentials("Ritu", "mylongpassword")).to.deep.eq("boolean");
  });
  it("should return true if the name is longer than 3 characters and the password is at least 8 characters", function() {
    expect(areValidCredentials("Ritu", "mylongpassword")).to.deep.eq(true);
  });
  it("should return false if the name is less than 3 characters", function() {
    expect(areValidCredentials("me", "mylongpassword")).to.deep.eq(false);
  });
  it("should return false if the password is not at least 8 characters", function() {
    expect(areValidCredentials("Someone", "1234567")).to.deep.eq(false);
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
* id: 705f1f9a-9afa-4ae7-be40-ddebbb95204b
* title: findMinLengthOfThreeWords

### !question

Write a function called "findMinLengthOfThreeWords".

Given 3 words, "findMinLengthOfThreeWords" returns the length of the shortest word.

```
var output = findMinLengthOfThreeWords('a', 'be', 'see');
console.log(output); // --> 1
```

### !end-question

### !placeholder

```js
function findMinLengthOfThreeWords(word1, word2, word3) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("findMinLengthOfThreeWords", function() {
  it("should return a number", function() {
    expect(typeof findMinLengthOfThreeWords("a", "be", "see")).to.deep.eq("number");
  });
  it("should return the minimimum length of three words", function() {
    expect(findMinLengthOfThreeWords("a", "be", "see")).to.deep.eq(1);
  });
  it("should return the minimimum length of three words when there is a tie", function() {
    expect(findMinLengthOfThreeWords("these", "three", "words")).to.deep.eq(5);
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
* id: c3fcc0c8-628e-40aa-992a-a85008a3d60d
* title: findMaxLengthOfThreeWords

### !question

Write a function called "findMaxLengthOfThreeWords".

Given 3 words, "findMaxLengthOfThreeWords" returns the length of the longest word.

```
var output = findMaxLengthOfThreeWords('a', 'be', 'see');
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function findMaxLengthOfThreeWords(word1, word2, word3) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("findMaxLengthOfThreeWords", function() {
  it("should return a number", function() {
    expect(typeof findMaxLengthOfThreeWords("a", "be", "see")).to.deep.eq("number");
  });
  it("should return the maximimum length of three words", function() {
    expect(findMaxLengthOfThreeWords("a", "be", "see")).to.deep.eq(3);
  });
  it("should return the maximimum length of three words when there is a tie", function() {
    expect(findMaxLengthOfThreeWords("these", "three", "words")).to.deep.eq(5);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
