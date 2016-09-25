# Sample: ElasticSearch and utils on CentOS6.x


usage

```
git clone https://github.com/uzuna/elasticseach-centos6.git

# elastic plugin をインストールした fluent のimageを作成
cd elasticseach-centos6/fluent
make build

# elastic search諸々起動
cd ../
docker-compose up -d

# elasticsearch-curatorをインストールした python のimageを作成
cd ../curator
make build

# curator起動
docker-compose up

```
