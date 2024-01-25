#include <stdio.h>

int main() {
    short numbers[10];

    // Pildome masyvą skaičiais
    for (int i = 0; i < 10; i++) {
        numbers[i] = i; // Galite keisti reikšmes pagal savo poreikius
    }

    // Adresas, kuriuo pradedame saugoti skaičius
    short* address = (short*)0x20000000;

    // Nukopijuojame masyvą į atmintį
    for (int i = 0; i < 10; i++) {
        *address = numbers[i];
        address++;
    }

    // Patikriname, ar skaičiai buvo sėkmingai saugomi atmintyje
    address = (short*)0x20000000;
    for (int i = 0; i < 10; i++) {
        printf("Adresas: 0x%X, Reikšmė: %d\n", address, *address);
        address++;
    }

    return 0;
}
