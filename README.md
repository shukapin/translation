# About
This is a CLI command to translate a word by using macOS's default dictionary.

# Setup
## 1. Change the command name
Set the command name by editing setup.py
(In default, the command name is `trs`)

## 2. Change the order of used dictionary
- Open `preferences` of Dictionary app.
- Move the dictionary that you want to use to the top.

## 3. Make command in /usr/local/bin
```
$ sudo pip install -e .
```

# Usage
```
$ trs <word> [<word for highlight>]
```