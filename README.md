# Computer Voice Commands

This is some glue software I'm working on that attempts to use voice recognition + PyAutoGUI to eventually give a user full control of their computer with just voice commands.

It is currently a work in progress. For now, I am trying to make it good enough to edit a text file in VS-Code. The current roadmap:
- Dictate edits to a file in vs code [WIP]
    - Typing text
    - Moving around, undoing
    - Error handling, debugging
- Move to different files in the editor
- Open different projects in the editor
- Move focus to other windows as needed

The main purpose of this software is to make something that is better than the OS's existing voice commands. 
While the voice command software that Windows comes with must be everything for everyone, I can fine-tune this python script to be really good at writing code, or playing games, for example.


## How to get set up

### Step 0 - Install python 3 onto your computer

Install python 3 onto your computer if you don't already have it.

### Step 1 - Set up a virtual environment

It is worth creating a new python virtual environment in this directory, where you can install your packages without polluting your global python install. Run this command:

```
python -m venv ./.venv
```

This should create a new python environment in the .venv directory. This folder should be ignored by git. On Windows, you can activate it by running 'activate.bat' (This is just a one line shell script that runs the real activation script located at `./.venv/Scripts/activate.bat`) (TODO: create something similar for other platforms). 

**You will need to make sure the environment is activated before you install new dependencies or run the program.**

### Step 2 - Install the requirements

Activate the environment (see the "Set up a virtual environment" step), then iInstall the required packages with this command:

```
pip install -r requirements.txt
```

### Step 3 - Run the program

Run the program with this command:

```
python main.py
```

