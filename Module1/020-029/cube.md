### !challenge

* type: local-snippet
* language: javascript
* id: 327a2860-4858-4627-9632-f451e415e7d4
* title: cube.md

### !question

Write a function called "cube".

Given a number, "cube" returns the cube of that number.

```
var output = cube(3);
console.log(output); // --> 27
```

### !end-question

### !placeholder

```js
function cube(num) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("cube", function() {
  it("should_cube_a_positive_number", function() {
    expect(cube(2)).to.deep.eq(8);
  });

  it("should_cube_0", function() {
    expect(cube(0)).to.deep.eq(0);
  });

  it("should_cube_a_number_greater_than_10", function() {
    expect(cube(12)).to.deep.eq(1728);
  });

  it("should_cube_a_negative_number", function() {
    expect(cube(-5)).to.deep.eq(-125);
  });
})

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
