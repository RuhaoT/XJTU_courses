TARGETS:= $(patsubst %.c,%.out,$(wildcard *.c))

all: $(TARGETS)
.PHONY: all
	
$(TARGETS): %.out: %.c
	gcc -o $@ $<

clean:
	rm -rf *.out
.PHONY: clean


