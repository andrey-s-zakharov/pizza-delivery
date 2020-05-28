`cd /vagrant`
`python3.7 -m venv env`
`source env/bin/activate`
`sudo apt-get update`
`sudo apt-get install mysql-server`
`sudo systemctl start mysql`
`sudo apt-get install python-mysqldb`
`sudo apt install python3-dev`
`sudo apt install python3-dev libmysqlclient-dev`
`pip install mysqlclient`

mysql
CREATE DATABASE pizza_delivery;
CREATE USER 'pizza_delivery'@'%' IDENTIFIED WITH mysql_native_password BY 'pizza_delivery';
GRANT ALL ON pizza_delivery.* TO 'pizza_delivery'@'%';
FLUSH PRIVILEGES;

`sudo nano /etc/mysql/pizza_delivery.cnf`

Paste below to cnf file
```
[client]
database = pizza_delivery
user = pizza_delivery
password = pizza_delivery
default-character-set = utf8
```

`sudo systemctl daemon-reload`
`sudo systemctl restart mysql`


