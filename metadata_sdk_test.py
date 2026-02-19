"""
Test script for the_idh_operational_technology_api_client assets endpoints.
Run this file and set breakpoints to step through in a debugger.
"""
import sys
import os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'sdk')))
from idh_ota_client.client import Client
from idh_ota_client.api.metadata import list_sources
from idh_ota_client.api.metadata import get_source_by_name_or_uuid
from idh_ota_client.api.metadata import get_source_tags
from idh_ota_client.api.metadata import get_state_sets
from idh_ota_client.api.metadata import get_state_set_by_name
from idh_ota_client.api.metadata import get_state_set_by_id

def main():
    # Set a breakpoint here to step through
    first_source: str = None
    client = Client(base_url="http://localhost:8080")
    try:
        sources = list_sources.sync(client=client)
        print("SDK parsed metadata sources response:", sources)
        first_source = next(iter(sources.additional_properties)) if sources else None
        if first_source:
            source_response = get_source_by_name_or_uuid.sync(client=client, name_or_uuid=first_source)
            print(f"SDK parsed metadata source response for name or UUID {first_source}:", source_response)
            query = '[{}]'  # empty is everything
            src_tags_response = get_source_tags.sync(client=client, source_uuid=first_source, query=query)
            print(f"SDK parsed metadata source tags response for source UUID {first_source}:", src_tags_response)
            state_sets = get_state_sets.sync(client=client, source_uuid=first_source)
            print(f"SDK parsed metadata source state sets response for source UUID {first_source}:", state_sets)
            # get the id (key) and name (value) of the first state_sets 
            if state_sets and state_sets.additional_properties:
                last_item = list(state_sets.additional_properties.items())[-1]
                last_state_set_id, last_state_set_name = last_item
                print(f"Last state set ID: {last_state_set_id}, name: {last_state_set_name}")
                by_name = get_state_set_by_name.sync(client=client, source_uuid=first_source, name=last_state_set_name)
                print(f"SDK parsed metadata source state set response for source UUID {first_source} and state set name {last_state_set_name}:", by_name)
                by_id = get_state_set_by_id.sync(client=client, source_uuid=first_source, id=last_state_set_id)
                print(f"SDK parsed metadata source state set response for source UUID {first_source} and state set ID {last_state_set_id}:", by_id)

    except Exception as e:
        print("Exception during SDK call:", e)
    # Always print the raw response for debugging
    import httpx
    with httpx.Client() as http_client:
        raw_sources = http_client.get("http://localhost:8080/api/v1/metadata/sources")
        print("\nRaw metadata sources response text:")
        print(raw_sources.text)
        if first_source:
            raw_source = http_client.get(f"http://localhost:8080/api/v1/metadata/sources/{first_source}")
            print(f"\nRaw metadata source response text for name or UUID {first_source}:")
            print(raw_source.text)
            raw_src_tags = http_client.get(f"http://localhost:8080/api/v1/metadata/sources/srctags/{first_source}?query={query}")
            print(f"\nRaw metadata source tags response text for source UUID {first_source}:")
            print(raw_src_tags.text)
            raw_state_sets = http_client.get(f"http://localhost:8080/api/v1/metadata/sources/statesets/{first_source}")
            print(f"\nRaw metadata source state sets response text for source UUID {first_source}:")
            print(raw_state_sets.text)
            if state_sets and state_sets.additional_properties:
                raw_by_name = http_client.get(f"http://localhost:8080/api/v1/metadata/sources/statesets/name/{first_source}?name={last_state_set_name}")
                print(f"\nRaw metadata source state set response text for source UUID {first_source} and state set name {last_state_set_name}:")
                print(raw_by_name.text)
                raw_by_id = http_client.get(f"http://localhost:8080/api/v1/metadata/sources/statesets/id/{first_source}?id={last_state_set_id}")
                print(f"\nRaw metadata source state set response text for source UUID {first_source} and state set ID {last_state_set_id}:")
                print(raw_by_id.text)
if __name__ == "__main__":
    main()