# Mystery Delivery System

## Overview

Mystery Delivery System is a Python-based delivery optimization program that determines the most efficient delivery agent for a given set of packages.

The system calculates the delivery cost or distance for different agents and identifies the most efficient option based on the provided warehouse, package, and agent data.

## Project Structure

```text
mystery-delivery-system/
│
├── main.py
├── test_cases/
│   ├── test1.json
│   ├── test2.json
│   └── ...
│
└── reports/
    ├── report_test1.json
    ├── report_test2.json
    └── ...
```

## Technologies Used

* Python
* JSON

## How to Run

Open a terminal in the project directory and run:

```bash
python main.py .\test_cases\test1.json
```

Replace `test1.json` with another test case when required.

For example:

```bash
python main.py .\test_cases\test2.json
```

## Input

The system accepts a JSON file containing warehouse locations, delivery agents, and package information.

Example:

```json
{
    "warehouses": {
        "W1": [45, 66],
        "W2": [34, 36]
    },
    "agents": {
        "A1": [50, 50]
    }
}
```

## Output

The program generates a report containing the calculated delivery results and identifies the most efficient delivery agent for the given input.

## Test Cases

The `test_cases` folder contains the provided test input files.

The `reports` folder contains the corresponding generated output reports.

## Assumptions

* Coordinates are represented as `[x, y]`.
* The provided JSON input format is followed.
* Delivery efficiency is determined using the calculation implemented in `main.py`.
* The program processes each test case independently.
