import os
import shutil


class FileManager:
    def __init__(self, working_directory):
        self.working_directory = working_directory

    def create_folder(self, folder_name):
        folder_path = os.path.join(self.working_directory, folder_name)
        os.mkdir(folder_path)
        print(f"Folder '{folder_name}' created successfully.")

    def delete_folder(self, folder_name):
        folder_path = os.path.join(self.working_directory, folder_name)
        shutil.rmtree(folder_path)
        print(f"Folder '{folder_name}' deleted successfully.")

    def change_directory(self, directory_name):
        if directory_name == "..":
            parent_directory = os.path.dirname(self.working_directory)
            self.working_directory = parent_directory
        else:
            new_directory = os.path.join(self.working_directory, directory_name)
            if os.path.isdir(new_directory):
                self.working_directory = new_directory
            else:
                print(f"Directory '{directory_name}' does not exist.")

    def create_file(self, file_name):
        file_path = os.path.join(self.working_directory, file_name)
        with open(file_path, "w"):
            pass
        print(f"File '{file_name}' created successfully.")

    def write_to_file(self, file_name, text):
        file_path = os.path.join(self.working_directory, file_name)
        with open(file_path, "w") as file:
            file.write(text)
        print(f"Text written to file '{file_name}' successfully.")

    def view_file(self, file_name):
        file_path = os.path.join(self.working_directory, file_name)
        try:
            with open(file_path, "r") as file:
                content = file.read()
                print(f"Content of file '{file_name}':")
                print(content)
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")

    def delete_file(self, file_name):
        file_path = os.path.join(self.working_directory, file_name)
        try:
            os.remove(file_path)
            print(f"File '{file_name}' deleted successfully.")
        except FileNotFoundError:
            print(f"File '{file_name}' not found.")

    def copy_file(self, source_file, destination_folder):
        source_path = os.path.join(self.working_directory, source_file)
        destination_path = os.path.join(self.working_directory, destination_folder)
        try:
            shutil.copy2(source_path, destination_path)
            print(f"File '{source_file}' copied to '{destination_folder}' successfully.")
        except FileNotFoundError:
            print(f"File '{source_file}' not found.")
        except FileExistsError:
            print(f"File '{source_file}' already exists in '{destination_folder}'.")

    def move_file(self, source_file, destination_folder):
        source_path = os.path.join(self.working_directory, source_file)
        destination_path = os.path.join(self.working_directory, destination_folder)
        try:
            shutil.move(source_path, destination_path)
            print(f"File '{source_file}' moved to '{destination_folder}' successfully.")
        except FileNotFoundError:
            print(f"File '{source_file}' not found.")
        except FileExistsError:
            print(f"File '{source_file}' already exists in '{destination_folder}'.")

    def rename_file(self, old_name, new_name):
        old_path = os.path.join(self.working_directory, old_name)
        new_path = os.path.join(self.working_directory, new_name)
        try:
            os.rename(old_path, new_path)
            print(f"File '{old_name}' renamed to '{new_name}' successfully.")
        except FileNotFoundError:
            print(f"File '{old_name}' not found.")
        except FileExistsError:
            print(f"File '{new_name}' already exists.")
