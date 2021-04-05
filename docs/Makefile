# Modern InterWebz!

index.html: tables.py graph.svg
	./tables.py > index.html

graph.svg: graph.py
	./graph.py | dot -T svg > graph.svg

clean:
	rm -f graph.svg index.html
