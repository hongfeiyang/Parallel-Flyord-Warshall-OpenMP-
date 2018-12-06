CC     = gcc
CFLAGS = -fopenmp -o3 -std=gnu99 -lm
EXE    = proj1
OBJ    = proj1.o

$(EXE): $(OBJ)
	$(CC) $(CFLAGS) -o $(EXE) $(OBJ)
clean:
	rm -f $(OBJ)
CLEAN: clean
	rm -f $(EXE)
cleanly: all clean
