FROM alpine/git AS CLONE
RUN mkdir /temp
WORKDIR /temp

ARG VERSION
ARG REPOSITORY

RUN git clone --branch ${VERSION} ${REPOSITORY}


FROM ignitehq/cli:v0.26.1 AS BUILD
COPY --from=CLONE /temp/c4e-chain /c4e-chain
WORKDIR /c4e-chain
USER root
RUN chmod -R 777 /c4e-chain/go.mod
RUN ignite chain build
CMD [  "chain","serve","--skip-proto" ]