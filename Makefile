all: main

main:
	python3 main.py

install:
	pip3 install -r requirements.txt

clean:
	rm -f tempCodeRunnerFile.py