from pathlib import Path

folder = Path(".")

for file in folder.iterdir():
    if file.is_file():
        if file.stem == "rename" or file.stem == "exception" or file.stem == "test_156":
            continue
        new_name = "prog_"+ file.stem[:3] + file.suffix
        new_path = folder / new_name

        if new_path.exists():
            print(f"Skipping {file.name} → {new_name}")
            continue

        file.rename(new_path)