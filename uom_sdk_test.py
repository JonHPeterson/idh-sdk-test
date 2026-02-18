"""
Test script for the_idh_operational_technology_api_client classifications endpoints.
Run this file and set breakpoints to step through in a debugger.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'sdk')))
from idh_ota_client.client import Client
from idh_ota_client.api.uom import get_api_v1_uom_prefixes
from idh_ota_client.api.uom import get_api_v1_uom_info_uom_name
from idh_ota_client.api.uom import get_api_v1_uom_parse
from idh_ota_client.api.uom import get_api_v1_uom_convert
from idh_ota_client.api.uom import get_api_v1_uom_uoms


def main():
    # Set a breakpoint here to step through
    client = Client(base_url="http://localhost:8080")
    try:
        uom_prefixes_response = get_api_v1_uom_prefixes.sync(client=client)
        print("SDK parsed UOM prefixes response:", uom_prefixes_response)
        uom_info_response = get_api_v1_uom_info_uom_name.sync(client=client, uom_name="meter")
        print("SDK parsed UOM info response for 'meter':", uom_info_response)
        parse_response = get_api_v1_uom_parse.sync(client=client, uom_string="km")
        print("SDK parsed UOM parse response for 'km':", parse_response)
        # Example of convert, converting 1 kilometer to miles
        convert_response = get_api_v1_uom_convert.sync(client=client, value=1, from_uom="km", to_uom="mile")
        print("SDK parsed UOM convert response for 1 km to miles:", convert_response)
        uoms_response = get_api_v1_uom_uoms.sync(client=client, filter_string="f*")
        print("SDK parsed UOM uoms response for 'f*':", uoms_response)
    except Exception as e:
        print("Exception during SDK call:", e)
    # Always print the raw response for debugging
    import httpx
    with httpx.Client() as http_client:
        raw_uom_prefixes = http_client.get("http://localhost:8080/api/v1/uom/prefixes")
        print("\nRaw UOM prefixes response text:")
        print(raw_uom_prefixes.text)
        raw_uom_info = http_client.get("http://localhost:8080/api/v1/uom/info/meter")
        print("\nRaw UOM info response text for 'meter':")
        print(raw_uom_info.text)
        raw_parse = http_client.get("http://localhost:8080/api/v1/uom/parse?uom_string=km")
        print("\nRaw UOM parse response text for 'km':")
        print(raw_parse.text)
        raw_convert = http_client.get("http://localhost:8080/api/v1/uom/convert?value=1&from_uom=km&to_uom=mile")
        print("\nRaw UOM convert response text for 1 km to miles:")
        print(raw_convert.text)
        raw_uoms = http_client.get("http://localhost:8080/api/v1/uom/uoms?filter=f*")
        print("\nRaw UOM uoms response text for 'f*':")
        print(raw_uoms.text)

if __name__ == "__main__":
    main()