#include <stdio.h>
#include <stdlib.h>

static void deadcode(void)
{
  system("/bin/sh");
}

int main(void)
{
  unsigned int *pointer = NULL;
  puts("Hello, hackers!");
  puts("Give me a pointer to jump to: ");

  scanf("%x", &pointer);

  printf("Execution will now jump to the given pointer (%x)", pointer);

  void (*func_ptr)(void) = (void (*)(void)) pointer;

  func_ptr();

  return 0;
}
