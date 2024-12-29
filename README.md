# mypymud

I need to get my Python programming skills back up to speed, so I'm writing
an old school text MUD in Python

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

