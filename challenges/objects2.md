# Objects 2

### !challenge

* type: local-snippet
* language: javascript
* id: 56940947-7f0a-444b-bb8a-635464d92f45
* title: addFullNameProperty

### !question

Write a function called "addFullNameProperty".

Given an object that has a "firstName" property and a "lastName" property, "addFullNameProperty" returns a "fullName" property whose value is a string with the first name and last name separated by a space.

```
var person = {
  firstName: 'Jade',
  lastName: 'Smith'
};
addFullNameProperty(person);
console.log(person.fullName); // --> 'Jade Smith'
```

### !end-question

### !placeholder

```js
function addFullNameProperty(obj) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js


describe("addFullNameProperty", function() {
  it("should create a fullName property with the firstName and lastName separated by a space", function() {
    var tim = {
      firstName: "Tim",
      lastName: "Goldfish"
    };
    addFullNameProperty(tim);
    expect(tim.fullName).to.deep.eq("Tim Goldfish");
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
* id: c3b7ef25-71fe-47ff-9a75-2f9965695f31
* title: addObjectProperty

### !question

Write a function called "addObjectProperty".

Given two objects and a key, "addObjectProperty" sets a new property on the 1st object at the given key. The value of that new property is the entire 2nd object.

```
var person1 = {
  name: 'Joe Blow',
  role: 'schlub'
};
var person2 = {
  name: 'Mr. Burns',
  role: 'supervisor'
};
addObjectProperty(person1, 'manager', person2);
console.log(person1.manager); // --> { name: 'Mr. Burns', role: 'supervisor' }
```

### !end-question

### !placeholder

```js
function addObjectProperty(obj1, key, obj2) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("addObjectProperty", function() {
  var obj1;
  var obj2;
  beforeEach(function() {
    obj1 = {};
    obj2 = {
      name: "Dude"
    };
  });
  it('should set the value at the passed in key on the passed in object to be the second passed in object', function() {
    addObjectProperty(obj1, 'testKey', obj2);
    expect(obj1.testKey).to.deep.eq(obj2);
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
* id: 67b64495-b5b3-4d3a-b3a2-7a471de45c03
* title: isPersonOldEnoughToDrinkAndDrive

### !question

Write a function called "isPersonOldEnoughToDrinkAndDrive".

Given a "person" object, that contains an "age" property, "isPersonOldEnoughToDrinkAndDrive" returns whether the given person is old enough to legally drink and drive in the United States.

Notes:
* The legal drinking age in the United States is 21.
* The legal driving age in the United States is 16.
* It is ALWAYS illegal to drink and drive in the United States.

```
var obj = {
  age: 45
};
var output = isPersonOldEnoughToDrinkAndDrive(obj);
console.log(output); // --> false
```

### !end-question

### !placeholder

```js
function isPersonOldEnoughToDrinkAndDrive(person) {
  // your code here
   

   
}

```

### !end-placeholder

### !tests

```js

describe("isPersonOldEnoughToDrinkAndDrive", function() {
  it("should return a boolean", function() {
    var person = {
      age: 55
    };
    expect(typeof isPersonOldEnoughToDrinkAndDrive(person)).to.deep.eq("boolean");
  });
  it("should return false", function() {
    expect(isPersonOldEnoughToDrinkAndDrive()).to.deep.eq(false);
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
