int LEDS[] = {3, 5, 6};
int leds_num = sizeof(LEDS) / sizeof(LEDS[0]);

void setup()
{
    Serial.begin(9600);
    for (int i = 0; i < leds_num; i++)
    {
        pinMode(LEDS[i], OUTPUT);
    }
}

void loop()
{
    if (Serial.available())
    {
        String command = Serial.readString();
        if (command[0] == 'C')
        {
            command = command.substring(2);
            int val = command.toInt();
            for (int i = 0; i < leds_num; i++)
            {
                Serial.println(val);
                analogWrite(LEDS[i], map(val, 0, 100, 0, 255));
            }
        }
    }
}