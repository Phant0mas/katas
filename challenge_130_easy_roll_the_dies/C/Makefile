CC = gcc
CFLAGS = -g -Wall -std=c99
TARGET = roll_the_dice

all: $(TARGET)

$(TARGET): $(TARGET).c
	$(CC) $(CFLAGS) -o $(TARGET) $(TARGET).c

clean:
	rm -rf *o $(TARGET)
