# Complex feature package

The concept of adding a feature consists of two parts. Generating code that is portable and easy to work
with and actually writing the code. 

## Code Structure
The code structure is as follows:

```
ComplexAnalysis
│   test_ComplexNumber.py
│      
└───complexPackage
│   │   __init__.py
│   └─  ComplexNumber.py
│   
└───Documentation
    └─  readme.md

```
In test_complexNumbers are all the test located for the different
complex package functions. 

The complex package consists of a complexNumber object of which the 
buildins are rewritten to accomodate complex calculation like addition, substraction
etc. 

## Code Functionality
The package consists of the following complex functions:

    1. Addition
    2. Subtraction
    3. True devision 
    4. Multiplication
    5. Absolute (magnitude)
    6. angle (Phase)
    7. Carthesian to polar conversion



## Adding this package on your IDE and usage
To install this package, add it to your library and it should be good to go. 
    
    - Generating a complex number: a = ComplexNumber(realpart a, Imaginarypart a)
    - Addition or any function: 
    a = ComplexNumber(realpart a, Imaginarypart a)
    b = ComplexNumber(realpart b, Imaginarypart b)
    c = a + b --> returns automatically c as a ComplexNumber

## Fitting this in on github
 Normally using a github like structure this feature would be added on a feature branch, which branches off from dev and
will be merged in back to dev via a PR. To ensure code portability, packages are ideal as stand-alone feature modules. 

