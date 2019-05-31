### !challenge

* type: local-snippet
* language: javascript
* id: 1d51ed19-4978-4574-bb07-9b65921ed07e
* title: square.md

### !question

Write a function called "square".

Given a number, "square" should return the square of the given number.

```
var output = square(5);
console.log(output); // --> 25
```

### !end-question

### !placeholder

```js
function square(num) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("square", function() {
  it("should_square_a_positive_number", function() {
    expect(square(2)).to.deep.eq(4);
  });

  it("should_square_0", function() {
    expect(square(0)).to.deep.eq(0);
  });

  it("should_square_a_number_greater_than_10", function() {
    expect(square(12)).to.deep.eq(144);
  });

  it("should_square_a_negative_number", function() {
    expect(square(-5)).to.deep.eq(25);
  });
})

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
