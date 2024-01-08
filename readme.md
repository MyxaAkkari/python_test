# Project Overview

This project is a small Python program consisting of multiple modules that showcase basic operations with numbers and iterable objects. The program includes three modules: `simp.py`, `comp.py`, and `col.py`, as well as a main script `main.py` that utilizes the functions defined in the modules.

## Module Descriptions

### simp.py

The `simp.py` module serves as a simple utility module with functions for basic arithmetic operations on numbers. It includes the following functions:

- **check_run():** Checks if any function from the module has been run. Returns `True` if a function has been called, and `False` otherwise.

- **add_nums(n1, n2):** Takes two numbers and returns their sum.

- **sub_nums(n1, n2):** Takes two numbers and returns their difference (n1 - n2).

### comp.py

The `comp.py` module imports functions from `simp.py` and defines additional functions that operate on numbers. It includes the following functions:

- **sumofdigits(num):** Takes a number and returns the sum of its digits. It checks if any function from the `simp` module has been run using the `check_run()` function.

- **ispal(num):** Takes a number and checks if it is a palindrome. Returns `True` if the number is a palindrome and `False` otherwise. It also checks if any function from the `simp` module has been run using the `check_run()` function.

### col.py

The `col.py` module defines a single function:

- **myzip(it1, it2):** Takes two iterable objects and returns them zipped together using the built-in `zip` function.

## How to Use

1. Clone the repository to your local machine.

2. Open the `main.py` file and uncomment the line `# print(sumofdigits(222))` if you want to see how an exception works when no function from the `simp` module has been called.

3. Run the `main.py` script. It imports functions from the `simp`, `comp`, and `col` modules and demonstrates the usage of these functions.


# Exception Handling

Both `sumofdigits` and `ispal` functions in the `comp.py` module include exception handling. If no function from the `simp` module has been called (`check_run()` returns `False`), an `Exception` is raised with the message "At least one function from simp module needs to be called first."

# Author

This Python project was created by [ Myxa_Akkari ]. Feel free to reach out with any questions or improvements!
