export PYTHONPATH = .

test:
	python3 -m unittest lib/test_*.py

solutions:
	python3 example/solutions.py

hello: hello.cpp
	gcc hello.cpp -o hello

say-hello: hello
	./hello

pbox/graph.svg:
	python3 pbox/graph.py > pbox/graph.dot
	dot -T svg -o pbox/graph.svg pbox/graph.dot

animation/forward.gif:
	python3 animation/frames.py | ./animation/ppmtogif.sh
	gifsicle --optimize --loop --scale 2 build/*.gif > animation/forward.gif

unroll:
	python3 pbox/unroll.py
	python3 sbox/unroll.py
	python3 mixer/unroll.py

clean:
	@rm -rf lib/__pycache__
	@rm -rf build
	@rm -f hello
