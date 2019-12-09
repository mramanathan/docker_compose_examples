appname=pyapp
be_name=redis
fe_name=pyapp_cities

create_net:
	@echo "[Network] :: Network will be == $(appname)net"
	docker network create -d bridge $(appname)net

build_fe:
	@echo "[Frontend] :: Generate image with name, $(appname)fe"
	docker build --rm -t $(appname)fe:latest -f Dockerfile.frontend .

build_be:
	@echo "[Backend] :: Generate image with name, $(appname)be"
	docker build --rm -t $(appname)be:latest -f Dockerfile.backend .


start_pyapp: create_net build_be build_fe
	@echo "[Start_Backend_Service] :: Starting Redis backend container..."
	docker container run --rm -d -it \
		-p 6379:6379 \
		--network $(appname)net \
	       	--name $(be_name) \
		$(appname)be
	@echo "[Start_Frontend_Service] :: Starting Python (Flask-based) frontend container..."
	docker container run --rm -d -it \
		-p 80:80 \
		--network $(appname)net \
	       	--name $(fe_name) \
		$(appname)fe

stop_pyapp:
	@echo "[Terminate_Service] :: Stop the running containers and remove the network..."
	docker container stop $(fe_name)
	docker container stop $(be_name)
	docker network rm $(appname)net
