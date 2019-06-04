### !challenge

* type: local-snippet
* language: javascript
* id: f55d3c6d-ea58-477c-9682-4573e7f48e75
* title: getEvenElementsAtProperty*.md

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
