# Variable Assignment

## Objectives

1. Assign a local variable.

## Instructions

You will assign a local variable named `greeting` that is equal to `"Hello World"`.

You should first make sure the test suite is running correctly by running `learn`.

Upon the first run of the test suite you should see:

```

======================================================================
ERROR: testGreeting (variable_test.TestVariable)
----------------------------------------------------------------------
Traceback (most recent call last):
  File "/Users/danielfenjves/development/google/python/cssi-prework-python-variable-assignment/variable_test.py", line 9, in testGreeting
    self.assertEqual(greeting, "Hello World")
NameError: global name 'greeting' is not defined

----------------------------------------------------------------------
Ran 1 test in 0.003s

FAILED (errors=1)

```

To solve this test failure, create a local variable `greeting` in the `variable.py` file. Set `greeting` equal to the string `"Hello World"`. Run `learn` to see if you did this correctly.

