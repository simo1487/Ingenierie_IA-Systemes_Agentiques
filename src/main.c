#include <stdio.h>

int main(void)
{
    int vehicle_speed = 50;
    float battery_level = 87.5F;
    char driving_mode = 'N';

    printf("Vehicle speed: %d km/h\n", vehicle_speed);
    printf("Battery level: %.1f %%\n", battery_level);
    printf("Driving mode: %c\n", driving_mode);

    return 0;
}
