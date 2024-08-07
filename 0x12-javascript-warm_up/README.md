# 0x12 JavaScript - Warm up

## Learning Objectives
* Why JavaScript programming is amazing
* How to run a JavaScript script
* How to create variables and constants
* What are differences between var, const and let
* What are all the data types available in JavaScript
* How to use the if, if ... else statements
* How to use comments
* How to affect values to variables
* How to use while and for loops
* How to use break and continue statements
* What is a function and how do you use functions
* What does a function that does not use any return statement return
* Scope of variables
* What are the arithmetic operators and how to use them
* How to manipulate dictionary
* How to import a file

## Code Requirements
* Allowed editors: vi, vim, emacs
* All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
* All your files should end with a new line
* The first line of all your files should be exactly `#!/usr/bin/node`
* A `README.md` file, at the root of the folder of the project, is mandatory
* Your code should be `semistandard` compliant (version 16.x.x). [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: [AirBnB style](https://github.com/airbnb/javascript)
* All your files must be executable
* The length of your files will be tested using `wc`

## More Info
### Install Node 14
#### Step 1: Install nvm
```
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.39.3/install.sh | bash
```
You may need to restart your terminal or source your shell configuration file to load nvm. For example, if you are using bash, you can run:
```
export NVM_DIR="$([ -z "${XDG_CONFIG_HOME-}" ] && printf %s "${HOME}/.nvm" || printf %s "${XDG_CONFIG_HOME}/nvm")"
[ -s "$NVM_DIR/nvm.sh" ] && \. "$NVM_DIR/nvm.sh"
```

#### Step 2: Install Node.js 14
```
nvm install 14
nvm use 14
nvm alias default 14
node -v
npm -v
```
This will ensure that you have Node.js 14 installed and set as the default version on your system using nvm.

### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
npm install semistandard --global
```

