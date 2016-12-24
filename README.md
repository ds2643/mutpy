**Note: this project is an incomplete. Please check back later before attempting to run.**

mutpy
======
Mutation testing tool for probing the quality of tests written in PyTest accompanying Python projects.

Description
------
An imperative implementation of a mutation testing framework in Python targeting PyTest tests.

Obviously, tests serve the purpose in the software development process of ensuring that code behaves as intended. However, developers often fail to question the quality of tests. Given a Python project with a test suite too large or complex to inspect manually, a strategy for judging the quality of tests might not be apparent. We therefore require a tool to make sure the tests cover as much behavior of the program as possible. Mutation testing automates this process to lower the cost of assuring test quality.

In a nutshell, mutation testing provides a litmus of the sensitivity of a project's tests to bugs. This is accomplished by introducing random changes to the source and observing the proportion of so-called mutants which continue to pass the test suite. Mutants that throw run-time errors are disgarded.

Approach
------
Mutpy creates a temporary copy of the project. Source files are rendered and munipulated as abstract syntax tree representions. Random point-mutations are applied to this structure. The code is then regenerated and tested with the packaged test library. Tests are monitored for failures. This process is repeated a number of times defined by the user of mutpy.


mutcl
------
This project is the sister version of an earlier mutation testing tool built in Clojure, mutcl. In my opinion, Clojure is slightly easier to mutate because of the language's homoiconicity: Code is treated as data, so the source is traversed as a tree of nested lists. Stocastic straversal of the program presents a challenge in the functional paradigm, but lessons learned implementing mutcl are to the benefit of this implementation.

Limitations:
------
Python's dynamic typing system provides a challenge to the goal of randomly transforming source. Whereas a statically typed language like Haskell, through the provision of type signatures, provides the necessary information to make unsupervised mutation of arbitrary nodes of a program's abstract syntax tree, mutation of programs in a dynamically typed language might be limited to a small subset of the language. This limitation introduces bias to mutpy's approach. This tool doesn't simulate a randomly selected subset of all possible mutations, but rather a randomly selected subset of some mutations.

Suggestions on type-checking arbitrary Python forms are welcome.

