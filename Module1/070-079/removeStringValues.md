### !challenge

* type: local-snippet
* language: javascript
* id: 8fa998a8-1847-4de4-aada-7c319bf55354
* title: removeStringValues.md

### !question

Write a function called "removeStringValues".

Given an object, "removeStringValues" removes any properties on the given object whose values are strings.

```
var obj = {
  name: 'Sam',
  age: 20
}
removeStringValues(obj);
console.log(obj); // { age: 20 }
```

### !end-question

### !placeholder

```js
function removeStringValues(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeStringValues", function() {
  it("should remove any properties with values that are strings", function() {
    var obj = {
      a: "hello",
      b: 2,
      c: "montana",
      d: 4
    };
    var result = {
      b: 2,
      d: 4
    };
    removeStringValues(obj);
    expect(obj).to.deep.eq(result);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
