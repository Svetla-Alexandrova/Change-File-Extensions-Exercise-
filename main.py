from pathlib import Path

root_dir = Path('files')

for path in root_dir.glob("*.txt"):
  if path.is_file():
    new_suffix = '.csv'
    new_filepath = path.with_suffix(new_suffix)
    path.rename(new_filepath)