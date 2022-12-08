---
layout: post
title: "Yet Another Guide to Python Decorators"
date: 2018-04-07
tags: programming python
---

To this day, I find functional programming to be slick.
I used Python to write an interpreter back in college, and fell in love with some of the paradigms of functional programming ever since.
While languages like Haskell and OCaml are more suited to parse grammars and traverse abstract syntax trees, Python is able to hold its own in this arena.
This is because functions in Python are first-class, meaning that functions can be:

1. assigned to variables and/or stored in data structures
2. passed in as parameters to another function
3. return values of another function

<!--more-->

We won't be discussing how write an interpreter in this guide, but we will be leveraging first-class functions to use Python decorators, which is just a language construct for a function to modify another function in an accessible and modular fashion.
If you're crystal clear on the semantics of first-class and higher-order functions, you can skip to the [section where we actually discuss Python decorators](#python-decorators).

**Note**:
We will be using Python 3 in this guide.
Also, the snippets of Python code used in the examples below are not isolated and instead will build off of each other as we progress.
The full python file can be downloaded [here](/resources/code/demo-python-decorators.py).
If you wish to tinker with the concepts in this guide as you read along, load it into the Python interpreter by invoking:
```
python -i .../demo-python-decorators.py
```

Minor note:
The footnotes are primarily reflections on revisiting first-class and higher-order functions in Python after using a language like Haskell.
They illustrate how functional programming concepts are much more elegant in a truly functional programming language.
The footnotes are more for my personal sake; it's me raving about how bloody awesome it is to see different language paradigms tackle problems in more expressive ways.




## Before we begin...
If you were taught programming in a conventional manner[^1], you were taught that there are *objects* and there are *functions*.
At least for me, there was a heavily implied distinction between *objects*, which are tangible are representations of data, and *functions*, which act as fleeting and ephemeral actions on such data.

In English, you could represent nouns as objects, and functions as verbs.
In this metaphor, it's rather nonsensical to put an action or verb into a box or container like you could for a noun.
Therefore it makes no sense to assign the act of doing something into a variable or object to later do something with.
After all, how would you verb a verb?
Thus functions were to always act exclusively on objects and were *not* objects themselves, or so you were led to believe...



## 1. Functions as objects
In Python, functions are treated just the same as objects; **anything you can do with an object, you can do with a function**.

Here's an example where we assign a function to a variable, much like how we would assign a number or an object to a variable, and proceed to use it as a traditional function:
```python
def addTwoNums(x, y):
  return x + y

justAnotherVariable = addTwoNums
justAnotherVariable(3, 3) # Returns 6
```

If functions are treated just like objects, can we have a list of functions?
How about a (function, function) tuple?
What about a function dictionary?
I'll give you five bucks if you can figure out how to use this list in a meaningful way:
```python
wat = justAnotherVariable
wonkyList = [1, 2.2, 'c', wat, [wat], (wat, wat), {wat: wat}]
```

To use functions as objects, we don't even need to assign `addTwoNums` to an intermediate variable; we can use functions as objects directly:
```python
def subtractTwoNums(x, y):
  return x - y

def multiplyTwoNums(x, y):
  return x * y

def divideTwoNums(x, y):
  return x / y

operations = [addTwoNums, subtractTwoNums, multiplyTwoNums, divideTwoNums]
for f in operations:
  print(f(3, 3)) # Prints 6, 9, 0, 1.0
```

To reiterate the key point: anything you can do with an object, you can do with a function.



## 2. Functions as parameters
A consequence of treating functions like objects is that we can pass functions as arguments to another function.
In Python, the parameters in the function definition `def foo(param1, param2)` can either be objects or functions.

Let's consider expanding our `addTwoNums/subtractTwoNums/...` functions to accept three arguments.
We'll evaluate the elements from left to right, i.e. `((x + y) + z)`, `((x - y) - z)`, and so on:
```python
def addThreeNums(x, y, z):
  return addTwoNums(addTwoNums(x, y), z)

def subtractThreeNums(x, y, z):
  return subtractTwoNums(subtractTwoNums(x, y), z)

def multiplyThreeNums(x, y, z):
  return multiplyTwoNums(multiplyTwoNums(x, y), z)

def divideThreeNums(x, y, z):
  return divideTwoNums(divideTwoNums(x, y), z)
```
So far so good, nothing conceptually new has happened; we're merely applying `addTwoNums/subtractTwoNums/...` two times.
However, I do think I'm getting carpal tunnel syndrome from typing all that out.
Surely there's a way to generalize what essentially looks like the same function?

