### !challenge

* type: local-snippet
* language: javascript
* id: b99bc1a5-bc3a-42c5-9372-745bcbea92a7
* title: areValidCredentials.md

### !question

Write a function called "areValidCredentials".

Given a name and a password, "areValidCredentials", returns true if the name is longer than 3 characters, AND, the password is at least 8 characters long. Otherwise it returns false.

```
var output = areValidCredentials('Ritu', 'mylongpassword')
console.log(output); // --> true
```

### !end-question

### !placeholder

```js
function areValidCredentials(name, password) {
  // your code here
   

   
}
```

### !end-placeholder

### !tests

```js

describe("areValidCredentials", function() {
  it("should return a boolean", function() {
    expect(typeof areValidCredentials("Ritu", "mylongpassword")).to.deep.eq("boolean");
  });
  it("should return true if the name is longer than 3 characters and the password is at least 8 characters", function() {
    expect(areValidCredentials("Ritu", "mylongpassword")).to.deep.eq(true);
  });
  it("should return false if the name is less than 3 characters", function() {
    expect(areValidCredentials("me", "mylongpassword")).to.deep.eq(false);
  });
  it("should return false if the password is not at least 8 characters", function() {
    expect(areValidCredentials("Someone", "1234567")).to.deep.eq(false);
  });
});


```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
