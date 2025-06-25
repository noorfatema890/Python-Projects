import os
import zipfile
import tarfile
import shutil
from pathlib import Path

def unpack_all_files(source_dir, destination_dir=None):
    """
    Unpacks all files from a directory, including extracting archives.
    
    Args:
        source_dir: Directory containing files to unpack
        destination_dir: Where to place unpacked files (defaults to source_dir)
    """
    if destination_dir is None:
        destination_dir = source_dir
    
    # Create destination if it doesn't exist
    Path(destination_dir).mkdir(parents=True, exist_ok=True)
    
    for item in os.listdir(source_dir):
        source_path = os.path.join(source_dir, item)
        
        # Skip directories (or handle them recursively if you want)
        if os.path.isdir(source_path):
            continue
            
        try:
            # Handle ZIP files
            if zipfile.is_zipfile(source_path):
                with zipfile.ZipFile(source_path, 'r') as zip_ref:
                    zip_ref.extractall(destination_dir)
                print(f"Extracted ZIP: {item}")
                
            # Handle TAR files (including .tar.gz, .tar.bz2)
            elif tarfile.is_tarfile(source_path):
                with tarfile.open(source_path) as tar_ref:
                    tar_ref.extractall(destination_dir)
                print(f"Extracted TAR: {item}")
                
            # Copy regular files
            else:
                shutil.copy2(source_path, destination_dir)
                print(f"Copied file: {item}")
                
        except Exception as e:
            print(f"Failed to process {item}: {str(e)}")

if __name__ == "__main__":
    import argparse
    
    parser = argparse.ArgumentParser(description='Unpack all files from a directory')
    parser.add_argument('source_dir', help='Directory containing files to unpack')
    parser.add_argument('--dest', help='Destination directory (defaults to source)')
    
    args = parser.parse_args()
    
    print(f"Unpacking files from: {args.source_dir}")
    unpack_all_files(args.source_dir, args.dest)
    print("Unpacking complete!")