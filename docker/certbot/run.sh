#!/bin/bash
sudo certbot certonly \
    --dns-cloudflare \
    --dns-cloudflare-credentials ./cloudflare.ini \
    --preferred-challenges dns-01 \
    -d 'example.de' \
    -d '*.example.de' \
    --server https://acme-v02.api.letsencrypt.org/directory 
