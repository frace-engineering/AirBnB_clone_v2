#!/usr/bin/env bash
# Script that prepares the webstatic for deployment

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test

echo "!DOCTYPE html>
<html>
	<head>
	</head>
	<body>
		<p>Holberton School</p>
	</body>
</html>
" | tee /data/web_static/releases/test/index.html > /dev/null

sudo ln -s /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/

echo "
server {
	listen 80;
	server_name $HOSTNAME;

	location /hbnb_static {
		alias /data/web_static/current;
	}
}
" | tee -a /etc/nginx/sites-available/default > /dev/null

sudo nginx -t
sudo service nginx restart
