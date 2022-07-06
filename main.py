from pathlib import Path


                            solution 1- Noob
root_dir= Path("files")
file_path= root_dir.glob("**/*")
                              
for path in file_path:
  if path.is_file():
    txt= path.parts[-1]
    txt_update= txt.replace("txt", "csv")
    new_filepath= path.with_name(txt_update)
    path.rename(new_filepath)

                           solution 2- Pro
root_dir= Path("files")
for path in root_dir.rglob("**/*"):
  if path.is_file():
    new_filepath= path.with_suffix(".csv")
    path.rename(new_filepath)
