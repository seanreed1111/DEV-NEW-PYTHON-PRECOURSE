# Objects 10

### !challenge

* type: local-snippet
* language: javascript
* id: 89965766-9afc-4a39-a053-974ea791eed3
* title: getSquaredElementsAtProperty

### !question

Write a function called "getSquaredElementsAtProperty".

Given an object and a key, "getSquaredElementsAtProperty" returns an array containing all the squared elements of the array located at the given key.

Notes:
* If the array is empty, it should return an empty array.
* If the property at the given key is not an array, it should return an empty array.
* If there is no property at the key, it should return an empty array.

```
var obj = {
  key: [2, 1, 5]
};
var output = getSquaredElementsAtProperty(obj, 'key');
console.log(output); // --> [4, 1, 25]
```

### !end-question

### !placeholder

```js
function getSquaredElementsAtProperty(obj, key) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("getSquaredElementsAtProperty", function() {
  it("should return an array containing all the squared elements of the array located at key", function() {
    var obj = {
      array: [1, 2, 7]
    };
    expect(getSquaredElementsAtProperty(obj, "array")).to.deep.eq([1, 4, 49]);
  });
  it("should return an empty array if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getSquaredElementsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getSquaredElementsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getSquaredElementsAtProperty(obj, "array")).to.deep.eq([]);
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
* id: 10993279-1166-4e9d-813b-aff9705fab7b
* title: getOddElementsAtProperty

### !question

Write a function called "getOddElementsAtProperty".

Given an object and a key, "getOddElementsAtProperty" returns an array containing all the odd elements of the array located at the given key.

Notes:
* If the array is empty, it should return an empty array.
* If it contains no odd elements, it should return an empty array.
* If the property at the given key is not an array, it should return an empty array.
* If there is no property at the key, it should return an empty array.

```
var obj = {
  key: [1, 2, 3, 4, 5]
};
var output = getOddElementsAtProperty(obj, 'key');
console.log(output); // --> [1, 3, 5]
```

### !end-question

### !placeholder

```js
function getOddElementsAtProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getOddElementsAtProperty", function() {
  it("should return an array containing all the odd elements of the array located at key", function() {
    var obj = {
      array: [1, 2, 7]
    };
    expect(getOddElementsAtProperty(obj, "array")).to.deep.eq([1, 7]);
  });
  it("should return an empty array if the array has only no odd elements", function() {
    var obj = {
      array: [2, 30]
    };
    expect(getOddElementsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getOddElementsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getOddElementsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getOddElementsAtProperty(obj, "array")).to.deep.eq([]);
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
* id: f55d3c6d-ea58-477c-9682-4573e7f48e75
* title: getEvenElementsAtProperty

### !question

Write a function called "getEvenElementsAtProperty".

Given an object and a key, "getEvenElementsAtProperty" returns an array containing all the even elements of the array located at the given key.

Notes:
* If the array is empty, it should return an empty array.
* If the array contains no even elements, it should return an empty array.
* If the property at the given key is not an array, it should return an empty array.
* If there is no property at the given key, it should return an empty array.

```
var obj = {
  key: [1000, 11, 50, 17]
};
var output = getEvenElementsAtProperty(obj, 'key');
console.log(output); // --> [1000, 50]
```

### !end-question

### !placeholder

```js
function getEvenElementsAtProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getEvenElementsAtProperty", function() {
  it("should return an array containing all the even elements of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getEvenElementsAtProperty(obj, "array")).to.deep.eq([2, 4]);
  });
  it("should return an empty array if the array has only no even elements", function() {
    var obj = {
      array: [1, 3]
    };
    expect(getEvenElementsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getEvenElementsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getEvenElementsAtProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getEvenElementsAtProperty(obj, "array")).to.deep.eq([]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