If we look closely, we can see the same structure hiding in all four of the functions: `f(f(x, y), z)`.
How about we take in a function as a parameter to offload some of the work?
```python
def operateOnThreeNums(operateOnTwoNums, x, y, z):
  return operateOnTwoNums(operateOnTwoNums(x, y), z)

operateOnThreeNums(addTwoNums, 8, 4, 2)      # Returns 14
operateOnThreeNums(subtractTwoNums, 8, 4, 2) # Returns 2
operateOnThreeNums(multiplyTwoNums, 8, 4, 2) # Returns 64
operateOnThreeNums(divideTwoNums, 8, 4, 2)   # Returns 1.0
```
We were able to take in a function that acts on two numbers as a parameter to `operateOnThreeNums`, and were able to apply that generic function twice.

How about operating on any number of arguments?
The `addAnyNums/subtractAnyNums/...` functions would all have the same structure: `f(f(f(f(...), x), y), z)`, which we could implement like so:
```python
def operateOnAnyNums(f, *nums):
  if len(nums) == 1:
    return nums[0]
  return f(operateOnAnyNums(f, *nums[:-1]), nums[-1])

operateOnAnyNums(addTwoNums, 2, 2, 2, 2, 2)      # Returns 10
operateOnAnyNums(subtractTwoNums, 2, 2, 2, 2, 2) # Returns -6
operateOnAnyNums(multiplyTwoNums, 2, 2, 2, 2, 2) # Returns 32
operateOnAnyNums(divideTwoNums, 2, 2, 2, 2, 2)   # Returns 0.125
```
By accepting a function argument to our function, we can abstract out some of the work we do in repeating ourselves.[^2]

A map is a commonly used function in many programming languages that takes in a function that acts on single element, applies it to every element in list, and returns a new list (or some similar form of list, like `map object` in Python).
Traditionally, we might apply a function over each element via a loop:
```python
def collatzFunction(n):
  if n % 2 == 0:
    return n // 2
  else:
    return 3 * n + 1

numList = [0, 1, 2, 3, 4, 5]
newList = []

for num in numList:
  newList.append(collatzFunction(num))
# newList is [0, 4, 1, 10, 2, 16]
```
We can just as easily use `map` to do that for us:
```python
list(map(collatzFunction, numList)) # Returns a new list [0, 4, 1, 10, 2, 16]
```

The ability for functions to receive functions as parameters is a powerful tool that allows functions to abstract out some of its work to another function.



## 3. Functions as return values
Another consequence of treating functions like objects is that we can also use them as return values of a function.
In a Python function, the statement `return foo` may very well return a function instead of an object.

Here is a function that returns a function:
```python
def createErrorMessageFunction(message):
  print("Defining your function with message: " + message)
  def errorMessageFunction():
    print("ERROR: " + message + "!")
  print("Finished defining your function, and now returning it")
  return errorMessageFunction

outOfBounds = createErrorMessageFunction("Array out of bounds")
fileNotFound = createErrorMessageFunction("File not found")

outOfBounds()
fileNotFound()

# Output:
# Defining your function with message: Array out of bounds
# Finished defining your function, and now returning it
# Defining your function with message: File not found
# Finished defining your function, and now returning it
# ERROR: Array out of bounds!
# ERROR: File not found!
```
Notice how the inner function has access to the variables in its outer scope.
Variables from the outer scope are bound to the inner function once the inner function is returned.
This concept is called a *closure* in programming. Closures allow access those bound variables, even when the function is invoked outside the scope it was defined in.

A closure is a formal term for saying that our inner `errorMessageFunction` has access to the variables in its outer scope, `createErrorMessageFunction`, and is able to use those variables even when it's no longer in the scope of `createErrorMessageFunction`.
This idea appears in other programming languages whenever a function is defined inside another function.
Closures are pretty implicit when they're being used; just remember that they exist.

Back to our example: we can see that using `createErrorMessageFunction` is a lot better than copying and pasting `"ERROR: ...!"` in the code over and over.
If we wanted to change the message, there's only one place where we would have to do so.
We can also see that it's better than formally defining a print function for each error messages (e.g. `def outOfBounds()` and `def fileNotFound()`), since it reduces the repetition of boilerplate code.

