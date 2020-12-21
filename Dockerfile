FROM alpine:3

RUN apk add openssh-client
RUN apk add python3

COPY fleet /app/fleet
RUN chmod 700 /app/fleet/.ssh

COPY scp-files /app/scp-files

COPY src /app/src

CMD [ "python3", "/app/src/main.py", "fleet=fleet", "scp=~/utils/config-dev.properties" ]
