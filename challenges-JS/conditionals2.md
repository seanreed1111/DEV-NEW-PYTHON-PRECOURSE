# Conditionals 2

### !challenge

* type: local-snippet
* language: javascript
* id: 3a5dfe0d-e0ea-49b3-a9b1-d7e973f03133
* title: checkAge

### !question

Write a function called "checkAge".
Given a person's name and age, "checkAge" returns one of two messages:
"Go home, {insert_name_here}!", if they are younger than 21.
"Welcome, {insert_name_here}!", if they are 21 or older.
Naturally, replace "{insert_name_here}" with the given name. :)

```
var output = checkAge('Adrian', 22);
console.log(output); // --> 'Welcome, Adrian!'
```

### !end-question

### !placeholder

```js
function checkAge(name, age) {
  // your code here
  
}

```

### !end-placeholder

### !tests

```js

describe("checkAge", function() {
  it("should return a string", function() {
    expect(typeof(checkAge("Dan", "24"))).to.deep.eq("string");
  });
  it("should welcome someone over 21", function() {
    expect(checkAge("Dan", "24")).to.deep.eq("Welcome, Dan!");
  });
  it("should welcome a 21 year old", function() {
    expect(checkAge("Toni", "21")).to.deep.eq("Welcome, Toni!");
  });
  it("should bounce someone under 21", function() {
    expect(checkAge("Rad", "4")).to.deep.eq("Go home, Rad!");
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
* id: 9f1f81f6-8067-40a8-82ce-c9de9c13bcae
* title: isGreaterThanTen

### !question

Write a function called "isGreaterThan10".
Given a number, "isGreaterThan10" returns whether the given number is greater than 10.

```
var output = isGreaterThan10(11);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isGreaterThan10(num) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("isGreaterThan10", function() {
  it("should return a boolean", function() {
    expect(typeof isGreaterThan10(40)).to.deep.eq("boolean");
  });
  it("should return false for a number less than 10", function() {
    expect(isGreaterThan10(4)).to.deep.eq(false);
  });
  it("should return true for a number greater than 10", function() {
    expect(isGreaterThan10(40)).to.deep.eq(true);
  });
  it("should return false for the number 10", function() {
    expect(isGreaterThan10(10)).to.deep.eq(false);
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
* id: 49586ccf-27da-4265-abb8-7ba92a2202cc
* title: isLessThan30

### !question

Write a function called "isLessThan30".
Given a number, "isLessThan30" returns whether the given number is less than 30.

```
var output = isLessThan30(9);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isLessThan30(num) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("isLessThan30", function() {
  it("should return a boolean", function() {
    expect(typeof isLessThan30(40)).to.deep.eq("boolean");
  });
  it("should return true for a number less than 30", function() {
    expect(isLessThan30(4)).to.deep.eq(true);
  });
  it("should return false for a number greater than 30", function() {
    expect(isLessThan30(400)).to.deep.eq(false);
  });
  it("should return false for the number 30", function() {
    expect(isLessThan30(30)).to.deep.eq(false);
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
* id: 1fa21321-c02b-43c3-b6b9-0bf633486f6f
* title: equalsTen

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
