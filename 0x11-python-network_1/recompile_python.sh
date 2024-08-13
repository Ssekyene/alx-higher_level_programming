
PYTHON_VERSION="3.8.16"
#OPENSSL_VERSION="1.1.1u"
OPENSSL_DIR="/usr/local/ssl"
#OPENSSL_TAR="openssl-${OPENSSL_VERSION}.tar.gz"
PYTHON_TAR="Python-${PYTHON_VERSION}.tgz"

# Install dependencies
echo "Installing required dependencies..."
sudo apt-get update
sudo apt-get install -y build-essential libssl-dev zlib1g-dev libbz2-dev \
libreadline-dev libsqlite3-dev wget curl llvm libncurses5-dev libncursesw5-dev \
xz-utils tk-dev libffi-dev liblzma-dev python3-openssl git

# Download and install OpenSSL
#echo "Downloading OpenSSL ${OPENSSL_VERSION}..."
#wget https://www.openssl.org/source/${OPENSSL_TAR}
#tar -xzf ${OPENSSL_TAR}
#cd openssl-${OPENSSL_VERSION}

#echo "Configuring and installing OpenSSL ${OPENSSL_VERSION}..."
#./config --prefix=${OPENSSL_DIR} --openssldir=${OPENSSL_DIR} shared zlib
#make -j$(nproc)
#sudo make install

#cd ..

# Download and install Python 3.8.16
echo "Downloading Python ${PYTHON_VERSION}..."
wget https://www.python.org/ftp/python/${PYTHON_VERSION}/${PYTHON_TAR}
tar -xzf ${PYTHON_TAR}
cd Python-${PYTHON_VERSION}

echo "Configuring Python ${PYTHON_VERSION} with OpenSSL ${OPENSSL_VERSION}..."
./configure --with-openssl=${OPENSSL_DIR} --enable-optimizations

echo "Compiling and installing Python ${PYTHON_VERSION}..."
make -j$(nproc)
sudo make altinstall

# Cleanup
cd ..
rm -rf openssl-${OPENSSL_VERSION} ${OPENSSL_TAR} Python-${PYTHON_VERSION} ${PYTHON_TAR}

# Verify the installation
echo "Verifying the Python installation..."
python3.8 -c "import ssl; print('OpenSSL version used by Python:', ssl.OPENSSL_VERSION)"

echo "OpenSSL ${OPENSSL_VERSION} and Python ${PYTHON_VERSION} installation complete."

