import os
import shutil

cwd = os.getcwd()

destination_dir = os.path.join(cwd, 'data/Legacy Music')
source_dir = os.path.join(cwd, 'data/Music')

# Delete the destination directory if it exists
if os.path.exists(destination_dir):
    shutil.rmtree(destination_dir)

# Recreate the destination directory
os.makedirs(destination_dir)

for root, dirs, files in os.walk(source_dir):
    for filename in files:
        if filename.endswith('.ootrs'):
            file_path = os.path.join(root, filename)

            # Get group dir path (e.g. `Banjo-Kazooie Series/Banjo-Kazooie`)
            relative_group_path = os.path.relpath(file_path, source_dir)

            # Append group path to destinarion dir
            sequence_output_dir = os.path.join(destination_dir, relative_group_path)
            shutil.unpack_archive(file_path, sequence_output_dir, 'zip')
