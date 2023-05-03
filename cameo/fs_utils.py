from pathlib import Path

def ensure_directory_exists(pathName):
    p = Path(pathName)
    if p.exists():
        if not p.is_dir():
            raise ValueError(f'{pathName} is not a directory.')
    else:
        p.mkdir(parents=True)

