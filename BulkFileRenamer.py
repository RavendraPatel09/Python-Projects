import os
def bulk_rename(folder, prefix, ext_filter):
    files = [f for f in git os.listdir(folder) if f.lower().endswith(ext_filter.lower())]
    files.sort()
    count = 0
    for i, filename in enumerate(files, start=1):
        old_path = os.path.join(folder, filename)
        ext = filename.split(".")[-1]
        new_name = f"{prefix}_{i}.{ext}"
        new_path = os.path.join(folder, new_name)
        os.rename(old_path, new_path)
        count += 1
    return count
def main():
    folder = input("Folder path: ")
    ext_filter = input("File extension to rename (e.g. .txt): ")
    prefix = input("New name prefix: ")
    count = bulk_rename(folder, prefix, ext_filter)
    print(f"Renamed {count} files")
if __name__ == "__main__":
    main()
