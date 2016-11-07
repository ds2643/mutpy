# mutpy

An imperative implementation of a mutation testing framework in Python. Obviously, tests serve the purpose in the software development process of ensuring that code behaves as intended. However, given some software project with a test suite too large to inspect by manually, how can we be sure the tests indeed accomplish this goal? That is, we need a tool to make sure the tests cover as much behavior of the program as possible.

Mutation testing helps us measure the sensitivity of a project's tests to bugs.
anyNote: See mutcl for a sister project written in Clojure (a functional lisp hosted on the JVM) that serves the same purpose as this project.

Note, the weakness of doing this in a dynamically typed language is the introduction of bias: Transformation of programmatic nodes in an unsupervised manner is not possible because nodes cannot be type-checked. Instead, mutations are only possible for a subset of the target language. In truth, this tool doesn't simulate a randomly selected subset of all possible mutations, but rather a randomly selected subset of some mutations.

# Notes:
1. AST Module: Initially, interface of standard AST module preferred over RedBaron, but RedBaron doesn't support dumping the ast, which is needed to run the test suite natively.
