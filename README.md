# pyLLVM

pyLLVM is a tool for compilers/interpreters written in Python that generates LLVM 2.6 code. pyLLVM is currently in development and is released only as a proof of concept.

# Example Usage

Install pyLLVM:

```
pip install pyLLVM
```

Import the "operations" class:

```python
>>> from pyLLVM import operations
```
Generate LLVM code for multiplying 1 and 2:

```python
>>> operations.mul(1, 2)
add i32 1, 2
```