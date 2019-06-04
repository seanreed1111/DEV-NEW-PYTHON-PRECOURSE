# Advanced 2

### !challenge

* type: local-snippet
* language: javascript
* id: 036e5563-3791-46d3-8d67-780c769396fb
* title: extend

### !question

Write a function called "extend".

Given two objects, "extend" adds properties from the 2nd object to the 1st object.

Notes:
* Add any keys that are not in the 1st object.
* If the 1st object already has a given key, ignore it (do not overwrite the property value).
* Do not modify the 2nd object at all.

```
var obj1 = {
  a: 1,
  b: 2
};
var obj2 = {
  b: 4,
  c: 3
};

extend(obj1, obj2);

console.log(obj1); // --> {a: 1, b: 2, c: 3}
console.log(obj2); // --> {b: 4, c: 3}
```

### !end-question

### !placeholder

```js
function extend(obj1, obj2) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("extend", function() {
  it("should extend the first object with unrepresented properties from the second object", function() {
    var obj1 = {
      a: 1,
      b: 2
    };
    var obj2 = {
      b: 4,
      c: 3
    };
    var result = {
      a: 1,
      b: 2,
      c: 3
    };

    extend(obj1, obj2);
    expect(obj1).to.deep.eq(result);
  });
  it("should extend the first object with unrepresented properties from the second object", function() {
    var obj1 = {
      a: 1,
      b: 2
    };
    var obj2 = {
      b: 4,
      c: 3
    };

    extend(obj1, obj2);
    expect(obj2).to.deep.eq({b: 4, c: 3});
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
