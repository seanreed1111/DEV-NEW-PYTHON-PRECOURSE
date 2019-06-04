### !challenge

* type: local-snippet
* language: javascript
* id: 0e621f19-ceb1-4565-8f07-e78a7b8a3adb
* title: sumDigits*.md

### !question

Write a function called "sumDigits".

Given a number, "sumDigits" returns the sum of all its digits.

```
var output = sumDigits(1148);
console.log(output); // --> 14
```

If the number is negative, the first digit should count as negative.

```
var output = sumDigits(-316);
console.log(output); // --> 4
```

Notes:
* In order to use some of the methods that will be most helpful to you, you will most likely want to do some string to number conversion and vice versa.
* Be sure to familiarize yourself with the "toString" method, as well as the "Number" function.

### !end-question

### !placeholder

```js
function sumDigits(num) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("sumDigits", function() {
  it("should return a number", function() {
    expect(typeof sumDigits(2002)).to.deep.eq("number");
  });
  it("should sum the digits of a positive number", function() {
    expect(sumDigits(2002)).to.deep.eq(4);
  });
  it("should sum the digits of a negative number", function() {
    expect(sumDigits(-2004)).to.deep.eq(2);
  });
  it("should sum return 0 if the number is 0", function() {
    expect(sumDigits(0)).to.deep.eq(0);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
