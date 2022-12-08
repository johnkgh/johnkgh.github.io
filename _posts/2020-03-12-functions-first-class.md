---
layout: post
title: "Functions: First Class"
tags: [Functional Programming, Haskell, Python]
---

![functions-first-class](../images/2017-03-12-functions-first-class.png)

Last time, we covered some of the basics of functional programming. We saw how
code could be comprised of and evaluated using entirely mathematical functions.
There was much emphasis defining functions as an entity that operates purely on
its _inputs_ and _outputs_. Let's further expound on that by thinking about
_what_ those inputs and outputs can be.

I like to imagine a typical imperative program as a story with nouns and verbs.
In this story, you have objects, and actions that can be performed on or by
objects. In Java, you may have a class to represent a `Dog` (noun), and that dog
can perform an action like `dog.eat(food)` (verb). In Ruby, where _everything_
is an object, you can invoke a method even on a number, e.g. `2.+(3)`. The point
remains: you have objects, and operations you can do with them.

<!--more-->

If we're thinking of code in the reductive grammatical framework of subjects and
predicates, we have only seen what it means to _verb_ a _noun_ so to speak. What
would it mean to _verb_ a _verb_? This is a question (and need) that functional
programming aims to address.

## First-class functions

In order to facilitate functional programming, a language must have support for
[first-class functions](https://en.wikipedia.org/wiki/First-class_function).
This means that a function can be:
1. assigned to a variable
1. passed in as input arguments to a function
1. returned as an output of a function

In other words, with these three behaviors, we will be able to treat functions
just like objects. Feel free to follow along using repl.it for
[Haskell](https://repl.it/languages/haskell) and
[Python](https://repl.it/languages/python3).

### (1) Functions assigned to a variable

In Haskell this is pretty easy:
```haskell
add a b c = a + b + c

d = add
d 1 2 3 -- This evaluates the function d with 3 integer arguments
```

We can do the same in Python:
```python
def add(a, b, c):
    return a + b + c

d = add
d(1, 2, 3)
```

Notice that `d(...)` is the invocation of the function `d` that we initialized
with the `add` function. Without those parenthesis, `d` is completely inert.

One use of this language feature is when the method you want from an object
is deeply nested within many other layers of objects:
```python
# We can invoke this clumsy function call everytime we need to use it
StaticObject1.StaticObject2.StaticObject3.doSomething(a, b, c)

# Or we can save it off into a variable for easy access and better readability
doSomething = StaticObject1.StaticObject2.StaticObject3.doSomething
doSomething(a, b, c)
```

### (2) Functions passed in as input arguments to a function

Now that we are able to assign functions to variables, we can also pass them
into functions as well. Here's what that looks like in Haskell:
```haskell
-- operate takes in a function and some arguments, and simply calls the input
-- function with its arguments. operate is function agnostic - as long as it
-- receives three inputs and the types match up, all is well.
operate f a b c = f a b c

add a b c = a + b + c
mul a b c = a * b * c

operate add 2 3 4 -- operate calls the add function with its arguments 2, 3, 4
operate mul 2 3 4 -- operate calls the mul function with its arguments 2, 3, 4
```

A function can also take in multiple functions:
```haskell
-- operate2 takes in two functions and a number. It applies function g to the
-- argument, then function f to the result of that.
operate2 f g n = f (g n)

double n = 2 * n
negate n = -n

operate2 negate double 4 -- doubles the number 4 and then negates it
operate2 double negate 4 -- negates the number 4 and then doubles it
```

This is the equivalent in Python:
```python
def operate(f, a, b, c):
    return f(a, b, c)

def add(a, b, c):
    return a + b + c

def mul(a, b, c):
    return a * b * c

operate(add, 2, 3, 4)
operate(mul, 2, 3, 4)
```

```python
def operate2(f, g, n):
    return f(g(n))

def double(n):
    return 2 * n

def negate(n):
    return -n

operate2(double, negate, 4)
operate2(negate, double, 4)
```

This idea is another tool to generalize code. If we understand that the
structure of a function takes in `n` arguments and can perform behaviors `x`,
`y`, and `z`, we can simply delegate the logic to the input function.

### (3) Function returned as an output of a function

We can pass in functions into functions, so one would expect to also return a
function from a function. Here is a contrived example in Haskell to illustrate
the point:
```haskell
-- Return the add function implemented earlier if the input is True; otherwise
-- return the multiply function.
addIfTrue boolValue
  | boolValue = add
  | otherwise = mul

(addIfTrue True) 2 3 4  -- addIfTrue returns add, then we evaluate add 2 3 4
(addIfTrue False) 2 3 4 -- addIfTrue returns mul, then we evaluate add 2 3 4
```

A Python example demonstrating the same concept:
```python
def excitedMessage(name):
    print(f"Hi {name}, I'm doing great!")

def sadMessage(name):
    print(f"I feel a bit blue today, {name}.")

def neutralMessage(name):
    print(f"How are you doing, {name}?")

def determineMessage(mood):
    if mood == 'happy':
        return excitedMessage
    elif mood == 'sad':
        return sadMessage
    else:
        return neutralMessage

currentMood = 'happy'
greetFunction = determineMessage(currentMood)  # This doesn't invoke anything yet
greetFunction('Brendon')  # Prints "Hi Brendon, I'm doing great!"
```

This is another a comically artificial usage of returning a function, but it
does demonstrate a point. You might be asking: why not just print the message
directly? Therein lies a key benefit - when we are able to return functions, we
are effectively _delaying the function application_. We are able to hold
functions in memory (via rule 1 of first-class functions) when we don't have all
of the necessary information to compute it.

Being able to return functions also helps us determine what function is
appropriate to use at a given time depending on the context. This usage reminds
me of the [factory pattern](https://en.wikipedia.org/wiki/Factory_method_pattern)
seen in object-oriented programming, where you ask a factory for a type of class
that implements a specific interface and it gives it to you. Here, we're calling
out to a function that returns another function which matches the type signature
that we expect.

## In summary

The point of these three conditions for a function to be considered a
[first-class citizen](https://en.wikipedia.org/wiki/First-class_citizen) in a
given programming language is to drive home the fact that they can be treated
just like objects. Thinking about code in this manner can ultimately encourage
better code reuse, modularize functions, create higher levels of abstraction,
and help enforce separation of concerns.

My first exposure to first-class functions was: _"Wait you can do that?"_ The
first two programming languages I ever learned were Java and C++, and many of
the ideas explored today are completely inconceivable in those languages, at
least not without some extra work. I was forced to see functions as data when
working purely in the functional programming paradigm, but I'm glad to see it
appear in many imperative langauges. I hope seeing functions this way can add
additional perspective if you didn't have exposure to these concepts already, as
it once did for me.
