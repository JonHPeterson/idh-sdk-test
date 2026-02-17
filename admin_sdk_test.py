"""
Test script for the_idh_operational_technology_api_client admin endpoints.
Run this file and set breakpoints to step through in a debugger.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'sdk')))
from the_idh_operational_technology_api_client.client import Client
from the_idh_operational_technology_api_client.api.admin import get_admin_health
from the_idh_operational_technology_api_client.api.admin import get_admin_version
from the_idh_operational_technology_api_client.models import VersionInfoResponse

def main():
    # Set a breakpoint here to step through
    client = Client(base_url="http://localhost:8080")
    try:
        health_response = get_admin_health.sync(client=client)
        print("SDK parsed response:", health_response)
        version_response: VersionInfoResponse = get_admin_version.sync(client=client)
        print("SDK parsed version response:", version_response)
    except Exception as e:
        print("Exception during SDK call:", e)
    # Always print the raw response for debugging
    import httpx
    with httpx.Client() as http_client:
        raw_health = http_client.get("http://localhost:8080/admin/health")
        print("\nRaw health response text:")
        print(raw_health.text)
        raw_version = http_client.get("http://localhost:8080/admin/version")
        print("\nRaw version response text:")
        print(raw_version.text)

if __name__ == "__main__":
    main()