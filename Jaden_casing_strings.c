#include <stdio.h>
#include <stdlib.h>

char *to_jaden_case (char *jaden_case, const char *string)
{
  int i; 
  for (i = 0; string[i] != '\0'; i++){
    jaden_case[i] = string[i];
    if (jaden_case[i-1] == 0x20){
      jaden_case[i] &= ~0x20;
    }
  }
  jaden_case[0] &= ~0x20;
  jaden_case[i] = '\0';
  return jaden_case;
}

int main() {
    char s[] = "Test string WITH multIPle casings";
    char *jaden = (char*) malloc(sizeof(s));
    jaden = to_jaden_case(jaden, s);
    printf("%s", s);
    printf("\n");
    printf("%s", jaden);
    free(jaden);
    return 0;
}
