#include <stdlib.h>
#include <stdio.h>

int main(void) {
  char secret_password[] = "This password is hardcoded and not normally visible.";
  char public_info[] = "Public info.";
  int index = 0;

  printf("The public string is: %s\n", public_info);

  printf("Input index to print from:\n");
  scanf("%d", &index);

  printf("%s", public_info + index);

  return 0;
}
