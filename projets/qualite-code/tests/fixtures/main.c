//#include <stdio.h>

int main(void)
{
    int vehicle_speed = 50;
    float battery_level = 87.5F;
    char driving_mode = 'N';

    //if(driving_mode)
    //  printf("Driving mode is set to: %c\n", driving_mode);
    printf("Vehicle speed: %d km/h\n", vehicle_speed);
    printf("Battery level: %.1f %%\n", battery_level);
    printf("Driving mode: %c\n", driving_mode);

    return 0;
}
