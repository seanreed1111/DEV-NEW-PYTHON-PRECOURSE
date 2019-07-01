### !challenge

* type: local-snippet
* language: javascript
* id: 1c684aae-9cf8-4c7b-907f-eb1e88a7084d
* title: greetCustomer.md

### !question

Write a function called "greetCustomers".

Given a name, "greetCustomers" returns a greeting based on how many times that customer has visited the restaurant.  Please refer to the customerData object.

The greeting should be different, depending on the name on their reservation.

Case 1 - Unknown customer ( Name is not present in customerData ):

```
var output = greetCustomer('Terrance');
console.log(output); // --> 'Welcome! Is this your first time?'
```

Case 2 - Customer who has visited only once ( 'visits' value is 1 ):

```
var output = greetCustomer('Joe');
console.log(output); // --> 'Welcome back, Joe! We're glad you liked us the first time!'
```

Case 3 - Repeat customer: ( 'visits' value is greater than 1 ):

```
var output = greetCustomer('Carol');
console.log(output); // --> 'Welcome back, Carol! So glad to see you again!'
```

Notes:
* Your function should not alter the customerData object to update the number of visits.
* Do not hardcode to the exact sample data. This is a BAD IDEA:

```
if (firstName === 'Joe') {
  // do something
}
```

### !end-question

### !placeholder

```js
var customerData = {
  'Joe': {
    visits: 1
  },
  'Carol': {
    visits: 2
  },
  'Howard': {
    visits: 3,
  },
  'Carrie': {
    visits: 4
  }
};

function greetCustomer(firstName) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe('greetCustomer', function() {
  it('handles 1st time visitor from sample data', function() {
    var output = greetCustomer('Voldemort');
    var expected = 'Welcome! Is this your first time?';
    expect(output).to.deep.eq(expected);
  });

  it('handles 2nd time visitor from sample data', function() {
    var output = greetCustomer('Joe');
    var expected = "Welcome back, Joe! We're glad you liked us the first time!";
    expect(output).to.deep.eq(expected);
  });

  it('handles 2nd time visitor from new nonsample data', function() {
    var oldCustomerDataJSON = JSON.stringify(customerData);

    customerData['Ben'] = {
      visits: 1
    };

    var output = greetCustomer('Ben');
    var expected = "Welcome back, Ben! We're glad you liked us the first time!";
    expect(output).to.deep.eq(expected);

    customerData = JSON.parse(oldCustomerDataJSON);
  });

  it('handles 3rd time visitor from sample data', function() {
    var output = greetCustomer('Howard');
    var expected = 'Welcome back, Howard! So glad to see you again!';
    expect(output).to.deep.eq(expected);
  });

  it('handles 4th time visitor from new nonsample data', function() {
    var oldCustomerDataJSON = JSON.stringify(customerData);

    customerData['Macklemore'] = {
      visits: 3
    };

    var output = greetCustomer('Macklemore');
    var expected = 'Welcome back, Macklemore! So glad to see you again!';
    expect(output).to.deep.eq(expected);

    customerData = JSON.parse(oldCustomerDataJSON);
  });

});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
