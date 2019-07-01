# Objects 6

### !challenge

* type: local-snippet
* language: javascript
* id: 0fa027aa-cf1a-4b02-a19e-5d43a6c83a32
* title: removeArrayValues

### !question

Write a function called "removeArrayValues".

Given an object, "removeArrayValues" removes any properties whose values are arrays.

```
var obj = {
  a: [1, 3, 4],
  b: 2,
  c: ['hi', 'there']
}
removeArrayValues(obj);
console.log(obj); // --> { b: 2 }
```

### !end-question

### !placeholder

```js
function removeArrayValues(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeArrayValues", function() {
  it("should remove any properties with values that are arrays", function() {
    var obj = {
      a: [true, false],
      b: 2,
      c: [8, 0],
      d: 4
    };
    var result = {
      b: 2,
      d: 4
    };
    removeArrayValues(obj);
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
* id: 717ab908-571e-4a56-a675-ec540640c6ea
* title: removeNumberValues

### !question

Write a function called "removeNumberValues".

Given an object, "removeNumberValues" removes any properties whose values are numbers.

```
var obj = {
  a: 2,
  b: 'remaining',
  c: 4
};
removeNumberValues(obj);
console.log(obj); // --> { b: 'remaining' }
```

### !end-question

### !placeholder

```js
function removeNumberValues(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js


describe("removeNumberValues", function() {
  it("should remove any properties with values that are numbers", function() {
    var obj = {
      a: [true, false],
      b: 2,
      c: [8, 0],
      d: 4
    };
    var result = {
      a: [true, false],
      c: [8, 0]
    };
    removeNumberValues(obj);
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
* id: 8fa998a8-1847-4de4-aada-7c319bf55354
* title: removeStringValues

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