This is somewhat of a superficial example, but much like the ability to take in functions as a function parameter, the ability to return a function in a function is yet another tool that helps us with abstraction.



## A detour into higher-order functions
Functions that satisfy either or both properties 2 and 3 of first-class functions are known as higher-order functions in mathematics.[^3]
So far, we've explored the three properties of first-class functions in isolated contexts.
We haven't talked about a function that takes in a function *and* returns a function.

If you've taken calculus, you've already been been exposed to a higher-order function that satisfies both properties.
In function differentiation, $$\frac{d}{dx}$$ is a function that takes in a function and returns its derivative (which is just another function).
Combining both properties of higher-order functions permits us to do even more cool things.

Hey remember function compositions from math classes gone by?

$$f(x) = x + 2$$

$$g(x) = x^2$$

$$(f \circ g)(x) = f(g(x)) = x^2 + 2$$

$$(g \circ f)(x) = g(f(x)) = (x + 2)^2$$

The nesting of $$f$$ and $$g$$ resembles what we did when we were able to take in functions as objects.
Furthermore, $$(f \circ g)$$ looks to be just another function that happened to be combined by $$f$$ and $$g$$; we might as well have called it an entirely different function $$h$$.
Let's implement these mathematical functions into their Python equivalents:
```python
def f(x):
  return x + 2

def g(x):
  return x**2

def dot(f1, f2):
  def composedFunction(x):
    return f1(f2(x))
  return composedFunction

dot(f, g)     # Returns <function ... at ...>, a function like we expected
dot(f, g)(2)  # Returns 6
dot(g, f)(2)  # Returns 16

h = dot(f, g)
h(2)          # Returns 6
```
It's a bit of a stretch, but `dot(f, g)(x)` looks somewhat like $$(f \circ g)(x)$$, neat![^4]

With functions being able to receive and return a function, we could have also implemented `addTwoNums` this way:
```python
def addTwoNumsRevisited(x):
  def returnResult(y):
    return x + y
  return returnResult

addTwoNumsRevisited(1)(2) # Returns 3
```
`addTwoNumsRevisited(1)` returns a function that adds 1 to any number. Then we call that function with argument `2`, giving us our result of `3`.

Similarly, we could have implemented `addThreeNums` like so:
```python
def addThreeNumsRevisited(x):
  def addTwoNumsRevisited(y):
    def returnResult(z):
      return x + y + z
    return returnResult
  return addTwoNumsRevisited

addThreeNumsRevisited(1)(2)(3) # Returns 6
```

Higher-order functions pop up everywhere in functional programming.
Although Python is nowhere close to being thought of as a proper functional programming language, its ability to use some functional programming concepts combined with its object-oriented features packs a powerful punch.
Having covered the basics of first-class and higher-order functions, we can finally move on to see how they're used in Python decorators.



## Python decorators
Decorators in Python is a language construct that allows us to do some of the demonstrations we've done with first-class functions above in a clean and accessible way.
The gist of decorators is to modify a predefined function by passing it into one or more functions (decorators) to extend its functionality.
The general structure of decorators and the decorator syntax in Python is such that:
```python
def myFunction():
  ...
myFunction = myDecorator(myFunction)
```
is roughly equivalent to:
```python
@myDecorator
def myFunction():
  ...
```

