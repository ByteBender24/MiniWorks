
### Steps to Launch Clipboard Manager with Incognito Mode

1.  **Locate the Browser Shortcut**:
    
    -   Right-click on your web browser shortcut (like Chrome or Firefox) on your desktop or in the Start menu and select "Properties."
2.  **Modify the Target Field**:
    
    -   In the "Target" field, you can add the command to run your clipboard manager before launching the browser. The exact command will depend on your clipboard manager's file path.
    
    Here's an example for Google Chrome:
    
    plaintext
    
    Copy code
    
    `"C:\Path\To\Your\ClipboardManager.py" & "C:\Program Files\Google\Chrome\Application\chrome.exe" --incognito` 
    
    Replace `C:\Path\To\Your\ClipboardManager.py` with the actual path to your clipboard manager script. Ensure that you enclose the paths in quotes if they contain spaces.
    
3.  **Save Changes**:
    
    -   Click "OK" to save the changes.