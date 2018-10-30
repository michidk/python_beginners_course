# Python Intro for Bloody Noobs
A collection of very basic steps into the python world


## What this is about (Info)
The intention is to make the noobs familiar with the basic use of a version control system (`git`) and give them a kick-start into writing scripts (`python`) to automatize tasks. This is a small definition in layman's terms:
* `git`: is a program that lets several people collaborate on the same project. They can work in parallel and git takes care of integrating their work into the same project. It can even merge changes inside the same file by different people at different times! `git` makes a snapshot whenever somebody changes something and the collection of snapshots is the `git` history. You can switch at any time to different points in the past of different people's workstream and investigate, copy code, change stuff etc. Programs like `git` make modern software development possible. The history can be saved online in a repository, famous services for this are github.com and gitlab.com.
* `python` is what this course is actually about. It's a programming language that reads almost like prose. It's very versatile and let's you start coding without much overhead. Believe me, every step below is super easy and straight forward compared with the steps necessary for most other languages.


## How to make it work (Setup)

### Discover the terminal
A terminal (or shell) is the direct way to communicate with a computer. To open one inside a directory do
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
   * download and install python3.6 for Mac
   * in a terminal, type `git`, then follow the install instruction
   * That's it! Now use a terminal and enter
  ```shell
  python3 --version
  # Python 3.6.6  (that's not a command but a comment, to show you what answer to expect)
  ```
Additionally, you need a good IDE (Integrated Development Environment), a text editor that knows the programming language and has nice colors and error checking. For a beginner I recommend [pycharm](https://www.jetbrains.com/pycharm/). Personally I'm a fan of [atom](https://atom.io/), but that's more general purpose and less "python".


### Set up the IDE
Python files are text files ending with `.py`. Your IDE will make it easier to write in them and execute and test them. Here are some more detailed instructions:
* pycharm: [HELP FOR PROJECT SETUP WANTED]. Execute your python code by clicking on 'Run' in the IDE. Pycharm also offers you a shell to start the script by hand. It also offers git integration.
* atom: just use it as text editor, execute all python code in the shell. There are a lot of extensions in atom that will help you once you've become more advanced.
* IDLE: use it as text editor to open and edit your `*.py` files with it. Execute python code either in the shell or directly via 'Run' or 'F5' in an IDLE built-in window.


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
* add an empty line and make python make yourself a compliment. The output should be something like
  ```
  Hi Andy!

  You are wearing a very nice hat today!
  ```

### Stage 1
* use two names as input from the command line and let them great each other
* store the names in variables and use them to make it less confusing
* let one of the two count from 0 to 4
* let one of them count from 0 to 19
* let one of them count until a number you specify on the command line

### Stage 2
* run the new file `calculus.py` and solve the riddles. Let python calculate!
* count the money in your wallet and use it as input from the command line. Then calculate how many beers you can buy until it's all used up.
* use the `sleep` command in the `time` library to wait 2 seconds before giving the answer
