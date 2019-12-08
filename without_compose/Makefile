appname=pyapp
timeref=`date +%y%m%d_%H%M`
be_name=redis
fe_name=pyapp_cities

create_net:
	@echo "[Network] :: Network will be == $(appname)net_$(timeref)"
	docker network create -d bridge $(appname)net_$(timeref)

build_fe:
	@echo "[Frontend] :: Generate image with name, $(appname)fe_$(timeref)"
	docker build --rm -t $(appname)fe_$(timeref):latest -f Dockerfile.frontend .

build_be:
	@echo "[Backend] :: Generate image with name, $(appname)be_$(timeref)"
	docker build --rm -t $(appname)be_$(timeref):latest -f Dockerfile.backend .


start_pyapp: create_net build_be build_fe
	@echo "[Start_Backend_Service] :: Starting Redis backend container..."
	docker container run --rm -d -it \
		-p 6379:6379 \
		--network $(appname)net_$(timeref) \
	       	--name $(be_name) \
		$(appname)be_$(timeref)
	@echo "[Start_Frontend_Service] :: Starting Python (Flask-based) frontend container..."
	docker container run --rm -d -it \
		-p 80:80 \
		--network $(appname)net_$(timeref) \
	       	--name $(fe_name) \
		$(appname)fe_$(timeref)

stop_pyapp:
	@echo "[Terminate_Service] :: Stop the running containers and remove the network..."
	docker container stop $(fe_name)
	docker container stop $(be_name)
	docker network rm $(appname)net_$(timeref)
