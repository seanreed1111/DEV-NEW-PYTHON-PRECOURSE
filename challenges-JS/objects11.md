# Objects 11

### !challenge

* type: local-snippet
* language: javascript
* id: c0da71bc-093b-4eae-a574-d31aa2cb1109
* title: getSmallestElementAtProperty

### !question

Write a function called "getSmallestElementAtProperty".

Given an object and a key, "getSmallestElementAtProperty" returns the smallest element in the array located at the given key.

Notes:
* If the array is empty, it should return undefined.
* If the property at the given key is not an array, it should return undefined.
* If there is no property at the key, it should return undefined.

```
var obj = {
  key: [2, 1, 5]
};
var output = getSmallestElementAtProperty(obj, 'key');
console.log(output); // --> 1
```

### !end-question

### !placeholder

```js

function getSmallestElementAtProperty(obj, key) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("getSmallestElementAtProperty", function() {
  it("should return the smallest element of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getSmallestElementAtProperty(obj, "array")).to.deep.eq(1);
  });
  it("should return undefined if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getSmallestElementAtProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getSmallestElementAtProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getSmallestElementAtProperty(obj, "array")).to.deep.eq(undefined);
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
* id: c63f092a-7fbe-496b-92f2-b3622b0da240
* title: getLargestElementAtProperty

### !question

Write a function called "getLargestElementAtProperty".

Given an object and a key, "getLargestElementAtProperty" returns the largest element in the array located at the given key.

Notes:
* If the array is empty, it should return undefined.
* If the property at the given key is not an array, it should return undefined.
* If there is no property at the key, it should return undefined.

```
var obj = {
  key: [1, 2, 4]
};
var output = getLargestElementAtProperty(obj, 'key');
console.log(output); // --> 4
```

### !end-question

### !placeholder

```js
function getLargestElementAtProperty(obj, key) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("getLargestElementAtProperty", function() {
  it("should return the largest element of the array located at key", function() {
    var obj = {
      array: [1, 2, 4]
    };
    expect(getLargestElementAtProperty(obj, "array")).to.deep.eq(4);
  });
  it("should return undefined if the array is empty", function() {
    var obj = {
      array: []
    };
    expect(getLargestElementAtProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property is not an array", function() {
    var obj = {
      array: "sike"
    };
    expect(getLargestElementAtProperty(obj, "array")).to.deep.eq(undefined);
  });
  it("should return undefined if the property does not exist", function() {
    var obj = {
      what: "sike"
    };
    expect(getLargestElementAtProperty(obj, "array")).to.deep.eq(undefined);
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
* id: eb2ace99-f027-4845-9d09-529ef85273ca
* title: getAllButLastElementOfProperty

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

### !challenge

* type: local-snippet
* language: javascript
* id: e43a1adc-c398-4090-9f18-be31fd425d6b
* title: getElementOfArrayProperty

### !question

Write a function called "getElementOfArrayProperty".

Given an object, a key, and a numerical index, "getElementOfArrayProperty" returns the value of the element at the given index of the array located within the given object at the given key.

Notes:
* If the array is empty, it should return undefined.
* If the given index is out of range of the array located at the given key, it should return undefined.
* If the property at the given key is not an array, it should return undefined.
* If there is no property at the key, it should return undefined.

```
var obj = {
 key: ['Jamil', 'Albrey']
};
var output = getElementOfArrayProperty(obj, 'key', 0);
console.log(output); // --> 'Jamil'
```


### !end-question

### !placeholder

```js
function getElementOfArrayProperty(obj, key, index) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe("getElementOfArrayProperty", function() {

  it("should return the element at the index of the array at the key of the passed in object", function() {
    var obj = {
      numbers: [4, 0, 1]
    };
    expect(getElementOfArrayProperty(obj, "numbers", 1)).to.deep.eq(0);
  });
  it("should return undefined if the index is out of range", function() {
    var obj = {
      numbers: [4, 0, 1]
    };
    expect(getElementOfArrayProperty(obj, "numbers", 5)).to.deep.eq(undefined);
  });
  it("should return undefined if the property at the key is not an array", function() {
    var obj = {
      name: "you"
    };
    expect(getElementOfArrayProperty(obj, "name", 0)).to.deep.eq(undefined);
  });
  it("should return undefined if there is no property at the key", function() {
    var obj = {
      name: "you"
    };
    expect(getElementOfArrayProperty(obj, "what", 0)).to.deep.eq(undefined);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
