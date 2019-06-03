# Objects 3

### !challenge

* type: local-snippet
* language: javascript
* id: eea9cf06-5305-4626-8955-00e5d02563fb
* title: isPersonOldEnoughToDrive

### !question

Write a function called "isPersonOldEnoughToDrive".

Given a "person" object, that contains an "age" property, "isPersonOldEnoughToDrive" returns whether the given person is old enough to drive.

Notes:
* The legal driving age in the United States is 16.

```
var obj = {
  age: 16
};
var output = isPersonOldEnoughToDrive(obj);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isPersonOldEnoughToDrive(person) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("isPersonOldEnoughToDrive", function() {
  it("should return a boolean", function() {
    var person = {
      age: 55
    };
    expect(typeof isPersonOldEnoughToDrive(person)).to.deep.eq("boolean");
  });
  it("should return true if a person has an age of over 16", function() {
    var person = {
      age: 55
    };
    expect(isPersonOldEnoughToDrive(person)).to.deep.eq(true);
  });
  it("should return true if a person has an age of 16", function() {
    var person = {
      age: 16
    };
    expect(isPersonOldEnoughToDrive(person)).to.deep.eq(true);
  });
  it("should return false if a person has an age under 16", function() {
    var person = {
      age: 15
    };
    expect(isPersonOldEnoughToDrive(person)).to.deep.eq(false);
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
* id: 6b52bff0-742b-4c12-b361-03d5e7457084
* title: isPersonOldEnoughToVote

### !question

Write a function called "isPersonOldEnoughToVote".

Given a "person" object, that contains an "age" property, "isPersonOldEnoughToVote" returns whether the given person is old enough to vote.

Notes:
* The legal voting age in the United States is 18.

```
var obj = {
  age: 19
};
var output = isPersonOldEnoughToVote(obj);
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function isPersonOldEnoughToVote(person) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("isPersonOldEnoughToVote", function() {
  it("should return a boolean", function() {
    var person = {
      age: 55
    };
    expect(typeof isPersonOldEnoughToVote(person)).to.deep.eq("boolean");
  });
  it("should return true if a person has an age of over 18", function() {
    var person = {
      age: 55
    };
    expect(isPersonOldEnoughToVote(person)).to.deep.eq(true);
  });
  it("should return true if a person has an age of 18", function() {
    var person = {
      age: 18
    };
    expect(isPersonOldEnoughToVote(person)).to.deep.eq(true);
  });
  it("should return false if a person has an age under 18", function() {
    var person = {
      age: 15
    };
    expect(isPersonOldEnoughToVote(person)).to.deep.eq(false);
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
* id: 53bb0534-cafa-44a2-85ce-1d450e1f79ef
* title: addArrayProperty

### !question

Write a function called "addArrayProperty".

Given an object, a key, and an array, "addArrayProperty" sets a new property on the object at the given key, with its value set to the given array.

```
var myObj = {};
var myArray = [1, 3];
addArrayProperty(myObj, 'myProperty', myArray);
console.log(myObj.myProperty); // --> [1, 3]
```

### !end-question

### !placeholder

```js
function addArrayProperty(obj, key, arr) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("addArrayProperty", function() {
  var testObj;
  var testArray;
  beforeEach(function() {
    testObj = {};
    testArray = [1, 4];
  });
  it("should set the value at the passed in key on the passed in object to be the passed in array", function() {
    addArrayProperty(testObj, "testKey", testArray);
    expect(testObj.testKey).to.deep.eq(testArray);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
