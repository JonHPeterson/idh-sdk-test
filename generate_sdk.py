import subprocess

def generate_sdk(openapi_yaml_url, output_dir):
    """
    Generate a Python SDK from an OpenAPI YAML URL using openapi-generator.
    Args:
        openapi_yaml_url (str): URL or local path to openapi.yaml
        output_dir (str): Directory to output the generated SDK
    """
    cmd = [
        "openapi-generator-cli", "generate",
        "-i", openapi_yaml_url,
        "-g", "python",
        "-o", output_dir
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    if result.returncode != 0:
        raise RuntimeError("SDK generation failed")
