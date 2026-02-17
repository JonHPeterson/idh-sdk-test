"""
Test script for the_idh_operational_technology_api_client classifications endpoints.
Run this file and set breakpoints to step through in a debugger.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'sdk')))
from idh_ota_client.client import Client
from idh_ota_client.api.classifications import get_api_v1_classificationsname
from idh_ota_client.models import ClassificationResponse

def main():
    # Set a breakpoint here to step through
    client = Client(base_url="http://localhost:8080")
    try:
        classification_name = "some_name"  # Replace with an actual classification name for testing
        classifications_response: ClassificationResponse = get_api_v1_classificationsname.sync(client=client, name=classification_name)
        print("SDK parsed classifications response:", classifications_response)
    except Exception as e:
        print("Exception during SDK call:", e)
    # Always print the raw response for debugging
    import httpx
    with httpx.Client() as http_client:
        raw_classification = http_client.get(f"http://localhost:8080/api/v1/classifications/{classification_name}")
        print("\nRaw classification response text:")
        print(raw_classification.text)

if __name__ == "__main__":
    main()