### !challenge

* type: local-snippet
* language: javascript
* id: c27c7922-479a-41ca-a400-d3bc984468f4
* title: convertArrayToObject1.md

### !question


Write a function 'transformFirstAndLast' that takes in an array, and returns an object with:
1) the first element of the array as the object's key, and
2) the last element of the array as that key's value.

Example input:
```
['Queen', 'Elizabeth', 'Of Hearts', 'Beyonce']
```

Function's return value (output):
```
{
  Queen : 'Beyonce'
}
```

Do not change the input array. Assume all elements in the input array will be of type 'string'.

Note that the input array may have a varying number of elements. Your code should flexibly accommodate that.

E.g. it should handle input like:
```
['Kevin', 'Bacon', 'Love', 'Hart', 'Costner', 'Spacey']
```

Function's return value (output):
```
{
  Kevin : 'Spacey'
}
```

### !end-question

### !placeholder

```js
function transformFirstAndLast(array) {
  // your code here
}
```

### !end-placeholder

### !tests

```js

describe('transformFirstAndLast', function() {
  it('should_properly_assign_key_and_value_pair', function (){

    var input = ['Marie', 'Kayla', 'Jackson', 'Richard', 'Kyle', 'Sarah', 'Mars', 'Wayne', 'Mary'];

    var output = transformFirstAndLast(input);

    expect(output).not.to.deep.eq(undefined);
    expect(typeof output).to.deep.eq('object');
    expect(output.Marie).to.deep.eq('Mary');
  });

  it('should_not_modify_input_array', function() {
    var input = ['Mars', 'Wayne', 'Mary'];
    var copy = input.slice(0);
    var output = transformFirstAndLast(input);

    expect(input.length).to.deep.eq(copy.length);
    expect(copy[0]).to.deep.eq(input[0]);
    expect(copy[1]).to.deep.eq(input[1]);
    expect(copy[2]).to.deep.eq(input[2]);

  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
