# JavaScript - Objects, Scopes and Closures

* Language - JavaScript

## Learning Objectives
* Why JavaScript programming is amazing
* How to create an object in JavaScript
* What this means
* What undefined means
* Why the variable type and scope is important
* What is a closure
* What is a prototype
* How to inherit an object from another

## Code Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 20.04 LTS using node (version 14.x)
* All your files should end with a new line
* The first line of all your files should be exactly #!/usr/bin/node
* A README.md file, at the root of the folder of the project, is mandatory
* Your code should be semistandard compliant. Rules of Standard + semicolons on top. Also as reference: AirBnB style
* All your files must be executable
* The length of your files will be tested using wc
* You are not allowed to use var

## install Node 14

### Step 1: Install nvm
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```
You may need to restart your terminal or source your shell configuration file to load nvm. For example, if you are using bash, you can run:
```
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

### Step 2: Install Node.js 14
```
nvm install 14
nvm use 14
nvm alias default 14
node -v
npm -v
```

### Step 3: Setup the interpreter shebang path
```
sudo ln -s $(which node) /usr/bin/node
```
This will ensure that you have Node.js 14 installed and set as the default version on your system using nvm. The last step is necessary since when using nvm, the node binary is not typically located there by default rather located at `/home/yourusername/.nvm/versions/node/v14.x.x/bin/node`.

## Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
npm install semistandard --global
```
**Note:**

- The folder [main_files](./main_files) contains test examples of the the modules each corresponding to a module with the same prefix number ie `4-main.js` corresponds to `4-rectangle.js`.
- Make sure you take a chronological follow up of the files for a step by step learning experience

