#include <stdio.h>
#include <string.h>

unsigned bin_to_decimal(const char *bin);

int main() {
    const char *source = "11";
    const unsigned result = bin_to_decimal(source);
    printf("%d\n",result);
}

unsigned bin_to_decimal(const char *bin){
    unsigned result = 0;
    int i;
    unsigned length = strlen(bin);
    for (i = length - 1; i >= 0; i--){
        if (bin[i] == '1'){
            result = (1 << (length - i - 1)) | result;
        }
    }
    return result;
}


