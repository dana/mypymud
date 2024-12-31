# mypymud

I need to get my Python programming skills back up to speed, so I'm writing
an old school text MUD in Python

# Classes

## Characters
A character is an entity that is or acts alive and can do things independently.
Examples include players, rabbits, an evil skeleton.

### Attributes

- name - The short name of the chracter, is not unique
- description - Longer textual description of the character

### Methods

## Players
Some Characters are Players.  A Player is a human that logs in and controls
one or more Characters.



## MUDNetwork

Handles low level networking, necessary to communicate with players.

### Dictionary of Options

- port - Which TCP port to bind to.  Defaults to 5000.

- callback - This is a code reference that's called by default ten times a second, defaults to nothing

- callback_timer - How many milliseconds between calls to callback.  Defaults to 100

### methods

- bind

- loop

# NOTES

## Basic Structure

## flow of thoughts

Abstracting out the networking stuff.

We're basically going to be looping on network connection handling,
except for some kind of regular ticks that allow other logic to happen.

I guess we need some kind of god-object that represents all of the
networking stuff.

After it is instantiated a method binds and listens to a port, and another
method runs the loop.  

class MUDNetwork
methods:


