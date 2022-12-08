---
layout: post
title: "Currying and Partial Application"
tags: [Functional Programming, Haskell, Python]
---

![curry](../images/2018-09-15-curry.png)

If you have read some of the earlier posts on this site, we saw examples of code
in Haskell. What was up with those arrows in the function type declaration? If
you recall, this is how we declared a function that takes in two integers as
input and returns an integer as output:
```haskell
addTwoNums :: Integer -> Integer -> Integer
addTwoNums a b = a + b
```

You would think that type declaration for such a function might look something
like this instead:
```haskell
addTwoNums :: Integer Integer --> Integer
```
<!--more-->

I'm going to load up this program in
[GHCi](https://downloads.haskell.org/~ghc/latest/docs/html/users_guide/ghci.html),
the Haskell interpreter, to see how it defines the function:
```
$ :t addTwoNums
addTwoNums :: Integer -> Integer -> Integer
```

Good, this confirms that the type signature of the `addTwoNums` function matches
the one we gave it. For the sake of experimentation, what happens if we provide
it a single input? I.e. we give the `addTwoNums` function just one of the two
expected Integer inputs:
```
$ :t addTwoNums 5
addTwoNums 5 :: Integer -> Integer
```

I'm surprised it didn't blow up on us! In Java, if you had a method like:
```java
public static int addTwoNums(int a, int, b) {
    return a + b;
}
```

And you only gave it one input, `addTwoNums(5)`, you would get an error - yet in Haskell we didn't. So what is the meaning of
`addTwoNums 5 :: Integer -> Integer`?

Based off the type signature alone, `addTwoNums 5` seems like a regular function
that takes in an Integer and returns an Integer. Let's test this theory by
invoking the function calls this way:
```haskell
-- Evaluate addTwoNums 5 first, then pass in 3
(addTwoNums 5) 3 -- returns 8
```

So our hypothesis is correct, and thus follows the beauty of function
application in Haskell. Our original `addTwoNums` function is one that takes in
a single Integer and outputs a _function that takes in an Integer and outputs
an Integer_. So when we invoke `addTwoNums 5 3`, we first get a new function that
just adds 5 to its integer input, and we pass in 3 to that new function to get
8.

This is another way of looking at it:
```haskell
addTwoNums :: Integer -> Integer -> Integer
addTwoNums a b = a + b

alwaysAdd5 :: Integer -> Integer
alwaysAdd5 = addTwoNums 5

alwaysAdd5 6
-- returns 11, since we passed it into a function that always adds 5 to its input
```

This idea is known as [_currying_](https://en.wikipedia.org/wiki/Currying). It
is the process of converting a function that takes multiple arguments into a
sequence of functions that each take a single argument. So again,
```haskell
-- If we defined the following function,
addFourNums :: Integer -> Integer -> Integer -> Integer -> Integer
addFourNums a b c d = a + b + c + d

-- and passed in four Integers,
addFourNums 5 6 7 8

-- what is actually happening is that:
-- 5 is consumed and a function that takes in 3 arguments is returned
-- 6 is consumed and a function that takes in 2 arguments is returned
-- 7 is consumed and a function that takes in 1 argument is returned
-- 8 is consumed and a function that takes in 0 arguments is returned
```

That's right, if a type signature `Integer -> Integer` means that a function
accepts one input and returns one output, then `Integer` represents a function
that takes in zero inputs and returns one output.

So this isn't a variable named pi with value 3.14:
```haskell
pi = 3.14
```
It's actually a _function_ pi that takes zero inputs and returns one output:
```haskell
pi :: Double
pi = 3.14
```

Mind blown 🤯.

### Implementing currying in Python

Python doesn't support currying by default, but since its functions are
first-class, we can implement a similar functionality. What we ultimately want
is to evaluate functions of the form `f(a)(b)(c)(d)` just like we would for
`f(a, b, c, d)`:
```python
def addFourNums(a):
    def addThreeNums(b):
        def addTwoNums(c):
            def evaluate(d):
                return a + b + c + d
            return evaluate
        return addTwoNums
    return addThreeNums

addFourNums(1)(2)(3)(4)
```

This was made possible through the use of
[closures](https://en.wikipedia.org/wiki/Closure_(computer_programming)), which
basically means that a nested function has access to free variables in the outer
scope and is returned by its enclosing function.

Here is a super elegant way to do the same thing using arrow functions in
Javascript (ES6):
```javascript
let addFourNums = a => b => c => d => a + b + c + d;
addFourNums(1)(2)(3)(4);
```

## Partial application

Partial application is a related but distinct concept from currying. Again,
currying is the process of breaking down a function that takes in `n` arguments
into a series of functions that must take in one parameter at a time; it
ultimately returns the same output as passing of the inputs all at once. Partial
application is simply accepting a subset of the expected arguments of a function
and returning a function; we can also partially apply more than one parameter to
a function.

This is an example of a partially applied function:
```python
def addFourNums(a, b, c, d) {
    return a + b + c + d
}

def partiallyApply(f, a, b):
    def evaluate(c, d):
        return f(a, b, c, d)
    return evaluate

f = partiallyApply(addFourNums, 1, 2)
# ... much later in the code ...
f(3, 4)
```

We partially applied inputs `a`, and `b` to the `addFourNums` function. This
allowed us to effectively _delay its function application_. Sometimes we don't
have all of the information necessary to compute a function eagerly and on the
spot, so this allows us to do so _lazily_. It also allows us to save off this
partially applied function and reuse it in cases where many of the parameters
would stay unchanged, in contrast to passing in the same invariant parameters
over and over again.

## Function composition

In the first blog post I brought up how `g(f(x))` was equivalent to
`(g ∘ f)(x)`, just the way you learned it in your math class. Using what we have
learned, we can implement the function composition operator in Python:
```python
def compose(g, f):
    def h(x):
        return g(f(x))
    return h

def f(x):
    return 2 * x + 1

def g(x):
    return -x

h = compose(g, f)
h(5)  # returns -11
```

## Conclusion

A lot of the discussion today has been in the programming-theory land, but these
concepts can actually be employed in our day-to-day programming. Currying is a
bit less practical, but we at least saw how partial function application can be
used to aid code maintainability. The exercise we did for implementing the
function composition operator will translate over into our discussion using
Python decorators, which is a neat way of processing and tranforming functions.
