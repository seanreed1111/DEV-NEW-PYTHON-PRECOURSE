### !challenge

* type: local-snippet
* language: javascript
* id: eb2ace99-f027-4845-9d09-529ef85273ca
* title: getAllButLastElementOfProperty.md

### !question

Write a function called "getAllButLastElementOfProperty".

Given an object and a key, "getAllButLastElementOfProperty" returns an array containing all but the last element of the array located at the given key.

Notes:
* If the array is empty, it should return an empty array.
* If the property at the given key is not an array, it return an empty array.
* If there is no property at the key, it should return an empty array.

```
var obj = {
  key: [1, 2, 3]
};
var output = getAllButLastElementOfProperty(obj, 'key');
console.log(output); // --> [1,2]
```

### !end-question

### !placeholder

```js
function getAllButLastElementOfProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getAllButLastElementOfProperty", function() {
  it("should return an array containing all but the last element of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getAllButLastElementOfProperty(obj, "array")).to.deep.eq([1, 2]);
  });
  it("should return an empty array if the array has only 1 element", function() {
    var obj = {
      array: [1]
    };
    expect(getAllButLastElementOfProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getAllButLastElementOfProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getAllButLastElementOfProperty(obj, "array")).to.deep.eq([]);
  });
  it("should return an empty array if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getAllButLastElementOfProperty(obj, "array")).to.deep.eq([]);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
