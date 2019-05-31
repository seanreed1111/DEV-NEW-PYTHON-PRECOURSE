### !challenge

* type: local-snippet
* language: javascript
* id: eae34f47-83d0-42c2-8ebc-9b72ae0482c3
* title: getAverageOfElementsAtProperty*.md

### !question

Write a function called "getAverageOfElementsAtProperty".

Given an object and a key, "getAverageOfElementsAtProperty" returns the average of all the elements in the array located at the given key.

Notes:
* If the array at the given key is empty, it should return 0.
* If the property at the given key is not an array, it should return 0.
* If there is no property at the given key, it should return 0.

```
var obj = {
  key: [1, 2, 3]
};
var output = getAverageOfElementsAtProperty(obj, 'key');
console.log(output); // --> 2
```

### !end-question

### !placeholder

```js
function getAverageOfElementsAtProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getAverageOfElementsAtProperty", function() {
  it("should return the average of all the elements of the array located at key", function() {
    var obj = {
      array: [1, 3, 5]
    };
    expect(getAverageOfElementsAtProperty(obj, "array")).to.deep.eq(3);
  });
  it("should return 0 if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getAverageOfElementsAtProperty(obj, "array")).to.deep.eq(0);
  });
  it("should return 0 if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getAverageOfElementsAtProperty(obj, "array")).to.deep.eq(0);
  });
  it("should return 0 if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getAverageOfElementsAtProperty(obj, "array")).to.deep.eq(0);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
