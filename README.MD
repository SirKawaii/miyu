# Miyu みゆ!

Miyu is a smol bot to get the public ip from my current minecraft server.

## commands 

` !miyu hola `

` !miyu ip `

## docker deploy 

* remember change your discord token key in the .env file

` docker build -t miyu:0.1 . `

` docker run --name miyu -d miyu:0.1 `