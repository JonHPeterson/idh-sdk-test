"""
Test script for the_idh_operational_technology_api_client assets endpoints.
Run this file and set breakpoints to step through in a debugger.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'sdk')))
from idh_ota_client.client import Client
from idh_ota_client.api.assets import get_api_v1_assets_rootassets
from idh_ota_client.api.assets import get_api_v_1_assets_asset_uuid
from idh_ota_client.models import AssetResponse

def main():
    # Set a breakpoint here to step through
    client = Client(base_url="http://localhost:8080")
    try:
        root_assets = get_api_v1_assets_rootassets.sync(client=client)
        print("SDK parsed root assets response:", root_assets)
        first_asset = next(iter(root_assets.additional_properties)) if root_assets else None
        if first_asset:
            asset_response: AssetResponse = get_api_v_1_assets_asset_uuid.sync(client=client, asset_uuid=first_asset)
            print(f"SDK parsed asset response for UUID {first_asset}:", asset_response)
    except Exception as e:
        print("Exception during SDK call:", e)
    # Always print the raw response for debugging
    import httpx
    with httpx.Client() as http_client:
        raw_root_assets = http_client.get("http://localhost:8080/api/v1/assets/rootassets")
        print("\nRaw root assets response text:")
        print(raw_root_assets.text)
        raw_root_assets = http_client.get("http://localhost:8080/api/v1/assets/rootassets")
        print("\nRaw root assets response text:")
        print(raw_root_assets.text)
        if first_asset:
            raw_asset = http_client.get(f"http://localhost:8080/api/v1/assets/{first_asset}")
            print(f"\nRaw asset response text for UUID {first_asset}:")
            print(raw_asset.text)
if __name__ == "__main__":
    main()