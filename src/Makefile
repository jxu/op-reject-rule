# Compile C or C++ based on problem number, ex. `make 150`

CC = gcc
CFLAGS = -O3 -Wall -Wextra -std=gnu99 -pedantic -Wno-unused-result
LDLIBS = -lm  # g++ links automatically

CXX = g++
CXXFLAGS = -O3 -Wall -Wextra -std=c++2a -pedantic

FC = f77
FFLAGS = -O3 -Wall -Wextra

% : %.c
	$(CC) $(CFLAGS) -o $@ $< $(LDLIBS)

% : %.cpp
	$(CXX) $(CXXFLAGS) -o $@ $<

# different binary name to distingush Fortran output
%f: %.f
	$(FC) $(FFLAGS) -o $@ $<

.PHONY: clean
clean:
	find . -type f -executable -not -name '*.sh' -delete
