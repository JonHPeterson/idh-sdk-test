"""
Test script for the_idh_operational_technology_api_client classifications endpoints.
Run this file and set breakpoints to step through in a debugger.
"""
from encodings.aliases import aliases
import sys
import os

from sdk.idh_ota_client.models import asset_response
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), 'sdk')))
from idh_ota_client.client import Client
from idh_ota_client.api.timeseries import list_aggregate_types
from idh_ota_client.api.timeseries import get_aggregate_usage_info
from idh_ota_client.api.timeseries import list_timeseries_types
from idh_ota_client.api.timeseries import get_tag_info
from idh_ota_client.api.timeseries import get_samples
from idh_ota_client.api.timeseries import get_plot_samples
from idh_ota_client.api.timeseries import get_aggregate_samples
from idh_ota_client.api.timeseries import get_grid_samples
from idh_ota_client.api.assets import get_asset_by_uuid 

def get_start_and_end_time(client: Client, tag_uuid: str) -> tuple[str, str]:
    try:
        tag_info_response = get_tag_info.sync(client=client, tag_uuid=tag_uuid)
        if tag_info_response and tag_info_response.earliest_time_iso8601 and tag_info_response.latest_time_iso8601:
            t1 = tag_info_response.earliest_time_iso8601
            t2 = tag_info_response.latest_time_iso8601
            # calculate 24 hours in the middle of tese two times, to use as a default time range for testing
            from datetime import datetime, timedelta
            t1_dt = datetime.fromisoformat(t1.replace("Z", "+00:00"))
            t2_dt = datetime.fromisoformat(t2.replace("Z", "+00:00"))
            middle_dt = t1_dt + (t2_dt - t1_dt) / 2
            starttime = (middle_dt - timedelta(hours=12)).isoformat()
            endtime = (middle_dt + timedelta(hours=12)).isoformat()
            return starttime, endtime
        else:
            print("Tag info response is missing start_time or end_time:", tag_info_response)

    except Exception as e:
        print("Exception during SDK call to get tag info:", e)
    # test the raw response as well for debugging
    import httpx
    with httpx.Client() as http_client:
        raw_tag_info = http_client.get(f"http://localhost:8080/api/v1/timeseries/taginfo/{tag_uuid}")
        print(f"\nRaw timeseries tag info response text for tag UUID {tag_uuid}:")
        print(raw_tag_info.text)    

def get_two_tags(client: Client) -> list[str]:
    try:
        all_tags_asset = "616a923a-8281-4795-b339-810625bcfa2e" # this asset exists on all systems
        asset_response = get_asset_by_uuid.sync(client=client, asset_uuid=all_tags_asset)
        # grab the uuid of two aliases
        aliases = asset_response.aliases
        tag_uuids = list(aliases.additional_properties.values())[:2]

        return tag_uuids
    except Exception as e:
        print("Exception during SDK call to get asset tags:", e)
        return []

def test_helper_funcs(client: Client):
    try:
        aggregate_types_response = list_aggregate_types.sync(client=client)
        print("SDK parsed timeseries aggregate types response:", aggregate_types_response)
        aggregate_usage_info_response = get_aggregate_usage_info.sync(client=client)
        print("SDK parsed timeseries aggregate usage info response:", aggregate_usage_info_response)
        types_response = list_timeseries_types.sync(client=client)
        print("SDK parsed timeseries types response:", types_response)
    except Exception as e:
        print("Exception during SDK call:", e)
    # Always print the raw response for debugging
    import httpx
    with httpx.Client() as http_client:
        raw_aggregate_types = http_client.get("http://localhost:8080/api/v1/timeseries/aggregatetypes")
        print("\nRaw timeseries aggregate types response text:")
        print(raw_aggregate_types.text)
        raw_aggregate_usage_info = http_client.get("http://localhost:8080/api/v1/timeseries/aggregateusageinfo")
        print("\nRaw timeseries aggregate usage info response text:")
        print(raw_aggregate_usage_info.text)
        raw_types = http_client.get("http://localhost:8080/api/v1/timeseries/types")
        print("\nRaw timeseries types response text:")
        print(raw_types.text)

