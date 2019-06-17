# Objects 8

### !challenge

* type: local-snippet
* language: javascript
* id: 4c450aa6-15da-4604-9aa9-b1f65d98850b
* title: getElementsGreaterThan10AtProperty

### !question

Write a function called "getElementsGreaterThan10AtProperty".

Given an object and a key, "getElementsGreaterThan10AtProperty" returns an array containing the elements within the array, located at the given key, that are greater than 10.

Notes:
* If the array is empty, it should return an empty array.
* If the array contains no elements greater than 10, it should return an empty array.
* If the property at the given key is not an array, it should return an empty array.
* If there is no property at the key, it should return an empty array.

```
var obj = {
  key: [1, 20, 30]
};
var output = getElementsGreaterThan10AtProperty(obj, 'key');
console.log(output); // --> [20, 30]
```

### !end-question

### !placeholder

```js
function getElementsGreaterThan10AtProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getElementsGreaterThan10AtProperty", function() {
  it("should return an array containing all the elements greater than 10 in the array located at key", function() {
    var obj = {
      array: [10, 20, 40]
    };
    expect(getElementsGreaterThan10AtProperty(obj, "array")).to.deep.eq([20, 40]);
  });
  it("should return an empty array if the array has no elements greater than 10", function() {
    var obj = {
      array: [1, 3]
    };
    expect(getElementsGreaterThan10AtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getElementsGreaterThan10AtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getElementsGreaterThan10AtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getElementsGreaterThan10AtProperty(obj, "array")).to.deep.eq([]);
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
* id: aa75a574-cc22-47c9-9464-6d9cf0a3b7de
* title: getFirstElementOfProperty

### !question

Write a function called "getFirstElementOfProperty".

Given an object and a key, "getFirstElementOfProperty" returns the first element of the array located at the given key.

Notes:
* If the array is empty, it should return undefined.
* If the property at the given key is not an array, it should return undefined.
* If there is no property at the key, it should return undefined.

```
var obj = {
  key: [1, 2, 4]
};
var output = getFirstElementOfProperty(obj, 'key');
console.log(output); // --> 1
```

### !end-question

### !placeholder

```js
function getFirstElementOfProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getFirstElementOfProperty", function() {
  it("should return the first element of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getFirstElementOfProperty(obj, "array")).to.deep.eq(1);
  });
  it("should return undefined if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getFirstElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getFirstElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getFirstElementOfProperty(obj, "array")).to.deep.eq(undefined);
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
* id: 30a364d6-98d8-4819-a1b6-67cbc47e85de
* title: getNthElementOfProperty

### !question

Write a function called "getNthElementOfProperty".

Given an object and a key, "getNthElementOfProperty" returns the nth element of an array located at the given key.

Notes:
* If the array is empty, it should return undefined.
* If n is out of range, it should return undefined.
* If the property at the given key is not an array, it should return undefined.
* If there is no property at the key, it should return undefined.

```
var obj = {
  key: [1, 2, 6]
};
var output = getNthElementOfProperty(obj, 'key', 1);
console.log(output); // --> 2
```

### !end-question

### !placeholder

```js
function getNthElementOfProperty(obj, key, n) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getNthElementOfProperty", function() {
  it("should return the nth element of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getNthElementOfProperty(obj, "array", 2)).to.deep.eq(4);
  });
  it("should return undefined if the n is out of range", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getNthElementOfProperty(obj, "array", 8)).to.deep.eq(undefined);
  });
  it("should return undefined if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getNthElementOfProperty(obj, "array", 8)).to.deep.eq(undefined);
  });
  it("should return undefined if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getNthElementOfProperty(obj, "array", 8)).to.deep.eq(undefined);
  });
  it("should return undefined if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getNthElementOfProperty(obj, "array", 8)).to.deep.eq(undefined);
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
* id: 0128dc86-b7a6-4022-8aa6-178ac9dd020b
* title: getLastElementOfProperty

### !question

Write a function called "getLastElementOfProperty".

Given an object and a key, "getLastElementOfProperty" returns the last element of an array located at the given key.

Notes:
* If the array is empty, it should return undefined.
* if the property at the given key is not an array, it should return undefined.
* If there is no property at the key, it should return undefined.

```
var obj = {
  key: [1, 2, 5]
};
var output = getLastElementOfProperty(obj, 'key');
console.log(output); // --> 5
```

### !end-question

### !placeholder

```js
function getLastElementOfProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getLastElementOfProperty", function() {
  it("should return the last element of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getLastElementOfProperty(obj, "array")).to.deep.eq(4);
  });
  it("should return undefined if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getLastElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getLastElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getLastElementOfProperty(obj, "array")).to.deep.eq(undefined);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
