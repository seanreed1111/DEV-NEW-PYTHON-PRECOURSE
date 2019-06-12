### !challenge

* type: local-snippet
* language: javascript
* id: 10993279-1166-4e9d-813b-aff9705fab7b
* title: getOddElementsAtProperty*.md

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
