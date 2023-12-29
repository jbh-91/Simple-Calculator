# Project: Calculator with GUI

This is a simple calculator with a GUI
> **Goal:** GUI, calculations and call functions in order

## Task

Create a Calculator

### Input

* GUI input
  * numbers
  * operations
    * Addition (+)
    * Substraction (-)
    * Multiplication (*)
    * Division (/)
    * Exponentiation
      * potentiation (**)
      * square root (sqrt())
      * qubic root (**(1./3.))
      * x root (**(1./x.))
  * minus sign (-)
  * float point
  * compute (=)

### Conversions

* check if calculation is possible (division by 0)
* calculate

### Output

* result
* Feedback when division is not possible

## Psuedo code

```text
TipCalculator
    Initialize calculator
    Initilaize GUI

    Prompt for equation

    Convert numbers to numbers (float)
    Calculate operations in order while checking if operations are possible
    
    Display result or feedback on error
End

```

## Tests

* Operations (as float)
  * Addition (+)
  * Substraction (-)
  * Multiplication (*)
  * Division (/)
  * Exponentiation
    * potentiation (**)
    * square root (sqrt())
    * qubic root (**(1./3.))
    * x root (**(1./x.))
* Division by 0
* Operations hirarchy (PEMDAS)
  * Parentheses, Exponents, Multiplication/Division, Addition/Subtraction from left to right.

### Assertion-Test: Operations (as float)

**Test-Plan: Addition (+)**

```text
Inputs:

Expected result:

```

**Test-Plan: Substraction (-)**

```text
Inputs:

Expected result:

```

**Test-Plan: Multiplication (*)**

```text
Inputs:

Expected result:

```

**Test-Plan: Division (/)**

```text
Inputs:

Expected result:

```

**Test-Plan: Exponentiation, potentiate (\*\*)**

```text
Inputs:

Expected result:

```

**Test-Plan: Exponentiation, square root (sqrt())**

```text
Inputs:

Expected result:

```

**Test-Plan: Exponentiation, qubic root (\*\*(1./3.))**

```text
Inputs:

Expected result:

```

**Test-Plan: Exponentiation, x root (\*\*(1./x.))**

```text
Inputs:

Expected result:

```

### Assertion-Test: Division by 0

**Test-Plan:**

```text
Inputs:

Expected result:

```

### Assertion-Test: Operations hirarchy (PEMDAS)

**Test-Plan:**

```text
Inputs:

Expected result:

```

## Additional, optional Tasks

* Add brackets/paranthethes functionality
* Add scientific calculations
* Display thousand-sepeartor on input "1,000,000.00"
