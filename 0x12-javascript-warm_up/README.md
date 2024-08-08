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
#### Step 3: Setup the interpreter shebang path
```
sudo ln -s $(which node) /usr/bin/node
```
This will ensure that you have Node.js 14 installed and set as the default version on your system using nvm. The last step is necessary since when using nvm, the node binary is not typically located there by default rather located at `/home/yourusername/.nvm/versions/node/v14.x.x/bin/node`.

### Install semi-standard
[Documentation](https://github.com/standard/semistandard)
```
npm install semistandard --global
```

## Tips
- Starting with file [2-arguments.js](./2-arguments.js) and so on you may refer to [process.argv](https://nodejs.org/api/process.html#process_process_argv)
- Starting with file [13-add.js](./13-add.js) you may refer to [Simple Intro to NodeJS Module Scope](http://51elliot.blogspot.com/2012/01/simple-intro-to-nodejs-module-scope.html)

## References
+ [Writing JavaScript Code](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
+ [Variables](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/First_steps/Variables)
+ [Data Types](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Data_structures)
+ [Operators](https://developer.mozilla.org/en-US/docs/Learn/Getting_started_with_the_web/JavaScript_basics)
+ [Operator Precedence](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Reference/Operators/Operator_precedence)
+ [Controlling Program Flow](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Control_flow_and_error_handling)
+ [Functions](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Building_blocks/Functions)
+ [Objects and Arrays](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
+ [Intrinsic Objects](https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects)
+ [Module patterns](https://darrenderidder.github.io/talks/ModulePatterns/#/)
+ [var, let and const](https://www.youtube.com/watch?v=sjyJBL5fkp8)
+ [JavaScript Tutorial](https://www.youtube.com/watch?v=vZBCTc9zHtI)
+ [Modern JS](https://github.com/mbeaudru/modern-js-cheatsheet)

**__HAPPY CODING... :smiley: NEVER STOP LEARNING... :pen:__**
