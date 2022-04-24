# Turtle Graphics

* Goal: to develop a simple simulation with Turtle Graphics
* The use of 
  * functions and methods
  * parameters, abstractions
  * simulation to explore behavior
* Using JES (MediaComputation) version 6.0  https://github.com/gatech-csl/jes/releases


## Example 1: Worlds and Turtles

```html
<!-- return values... -->
<!-- functions return values -->
def newTurtle():
  w = makeWorld(500, 500)
  t = makeTurtle(w)
  return t
```
* now  t = newTurtles()  creates a world, turtle and returns it
* w = makeWorld(500, 500) creates a world with 500x500 space large

### Moving turtles

```html
<!-- Moving turtles -->
>>> t = newTurtle()
>>> t.forward()
>>> t.setBodyColor(red)
>>> t.setColor(red)
>>> t.turnRight()
>>> t.forward()
>>> t.setPenWidth(4)
>>> t.forward()
```
* forward(t,d) - move t forward d units, default is 100
* turnRight(t) - turn t 90 degrees to the right

* functions also available as methods off the turtle itself
* forward(t) - t.forward()
