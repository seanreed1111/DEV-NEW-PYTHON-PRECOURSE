### !challenge

* type: local-snippet
* language: javascript
* id: 547a6787-3d47-4a09-83d6-ca86e7aa26c9
* title: isEvenAndGreaterThan10.md

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
