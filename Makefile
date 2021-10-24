export PYTHONPATH = .

test:
	python3 -m unittest game/test_*.py

all: assets/solutions.gif assets/steps.gif assets/pbox.svg assets/sbox.svg challenge/hello docs/index.html

docs/graph.svg: docs/graph.py
	docs/graph.py | dot -T svg > docs/graph.svg

docs/index.html: docs/definition.py docs/εὕρηκα.py docs/graph.svg docs/notes.py
	docs/notes.py > docs/index.html

εὕρηκα: docs/εὕρηκα.py
	docs/εὕρηκα.py

example:
	@tools/reverse-level2.py 'Hello, World!' | tools/forward.py

perftest:
	@pypy3 tools/reverse.py 8192 ZGlzdGluZ3Vpc2hl perftest > /dev/null
	@pypy3 tools/reverse.py 8192 ZCBub3Qgb25seSBi perftest > /dev/null
	@pypy3 tools/reverse.py 8192 eSByZWFzb24gYnV0 perftest > /dev/null
	@pypy3 tools/reverse.py 8192 IGJ5IHBhc3Npb24= perftest > /dev/null

assets/solutions.txt:
	tools/reverse.py 800 'Hello, World!!!!' > assets/solutions.txt

assets/solutions.gif: assets/solutions.txt
	@#tools/animate-solutions.py < assets/solutions.txt > assets/solutions.gif
	tools/animate-solutions.py < assets/solutions.txt | convert - -scale 200%% -strip assets/solutions.gif

assets/steps.gif:
	@#tools/reverse-level2.py "Hello, World!" | tools/animate-steps.py > assets/steps.gif
	tools/reverse-level2.py 'Hello, World!' | tools/animate-steps.py | convert - -scale 200%% -strip assets/steps.gif

assets/pbox.dot:
	tools/pbox.py > assets/pbox.dot
assets/sbox.dot:
	tools/sbox.py > assets/sbox.dot

assets/pbox.svg: assets/pbox.dot
	dot -T svg < assets/pbox.dot > assets/pbox.svg
assets/sbox.svg: assets/sbox.dot
	dot -T svg < assets/sbox.dot > assets/sbox.svg

unroll:
	tools/unroll.py

challenge/hello: challenge/hello.cpp
	cd challenge; clang hello.cpp -o hello

clean:
	@rm -rf game/__pycache__ tools/__pycache__
	@rm -f assets/solutions.txt assets/solutions.gif assets/steps.gif assets/pbox.dot assets/pbox.svg assets/sbox.dot assets/sbox.svg
	@rm -f challenge/hello
	@rm -f docs/graph.svg docs/index.html
