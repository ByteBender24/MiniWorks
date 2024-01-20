import sys
import clipboard
import json

'''
Clipboard Manager Script

Usage:
  - Make sure to install the 'clipboard' module before running this script:
    ```
    pip install clipboard
    ```

Execution:
  - Execute the script from the command line with a single command as an argument.
    ```
    python script_name.py [command]
    ```
    Replace 'script_name.py' with the actual name of your script file.

Available Commands:
  1. Save Command ('save'):
     - Description: Saves the current contents of the clipboard associated with a user-defined key.
  2. Load Command ('load'):
     - Description: Loads the clipboard with the contents associated with a previously saved key.
  3. List Command ('list'):
     - Description: Lists all saved keys and their corresponding clipboard contents.

'''

SAVE_FILE = '.\clipboard.json'


def save_data(filepath, data):
    '''
    Saves data to the specified file in JSON format.

    Args:
      - filepath (str): The file path where the data will be saved.
      - data (dict): The data to be saved.

    Returns:
      None
    '''
    with open(filepath, 'w') as f:
        json.dump(data, f, indent=2)
    print("Data saved successfully.")


def load_data(filepath):
    '''
    Loads data from the specified file in JSON format.

    Args:
      - filepath (str): The file path from which data will be loaded.

    Returns:
      dict: Loaded data, or an empty dictionary if the file is not found or an error occurs.
    '''
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
        print("Data loaded successfully.")
        return data
    except:
        return {}


if len(sys.argv) == 2:
    command = sys.argv[1].lower()

    data = load_data(SAVE_FILE)

    if command == "save":
        key = input("Enter a key: ")
        data[key] = clipboard.paste()
        save_data(SAVE_FILE, data)
        print("Saved clipboard content successfully.")

    elif command == "load":
        key = input("Enter a key: ")
        if key in data:
            clipboard.copy(data[key])
            print("Loaded clipboard content successfully.")
        else:
            print("Key not found. Use 'list' command to view available keys.")

    elif command == "list":
        print("Available Keys and Clipboard Contents:")
        for key, content in data.items():
            print(f"- Key: {key}, Content: {content}")

    else:
        print("Invalid command. Use 'save', 'load', or 'list'.")

else:
    print("Enter a single command!!")
