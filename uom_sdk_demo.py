import sdk.idh_ota_client
from sdk.idh_ota_client.api.timeseries import get_plot_samples
from sdk.idh_ota_client.api.uom import list_prefixes


def uom_demo(client: sdk.idh_ota_client.Client):
    from sdk.idh_ota_client.api.uom import list_prefixes
    print("UOM Demonstration:")
    prefixes = list_prefixes.sync(client=client)
    print("name\tsymbol\tfactor")
    for i in range(len(prefixes.prefix_name)):
        print(f"{prefixes.prefix_name[i]}\t{prefixes.prefix_symbol[i]}\t{prefixes.prefix_factor[i]}")

    # You can list UOMs based on a passed filter.
    from sdk.idh_ota_client.api.uom import list_uoms
    filter_string = 'h*'
    uoms = list_uoms.sync(client=client, filter_string=filter_string)
    for i in range(len(uoms.names)):
        print(f"{uoms.names[i]}\t{uoms.definitions[i]}\t{uoms.aliases[i]}")

    # Get UOM information based on a exact match to uom name or uom alias
    from sdk.idh_ota_client.api.uom import get_uom_info
    uom_name = 'm'
    uom_info = get_uom_info.sync(client=client, uom_name=uom_name)
    print(uom_info)

    from sdk.idh_ota_client.api.uom import parse_uom
    uom_string = 'ft'
    parsed_uom = parse_uom.sync(client=client, uom_string=uom_string)
    print(parsed_uom)    

    from sdk.idh_ota_client.api.uom import convert_uom
    value = 1
    from_uom = 'km'
    to_uom = 'mile'
    converted_uom = convert_uom.sync(client=client, value=value, from_uom=from_uom, to_uom=to_uom)
    print ( f"Converted {value} {from_uom} to {converted_uom['convertedValue']} {to_uom}" )
    value = 32.174
    from_uom = 'ft/s^2'
    to_uom = 'm/s^2'
    converted_uom = convert_uom.sync(client=client, value=value, from_uom=from_uom, to_uom=to_uom)
    print ( f"Converted {value} {from_uom} to {converted_uom['convertedValue']} {to_uom}" )

def compare_converted_samples (converted_samples, unconverted_samples, tag_uuid: str):
    import importlib
    import idh_helpers
    importlib.reload(idh_helpers) # reload the functions in case they have been updated since the last import
    import numpy as np
    if len(converted_samples.items()) == 0 or len(unconverted_samples.items()) == 0:
        print("No samples to compare.")
        return    
    converted_table = converted_samples[tag_uuid]
    converted_values = np.array(converted_table.values)
    converted_times = np.array(converted_table.timestamps_ns)
    unconverted_table = unconverted_samples[tag_uuid]
    unconverted_values = np.array(unconverted_table.values)
    unconverted_times = np.array(unconverted_table.timestamps_ns)
    with np.errstate(divide='ignore', invalid='ignore'):
        ratio = unconverted_values/converted_values
    print("converted | unconverted | ratio")
    for i in range(5,len(converted_values)):
        print(f"{converted_values[i]} | {unconverted_values[i]} | {ratio[i]}")
        if i > 10:
            break;
    
    #print(f"unconverted uom: {from_uoms[to_uoms.index(converted_table.array_info.uom)]}, converted uom: {converted_table.array_info.uom}")
    #fig = idh_helpers.plot_data_arrays([unconverted_times, converted_times], [unconverted_values, converted_values], ['unconverted', 'converted',] )
    #fig.show()


def conversion_demo(client: sdk.idh_ota_client.Client):
    # Get a classification to get an asset and a time range to use for the UOM conversion
    from sdk.idh_ota_client.api.timeseries import get_samples
    from sdk.idh_ota_client.api.timeseries import get_plot_samples
    from sdk.idh_ota_client.api.classifications import get_root_classifications
    from sdk.idh_ota_client.api.classifications import get_classification_by_uuid
    from sdk.idh_ota_client.api.assets import get_asset_by_uuid
    classifications = get_root_classifications.sync(client=client).additional_properties
    for k,v in classifications.items():
        classification_uuid = k #next(iter(classifications))
        classification = get_classification_by_uuid.sync(client=client, classification_uuid=classification_uuid)
        aliases = get_asset_by_uuid.sync(client=client, asset_uuid=classification.asset_uuid).aliases.additional_properties
        # get the float32 tags for this demo
        tag_uuids = list()
        for name, uuid in aliases.items():
            if name.find("Float32") != -1:
                print(f"Adding alias {name} with uuid {uuid} to the tag list")
                tag_uuids.append(uuid)
        from_uoms = ['m', 'kg', 'N', 'm/s^2', 'm']
        to_uoms = ['ft', 'lb', 'lbf', 'ft/s^2', 'mile']
        lanes = 2000
        print(f"{classification.classification_name}: {classification.starttime},  {classification.endtime}")
        converted_samples = get_plot_samples.sync(client=client, starttime=classification.starttime, endtime=classification.endtime, lanes=lanes, max_samples=1000000, tag_uuids=tag_uuids, from_uoms=from_uoms, to_uoms=to_uoms).data.additional_properties
        unconverted_samples = get_plot_samples.sync(client=client, starttime=classification.starttime, endtime=classification.endtime, lanes=lanes, max_samples=1000000, tag_uuids=tag_uuids).data.additional_properties
        compare_converted_samples(converted_samples, unconverted_samples, tag_uuid=tag_uuids[0])



if __name__ == "__main__":
    from sdk.idh_ota_client.client import Client
    client = Client(base_url="http://localhost:8080")
    uom_demo(client)
    conversion_demo(client)

