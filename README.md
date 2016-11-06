# mutpy

An imperative implementation of a mutation testing framework in Python. Obviously, tests serve the purpose in the software development process of ensuring that code behaves as intended. However, given some software project with a test suite too large to inspect by manually, how can we be sure the tests indeed accomplish this goal? That is, we need a tool to make sure the tests cover as much behavior of the program as possible.

Mutation testing helps us measure the sensitivity of a project's tests to bugs.

Note: See mutcl for a sister project written in Clojure (a functional lisp hosted on the JVM) that serves the same purpose as this project.

# Notes:
1. AST Module: Initially, interface of standard AST module preferred over RedBaron, but RedBaron doesn't support dumping the ast, which is needed to run the test suite natively.
