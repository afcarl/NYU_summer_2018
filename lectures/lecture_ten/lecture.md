# Lecture 10 - Web Development Introduction

Today we are going to begin our journey into web development.

In order to do that, we'll need to cover one concept first though - the decorator.

## Decorators

A decorator is a function that takes as input a function and then does something either to the function's input, output or both.

We can think of a decorator as a transformation on a function.  In mathematics, we'd call this a functor.

## Example

```
def decorator(f):
   def internal(*args, **kwargs):
       return f(args)+5
   return internal

@decorator
def func(x, y=0):
    return x

func(5)
```

## The client and server model - nouns and verbs of the internet

When developing applications on the internet, there is always this notion of your code going between a connection.  We can think of this as connection oriented programming, although no one calls it that.  So web development is interested with how programs run, that are designed to pass data from piece of code to piece of code.

It is the central concern, in all web development.

So what's the best model for dealing with passing information via a communication channel from piece of code to piece of code?  Well usually the best model is the simplest that is sufficiently complex to solve the problem.  And this turns out to be a model that considers a single connection between two entities that can send messages.

From this simple model, of course we can extend to many pieces of code that exchange information.  But all of it relies on understanding this simple model of code communicating with other code.

Before we answer the question of how we do this communication, let's spend a little time understanding why it communicates.  This is done for one simple reason: So that different pieces of code can live on different machines and effectively so different machines can talk to each other.

Thus our system of communication is about understanding how to make different computers talk to each other, perhaps without having to consider all of the necessary abstractions that make this communication work.

Thus we are now ready to talk about how they communicate:

This is done via the Client and Server model.

**Definition** _Client_ := a client is the part of the web service that renders content visually to an end user.  The expectation is lots of individuals will touch the client, either through a graphical user interface, or through api code.

**Definition** _Server_ := a server is the part of the web service that handles the sending of and receiving of data.  Both from the client as well as other services.  It is responsible for making connections and ensuring they are fast.  Most intensive processing happens on the server side of the code.


Most web applications are _server_ centric, because the web is built to be server centric.  This means that all methods associated with the web are made with respect to the server.

At a very basic level web based code or communication is about communicating between two pieces of code - code that lives on your machine and code that lives on someone elses machine.  And there are basic verbs associated with this communication.

The most common verbs are:

* GET
* POST
* PUT
* DELETE

We'll in fact, only focus on two of these:

* GET
* POST

Both of these verbs are used in a communication protocol called `HTTP` and `HTTPS`.  The reason `HTTP` comes in two flavors, is because sometimes the communication is encrypted, like with `HTTPS` and some times its not.  If it's not, then its called `HTTP`.

The way that a protocol is specified on the web is at the start of a `URI` or uniform resource identifier.  We also sometimes called specific kinds of `URI`s, `URL`s.

So when we go to a website like:

[https://www.google.com](https://www.google.com)

What we are really doing is having our browser point at the content, via the `URI`, which resolves to a server and then make a `GET` request from the server.

The `GET` returns the content - in this case, HTML, CSS and Javascript code, which our browser then renders.

## Our first Server

Now that we have the basics of the web down, let's talk about writing our own server.  We'll be using a library called flask.  To get it simply do:

`sudo python -m pip install flask`

Now let's see how our first server will look:

```
from flask import Flask

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return "Hello World!"

if __name__ == '__main__':
   app.run(debug=True)
```

## URL handling in flask

One of the great things about flask is it's clear and obvious handling of urls.  You put the urls right next to the functions, so it's easy to figure out what maps to what.  (Not always the case in all web frameworks).

Additionally, we can make our urls easily variablized like so:

```
from flask import Flask

app = Flask(__name__)

@app.route("/<name>", methods=["GET"])
def index(name):
    return "Hello " + name

if __name__ == '__main__':
   app.run()
```

We can also specify url's by type:

```
from flask import Flask

app = Flask(__name__)

@app.route("/<int:birthday>", methods=["GET"])
def index(birthday):
    return birthday+1

if __name__ == '__main__':
   app.run()
```

