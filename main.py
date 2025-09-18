"""
Main application for document validation system.
"""
import warnings
from google.auth import default

# Suppress the specific warning
warnings.filterwarnings("ignore", 
    message="Your application has authenticated using end user credentials")
import json
from services.firestore_service import FirestoreService
from services.gemini_service import GeminiService
from rules import RULES
from config import FIRESTORE_COLLECTION, DOCUMENT_ID

def format_rule_description(rule_id):
    """Format a rule into a human-readable string."""
    rule = RULES[rule_id]
    return f"""
Rule ID: {rule_id}
Description: {rule['description']}
Condition: {rule['condition']}
Action: {rule['action']}"""

def main():
    """Main function to run the document validation."""
    # Initialize services
    firestore_service = FirestoreService()
    gemini_service = GeminiService()
    
    # Fetch document from Firestore
    document_data = firestore_service.get_document(FIRESTORE_COLLECTION, DOCUMENT_ID)
    
    if not document_data:
        print("Error: Document not found or could not be fetched.")
        return
    
    # Apply each rule and collect results
    results = {}
    for rule_id in RULES:
        rule_description = format_rule_description(rule_id)
        result = gemini_service.generate_validation_report(document_data, rule_description)
        results[rule_id] = result
    
    # Print the results
    print("\n--- Validation Results ---")
    for rule_id, result in results.items():
        print(f"\nRule: {rule_id}")
        print("-" * 50)
        print(result)
        print("-" * 50)

if __name__ == "__main__":
    main()
