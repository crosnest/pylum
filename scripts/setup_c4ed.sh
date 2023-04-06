# Install c4ed
git clone https://github.com/chain4energy/c4e-chain
cd c4e-chain
git checkout v1.2.0
make install

# Remove c4ed git folder
cd .. && rm -rf c4e-chain


# Add symlink of c4ed
sudo ln -s ~/go/bin/ce4ed /usr/local/bin/c4ed

# Export PATH
if [[ "$OSTYPE" == "darwin"* ]]; then
  export GOPATH=$HOME/go
  export PATH=$GOPATH/bin:$PATH
fi

# Clear the existing configuration
rm -rf ~/.c4ed*

# Add keys
echo "erase weekend bid boss knee vintage goat syrup use tumble device album fortune water sweet maple kind degree toss owner crane half useless sleep" |c4ed keys add validator --recover

echo "account snack twist chef razor sing gain birth check identify unable vendor model utility fragile stadium turtle sun sail enemy violin either keep fiction" | c4ed keys add bob --recover

# Start c4ed local node

# Configure node
c4ed init --chain-id=testing testing
c4ed add-genesis-account $(c4ed keys show validator -a) 100000000000000000000000stake 
c4ed add-genesis-account $(c4ed keys show bob -a) 100000000uc4e
c4ed gentx validator 10000000000000000000000stake --chain-id testing
c4ed collect-gentxs

# Enable rest-api
sed -i '/^\[api\]$/,/^\[/ s/^enable = false/enable = true/' ~/.c4ed/config/app.toml
