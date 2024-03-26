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

# Iterate through files
for root, dirs, files in os.walk(source_dir):
    for filename in files:
        if filename.endswith('.ootrs'):
            # Construct full path to the file
            file_path = os.path.join(root, filename)

            group_name = os.path.basename(os.path.dirname(file_path))
            sequence_output_dir = os.path.join(destination_dir, group_name)
            shutil.unpack_archive(file_path, sequence_output_dir, 'zip')
