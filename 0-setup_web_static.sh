#!/usr/bin/env bash
# Script that prepares the webstatic for deployment

sudo apt-get update
sudo apt-get install -y nginx

sudo mkdir -p /data/web_static/shared/
sudo mkdir -p /data/web_static/releases/test/
fake_file="/data/web_static/releases/test/index.html"
echo -e "<html>\n\t<head>\n\t</head>\n\t<body>\n\t\tHolbertonSchool\n\t</body>\n<\html>" | sudo tee $fake_file > /dev/null

sudo ln -sf /data/web_static/releases/test/ /data/web_static/current
sudo chown -R ubuntu:ubuntu /data/


config_file=/etc/nginx/sites-available/default
sed -i '55a \ \tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' $config_file

sudo nginx -t
sudo service nginx restart
