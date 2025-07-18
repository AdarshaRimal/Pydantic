# Pydantic Data Validation Guide

This repository demonstrates how to implement robust data validation in Python using Pydantic. The examples progress from basic type hinting to advanced validation techniques, showing how Pydantic ensures data integrity throughout your application.

## Key Concepts

### 1. Why Pydantic?
Python's dynamic typing can lead to unexpected data issues. We explore three approaches to validation:
- Type hinting (limited enforcement)
- Manual validation (verbose and unscalable)
- **Pydantic solution**: Declarative validation with automatic error handling

### 2. Core Validation Features
- **Type Validation**: Enforce data types for model fields
- **Structured Data**: Define required/optional fields with defaults
- **Special Validators**: Built-in validation for emails (`EmailStr`) and URLs (`AnyUrl`)
- **Field Constraints**: Add metadata with `Field()` (length limits, value ranges, descriptions)

### 3. Advanced Validation Techniques
#### Field Validators
- Per-field validation logic
- Type coercion (convert strings to numbers)
- Value transformation (e.g., uppercase names)
- Custom rules (e.g., domain whitelisting)

#### Model Validators
- Cross-field validation
- Complex business rules (e.g., "emergency contact required for seniors")
- Pre/post processing hooks

### 4. Special Features
- **Computed Fields**: Dynamically generated properties (e.g., BMI from weight/height)
- **Nested Models**: Hierarchical data structures with independent validation
- **Serialization**: Convert models to:
  - Python dictionaries (`model_dump()`)
  - JSON (`model_dump_json()`)
  - With options to exclude unset/default values

