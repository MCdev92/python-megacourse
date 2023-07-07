import zipfile
import pathlib

# Code needs to be revised for debug go back to section 18
def make_archive(filepaths, dest_dir):
    dest_path = pathlib.Path(dest_dir, "compressed.zip")
    with zipfile.ZipFile(dest_dir, 'w') as archive:
        for filepath in filepaths:
            filepath = pathlib.Path(filepath)
            archive.write(filepath, arcname=filepath.name)

if __name__ == "__main__":
    make_archive(filepaths= ["newfile1.py", "newfile2.py"], dest_dir="")