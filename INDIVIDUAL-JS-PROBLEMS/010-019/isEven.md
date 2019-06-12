### !challenge

* type: local-snippet
* language: javascript
* id: 32135330-a5c2-49cd-b9a4-cffe41db64b3
* title: isEven.md

### !question

Write a function called "isEven".
Given a number, "isEven" returns whether it is even.

```
var output = isEven(11);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isEven(num) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isEven", function() {
  it("should return a boolean", function() {
    expect(typeof isEven(40)).to.deep.eq("boolean");
  });
  it("should return if the number is even", function() {
    expect(isEven(8)).to.deep.eq(true);
  });
  it("should return true if the number is 0", function() {
    expect(isEven(0)).to.deep.eq(true);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
