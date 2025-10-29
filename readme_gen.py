import os
import sys

def check_existing_readme():
    if (os.path.isfile("README.md")):

        print("README.md file already exists.\nOverwrite existing file?\n(y/n)")
        while True:
            try:
                choice = input()
                if (choice == "y"):
                    return True
                elif (choice == "n"):
                    print("Keeping existing file. Exiting...")
                    return False
                else:
                    print("invalid choice.")
            except Exception:
                print("invalid choice.")
    else: # no README.md file found
        return True

if __name__ == "__main__":
    print("### README GENERATOR ###")

    # Check for existing README.md
    if not check_existing_readme():
        sys.exit()

    print("--Enter Project Details--")
    print("Project Name: ", end="")
    proj_name = input()
    print("Description: ", end="")
    description = input()
    print("Installation Steps: ", end="")
    install_steps = input()
    print("Usage: ", end="")
    usage = input()

    # Create README File
    with open("README.md", "w", encoding="utf-8", newline="\n") as rm:
        rm.write(f"# {proj_name}\n")
        rm.write(f"{description}\n")
        rm.write(f"## Installation\n{install_steps}\n")
        rm.write(f"## Usage\n{usage}")