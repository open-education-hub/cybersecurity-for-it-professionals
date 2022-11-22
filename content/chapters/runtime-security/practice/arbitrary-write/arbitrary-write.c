#include <stdlib.h>
#include <stdio.h>

#define READ_LENGTH 4

int main(void) {
  char alphabet[] = "ABCDEFGHIJKLMNOPQRSTUVWXYZ";
  char public_buffer[] = "........";
  int index = 0;

  printf("The alphabet is: %s\n", alphabet);
  printf("The public buffer is: %s\n", public_buffer);

  printf("Input index at which to start reading:\n");
  scanf("%d", &index);

  read(0, public_buffer + index, READ_LENGTH);

  printf("The alphabet is: %s\n", alphabet);
  printf("The public buffer is: %s\n", public_buffer);

  return 0;
}
