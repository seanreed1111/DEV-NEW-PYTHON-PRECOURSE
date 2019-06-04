# Conditionals 5

### !challenge

* type: local-snippet
* language: javascript
* id: 9a167567-dfa8-4854-a21c-3d773b0c1ef5
* title: isOddLength

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

### !challenge

* type: local-snippet
* language: javascript
* id: 3e56d53e-7025-45e4-a697-fd2851b6495d
* title: isEvenLength

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

### !challenge

* type: local-snippet
* language: javascript
* id: 547a6787-3d47-4a09-83d6-ca86e7aa26c9
* title: isEvenAndGreaterThan10

### !question

Write a function called "isEvenAndGreaterThanTen".

Given a number, "isEvenAndGreaterThanTen" returns whether it is both even and greater than 10.

```
var output = isEvenAndGreaterThanTen(13);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isEvenAndGreaterThanTen(num) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("isEvenAndGreaterThanTen", function() {
  it("should return a boolean", function() {
    expect(typeof isEvenAndGreaterThanTen(40)).to.deep.eq("boolean");
  });
  it("should return true if the number is even and greater than 10", function() {
    expect(isEvenAndGreaterThanTen(80)).to.deep.eq(true);
  });
  it("should return false if the number is odd", function() {
    expect(isEvenAndGreaterThanTen(91)).to.deep.eq(false);
  });
  it("should return false if the number is less than 10", function() {
    expect(isEvenAndGreaterThanTen(8)).to.deep.eq(false);
  });
  it("should return false if the number is 10", function() {
    expect(isEvenAndGreaterThanTen(10)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
