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

<img src="https://github.com/CleitonBrito/Math/blob/master/Problem01/Pictures/Problem01-ValueInterval.png">

Now, we will find values of the positions of the rectangles to distribute equally in the area. <br />
<b>Obs: It will be taken into account the left edge of the rectangle to position</b>

For this, we will used the second formula:

<img src="https://github.com/CleitonBrito/Math/blob/master/Problem01/Pictures/Problem01-Formula02.png">

Variables     | Description
--------------|-----------------------
<b>Pos</b>    | Result of the item position
<b>x</b>      | Rectangle index
<b>In</b>     | Result of the interval
<b>wi</b>     | Rectangles width

Rules:
 - The variable <b>x</b> needs starting at 0 and increment until <b>i - 1</b>
 - The variable <b>In</b> need to be >= 0
 
 See:
 
  x  | Apply formula                   | Position
  ---|---------------------------------|------------
  0  | 30 + ( <b>0</b> * ( 80 + 30 ))  | 30px
  1  | 30 + ( <b>1</b> * ( 80 + 30 ))  | 140px
  2  | 30 + ( <b>2</b> * ( 80 + 30 ))  | 250px
  3  | 30 + ( <b>3</b> * ( 80 + 30 ))  | 360px
  4  | 30 + ( <b>4</b> * ( 80 + 30 ))  | 470px
  5  | 30 + ( <b>5</b> * ( 80 + 30 ))  | 580px
  6  | 30 + ( <b>6</b> * ( 80 + 30 ))  | 690px
  
  <img src="https://github.com/CleitonBrito/Math/blob/master/Problem01/Pictures/Problem01-PositionsValues.png">