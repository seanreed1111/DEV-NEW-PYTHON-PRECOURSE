# Math 1

### !challenge

* type: local-snippet
* language: javascript
* id: 6a2a074c-7652-488e-b51c-0a441fa0fae9
* title: average

### !question

Write a function called "average".

Given two numbers, "average" returns their average.

```
var output = average(4, 6);
console.log(output); // --> 5
```

### !end-question

### !placeholder

```js
function average(num1, num2) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("average", function() {
  it("should return a number", function() {
    expect(typeof average(1, 12)).to.deep.eq("number");
  });
  it("should return the average of two numbers", function() {
    expect(average(2, 4)).to.deep.eq(3);
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
* id: bb88d243-fda0-4b49-ba45-f4a19ead5d03
* title: computeAreaOfATriangle

### !question

Write a function called "computeAreaOfATriangle".

Given the base and height of a triangle, "computeAreaOfATriangle" returns its area.

```
var output = computeAreaOfATriangle(4, 6);
console.log(output); // --> 12
```

### !end-question

### !placeholder

```js
function computeAreaOfATriangle(base, height) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("computeAreaOfATriangle", function() {
  it("should return a number", function() {
    expect(typeof computeAreaOfATriangle(6, 4)).to.deep.eq("number");
  });
  it("should return the area of a triangle", function() {
    expect(computeAreaOfATriangle(6, 4)).to.deep.eq(12);
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
* id: 327a2860-4858-4627-9632-f451e415e7d4
* title: cube

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

### !challenge

* type: local-snippet
* language: javascript
* id: 1d51ed19-4978-4574-bb07-9b65921ed07e
* title: square

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