From a cursory glance at `myDecorator` above, we might posit that it is a function that **takes in a function ([2](#2-functions-as-parameters))**, and **returns a function ([3](#3-functions-as-return-values))**.
Its return value is then re**assigned ([1](#1-functions-as-objects))** to the original function that was passed in.

Let's implement this concept as a working function:
```python
def simpleFunction():
  return "We're inside simpleFunction()!"

def simpleDecorator(functionToModify):
  def functionToReturn():
    return functionToModify() + " Now augmenting the function >:D"
  return functionToReturn

simpleFunction = simpleDecorator(simpleFunction)
simpleFunction() # Prints "We're inside simpleFunction()! Now augmenting the function >:D"
```

From what we know about first-class functions, this is still familiar territory.
Although, I don't like that we had to reassign the output of `simpleDecorator(simpleFunction)` back into itself, which is where the Python decorator syntax brings in concision:
```python
@simpleDecorator
def decoratedFunction():
  return "We're inside decoratedFunction()!"

# This function is unchanged from the previous snippet
def simpleDecorator(functionToModify):
  def functionToReturn():
    return functionToModify() + " Now augmenting the function >:D"
  return functionToReturn

decoratedFunction() # Prints "We're inside decoratedFunction()! Now augmenting the function >:D"
```
Using Python decorators allowed us to skip doing `simpleFunction = simpleDecorator(simpleFunction)`, since putting `@simpleDecorator` on top of the function we're modifying did it for us.
Any decorator function using the `@decorator` syntax takes in a single function as its only argument and returns a function.

But if we want a decorator to take in more than the default single function parameter, we need to wrap them in another function like so:
```python
@addSource("Wayne Gretzky")
def generateQuote(quote):
  return '"' + quote + '"'

def addSource(source): # This function wraps the actual decorator below
  def decoratorFunction(getQuote):
    def newQuote(quote):
      return getQuote(quote) + " - " + source
    return newQuote
  return decoratorFunction

generateQuote("You miss 100 percent of the shots you don't take.")
# Returns '"You miss 100 percent of the shots you don\'t take." - Wayne Gretzky'
```
We're first evaluating `addSource("Wayne Gretzky")`, which returns the `decoratorFunction` function, which then gets evaluated with the `@` syntax for the `generateQuote` function.

Since decorators take in and return only one function, we can stack multiple decorators on a function:
```python
@addSource("The Office (US)")
@addSource("Michael Scott")
@addSource("Wayne Gretzky")
def generateQuote(quote):
  return '"' + quote + '"'

def addSource(source):
  def decoratorFunction(getQuote):
    def newQuote(quote):
      return getQuote(quote) + " - " + source
    return newQuote
  return decoratorFunction

generateQuote("You miss 100 percent of the shots you don't take.")
# Returns '"You miss 100 percent of the shots you don\'t take." - Wayne Gretzky - Michael Scott - The Office (US)'
```
The `@` syntax binds bottom up, meaning that the original function is fed upwards into each successive decorator.

Note that without the `@` syntax, we would have to concoct this horror to do what we did above:
```python
# One liner:
generateQuote = addSource("The Office (US)")(addSource("Michael Scott")(addSource("Wayne Gretzky")(generateQuote)))

# For readability:
generateQuote = addSource("The Office (US)")(
                  addSource("Michael Scott")(
                    addSource("Wayne Gretzky")(
                      generateQuote)))
```
In a sense, we were able to "unwind" the nested "function inside function" structure by using decorators.[^5]

How about another math example?
We can use decorators to do linear transformations on points from one vector space onto another:
```python
def translatePoint(dx, dy):
  def decorator(getPoint):
    def newPoint(point):
      return (getPoint(point)[0] + dx, getPoint(point)[1] + dy)
    return newPoint
  return decorator

def reflectPoint(axis):
  def decorator(getPoint):
    def newPoint(point):
      if axis == 'x':
        return (getPoint(point)[0], -getPoint(point)[1])
      elif axis == 'y':
        return (-getPoint(point)[0], getPoint(point)[1])
    return newPoint
  return decorator

def scalePoint(x, y):
  def decorator(getPoint):
    def newPoint(point):
      return (getPoint(point)[0] * x, getPoint(point)[1] * y)
    return newPoint
  return decorator

@reflectPoint('y')
@scalePoint(2, 2)
@reflectPoint('x')
@translatePoint(2, 2)
def transformPoint(point):
  return (point[0], point[1])

transformPoint((0, 0)) # Returns (-4, -4)
```
In visual form:

![transform-point.gif](/resources/images/transform-point.gif)

To hammer the point, this is how `transformPoint` might look like without the `@` syntax:
```python
# One liner:
transformPoint = reflectPoint('y')(scalePoint(2, 2)(reflectPoint('x')(translatePoint(2, 2)(transformPoint))))

# For readability:
transformPoint = reflectPoint('y')(
                   scalePoint(2, 2)(
                     reflectPoint('x')(
                       translatePoint(2, 2)(
                         transformPoint))))
```

To summarize, Python decorators are a great way to modify the functionality of an existing function while keeping this mechanism of doing so well modularized.
They fully utilize the benefits of first-class and higher-order functions, but in a way that avoids the mess that nested function calls bring.

While some of the examples in this guide were a bit contrived for the sake of demonstration, I hope you learned something useful about first-class functions and Python decorators.
These programming paradigms carry over from language to language, so it's always nice to have more tools in the toolkit.

As an exercise, think about how you might invoke a decorator's parameters with variables, or you might conditionally call a decorator in the first place.
*Hint*: Imagine a function that takes in a number and returns that same number if it's even, or does something with it if it's odd.

For further reading, take a gander at the original [motivations of introducing decorators into the Python language](https://www.python.org/dev/peps/pep-0318/).



## Notes and errata:
[^1]:
    Conventional, meaning that you either started with Java or Python in a purely imperical approach.
    [A notorious introductory programming text once used at MIT](https://mitpress.mit.edu/sicp/full-text/book/book-Z-H-4.html) starts discussing higher-order functions as early as chapter one.
    Looking back on my own education, it may have been helpful to learn about functions as data early on, instead of later unlearning the assumption that only objects are data.

[^2]:
    The funny thing is, we repeated ourselves three times in our earlier exercise of defining our initial `addTwoNums/subtractTwoNums/...` functions.
    Just like how we saw a common structure for `addThreeNums/subtractThreeNums/...` and `addAnyNums/subtractAnyNums/...`, we can observe the same generic structure for our 2 parameter operator functions being `f(x, y)`.

    Ideally, we can take this function:
    ```python
    def addTwoNums(x, y):
      return x + y
    ```
    and do this
    ```python
    def operateTwoNums(f, x, y):
      return f(x, y)
    ```

    This would work if the function calls `+(1, 1)` and `-(1, 1)` syntactically made sense in the same way `f(1, 1)` does.
    In a language like Haskell, an expression like this *is* totally valid:
    ```haskell
    (+) 8 4 -- Returns 12
    (-) 8 4 -- Returns 4
    (*) 8 4 -- Returns 32
    (/) 8 4 -- Returns 2.0
    ```

    We can pass the operators `(+)`, `(-)`, `(*)`, `(/)`, just the same as functions, thereby allowing us to skip our intermediate step of defining `addTwoNums/subtractTwoNums/...` that we had to do in Python. Instead, we can jump straight ahead to make these functions directly:
    ```haskell
    operateThreeNums f x y z = f (f x y) z
    operateNumList f numList = foldl1 f numList
    ```
    A function that operates on list elements from left to right to converge on a single value is known as a `foldl` in Haskell.

    We can clean up `operateNumList` even further by informally "cancelling out" the function and list arguments from both sides of the "equation":
    ```haskell
    operateNumList = foldl1
    ```
    Which means that our function `operateNumList` *is* the `foldl` function that we just described.
    To get deeper into higher-order-ism and functional programming in general, [learn more about how cool Haskell is!](https://en.wikibooks.org/wiki/Haskell)

[^3]:
    An important semantic distinction to make is that first-class functions **are not** higher-order functions.
    Higher-order-ism is a mathematical property that can be divorced from programming, while the idea of first-class functions relates to how functions are implemented in a given programming language.
    If a language supports first-class functions, it follows that it supports higher-order functions as well.

[^4]:
    $$(f \circ g)(x)$$ is nearly identical to the built-in syntax used in Haskell for function compositions:
    ```haskell
    f x = x + 2
    g x = x * x

    f . g     -- Returns a function that takes in a number
    (f . g) 2 -- Returns 6
    (g . f) 2 -- Return 16
    ```

[^5]:
    Decomposing nested structures into chained operations is fascinating, and it pops up in other contexts in programming.
    If you've handled multiple asynchronous events in Javascript, you may be familiar with callback hell:
    ```javascript
    doSomething1(function() {
      doSomething2(function() {
        doSomething3(function() {
          doSomething4(function() {
            doSomething5(function() {
              console.log("Are you not entertained?");
            });
          });
        });
      });
    });
    ```

    We can turn that monstrosity into something more palatable using Javascript promises:
    ```javascript
    doSomething1().then(function() {
      return doSomething2();
    }).then(function() {
      return doSomething3();
    }).then(function() {
      return doSomething4();
    }).then(function() {
      return doSomething5();
    }).then(function() {
      console.log("Are you not entertained?");
    })
    ```
    Beautiful.

    Read more about [chaining promises](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Using_promises#Chaining), or learn about how Haskell is able to [generalize nested structures for a wider gamut of abstractions using monads](https://philipnilsson.github.io/Badness10k/escaping-hell-with-monads/)
