### !challenge

* type: local-snippet
* language: javascript
* id: eea9cf06-5305-4626-8955-00e5d02563fb
* title: isPersonOldEnoughToDrive.md

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
