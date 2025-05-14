import os
import subprocess

# Define size threshold (e.g., 10 MB)
SIZE_THRESHOLD_MB = 10
project_root = os.getcwd()

tracked_exts = set()

# Walk through all files in the project
for root, dirs, files in os.walk(project_root):
    for file in files:
        path = os.path.join(root, file)
        size_mb = os.path.getsize(path) / (1024 * 1024)

        if size_mb > SIZE_THRESHOLD_MB:
            ext = os.path.splitext(file)[1]
            if ext and ext not in tracked_exts:
                print(f"Tracking {ext} via Git LFS (file: {file}, size: {size_mb:.2f} MB)")
                subprocess.run(["git", "lfs", "track", f"*{ext}"])
                tracked_exts.add(ext)

print("\n✅ Done. Check your .gitattributes file.")
