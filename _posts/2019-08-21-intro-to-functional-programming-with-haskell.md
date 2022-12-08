---
layout: post
title: "Intro to Functional Programming With Haskell"
tags: [Functional Programming, Haskell]
---

![pbj](../images/2016-08-21-pbj.jpg)

Every single person who learns how to program is almost always taught in the
imperative style first. Meaning that the students are meant to visualize a
computer program as a set of step-by-step instructions to accomplish a
particular task. The example I've been given many times is writing a recipe to
construct a peanut butter and jelly sandwich. Thinking about how algorithms are
executed imperatively is excellent for understanding programming in general, and
I would argue that it is the most intuitive way of looking at the world.

However, it is not the only style of programming that exists. There is
declarative programming, which specifies _what_ you want and not the _how_. This
is akin to saying _"Create a peanut butter sandwich"_, instead of fleshing out
each detail on how to do so. If you have ever used SQL, you have most certainly
written declarative code, e.g.
`SELECT * FROM employees WHERE last_name='Smith' ORDER BY first_name;`. It is
almost like magic: you've merely told the computer what you want and somehow
it has found the answer without you specifying the implementation.

<!--more-->

Of course, the line between imperative and declarative programming is not so
black and white. Functional programming, which has all to do with functions as
the name implies, sits more in the declarative camp. By decomposing programs as
functions with only inputs and outputs and no state, we can benefit from some
advantages which we'll see later.

## A Primer on Haskell

Haskell is a pure functional programming language. It treats all computation as
the evaluation of functions and prevents mutating state. While it looks rather
esoteric at first, it is a good way to learn functional programming because of
how strictly it enforces this paradigm. Haskell also has an extensive type
system and so many other nifty features that I won't be able to cover in a
single post. For now, we will only look at how it uses functions.

