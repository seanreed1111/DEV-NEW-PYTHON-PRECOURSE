### !challenge

* type: local-snippet
* language: javascript
* id: af0470f5-db25-4019-881b-3f73c0bda343
* title: convertObjectToList2.md

### !question

Write a function called "listAllValues" which returns an array of all the input object's values.
Example input:

```
{
  name : 'Krysten',
  age : 33,
  hasPets : false
}
```

Function's return value (output):

```
['Krysten', 33, false]
```

Note that the input may have a different number of keys and values than the given sample.
E.g. it should also handle an input like:

```
{
  a : 'a',
  number : 11,
  hungry : true,
  grammyWins : 1
}
```

Function's return value (output):

```
['a', 11, true, 1]
```

### !end-question

### !placeholder

```js
function listAllValues(obj) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe ('listAllValues', function() {
  it ('should_output_an_array_of_values', function(){
    var input = {
      foo: 'bar',
      level: 1,
      red: 'green',
      number: true,
      cry: 'excelsior'
    }

    var output = listAllValues(input);
    console.log(Array.isArray(output));
    console.log(output);

    expect(output).not.to.deep.eq(undefined);
    expect(output[0]).to.deep.eq('bar');
    expect(output[1]).to.deep.eq(1);
    expect(output[2]).to.deep.eq('green');
    expect(output[3]).to.deep.eq(true);
    expect(output[4]).to.deep.eq('excelsior');
  });

});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
