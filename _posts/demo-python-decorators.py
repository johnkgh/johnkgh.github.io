def addTwoNums(x, y):
  return x + y

justAnotherVariable = addTwoNums
justAnotherVariable(3, 3) # Returns 6

wat = justAnotherVariable
wonkyList = [1, 2.2, 'c', wat, [wat], (wat, wat), {wat: wat}]

def subtractTwoNums(x, y):
  return x - y

def multiplyTwoNums(x, y):
  return x * y

def divideTwoNums(x, y):
  return x / y

operations = [addTwoNums, subtractTwoNums, multiplyTwoNums, divideTwoNums]
for f in operations:
  print(f(3, 3)) # Prints 6, 9, 0, 1.0

def addThreeNums(x, y, z):
  return addTwoNums(addTwoNums(x, y), z)

def subtractThreeNums(x, y, z):
  return subtractTwoNums(subtractTwoNums(x, y), z)

def multiplyThreeNums(x, y, z):
  return multiplyTwoNums(multiplyTwoNums(x, y), z)

def divideThreeNums(x, y, z):
  return divideTwoNums(divideTwoNums(x, y), z)

def operateOnThreeNums(operateOnTwoNums, x, y, z):
  return operateOnTwoNums(operateOnTwoNums(x, y), z)

operateOnThreeNums(addTwoNums, 8, 4, 2)      # Returns 14
operateOnThreeNums(subtractTwoNums, 8, 4, 2) # Returns 2
operateOnThreeNums(multiplyTwoNums, 8, 4, 2) # Returns 64
operateOnThreeNums(divideTwoNums, 8, 4, 2)   # Returns 1.0

def operateOnAnyNums(f, *nums):
  if len(nums) == 1:
    return nums[0]
  return f(operateOnAnyNums(f, *nums[:-1]), nums[-1])

operateOnAnyNums(addTwoNums, 2, 2, 2, 2, 2)      # Returns 10
operateOnAnyNums(subtractTwoNums, 2, 2, 2, 2, 2) # Returns -6
operateOnAnyNums(multiplyTwoNums, 2, 2, 2, 2, 2) # Returns 32
operateOnAnyNums(divideTwoNums, 2, 2, 2, 2, 2)   # Returns 0.125

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

list(map(collatzFunction, numList)) # Returns a new list [0, 4, 1, 10, 2, 16]

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

def addTwoNumsRevisited(x):
  def returnResult(y):
    return x + y
  return returnResult

addTwoNumsRevisited(1)(2) # Returns 3

def addThreeNumsRevisited(x):
  def addTwoNumsRevisited(y):
    def returnResult(z):
      return x + y + z
    return returnResult
  return addTwoNumsRevisited

addThreeNumsRevisited(1)(2)(3) # Returns 6

def simpleFunction():
  return "We're inside simpleFunction()!"

def simpleDecorator(functionToModify):
  def functionToReturn():
    return functionToModify() + " Now augmenting the function >:D"
  return functionToReturn

simpleFunction = simpleDecorator(simpleFunction)
simpleFunction() # Prints "We're inside simpleFunction()! Now augmenting the function >:D"

@simpleDecorator
def decoratedFunction():
  return "We're inside decoratedFunction()!"

decoratedFunction() # Prints "We're inside decoratedFunction()! Now augmenting the function >:D"

def addSource(source): # This function wraps the actual decorator below
  def decoratorFunction(getQuote):
    def newQuote(quote):
      return getQuote(quote) + " - " + source
    return newQuote
  return decoratorFunction

@addSource("The Office (US)")
@addSource("Michael Scott")
@addSource("Wayne Gretzky")
def generateQuote(quote):
  return '"' + quote + '"'

generateQuote("You miss 100 percent of the shots you don't take.")
# Returns '"You miss 100 percent of the shots you don\'t take." - Wayne Gretzky - Michael Scott - The Office (US)'

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
