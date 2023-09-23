TARGETS:= $(patsubst %.c,%.out,$(wildcard *.c))

all: $(TARGETS)
.PHONY: all
	
$(TARGETS): %.out: %.c
	gcc -o $@ $<

clean:
	rm -rf *.out
.PHONY: clean

clean_latex:
	rm -f *.aux *.log *.out *.toc *.fdb_latexmk *.fls *.pdf *.synctex.gz
.PHONY: clean_latex

clean_all: clean clean_latex
.PHONY: clean_all

