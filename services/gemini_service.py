"""
Gemini service for interacting with Google's Gemini API.
"""
import json
import google.generativeai as genai
from config import GEMINI_API_KEY, GEMINI_MODEL_NAME

class GeminiService:
    """Service class for Gemini API operations."""
    
    def __init__(self):
        """Initialize Gemini API with the configured API key."""
        genai.configure(api_key=GEMINI_API_KEY)
        self.model = genai.GenerativeModel(model_name=GEMINI_MODEL_NAME)
    
    def generate_validation_report(self, document_data, rule_description):
        """
        Generate a validation report using Gemini based on the provided rule.
        
        Args:
            document_data (dict): The document data to validate
            rule_description (str): The rule to apply to the document
            
        Returns:
            str: The generated validation report
        """
        extracted_json_string = json.dumps(document_data, indent=2)
        
        prompt = f"""
Role: You are an expert document validation system.

Objective: Apply a given business rule to a provided JSON object and return a detailed report in a structured JSON format.

Context: The JSON data represents information extracted from a document. The rule is provided in natural language. Your task is to accurately parse and apply the rule's condition to the JSON data.

Instructions:
1. Analyze the `rule_description` to identify the condition and the data fields to check.
2. Traverse the `extracted_json_string` to find the relevant data fields.
3. Apply the rule's condition to the found data.
4. Generate a JSON report based on the outcome.

Here is the rule you must apply:
{rule_description}

Here is the JSON data you must validate:
{extracted_json_string}

Your output should be a JSON object in the following format:
{{
  "rule_id": "R001",
  "status": "PASS" or "FAIL",
  "reason": "Rule condition met." or "Rule condition not met.",
  "value_checked": "The value from the JSON that was checked"
}}
"""
        try:
            response = self.model.generate_content(prompt)
            return response.text
        except Exception as e:
            print(f"Error generating validation report: {e}")
            return None
