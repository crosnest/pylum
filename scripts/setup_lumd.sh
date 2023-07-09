# Install lumd
git clone https://github.com/lum-network/chain
cd chain
git checkout v1.4.5
make install

# Remove lumd git folder
cd .. && rm -rf chain


# Add symlink of lumd
sudo ln -s ~/go/bin/lumd /usr/local/bin/lumd

# Export PATH
if [[ "$OSTYPE" == "darwin"* ]]; then
  export GOPATH=$HOME/go
  export PATH=$GOPATH/bin:$PATH
fi

# Clear the existing configuration
rm -rf ~/.lum*

# Add keys
echo "erase weekend bid boss knee vintage goat syrup use tumble device album fortune water sweet maple kind degree toss owner crane half useless sleep" |lumd keys add validator --recover

echo "account snack twist chef razor sing gain birth check identify unable vendor model utility fragile stadium turtle sun sail enemy violin either keep fiction" | lumd keys add bob --recover

# Start lumd local node

# Configure node
lumd init --chain-id=testing testing
lumd add-genesis-account $(lumd keys show validator -a) 100000000000000000000000stake 
lumd add-genesis-account $(lumd keys show bob -a) 100000000ulum
lumd gentx validator 10000000000000000000000stake --chain-id testing
lumd collect-gentxs

# Enable rest-api
sed -i '/^\[api\]$/,/^\[/ s/^enable = false/enable = true/' ~/.lumd/config/app.toml
