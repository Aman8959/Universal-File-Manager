from pathlib import Path

BASE_PATH = Path.cwd()


def list_all_files():
    print("\nAll Available Files:\n")
    files = list(BASE_PATH.rglob("*"))

    files = [f for f in files if f.is_file()]

    if not files:
        print("No files found.\n")
        return

    for index, file in enumerate(files, start=1):
        print(f"{index}. {file.relative_to(BASE_PATH)}")

    print()


def create_file():
    try:
        name = input("Enter file name with extension (example: test.txt): ").strip()
        file_path = BASE_PATH / name

        if file_path.exists():
            print("File already exists.\n")
            return

        file_path.parent.mkdir(parents=True, exist_ok=True)

        content = input("Enter content for the file:\n")
        file_path.write_text(content)

        print("File created successfully.\n")

    except Exception as err:
        print(f"Error: {err}\n")


def read_file():
    try:
        name = input("Enter file name to read: ").strip()
        file_path = BASE_PATH / name

        if not file_path.is_file():
            print("File does not exist.\n")
            return

        print("\nFile Content:\n")
        print(file_path.read_text())
        print("\nFile read successfully.\n")

    except Exception as err:
        print(f"Error: {err}\n")


def update_file():
    try:
        name = input("Enter file name to update: ").strip()
        file_path = BASE_PATH / name

        if not file_path.is_file():
            print("File does not exist.\n")
            return

        print("\n1. Rename file")
        print("2. Overwrite content")
        print("3. Append content")

        choice = input("Select option: ").strip()

        if choice == "1":
            new_name = input("Enter new file name: ").strip()
            file_path.rename(BASE_PATH / new_name)
            print("File renamed successfully.\n")

        elif choice == "2":
            data = input("Enter new content:\n")
            file_path.write_text(data)
            print("File overwritten successfully.\n")

        elif choice == "3":
            data = input("Enter content to append:\n")
            with file_path.open("a") as f:
                f.write("\n" + data)
            print("Content appended successfully.\n")

        else:
            print("Invalid option.\n")

    except Exception as err:
        print(f"Error: {err}\n")


def delete_file():
    try:
        name = input("Enter file name to delete: ").strip()
        file_path = BASE_PATH / name

        if not file_path.is_file():
            print("File does not exist.\n")
            return

        confirm = input("Are you sure? (yes/no): ").lower()

        if confirm == "yes":
            file_path.unlink()
            print("File deleted successfully.\n")
        else:
            print("Deletion cancelled.\n")

    except Exception as err:
        print(f"Error: {err}\n")


def main():
    while True:
        print("===== UNIVERSAL FILE MANAGER =====")
        print("1. List All Files")
        print("2. Create File")
        print("3. Read File")
        print("4. Update File")
        print("5. Delete File")
        print("6. Exit")

        choice = input("Enter your choice: ").strip()

        if choice == "1":
            list_all_files()
        elif choice == "2":
            create_file()
        elif choice == "3":
            read_file()
        elif choice == "4":
            update_file()
        elif choice == "5":
            delete_file()
        elif choice == "6":
            print("Exiting program...")
            break
        else:
            print("Invalid choice.\n")


if __name__ == "__main__":
    main()