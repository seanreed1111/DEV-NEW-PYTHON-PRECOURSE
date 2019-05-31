### !challenge

* type: local-snippet
* language: javascript
* id: 1fa21321-c02b-43c3-b6b9-0bf633486f6f
* title: equalsTen.md

### !question

Write a function called "equalsTen".
Given a number, "equalsTen" returns whether or not the given number is 10.

```
var output = equalsTen(9);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function equalsTen(num) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("equalsTen", function() {
  it("should return a boolean", function() {
    expect(typeof equalsTen(10)).to.deep.eq("boolean");
  });
  it("should return true for the number 10", function() {
    expect(equalsTen(10)).to.deep.eq(true);
  });
  it("should return false for a number greater than 10", function() {
    expect(equalsTen(400)).to.deep.eq(false);
  });
  it("should return false for the number 10", function() {
    expect(equalsTen(3)).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
