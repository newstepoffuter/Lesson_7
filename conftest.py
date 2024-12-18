import os
import zipfile
import pytest

current_file = os.path.abspath(__file__)
current_dir = os.path.dirname(current_file)
path_to_directory_files = os.path.join(current_dir, "resources")
path_to_directory_archive = os.path.join(current_dir, "archives")


@pytest.fixture(scope="function", autouse=True)
def create_zip_for_files():
    if not os.path.exists(path_to_directory_archive):
        os.mkdir(path_to_directory_archive)

    file_dir = os.listdir(path_to_directory_files)

    zip_file_path = os.path.join(path_to_directory_archive, "test.zip")
    with zipfile.ZipFile(zip_file_path, mode="w") as zf:
        for file in file_dir:
            add_file = os.path.join(path_to_directory_files, file)
            zf.write(add_file, os.path.basename(add_file))
    yield

    if os.path.exists(zip_file_path):
        os.remove(zip_file_path)
