import os
import shutil
import zipfile
import re

def extract_files_with_extension(zip_file, output_dir):
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        files_to_extract = []
        filelist = zip_ref.infolist()
        for member in filelist:
            if member.filename.endswith('.meta'):
                with zip_ref.open(member) as file:
                    file_content = file.read().decode('utf-8')
                    if not re.search(r'\nZSOUND:', file_content):
                        seq_filename = member.filename.replace('.meta', '.seq')
                        seq_file = next(f for f in filelist if f.filename == seq_filename)
                        if (seq_file):
                            files_to_extract.append(member)
                            files_to_extract.append(seq_file)

        for member in files_to_extract:        
            zip_ref.extract(member, output_dir)
                

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
            relative_group_path = os.path.relpath(os.path.dirname(file_path), source_dir)

            # Append group path to destinarion dir
            sequence_output_dir = os.path.join(destination_dir, relative_group_path)
            extract_files_with_extension(file_path, sequence_output_dir)
