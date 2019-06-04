# Objects 4

### !challenge

* type: local-snippet
* language: javascript
* id: 09b2c4c3-d899-49fa-a943-60a03de413c2
* title: removeNumbersLargerThan

### !question

Write a function called "removeNumbersLargerThan".

Given a number and an object, "removeNumbersLargerThan" removes any properties whose values are numbers greater than the given number.

```
var obj = {
  a: 8,
  b: 2,
  c: 'montana'
}
removeNumbersLargerThan(5, obj);
console.log(obj); // --> { b: 2, c: 'montana' }
```

### !end-question

### !placeholder

```js
function removeNumbersLargerThan(num, obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeNumbersLargerThan", function() {
  it("should remove any properties with values that are numbers greater than num", function() {
    var obj = {
      a: "hello",
      b: 2,
      c: "montana",
      d: 4
    };
    var result = {
      a: "hello",
      b: 2,
      c: "montana"
    };
    removeNumbersLargerThan(3, obj);
    expect(obj).to.deep.eq(result);
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
* id: ee54e130-d037-4ff7-9c59-5461322523e1
* title: removeNumbersLessThan

### !question

Write a function called "removeNumbersLessThan".

Given a number and an object, "removeNumbersLessThan" removes any properties whose values are numbers less than the given number.

```
var obj = {
  a: 8,
  b: 2,
  c: 'montana'
}
removeNumbersLessThan(5, obj);
console.log(obj); // --> { a: 8, c: 'montana' }
```

### !end-question

### !placeholder

```js
function removeNumbersLessThan(num, obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeNumbersLessThan", function() {
  it("should remove any properties with values that are numbers less than num", function() {
    var obj = {
      a: "hello",
      b: 2,
      c: "montana",
      d: 4
    };
    var result = {
      a: "hello",
      c: "montana",
      d: 4
    };
    removeNumbersLessThan(3, obj);
    expect(obj).to.deep.eq(result);
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
* id: 47b07382-07c8-41b1-98e0-dae82ed992da
* title: removeStringValuesLongerThan

### !question

Write a function called "removeStringValuesLongerThan".

Given an number and an object, "removeStringValuesLongerThan" removes any properties on the given object whose values are strings longer than the given number.

```
var obj = {
  name: 'Montana',
  age: 20,
  location: 'Texas'
};
removeStringValuesLongerThan(6, obj);
console.log(obj); // { age: 20, location: 'Texas' }
```

### !end-question

### !placeholder

```js
function removeStringValuesLongerThan(num, obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeStringValuesLongerThan", function() {
  it("should remove any properties with values that are strings longer than num", function() {
    var obj = {
      a: "hello",
      b: 2,
      c: "montana",
      d: 4
    };
    var result = {
      a: "hello",
      b: 2,
      d: 4
    };
    removeStringValuesLongerThan(5, obj);
    expect(obj).to.deep.eq(result);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
