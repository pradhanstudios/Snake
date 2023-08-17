all: main

main:
	python3 src/main.py

install:
	pip3 install -r requirements.txt

clean:
	rm -f tempCodeRunnerFile.py