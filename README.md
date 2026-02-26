# Test Repo Documentation

A small Python demo repository used for testing RAG ingestion and graph-aware querying.

## Overview

This repository contains two Python modules that demonstrate basic calculator and utility functionality.

### Modules

- `math_utils.py` — provides the `Calculator` class and `utility_function`
- `main_app.py` — entry point that demonstrates usage of both modules

## math_utils

The `math_utils` module provides reusable arithmetic components.

### Calculator

The `Calculator` class supports basic arithmetic operations and maintains a history of all calculations performed.

#### Initialization

The constructor initializes an empty history list.

```python
calc = Calculator()
```

#### add

Adds two numbers and records the operation in history.

```python
result = calc.add(3, 4)   # returns 7
```

#### multiply

Multiplies two numbers and records the operation in history.

```python
result = calc.multiply(5, 6)   # returns 30
```

### utility_function

A standalone helper function that doubles its input value.

```python
doubled = utility_function(10)   # returns 20
```

## main_app

The `main_app` module is the entry point for the demo.

### App

The `App` class wires together the components from `math_utils` and runs a demonstration.

#### Initialization

Creates an internal `Calculator` instance on startup.

#### run_demo

Runs a fixed demonstration sequence:

1. Calls `calc.add(3, 4)` — expected result: 7
2. Calls `calc.multiply(5, 6)` — expected result: 30
3. Calls `utility_function(10)` — expected result: 20
4. Prints all three results to stdout

```python
app = App()
app.run_demo()
# Output: Results: 7, 30, 20
```

## Dependencies

No external dependencies. Standard Python 3 only.

## Usage

```bash
python main_app.py
```

Expected output:

```
Results: 7, 30, 20
```

## Testing

To verify the extraction and RAG query pipeline works correctly, ingest this repository and try the following queries:

- *"What does the Calculator class do?"*
- *"What does run_demo call?"*
- *"What is utility_function?"*
- *"What methods does Calculator have?"*
- *"What does add do?"*
