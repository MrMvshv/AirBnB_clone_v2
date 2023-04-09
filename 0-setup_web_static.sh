#!/usr/bin/env bash
# sets up web servers for deployment of web_static
# script should run as sudo

# installing nginx
apt-get -y update
apt-get -y install nginx

# creating folders
mkdir -p /data/web_static/releases/test/ 
mkdir -p /data/web_static/shared/

# fake html file
cat <<EOL >> /data/web_static/releases/test/index.html
<html>
  <head>
  </head>
  <body>
    Holberton School
  </body>
</html>
EOL

# symbolic link
ln -sf /data/web_static/releases/test/ /data/web_static/current

# ownership of folder tree to ubuntu:ubuntu
chown -R ubuntu:ubuntu /data/

# nginx config
sed -i '38i\\tlocation /hbnb_static/ {\n\t\talias /data/web_static/current/;\n\t}\n' /etc/nginx/sites-available/default

service nginx restart
