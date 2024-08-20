# JavaScript - Web scraping
## Learning Objectives
- Why JavaScript programming is amazing
- How to manipulate JSON data
- How to use request and fetch API
- How to read and write a file using fs module
## Code Requirements
- Allowed editors: vi, vim, emacs
- All your files will be interpreted on Ubuntu 20.04 LTS using `node` (version 14.x)
- All your files should end with a new line
- The first line of all your files should be exactly `#!/usr/bin/node`
- A README.md file, at the root of the folder of the project, is mandatory
- Your code should be `semistandard` compliant. [Rules of Standard](https://standardjs.com/rules.html) + [semicolons on top](https://github.com/standard/semistandard). Also as reference: AirBnB style
- All your files must be executable
- The length of your files will be tested using `wc`
- You are not allowed to use `var`
## More Info
### install Node 14
#### Step 1: Install nvm
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
## Install `request` module and use it

[Documentation](https://github.com/request/request)

```
npm install request --global
export NODE_PATH=~/.nvm/versions/node/v14.21.3/lib/node_modules/
```

**Notes:** Request module has been deprecated since February 2020 - the team is considering alternative to replace this module - however, it’s a really simple and powerful module for practicing web-scraping in JavaScript (and still used a lot in the industry).

Also you may consider using `~/.bashrc` file to do automatic set up of the `NODE_PATH` environment variable.

