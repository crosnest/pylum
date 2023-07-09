#!/bin/sh

export CHAIN_URL=https://github.com/lum-network/chain
export CHAIN_VERSION=v1.4.5

docker build  --build-arg VERSION=${CHAIN_VERSION} --build-arg REPOSITORY=${CHAIN_URL} \
  -t lumchain_serve ./scripts/

docker run --name testchain -v ${PWD}:/test -d -p 1317:1317 -p 4500:4500 -p 26657:26657 -t --rm lumchain_serve chain serve --skip-proto

docker exec testchain bash -c "apt-get update && apt-get install -y python3-pip"
docker exec testchain bash -c "pip install tox==3.25.1 poetry"
#docker exec testchain bash -c "cd /test && poetry run make new-env"

while [ -z "$(docker exec testchain curl -sv localhost:26657/health )" ] ; do sleep 1; done

docker exec testchain bash -c "cd /test && tox -e test-integration"

#docker stop testchain