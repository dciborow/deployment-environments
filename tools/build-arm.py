# ------------------------------------
# Copyright (c) Microsoft Corporation.
# Licensed under the MIT License.
# ------------------------------------

import os
import shutil
import subprocess
from pathlib import Path

repository_root = Path(__file__).resolve().parent.parent
environments_path = repository_root / 'Environments'

print('Building ARM templates from bicep files...')
environments = [
    Path(dirpath)
    for dirpath, dirnames, files in os.walk(environments_path)
    if not environments_path.samefile(dirpath)
    and Path(dirpath).parent.samefile(environments_path)
]

# get the full path to the azure cli executable
az = shutil.which('az')

for environment in environments:
    print(f'  Compiling template: {environment}')
    # run the azure cli command to compile the template
    subprocess.run([az, 'bicep', 'build', '--file', environment / 'main.bicep', '--outfile', environment / 'azuredeploy.json'])

print('Done')
