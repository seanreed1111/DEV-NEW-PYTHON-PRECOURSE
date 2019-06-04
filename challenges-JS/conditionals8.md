# Conditionals 8

### !challenge

* type: local-snippet
* language: javascript
* id: f328e513-d275-4a7b-aa70-b3ac917ce57a
* title: convertScoreToGrade

### !question

Write a function called "convertScoreToGrade".

Given a score, "convertScoreToGrade" returns a string representing the letter grade corresponding to the given score.

Notes:
* (100 - 90) --> 'A'
* (89  - 80) --> 'B'
* (79  - 70) --> 'C'
* (69  - 60) --> 'D'
* (59  -  0) --> 'F'
* If the given score is greater than 100 or less than 0, it should return 'INVALID SCORE'.

```
var output = convertScoreToGrade(91);
console.log(output); // --> 'A'
```

### !end-question

### !placeholder

```js
function convertScoreToGrade(score) {
  // your code here

}
```

### !end-placeholder

### !tests

```js

describe("convertScoreToGrade", function() {
  it("should return a string", function() {
    expect(typeof(convertScoreToGrade(95))).to.deep.eq("string");
  });
  it("should return 'A' for scores between 90 and 100", function() {
    expect(convertScoreToGrade(95)).to.deep.eq("A");
  });
  it("should return 'B' for scores between 80 and 89", function() {
    expect(convertScoreToGrade(80)).to.deep.eq("B");
  });
  it("should return 'C' for scores between 70 and 79", function() {
    expect(convertScoreToGrade(79)).to.deep.eq("C");
  });
  it("should return 'D' for scores between 60 and 69", function() {
    expect(convertScoreToGrade(60)).to.deep.eq("D");
  });
  it("should return 'F' for 59", function() {
    expect(convertScoreToGrade(59)).to.deep.eq("F");
  });
  it("should return 'F' for scores between 0 and 59", function() {
    expect(convertScoreToGrade(50)).to.deep.eq("F");
  });
  it("should return 'F' for 0", function() {
    expect(convertScoreToGrade(0)).to.deep.eq("F");
  });
  it("should return 'INVALID SCORE' for scores less than 0", function() {
    expect(convertScoreToGrade(-1)).to.deep.eq("INVALID SCORE");
  });
  it("should return 'INVALID SCORE' for scores greater than 100", function() {
    expect(convertScoreToGrade(101)).to.deep.eq("INVALID SCORE");
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
* id: d53cbbaf-dfb4-44ab-a0a9-9512018da2be
* title: convertScoreToGradeWithPlus

### !question

Write a function called "convertScoreToGradeWithPlusAndMinus".

Given a score, "convertScoreToGradeWithPlusAndMinus" returns a string representing the letter grade corresponding to the given score.

Notes:
* (100 - 90) --> 'A'
* (89  - 80) --> 'B'
* (79  - 70) --> 'C'
* (69  - 60) --> 'D'
* (59  -  0) --> 'F'
* If the given score is greater than 100 or less than 0, it should return 'INVALID SCORE'.
* If the score is between the 0 and 2 (inclusive) of a given range, return the letter with a '-'
* If the score is be the 8 and 9 (inclusive) of a given range, return the letter with a '+'
* There are is no F+ and there is no F-.

```
var output = convertScoreToGradeWithPlusAndMinus(91);
console.log(output); // --> 'A-'
```

### !end-question

### !placeholder

```js
function convertScoreToGradeWithPlusAndMinus(score) {
  // your code here
  
}
```

### !end-placeholder

### !tests

```js

describe("convertScoreToGradeWithPlusAndMinus", function() {
  it("should return a string", function() {
    expect(typeof(convertScoreToGradeWithPlusAndMinus(95))).to.deep.eq("string");
  });
  it("should return 'A+' for scores between 98 and 100", function() {
    expect(convertScoreToGradeWithPlusAndMinus(100)).to.deep.eq("A+");
  });
  it("should return 'A-' for scores between 90 and 92", function() {
    expect(convertScoreToGradeWithPlusAndMinus(90)).to.deep.eq("A-");
  });
  it("should return 'A' for scores between 93 and 97", function() {
    expect(convertScoreToGradeWithPlusAndMinus(95)).to.deep.eq("A");
  });
  it("should return 'B+' for scores between 88 and 89", function() {
    expect(convertScoreToGradeWithPlusAndMinus(89)).to.deep.eq("B+");
  });
  it("should return 'B-' for scores between 80 and 82", function() {
    expect(convertScoreToGradeWithPlusAndMinus(80)).to.deep.eq("B-");
  });
  it("should return 'B' for scores between 83 and 87", function() {
    expect(convertScoreToGradeWithPlusAndMinus(84)).to.deep.eq("B");
  });
  it("should return 'C+' for scores between 78 and 79", function() {
    expect(convertScoreToGradeWithPlusAndMinus(79)).to.deep.eq("C+");
  });
  it("should return 'C-' for scores between 70 and 72", function() {
    expect(convertScoreToGradeWithPlusAndMinus(70)).to.deep.eq("C-");
  });
  it("should return 'C' for scores between 73 and 77", function() {
    expect(convertScoreToGradeWithPlusAndMinus(76)).to.deep.eq("C");
  });
  it("should return 'D+' for scores between 68 and 69", function() {
    expect(convertScoreToGradeWithPlusAndMinus(69)).to.deep.eq("D+");
  });
  it("should return 'D' for scores between 63 and 67", function() {
    expect(convertScoreToGradeWithPlusAndMinus(64)).to.deep.eq("D");
  });
  it("should return 'D-' for scores between 60 and 62", function() {
    expect(convertScoreToGradeWithPlusAndMinus(60)).to.deep.eq("D-");
  });
  it("should return 'F' for scores between 0 and 59", function() {
    expect(convertScoreToGradeWithPlusAndMinus(0)).to.deep.eq("F");
  });
  it("should return 'INVALID SCORE' for scores less than 0", function() {
    expect(convertScoreToGradeWithPlusAndMinus(-1)).to.deep.eq("INVALID SCORE");
  });
  it("should return 'INVALID SCORE' for scores greater than 100", function() {
    expect(convertScoreToGradeWithPlusAndMinus(101)).to.deep.eq("INVALID SCORE");
  });
});

```

### !end-tests

### !explanation

### !end-explanation

### !end-challenge
