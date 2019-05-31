### !challenge

* type: local-snippet
* language: javascript
* id: e5a953a0-42f3-414c-bd77-c4247d272f7a
* title: doubleSquareRootOf.md

### !question

Write a function called "doubleSquareRootOf".
Given a number, "doubleSquareRootOf" returns double its square root.

```
var output = doubleSquareRootOf(121);
console.log(output); // --> 22
```

### !end-question

### !placeholder

```js
function doubleSquareRootOf(num) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("doubleSquareRootOf", function() {
  it("should return a number", function() {
    expect(typeof doubleSquareRootOf(9)).to.deep.eq("number");
  });
  it("should return the doubled square root of the passed in number", function() {
    expect(doubleSquareRootOf(9)).to.deep.eq(6);
  });
})

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
