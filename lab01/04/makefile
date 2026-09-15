all: main.exe
main.exe: message.o hello.o goodbye.o main.o
	g++ message.o hello.o goodbye.o main.o -o main.exe 
main.o: main.cpp hello.h goodbye.h
	g++ -c main.cpp -o main.o
message.o: message.h message.cpp
	g++ message.cpp -o message.o -c
hello.o: message.h hello.h hello.cpp
	g++ hello.cpp -o hello.o -c
goodbye.o: message.h goodbye.h goodbye.cpp
	g++ goodbye.cpp -o goodbye.o -c

