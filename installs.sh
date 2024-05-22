echo "Make sure you are running as root."
read ABC
echo "Installing Tor Services..."
pacman -S macchanger tor-runit tor-browser vim
git clone https://aur.archlinux.org/obfs4proxy
cd obfs4proxy
mkpkg -irs
cd ..

echo "Ready to edit tor config?"
read ACB
vim /etc/tor/torrc

echo "Linking Services..."
ln -s /etc/sv/tor /var/service
sv restart tor

mv .bashrc ..
