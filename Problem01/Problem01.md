# Problem 01

#### Description: I developed two formulas to solve a mathematical problem of the distribution of items in areas with equals intervals.

Representation of the problem that I will explanish below:

<img src="https://github.com/CleitonBrito/Math/blob/master/Problem01/Pictures/Problem01-Model.png">

## Solving the problem...
To solve this problem, we need know some information:

 <img src="https://github.com/CleitonBrito/Math/blob/master/Problem01/Pictures/Problem01-TheProblem.png">
  
  - a) What is area width?
  - b) How many rectangles?
  - c) What is rectangle width?
  
 Well!
 
  - a) 800px area width
  - b) Seven (7) rectangles
  - c) 80px rectangle width
 
 <img src="https://github.com/CleitonBrito/Math/blob/master/Problem01/Pictures/Problem01-Rectangle.png">
 
First, let's find the interval value between of the rectangles

<img src="https://github.com/CleitonBrito/Math/blob/master/Problem01/Pictures/Problem01-IntervalBetween.png">

For this, I will use the first formula:

<img src="https://github.com/CleitonBrito/Math/blob/master/Problem01/Pictures/Problem01-Formula01.png">

Variables    | Description            | Values
-------------|------------------------|---------
<b>In</b>    | Result of the interval | ? (unknow)
<b>xt</b>    | Total area width       | 800px
<b>i</b>     | Rectangles quantity    | 7 unit
<b>wi</b>    | Rectangles width       | 80px

Knowing the values, we can calculate the interval:

````
        800 - (7 * 80)                800 - 560                 240
 In =  ----------------   =>    In = -----------    =>    In = ------    =>    In = 30
           7 + 1                         8                       8
````
The interval value is 30px.<br />
Great! We find the interval value between of the rectangles, and interval between the area edge.
