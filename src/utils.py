import os
import shutil


def create_clean_public_dir(public_dir):
	if os.path.exists(public_dir):
		print(f"Removing existing directory: {public_dir}")
		shutil.rmtree(public_dir)
	print(f"Creating directory: {public_dir}")
	os.mkdir(public_dir)


def copy_dir(src, dst):
	for item in os.listdir(src):
		item_path = os.path.join(src, item)
		dest_path = os.path.join(dst, item)
		if os.path.isfile(item_path):
			print(f"Copying file: {item_path} -> {dest_path}")
			shutil.copy(item_path, dest_path)
		elif os.path.isdir(item_path):
			print(f"Creating subdirectory: {dest_path}")
			os.mkdir(dest_path)
			copy_dir(item_path, dest_path)
