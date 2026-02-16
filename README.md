# Mik CVR Penta Matrix

This repository contains the system architecture and financial logic for the **Mik CVR Penta Matrix** project, designed for an ERP system or dashboard.

## Overview

The data defines the `Entity_Mechanics` (how the team functions) and the `Financial_Algorithm` (how money is optimized and distributed).

## Files

### Data Files
*   **`system_architecture.json`**: Defines the `Entity_Mechanics`. It includes profiles for:
    *   **Mik Core**: Product Generator
    *   **Sofie Platform**: Interface Manager
    *   **Tomas Backend**: System Architect
*   **`financial_logic.json`**: Defines the `Financial_Algorithm`. It includes logic for:
    *   **Revenue Streams**: Artistic Sales vs. Commercial Services
    *   **Expense Optimization**: Deduction rules for catering, travel, and tech.
    *   **Tax Engine**: VSO model logic.
    *   **Distribution Protocol**: Profit splitting ratios.

### Source Documents
*   **`mik.md`**: Detailed profile for Mik Core.
*   **`sofie.md`**: Detailed profile for Sofie Platform.
*   **`tomas.md`**: Detailed profile for Tomas Backend.

### Utilities
*   **`validate_data.py`**: A Python script to validate the integrity of the JSON data files.

## Usage

To validate the data files, run:

```bash
python3 validate_data.py
```
