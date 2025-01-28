import os
import shutil

# folder paths
source_folder = '/path/to/source'
destination_folders = {
    'Images': '/path/to/images',
    'Documents': '/path/to/docs',
    'Music': '/path/to/music'
}

# file extensions
file_types = {
    '.jpg': 'Images',
    '.png': 'Images',
    '.pdf': 'Documents',
    '.mp3': 'Music',
}

# Move files to respective folders

for filename in os.listdir(source_folder):
    ext = os.path.splitext(filename)[1].lower()
    if ext in file_types:
        shutil.move(os.path.join(source_folder, filename), destination_folders[file_types[ext]])