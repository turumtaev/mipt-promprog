docker pull mongo
docker pull rabbitmq
docker-compose up -d mongo rabbitmq
docker-compose up producer consumer
