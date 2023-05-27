from file_manager import FileManager


def main():
    working_directory = "/Users/Gret/PycharmProjects/Практикум_4сем/venv/File_manager"
    file_manager = FileManager(working_directory)

    while True:
        print("\nFile Manager Commands:")
        print("1. create_folder <folder_name>")
        print("2. delete_folder <folder_name>")
        print("3. change_directory <directory_name>")
        print("4. create_file <file_name>")
        print("5. write_to_file <file_name> <text>")
        print("6. view_file <file_name>")
        print("7. delete_file <file_name>")
        print("8. copy_file <source_file> <destination_folder>")
        print("9. move_file <source_file> <destination_folder>")
        print("10. rename_file <old_name> <new_name>")
        print("11. exit")

        command = input("Enter a command: ")
        command_parts = command.split()

        if command_parts[0] == "create_folder":
            file_manager.create_folder(command_parts[1])
        elif command_parts[0] == "delete_folder":
            file_manager.delete_folder(command_parts[1])
        elif command_parts[0] == "change_directory":
            file_manager.change_directory(command_parts[1])
        elif command_parts[0] == "create_file":
            file_manager.create_file(command_parts[1])
        elif command_parts[0] == "write_to_file":
            file_manager.write_to_file(command_parts[1], " ".join(command_parts[2:]))
        elif command_parts[0] == "view_file":
            file_manager.view_file(command_parts[1])
        elif command_parts[0] == "delete_file":
            file_manager.delete_file(command_parts[1])
        elif command_parts[0] == "copy_file":
            file_manager.copy_file(command_parts[1], command_parts[2])
        elif command_parts[0] == "move_file":
            file_manager.move_file(command_parts[1], command_parts[2])
        elif command_parts[0] == "rename_file":
            file_manager.rename_file(command_parts[1], command_parts[2])
        elif command_parts[0] == "exit":
            break
        else:
            print("Invalid command.")


if __name__ == "__main__":
    main()
