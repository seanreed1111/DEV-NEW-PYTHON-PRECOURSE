### !challenge

* type: local-snippet
* language: javascript
* id: d502830a-6d86-479d-9bd3-664e13d2a686
* title: isSameLength.md

### !question

Write a function called "isSameLength".

Given two words, "isSameLength" returns whether the given words have the same length.

```
var output = isSameLength('words', 'super');
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isSameLength(word1, word2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isSameLength", function() {
  it("should return a boolean", function() {
    expect(typeof isSameLength("hi", "there")).to.deep.eq("boolean");
  });
  it("should return true if the two words are the same length", function() {
    expect(isSameLength("yes", "you")).to.deep.eq(true);
  });
  it("should return false if the two words are not the same length", function() {
    expect(isSameLength("hi", "there")).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
