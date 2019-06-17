# Objects 5

### !challenge

* type: local-snippet
* language: javascript
* id: 5c68f405-579c-4427-8f13-9df8539009c7
* title: removeEvenValues

### !question

Write a function called "removeEvenValues".

Given an object, "removeEvenValues" removes any properties whose values are even numbers.

Do this in place and return the original object, do not construct a cloned object that omits the properties.

Example:

```
var obj = {
  a: 2,
  b: 3,
  c: 4
};
removeEvenValues(obj);
console.log(obj); // --> { b: 3 }
```

### !end-question

### !placeholder

```js
function removeEvenValues(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeEvenValues", function() {
  it("should remove any properties with values that are even numbers", function() {
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
    removeEvenValues(obj);
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
* id: 74b7a416-a4bc-4854-b870-0f92c6d57335
* title: countNumberOfKeys

### !question

Write a function called "countNumberOfKeys".

Given an object, "countNumberOfKeys" returns how many properties the given object has.

```
var obj = {
  a: 1,
  b: 2,
  c: 3
};
var output = countNumberOfKeys(obj);
console.log(output); // --> 3
```

### !end-question

### !placeholder

```js
function countNumberOfKeys(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("countNumberOfKeys", function() {
  it("should return a number", function() {
    var obj = {};
    expect(typeof(countNumberOfKeys(obj))).to.deep.eq("number");
  });
  it("should return the number of keys for an object", function() {
    var obj = {
      a: 1,
      b: 2,
      c: 3
    };
    expect(countNumberOfKeys(obj)).to.deep.eq(3);
  });
  it("should return 0 for an object with no keys", function() {
    var obj = {};
    expect(countNumberOfKeys(obj)).to.deep.eq(0);
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
* id: e01182d1-9906-49b8-830d-bae725ad5b4b
* title: removeOddValues

### !question

Write a function called "removeOddValues".

Given an object, "removeOddValues" removes any properties whose values are odd numbers.

```
var obj = {
  a: 2,
  b: 3,
  c: 4
};
removeOddValues(obj);
console.log(obj); // --> { a: 2, c: 4 }
```

### !end-question

### !placeholder

```js
function removeOddValues(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("removeOddValues", function() {
  it("should remove any properties with values that are odd numbers", function() {
    var obj = {
      a: 1,
      b: 2,
      c: 3,
      d: 4
    };
    var result = {
      b: 2,
      d: 4
    };
    removeOddValues(obj);
    expect(obj).to.deep.eq(result);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
