### !challenge

* type: local-snippet
* language: javascript
* id: 3e56d53e-7025-45e4-a697-fd2851b6495d
* title: isEvenLength.md

### !question

Write a function called "isEvenLength".

Given a word, "isEvenLength" returns whether the length of the word is even.

```
var output = isEvenLength('wow');
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isEvenLength(word) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isEvenLength", function() {
  it("should return a boolean", function() {
    expect(typeof isEvenLength("wow")).to.deep.eq("boolean");
  });
  it("should return if the length of the word is even", function() {
    expect(isEvenLength("specials")).to.deep.eq(true);
  });
  it("should return true if the string is empty", function() {
    expect(isEvenLength("")).to.deep.eq(true);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
