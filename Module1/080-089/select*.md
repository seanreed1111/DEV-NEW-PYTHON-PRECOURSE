### !challenge

* type: local-snippet
* language: javascript
* id: e7a0d366-b299-4c2a-81ac-45fcbacd2b54
* title: select*.md

### !question

Write a function called "select".

Given an array and an object, "select" returns a new object whose properties are those in the given object AND whose keys are present in the given array.

Notes:
* If keys are present in the given array, but are not in the given object, it should ignore them.
* It does not modify the passed in object.

```
var arr = ['a', 'c', 'e'];
var obj = {
  a: 1,
  b: 2,
  c: 3,
  d: 4
};
var output = select(arr, obj);
console.log(output); // --> { a: 1, c: 3 }
```

### !end-question

### !placeholder

```js
function select(arr, obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("select", function() {
  it("should return an object", function() {
    var keys = ["a", "c", "e"];
    var obj = {
      a: 1,
      b: 2,
      c: 3,
      d: 4
    };
    expect(typeof select(keys, obj)).to.deep.eq("object");
  });
  it("should return an object with properties in from the passed in object whose keys are present in the given function", function() {
    var keys = ["a", "c", "e"];
    var obj = {
      a: 1,
      b: 2,
      c: 3,
      d: 4
    };
    var result = {
      a: 1,
      c: 3
    };
    expect(select(keys, obj)).to.deep.eq(result);
  });
  it("should not modify the passed in object", function() {
    var keys = ["a", "c", "e"];
    var obj = {
      a: 1,
      b: 2,
      c: 3,
      d: 4
    };
    select(keys, obj)
    expect(Object.keys(obj).length).to.deep.eq(4);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
