## ElasticSearch Curator


### install

`pip install elasticsearch-curator`


Actionfileにjobを書き下してcuratorで呼ぶ形で使う


### NExt

docker cronの使用法

apt-get cronでinstall
cron.dにfileをセット

```
crontab /etc/cron.d/list-cron
chmod 0644 /etc/cron.d/list-cron
cron -f
```


cron = 最小単位毎分


jobは直接セットできない = root権限がひつよう
