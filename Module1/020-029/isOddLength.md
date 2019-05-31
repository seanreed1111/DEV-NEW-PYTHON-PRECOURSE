### !challenge

* type: local-snippet
* language: javascript
* id: 9a167567-dfa8-4854-a21c-3d773b0c1ef5
* title: isOddLength.md

### !question

Write a function called "isOddLength".

Given a word, "isOddLength" returns whether the length of the given word is odd.

```
var output = isOddLength('special');
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isOddLength(word) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("isOddLength", function() {
  it("should return a boolean", function() {
    expect(typeof isOddLength("wow")).to.deep.eq("boolean");
  });
  it("should return if the length of the word is even", function() {
    expect(isOddLength("special")).to.deep.eq(true);
  });
  it("should return false if the string is empty", function() {
    expect(isOddLength("")).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
