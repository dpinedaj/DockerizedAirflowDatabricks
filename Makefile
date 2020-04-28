up:
	cd app && docker-compose up
	
build:
	cd app && docker-compose up --build

down:
	cd app && docker-compose down

clean:
	cd app && docker-compose down -v