def main():
    # Set a breakpoint here to step through
    client = Client(base_url="http://localhost:8080")
    test_helper_funcs(client)
    max_samples = 100000
    tag_uuids = get_two_tags(client)
    starttime, endtime = get_start_and_end_time(client, tag_uuid=tag_uuids[0])  # replace with an actual tag UUID for testing
    print("Two tag UUIDs for testing:", tag_uuids)
    from_uoms = ["m", "N"]
    two_uoms = ["feet", "lbf"] 
    try:
        samples_response = get_samples.sync(client=client, starttime=starttime, endtime=endtime, max_samples=max_samples, tag_uuids=tag_uuids, from_uoms=from_uoms, to_uoms=two_uoms)
        print("SDK parsed timeseries samples response:", samples_response)
        samples_response = get_plot_samples.sync(client=client, starttime=starttime, endtime=endtime, lanes=100, max_samples=max_samples, tag_uuids=tag_uuids, from_uoms=from_uoms, to_uoms=two_uoms)
        print("SDK parsed timeseries samples response:", samples_response)
        samples_response = get_aggregate_samples.sync(client=client, starttime=starttime, endtime=endtime, aggregate_type=1, window=60, max_samples=max_samples, tag_uuids=tag_uuids, from_uoms=from_uoms, to_uoms=two_uoms)
        print("SDK parsed timeseries samples response:", samples_response)
        samples_response = get_grid_samples.sync(client=client, starttime=starttime, endtime=endtime, grid=60, max_samples=max_samples, tag_uuids=tag_uuids, from_uoms=from_uoms, to_uoms=two_uoms)
        print("SDK parsed timeseries samples response:", samples_response)

    except Exception as e:
        print("Exception during SDK call:", e)
    # Always print the raw response for debugging
    import httpx
    with httpx.Client() as http_client:
        # tag info raw response for debugging
        raw_tag_info = http_client.get(f"http://localhost:8080/api/v1/timeseries/taginfo/{tag_uuids[0]}")
        print(f"\nRaw timeseries tag info response text for tag UUID {tag_uuids[0]}:")
        print(raw_tag_info.text) 
        # timeseries types raw response for debugging
        raw_types = http_client.get("http://localhost:8080/api/v1/timeseries/types")
        print("\nRaw timeseries types response text:")
        print(raw_types.text)
        # aggregate types raw response for debugging
        raw_aggregate_types = http_client.get("http://localhost:8080/api/v1/timeseries/aggregatetypes")
        print("\nRaw timeseries aggregate types response text:")
        print(raw_aggregate_types.text)
        # aggregate usage info raw response for debugging
        raw_aggregate_usage_info = http_client.get("http://localhost:8080/api/v1/timeseries/aggregateusageinfo")
        print("\nRaw timeseries aggregate usage info response text:")
        print(raw_aggregate_usage_info.text)
        
        # print the URL being called for debugging
        url = f"http://localhost:8080/api/v1/timeseries/samples?starttime={starttime}&endtime={endtime}&maxSamples={max_samples}&tagUuids={','.join(tag_uuids)}&fromUoms={','.join(from_uoms)}&toUoms={','.join(two_uoms)}"
        print("URL being called:", url)
        raw_samples = http_client.get(url)
        print("\nRaw timeseries samples response text:")
        print(raw_samples.text)
        url = f"http://localhost:8080/api/v1/timeseries/plotsamples?starttime={starttime}&endtime={endtime}&lanes=100&maxSamples={max_samples}&tagUuids={','.join(tag_uuids)}&fromUoms={','.join(from_uoms)}&toUoms={','.join(two_uoms)}"
        print("URL being called:", url)
        raw_samples = http_client.get(url)
        print("\nRaw timeseries plot samples response text:")
        print(raw_samples.text)
        url = f"http://localhost:8080/api/v1/timeseries/aggregatesamples?starttime={starttime}&endtime={endtime}&aggregateType=1&window=60&maxSamples={max_samples}&tagUuids={','.join(tag_uuids)}&fromUoms={','.join(from_uoms)}&toUoms={','.join(two_uoms)}"
        print("URL being called:", url)
        raw_samples = http_client.get(url)
        print("\nRaw timeseries aggregate samples response text:")
        print(raw_samples.text) 
        url = f"http://localhost:8080/api/v1/timeseries/gridsamples?starttime={starttime}&endtime={endtime}&grid=60&maxSamples={max_samples}&tagUuids={','.join(tag_uuids)}&fromUoms={','.join(from_uoms)}&toUoms={','.join(two_uoms)}"
        print("URL being called:", url)
        raw_samples = http_client.get(url)
        print("\nRaw timeseries grid samples response text:")
        print(raw_samples.text)

 
if __name__ == "__main__":
    main()