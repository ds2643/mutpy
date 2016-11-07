**Note: this project is incomplete and still a work in progress. Please check back later before attempting to run.**

# mutpy

An imperative implementation of a mutation testing framework in Python. Obviously, tests serve the purpose in the software development process of ensuring that code behaves as intended. However, given some software project with a test suite too large to inspect by manually, how can we be sure the tests indeed accomplish this goal? That is, we need a tool to make sure the tests cover as much behavior of the program as possible.

Mutation testing helps us measure the sensitivity of a project's tests to bugs. This is accomplished by 1) iteratively introducing randomly selected bugs to the program in random places 2) observing the proportion of so-called mutants which continue to pass the test suite compared to those mutants which fail the tests (mutants that throw run-time errors are disgarded). In short, mutation testing tests tests by seeing how sensitive tests are to bugs.

The approach involves tranforming the program in question to an abstract syntax tree (which is easily accomplished in Python using libraries like RedBaron or AST), applying psudo-random point-mutations (single node) to the AST. The code is then regenerated (a helpful feature of RedBaron not found in the standard AST module) and tested with the included test library.

Note, this is a second version of my mutation testing framesworks. See mutcl for a sister project written in Clojure (a functional lisp hosted on the JVM) that serves the same purpose as this project. In my opinion, Clojure is slightly easier to mutate because lisps are homoiconic (the program is easier to munipute). In the case of mutcl, mutation is simply a stochastic traversal and function application to the program (represented as a tree of nested lists).

Note, the weakness of doing this in a dynamically typed language is the introduction of bias: Transformation of programmatic nodes in an unsupervised manner is not possible because nodes cannot be type-checked. Instead, mutations are only possible for a subset of the target language. In truth, this tool doesn't simulate a randomly selected subset of all possible mutations, but rather a randomly selected subset of some mutations.

# Notes:
1. AST Module: Initially, interface of standard AST module preferred over RedBaron, but RedBaron doesn't support dumping the ast, which is needed to run the test suite natively.
