import subprocess
import sys
import os
import requests

def download_openapi_yaml(url, output_path):
    response = requests.get(url)
    response.raise_for_status()
    with open(output_path, 'wb') as f:
        f.write(response.content)
    print(f"Downloaded openapi.yaml to {output_path}")

def generate_sdk(openapi_yaml_path, output_dir):
    # Remove old SDK if it exists
    if os.path.exists(output_dir):
        import shutil
        shutil.rmtree(output_dir)
    cmd = [
        sys.executable, '-m', 'openapi_python_client', 'generate',
        '--path', openapi_yaml_path,
        '--output-path', output_dir
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    print("STDOUT:", result.stdout)
    print("STDERR:", result.stderr)
    if result.returncode != 0:
        raise RuntimeError("SDK generation failed")

def main():
    openapi_url = "http://localhost:8080/openapi.yaml"
    openapi_yaml = "openapi.yaml"
    sdk_dir = "sdk"
    download_openapi_yaml(openapi_url, openapi_yaml)
    generate_sdk(openapi_yaml, sdk_dir)
    print("SDK generation complete.")

if __name__ == "__main__":
    main()
