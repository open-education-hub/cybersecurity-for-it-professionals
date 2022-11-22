#include <stdlib.h>
#include <stdio.h>

#define OK_SIZE 4

int main(void) {
  int b = 0;
  char a[] = "abcd";

  printf("a (initial): %s\n", a);
  printf("b (initial): %d\n", b);

  printf("\nRead some value into variable a:\n");
  read(0, a, OK_SIZE);
  printf("\n");

  printf("a (final): %s\n", a);
  printf("b (final): %d\n", b);

  return 0;
}
