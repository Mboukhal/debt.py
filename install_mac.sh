#!/bin/bash

function install_python()
{
	echo "Python3 installing [ y/n ]: "
	read install
	if [ $install = "y" ] ; then
		brew install python3
	else
		exit 127
	fi
}

function install_brew()
{
	echo "brew not installed"
	echo "brew installing [ y/n ]: "
	read install
	if [ $install = "y" ] ; then
		/bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)"
	else
		exit 127
	fi
}

if python3 --version > /dev/null; then
    echo "python3 installed"
else
    echo "python3 not installed"
	if brew -v 2> /dev/null ; then
		echo "brew not installed"
		install_python
	else
		install_brew
		install_python
	fi
		
fi

mkdir ~/debt
cp debt.py ~/debt
python3 -m pip install pandas
echo "alias debt=\'python3 ~/debt/debt.py\'" >> ~/.zshrc
source ~/.zshrc
