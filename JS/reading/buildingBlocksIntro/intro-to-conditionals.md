# Intro to Conditionals

## Key Takeaways

In this section, you will:
* Translate real-life decisions into code using conditional statements
* Model more complex problems using logical operators
* Get introduced to imposter syndrome

## Explanation #1

Complete the third section of Udacity's JS101.

* [Complete Lesson 3: Conditionals](https://classroom.udacity.com/courses/ud803)

## Explanation #2

[Here's another nice video on conditionals](https://www.youtube.com/watch?v=Gy87ZS5sb1w) that watches someone play with comparisons in the console.

In general, [doing research](http://www.theallium.com/engineering/computer-programming-to-be-officially-renamed-googling-stackoverflow/) as a software engineer is a big part of the job. YouTube, StackOverflow, blogs, and official documentation are all things you will have to be comfortable using in your day-to-day. If one explanation doesn't work, find another. Sometimes when you finally find the explanation that makes things click you may think to yourself, "Jeez, I wish I found this resource first, I would have saved a lot of time." Although a natural reaction, you should realize that a lot of times it's not the final resource that solved your problem, but the sum of all the work you did up to that point. Appreciate and acknowledge the journey, not just the destination!

## Explanation #3
Read [this article](https://medium.com/@aliciatweet/overcoming-impostor-syndrome-bdae04e46ec5) on imposter syndrome.

Once you do that, read through [this reddit](https://www.reddit.com/r/cscareerquestions/comments/7dri9z/does_imposter_syndrome_ever_go_away/) thread on the topic to get a sense of what the broader community thinks on the topic.

Imposter syndrome is a natural part of learning something new, especially in computer science where it feels like there is always more to learn and you don't have experience in the industry to understand how you compare to others. It will take a very long time to "beat" imposter syndrome, so it's important to be aware of what it is and how to manage it. There are many ways to approach managing imposter syndrome, having a [growth mindset](https://www.youtube.com/watch?v=hiiEeMN7vbQ) is one we highly recommend.

If you are a reddit user (or even if you're not) we recommend that you subscribe to the [/r/cscareerquestions](https://reddit.com/r/cscareerquestions/) subreddit. It has some really great discussions and will start giving you some context to the challenges developers have and will hopefully give you the feeling that you're not alone in your struggles. Here are some of our favorite articles (disclaimer: what you read on these threads do not necessarily represent the views of Hack Reactor. It's an open forum on the internet, treat it as such).
* [Story](https://www.reddit.com/r/cscareerquestions/comments/6278bi/my_journey_and_tips_29_gpa_at_a_noname_liberal/) of how a 2.9 GPA CS student got four full time offers, including one from Facebook
* [An AMA](https://www.reddit.com/r/cscareerquestions/comments/6enydz/im_gayle_laakmann_mcdowell_author_of_cracking_the/) with Gayle Laakmann McDowell, author of [Cracking the Coding Interview](https://www.amazon.com/Cracking-Coding-Interview-Programming-Questions/dp/0984782850), which we highly recommend as a resource for extra toy problems after you finish this prep program. You can even google the JavaScript solutions to the exercises.
* [Salary negotiation](https://www.reddit.com/r/cscareerquestions/comments/8cta0d/my_first_negotiation_a_success_story/) success story and advice
* [Mild annoyances](https://www.reddit.com/r/cscareerquestions/comments/7kwwim/mild_annoyances_of_being_a_female_developer/) of a female developer

## Vocabulary List
Some vocab words to add to your mental glossary:
* !=
* &&
* ||
* == vs ===
* Falsy
* Growth mindset
* If... Else
* Imposter syndrome
* Switch statements
* Ternary operator
* Truthy

## Check For Understanding

<!--BEGIN CHALLENGE-->

### !challenge

* type: local-snippet
* language: javascript
* id: aa4ecec2-6844-472d-82d2-4171995d3e22
* title: Conditionals

### !question

Two variables will be passed into your code: `day` and `money`.

* If `day` is `'Sunday'` and `money` is `20.0` or more, console log `'Avocado toast for breakfast today!'`

* Otherwise, console log `'Cereal again.'`

### !end-question

### !placeholder

```js
function myFunction(money, day) {
  // Write a conditional statement below.
  // Check the values of `money` and `day`.
  // Console.log the message described above.

}
```

### !end-placeholder

### !tests

```js

describe('Uses conditionals', function(money, day) {

    it("has avocado toast for breakfast on Sunday if $20", function() {
      var originalLogger = console.log;
      var capturedMessage = '';
      console.log = function(message) {
        capturedMessage += message;
      }

      myFunction(20, "Sunday");

      console.log = originalLogger;

      expect(capturedMessage, "money = 20; day = 'Sunday'").to.deep.eq('Avocado toast for breakfast today!')
    })

    it("has avocado toast for breakfast on Sunday if > $20", function() {
      var originalLogger = console.log;
      var capturedMessage = '';
      console.log = function(message) {
        capturedMessage += message;
      }

      myFunction(21, "Sunday");

      console.log = originalLogger;

      expect(capturedMessage, "money = 21; day = 'Sunday'").to.deep.eq('Avocado toast for breakfast today!')
    })

    it("has cereal for breakfast on Sunday if < $20", function() {
      var originalLogger = console.log;
      var capturedMessage = '';
      console.log = function(message) {
        capturedMessage += message;
      }

      myFunction(19, "Sunday");

      console.log = originalLogger;

      expect(capturedMessage, "money = 19; day = 'Sunday'").to.deep.eq('Cereal again.')
    })

    it("has cereal for breakfast on Monday if > $20", function() {
      var originalLogger = console.log;
      var capturedMessage = '';
      console.log = function(message) {
        capturedMessage += message;
      }

      myFunction(21, "Monday");

      console.log = originalLogger;

      expect(capturedMessage, "money = 21; day = 'Monday'").to.deep.eq('Cereal again.')
    })
})

```

### !end-tests

### !end-challenge

<!--END CHALLENGE-->

## Survey

These are optional, anonymous surveys that help us improve the course.

<p><iframe src="https://docs.google.com/forms/d/e/1FAIpQLSechoL38mbH743LBqOkfT99j-wBcrIazibPMn36cA1_RR6W5g/viewform?embedded=true" width="700" height="720" frameborder="0" marginheight="0" marginwidth="0">Loading...</iframe></p>
