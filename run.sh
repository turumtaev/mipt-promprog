docker pull mongo
docker pull rabbitmq
docker-compose up -d mongo rabbitmq
sleep 10
docker-compose up producer consumer
