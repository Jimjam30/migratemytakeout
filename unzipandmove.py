import os
import zipfile
import shutil
import logging

def setup_logger(log_file):
    """Set up the logger."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",)

def unzip_and_copy_images_videos(zip_folder, output_folder, destination_folder):
    # Ensure the output folder exists
    os.makedirs(output_folder, exist_ok=True)

    #Set up the logger
    setup_logger(log_file)

    # Loop through each zip file in the specified folder
    for zip_file in os.listdir(zip_folder):
        if zip_file.endswith(".zip"):
            zip_path = os.path.join(zip_folder, zip_file)
            print(f"Unzipping {zip_path}")
            logging.info(f"Unzipping {zip_path}")
            
            # Extract the contents of the zip file
            with zipfile.ZipFile(zip_path, 'r') as zip_ref:
                # Extract all files to the output folder
                zip_ref.extractall(output_folder)
                print(f"Extracted files to {output_folder}")
                logging.info(f"Extracted files to {output_folder}")
            
            #loop through the extracted files and copy only the images to another folder
            for root, dirs, files in os.walk(output_folder):
                for file in files:
                    file_path = os.path.join(root, file)
                    if file.lower().endswith(('.png', '.jpg', '.jpeg', '.gif', '.mp4', '.avi', '.mkv')):
                        destination_path = os.path.join(destination_folder, file)
                        if not os.path.exists(destination_path):
                        # Copy the file to the destination folder
                            shutil.copy(file_path, destination_folder)
                            print(f"Copied file: {file_path}")
                            logging.info(f"Copied file: {file_path} to {destination_path}")
                    else:
                        logging.warning(f"File {file} already exists in the destination folder. Skipped.")
                                
         # Clear the output folder for the next zip file
            shutil.rmtree(output_folder)
            os.makedirs(output_folder, exist_ok=True)

# Specify the input and output folders
zip_folder = "E:\\GoogleMigration"
output_folder = "E:\\Output"
destination_folder = "C:\\Users\\"
log_file = "E:\\GoogleMigration\\Output\\script_log.txt"

# Call the function
unzip_and_copy_images_videos(zip_folder, output_folder, destination_folder)
