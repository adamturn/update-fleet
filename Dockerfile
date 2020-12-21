FROM alpine:3

RUN apk add openssh-client
RUN apk add python3

COPY fleet /app/fleet
COPY scp-files /app/scp-files
COPY src /app/src

RUN mkdir ~/.ssh && \
    chmod 700 ~/.ssh && \
    # TODO: inject key some other way
    cp -a ~/.ssh/id_rsa ~/.ssh/id_rsa

CMD [ "python3", "/app/src/main.py", "fleet=fleet", "scp=~/utils/config-dev.properties" ]