If you want to follow along, you can compile and run Haskell code on
[repl.it](https://repl.it/languages/haskell).

### Variables

Before we jump into writing functions, this is how you assign a variable in
Haskell:
```haskell
x = 1
```

Simple enough right? Well let's try:
```haskell
x = 1
x = 2
```

We get an error:
```
error: Multiple declarations of ‘x’
```

In Haskell, a variable is defined only once in a given scope and cannot be
changed afterwards. In other words, all values are immutable. Think about this
mathematically: at no point in your algebra class did you write `x = 1`, then
`x = 2` later on in the problem.

Here is another example:
```haskell
x = 1
x = x + 1
```

This is perfectly valid code for Python, but not Haskell. In imperative
languages, we can modify values in a computer's memory, but in Haskell we must
think about this mathematically. Again, think back to your calculus class: did
you ever redefine a variable later in a problem? Would it make sense to write
`x = 1`, then `x = x + 1` in that context? This property that all values are
immutable is absolutely crucial for reasons we'll see soon.

### Functions

This is a function that adds three numbers:
```haskell
add a b c = a + b + c
```

It can be invoked like so:
```haskell
add 1 2 3
```

Note that the function arguments are separated by spaces and the arguments
follow the function name.

Let's add a type signature to the function declaration so that we can determine
its inputs and outputs:
```haskell
add :: Integer -> Integer -> Integer -> Integer
add a b c = a + b + c
```

Here we're describing that the function takes in three integers and outputs a
single integer. We'll get to why these arguments are all separated by arrows in
a future post, but think of everything before the last arrow as input argument
types, and what follows after as the return type.

Here is another simple function:
```haskell
isEven :: Integer -> Bool
isEven n = (mod n 2) == 0
```

Remember that the function and its arguments are space separated. `mod n 2` is
just like invoking `mod(n, 2)` in many languages if `mod(n, m)` was implemented
using the modulo operator (`%`).

### Control flow

There are several ways to evaluate "conditions" in Haskell programs, which are
(1) guards, (2) if expressions, (3) pattern matching, and (4) case expressions.
I will briefly cover (1) and (3) as those two control flows will be your bread
and butter in writing Haskell programs.

#### Guards

Let's create a function to strip the magnitude of a number and keep its
direction, i.e. negative numbers go to -1, positive numbers go to 1, and 0 stays
0:
```haskell
direction :: Integer -> Integer
direction n
  | n < 0     = -1
  | n == 0    = 0
  | otherwise = 1
```

All input possibilities must be addressed, or else the compiler will complain
about any unhandled cases. Here is another function with guards using our
`isEven` function above:
```haskell
consume :: Integer -> [Char]
consume n
  | isEven n  = "Even numbers are delicious!"
  | otherwise = "Odd numbers don't taste good..."
```

### Pattern matching

While guards check that the predicate matches a certain condition, pattern
matching checks the _structure_ of the function and its arguments.

Here is a factorial function:
```haskell
factorial :: Integer -> Integer
factorial 0 = 1
factorial n = n * factorial (n - 1)
```

Wait what's the deal? We could have used guards! A more common use of pattern
matching is destructuring lists and tuples. Here is how to get the length of a
list, similar to how one might compute it for a singly linked list:
```haskell
length :: [Integer] -> Integer
length [] = 0
length (x:xs) = 1 + length xs
```

This basically reads: _"If the list looks empty, return 0. Otherwise, split the
list into a single head element, and the rest of the list. Recurse on the rest
of the list"_. Here is a function to double every other element in a list:
```haskell
multiply :: [Integer] -> [Integer]
multiply []       = []
multiply (x:y:ys) = 2 * x : y : multiply ys
multiply (x:xs)   = 2 * x : multiply xs
```

Guards and patterns are checked top to bottom. That's why the `(x:y:ys)`
structure comes before `(x:xs)` - we care more about matching lists with two or
more elements. If `(x:xs)` was before `(x:y:ys)`, then we would never enter the
expression for `(x:y:ys)`.

## Putting it together

![function](../images/2016-08-21-function.png)

Notice that for all of these functions, we never kept track of state. While
these functions are quite basic, there was no object or variable that we
mutated. We should simply be thinking of inputs and outputs and how we can
_only_ use them to compute data - let's pretend that `void` functions and the
like are strictly forbidden in this new land. The beauty of removing side
effects from code execution is that you can be more confident that a function
call is not going to launch the missiles unknowingly per se. After all, I'm sure
many of us have been burned by functions that changed some object state with a
name as innocuous as `computeSomeProperty()`.

The functions we have written thus far are known as
[pure](https://en.wikipedia.org/wiki/Pure_function) functions. That's not to say
you can't functions without side effects in imperative languages, but the
difference is that Haskell programs are solely comprised of such functions. Pure
functions also imply another concept called
[referential transparency](https://en.wikipedia.org/wiki/Referential_transparency),
where given a function and its inputs, you will always receive the same output.
In other words, the function is deterministic.

This opens a whole can of worms: well how can you do anything? What about random
number generators? Reading files? Calling other programs? Caching data? Haskell
has ways of dealing with all of these valid concerns that I won't detail here,
but it is definitely why people feel restricted writing code with it, myself
included.

## Functional programming in the wild

Let's solve a real world problem: validating credit card numbers. Believe it or
not, vendors don't actually check a card's number against a database. Instead,
we can use [Luhn's algorithm](https://en.wikipedia.org/wiki/Luhn_algorithm) to
validate it ourselves, which is described as such:
1. Drop the last digit from the credit card number; this is known as the check
   digit
1. Reverse the numbers
1. Multiply the digits in every other position by 2
  * If this number higher than 9, subtract 9
1. Add all the numbers together
1. Verify that the check digit is the amount that you would need to add to the
  result in order to get a multiple of 10

Let's quickly run through the algorithm with an example:
```
-- Sample credit card number
371449635398431

-- Drop the check digit
37144963539843 | 1

-- Let's space out the rest of the numbers for readability
3  7  1  4  4  9  6  3  5  3  9  8  4  3

-- Reverse the sequence
3  4  8  9  3  5  3  6  9  4  4  1  7  3

-- Multiply every other number by 2
3  .  8  .  3  .  3  .  9  .  4  .  7  .
6     16    6     6     18    8     14

-- Subtract 9 from any of these greater than 9
3  .  8  .  3  .  3  .  9  .  4  .  7  .
6     7     6     6     9     8     5

-- Sum up all of the numbers
6  4  7  9  6  5  6  6  9  4  8  1  5  3 = 79

-- Check digit + the result should be a multiple of 10
(1 + 79) % 10 == 0
```

This is how I might write it in Haskell. Let's start with the skeleton:
```haskell
luhn :: Integer -> Bool
luhn n = validate (last list) (result (init list)) where
  list = toList n

-- toList 371449635398431 -> [3,7,1,4,4,9,6,3,5,3,9,8,4,3,1]
toList :: Integer -> [Integer]
toList n
  | n > 0     = toList (div n 10) ++ [mod n 10]
  | otherwise = []

-- These functions to split a list are already built-in:
-- last [3,7,1,4,4,9,6,3,5,3,9,8,4,3,1] -> 1
-- init [3,7,1,4,4,9,6,3,5,3,9,8,4,3,1] -> [3,7,1,4,4,9,6,3,5,3,9,8,4,3]

-- validate 79 1 -> True, validate 78 1 -> False
validate :: Integer -> Integer -> Bool
validate checkDigit result = mod (checkDigit + result) 10 == 0
```

This is tackling the problem top down. Convert the number to a list of digits,
and validate that the check digit + result is a multiple of 10. Here is what the
`last` and `init` built-in Haskell functions represent when given a list:
![listmonster](../images/2016-08-21-listmonster.png)

Now let's write the `result` function, the main meat of the problem:
```haskell
-- We are passed in a list of all of the credit card digits except the last one
-- result [3,7,1,4,4,9,6,3,5,3,9,8,4,3] -> 79
result :: [Integer] -> Integer
result list = sum (multiply (reverse list))

-- reverse [3,7,1,4,4,9,6,3,5,3,9,8,4,3] -> [3,4,8,9,3,5,3,6,9,4,4,1,7,3]
-- The reverse function is already built-in

-- multiply [3,4,8,9,3,5,3,6,9,4,4,1,7,3] -> [6,4,7,9,6,5,6,6,9,4,8,1,5,3]
multiply :: [Integer] -> [Integer]
multiply []       = []
multiply (x:y:ys) = (process x) : y : multiply ys
multiply (x:xs)   = (process x) : multiply xs

-- process 4 -> 8, process 5 -> 1, process 8 -> 7, etc
process :: Integer -> Integer
process n
  | (2 * n) > 9 = (2 * n) - 9
  | otherwise   = (2 * n)

-- sum [6,4,7,9,6,5,6,6,9,4,8,1,5,3] -> 79
-- The sum function is already built-in
```

So now we can invoke the `luhn` function, since its constituent parts are all
implemented:
```haskell
luhn 371449635398431  -- True
luhn 371449635398432  -- False
luhn 341410444756588  -- True
luhn 341410444756589  -- False
luhn 4539210762233333 -- True
luhn 4539210762233334 -- False
```

When you are confined to solving a problem using only functions, it helps to
break up it up into small pieces you can put together like legos. This is one of
the biggest benefits of functional programming: you're essentially forced into
writing functions that are modular and _composable_.

You'll see that with functional programming, there is a _heavy_ emphasis on
using recursion. Perhaps not so much with this particular problem, but your
typical loop constructs are always delegated with function calls. If definitely
takes a bit of time to completely rewire over way of thinking to this new
paradigm if all you have been using is Java, Python, and the like.

Consider how one might naively approach this problem with C++. If given a list,
they might loop over it backwards and mutate it as they process each element.
While this may be more algorithmically performant in terms of time and space,
you could argue that the Haskell variant is cleaner and more maintainable. Of
course, you can port over this implementation to C++, but C++ isn't opinionated
as a language for its users to write code in this fashion. It is telling that
many new and existing languages are adding functional programming constructs to
better facilitate code maintainability (such as lambdas and higher order
functions that we may explore eventually).

#### Digression on function composability
Here is a little bit extra that Haskell can gift you. This was our `result`
function:
```
result list = sum (multiply (reverse list))
```

If you think about the input and return type of each of the functions on the
right, you'll notice that they take in a list and return a list. Do you
remember in your math class how `g(f(x))` was equivalent to `(g ∘ f)(x)`? You
can do the same thing here, so this function can actually look like:
```
result list = (sum . multiply . reverse) list
```

The `.` is the function composition operator, similar to the `∘` sign in math.
Finally, since the `result` function **is** the composition of those three
functions, we can "cancel" out the `list` term on both sides:
```
result = sum . multiply . reverse
```

Wow - very elegant! This is called
[point-free style](https://en.wikipedia.org/wiki/Tacit_programming) programming,
and is one of many goodies that you can use when writing pure and composable
functions in Haskell.

## Wrapping up

This was just a brief and informal introduction to Haskell in order to highlight
some of the essence of functional programming. The point here isn't to learn
Haskell and start use it everywhere; on the contrary, writing code without
mutating data and isolating side effects is often tedious. I think the crucial
lesson is to take these concepts and see how they can be applied in day-to-day
programming. E.g. do we really need to represent this problem as Java object
with mutable class variables? Can we refactor these Python methods to strictly
process inputs and outputs and avoid using this `global var`?

Haskell is often touted as bug-free after compilation due to its pure functional
nature and strong static type system. While that may be true, we can certainly
be inspired by its ideas and execute them in other programming environments,
even if we never have the chance to work directly with pure functional programming
languages. Concepts like function purity (and referential transparency less so)
_do_ appear in the real world, so it's beneficial to have some grasp about the
terminology.

If the content from this post piqued your interest in Haskell, here are some
excellent resources to get started:
* [Learn You a Haskell](http://learnyouahaskell.com/introduction)
* [Haskell Wikibooks](https://en.wikibooks.org/wiki/Haskell)
* [CIS 194 Course](https://www.cis.upenn.edu/~cis194/spring13/)
