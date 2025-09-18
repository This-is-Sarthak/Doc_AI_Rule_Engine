"""
Rule definitions for document validation.

"""
RULES = {
    "R001": {
        "description": "Verify that a 'driver_license' document is present in the classification results.",
        "condition": "The 'doc_type' field in the 'classification' result array must contain the value 'driver_license'.",
        "action": "If the condition is met, the status is 'PASS'. Otherwise, the status is 'FAIL'."
    }
}
