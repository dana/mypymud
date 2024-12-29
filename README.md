# mypymud

I need to get my Python programming skills back up to speed, so I'm writing
an old school text MUD in Python

# Classes

## MUDNetwork

Takes an optional dictionary of options, including:

### port

Which TCP port to bind to.  Defaults to 5000.

### callback

This is a code reference that's called by default ten times a second
Defaults to nothing

### callback_timer

How many milliseconds between calls to callback.
Defaults to 100

## methods

### bind

### loop

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

