import json
import os
import sys

def validate_system_architecture():
    filepath = 'system_architecture.json'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        required_keys = ['system_name', 'entities']
        for key in required_keys:
            if key not in data:
                print(f"Error: Missing key '{key}' in {filepath}.")
                return False

        print(f"Success: {filepath} is valid.")
        return True
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON in {filepath}: {e}")
        return False

def validate_financial_logic():
    filepath = 'financial_logic.json'
    if not os.path.exists(filepath):
        print(f"Error: {filepath} not found.")
        return False

    try:
        with open(filepath, 'r') as f:
            data = json.load(f)

        if 'financial_logic' not in data:
            print(f"Error: Missing key 'financial_logic' in {filepath}.")
            return False

        logic = data['financial_logic']
        required_subkeys = ['revenue_streams', 'expense_optimization_algo', 'tax_engine', 'distribution_protocol']
        for key in required_subkeys:
            if key not in logic:
                print(f"Error: Missing subkey '{key}' in 'financial_logic'.")
                return False

        print(f"Success: {filepath} is valid.")
        return True
    except json.JSONDecodeError as e:
        print(f"Error: Failed to decode JSON in {filepath}: {e}")
        return False

def main():
    valid_arch = validate_system_architecture()
    valid_fin = validate_financial_logic()

    if valid_arch and valid_fin:
        print("\nAll JSON files are valid.")
        sys.exit(0)
    else:
        print("\nValidation failed.")
        sys.exit(1)

if __name__ == "__main__":
    main()
