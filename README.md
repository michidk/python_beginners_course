# Python Intro for Bloody Noobs
A collection of very basic steps into the python world


## What this is about (Info)
The intention is to make the noobs familiar with the basic use of a version control system (`git`) and give them a kick-start into writing scripts (`python`) to automatize tasks.


## How to make it work (Setup)

### Discover the terminal
A terminal is the direct way to communicate with a computer. To open one inside a directory do
* Windows: shift+right click -> Open Powershell Window here
* Linux: right click -> Open in Terminal
* Mac: right click -> Open Terminal
Type a command and hit enter to send it off:
```shell
echo 'Hello World!'
```


### Download the software

First, we install python and git. Follow those steps:
* Windows:
  * download and install python3.6 for windows (google it, I trust in you!)
  * download and install git for windows
  * Done! Now test if it worked fine. Open a terminal and enter
  ```shell
  python --version
  # Python 3.6.6  (that's not a command but a comment, to show you what answer to expect)
  ```
* Linux:
  * open a terminal and enter
  ```shell
  sudo apt update
  sudo apt install python3.6
  sudo apt install git
  ```
  * That's it! Now use a terminal and enter
  ```shell
  python3 --version
  # Python 3.6.6  (that's not a command but a comment, to show you what answer to expect)
  ```
* Mac:
   * open a terminal and enter
   ```shell
   xcode-select --install
   /usr/bin/ruby -e "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install)"
   brew doctor  # just to test if it's working
   brew install python3
   brew install git
   ```
   * That's it! Now use a terminal and enter
  ```shell
  python3 --version
  # Python 3.6.6  (that's not a command but a comment, to show you what answer to expect)
  ```

### Download the source code
Create a folder (for example on your desktop) and start a terminal in there. Then download all the code and its history with
```shell
git clone git@github.com:andb0t/python_beginners_course.git  # this creates a new directory
cd python_beginners_course  # this enters the directory in the terminal
```
You have now everything you need to develop a little program!


## Time to roll! (Execution)
Now that we got it all set-up, we can start our first try! You just downloaded the final version of the course code. But we walk before we run, so we go back in history to the very beginning. Execute
```shell
git log  # shows all the history consisting of single steps, called 'commits'
```
and search for a commit with the description 'Stage 0'. Copy its hash number. Then use the time machine to go back!
```shell
git checkout HASH  # HASH has to be replaced with the number associated with that commit.
```

Done! Now execute your first python command (not counting the `python --version` before):
```shell
python hello.py  # Linux and Mac users will have to type 'python3' instead of 'python' to get the correct python version
```
From now on just sit back, enjoy the course and `git checkout THE_NEXT_COMMIT` from time to time.


## Steps to Geek Wallhall (Tasks)

### Stage 0
* make it say 'Hi YOURNAME!' only. No empty lines, no congratulations message
* make it pick up your name from outside, such that you can type `python hello.py YOURNAME` or `python hello.py OTHERNAME`
