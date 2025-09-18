"""
Firestore service for interacting with Google Cloud Firestore.
"""
import os
import sys
from google.cloud import firestore
from config import GOOGLE_CLOUD_PROJECT, FIRESTORE_DATABASE_ID

class FirestoreService:
    """Service class for Firestore operations."""
    
    def __init__(self):
        """Initialize Firestore client with project and database settings."""
        self.db = firestore.Client(
            project=GOOGLE_CLOUD_PROJECT,
            database=FIRESTORE_DATABASE_ID
        )
    
    def get_document(self, collection_name, document_id):
        """
        Retrieve a document from Firestore.
        
        Args:
            collection_name (str): Name of the collection
            document_id (str): Document ID to retrieve
            
        Returns:
            dict: Document data if found, None otherwise
        """
        try:
            doc_ref = self.db.collection(collection_name).document(document_id)
            doc = doc_ref.get()
            return doc.to_dict() if doc.exists else None
        except Exception as e:
            print(f"Error fetching Firestore document: {e}", file=sys.stderr)
            return None
