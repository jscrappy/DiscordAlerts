echo "Installing pip"
apt install python3-pip

echo "Installing discord API"
python3 -m pip install discord.py
echo "Moving to executable Directory"
cp $PWD/dca.py /usr/local/bin/dca
chmod a+x /usr/local/bin/dca
