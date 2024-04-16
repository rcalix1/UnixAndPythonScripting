#!/bin/sh

#########################################################################
#taken from https://tome.crates.im/nemo/8551cf12d12c47048aa0f4a2705d2ccd#
#########################################################################

set -euo pipefail

# change this based on ur spec, slurm messes of the results of $(nproc)
export CORES=32

# your prefix string _must_ be fullpath and should not contain trailing slashes
# please ensure any env variables used here are actually set
# do not run this script as root as:
# 1) you shouldnt be running commands as root that dont need escalated privileges to begin with
# 2) a mistake in the prefix could delete data from /
export PREFIX=$HOME/.local/our_prefix

# you can change all of these to HEAD or whatever commit you like
export LIBFFI_COMMIT=b0304e9
export OPENSSL_COMMIT=b372b1f764
export TCL_COMMIT=e01408c9f8
export TK_COMMIT=e184e0fa0
export CPYTHON_COMMIT=ced359855e

#################################################################
#do not touch beyond this point unless you know what youre doing#
#################################################################

export PKG_DIR=$PREFIX/.pkg_cache
rm -rf $PKG_DIR
mkdir -p $PKG_DIR
mkdir -p $PREFIX/env

echo export PATH=$PREFIX/bin:\$PATH > $PREFIX/env/activate
echo export PKG_CONFIG_PATH=$PREFIX/lib/pkgconfig >> $PREFIX/env/activate
echo export LD_LIBRARY_PATH=$PREFIX/lib:\$LD_LIBRARY_PATH >> $PREFIX/env/activate
source $PREFIX/env/activate

cd $PKG_DIR
git clone https://github.com/libffi/libffi
cd libffi
git reset --hard $LIBFFI_COMMIT
./configure --prefix=$PREFIX
make -j$CORES
make -j$CORES install

cd $PKG_DIR
git clone https://github.com/openssl/openssl
cd openssl
git reset --hard $OPENSSL_COMMIT
./config --prefix=$PREFIX
make -j$CORES
make -j$CORES install

cd $PKG_DIR
git clone https://github.com/tcltk/tcl
cd tcl
git reset --hard $TCL_COMMIT
cd unix
./configure --prefix=$PREFIX
make -j$CORES
make -j$CORES install

cd $PKG_DIR
git clone https://github.com/tcltk/tk
cd tk
git reset --hard $TK_COMMIT
cd unix
./configure --prefix=$PREFIX
make -j$CORES 
make -j$CORES install

cd $PKG_DIR
git clone https://github.com/python/cpython
cd cpython
git reset --hard $CPYTHON_COMMIT
./configure --prefix=$PREFIX --with-ensurepip --enable-optimizations
make -j$CORES
make -j$CORES install

python3 -m venv $PREFIX/venv/nightly
source $PREFIX/venv/nightly/bin/activate
pip3 install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/cu121
pip3 install torcheval
pip3 install jupyter
python3 -m ipykernel install --name our_prefix --user
echo source $PREFIX/venv/nightly/bin/activate >> $PREFIX/env/activate

echo to activate the new environment, source $PREFIX/env/activate
echo to make the new environment the default, add \"source $PREFIX/env/activate\" to your \~/.profile
echo side effects caused by this script are bounded to \"$PREFIX\"
