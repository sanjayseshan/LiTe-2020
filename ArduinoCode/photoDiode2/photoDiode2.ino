int sensorPin = A0; // select the input pin for LDR(s)
int sensorPin2 = A1; 
int sensorPin3 = A2; 
int sensorPin4 = A3; 
int sensorPin5 = A4; 

int sensorValue = 0; // variable(s) to store the value coming from the sensor
int sensorValue2 = 0;
int sensorValue3 = 0; 
int sensorValue4 = 0; 
int sensorValue5 = 0;

void setup() {
    Serial.begin(9600); //sets serial port for communication
    pinMode(LED_BUILTIN, OUTPUT);
}
void loop() {
    sensorValue = analogRead(sensorPin); // read the value(s) from the sensor(s)
    sensorValue2 = analogRead(sensorPin2);
    sensorValue3 = analogRead(sensorPin3);
    sensorValue4 = analogRead(sensorPin4); 
    sensorValue5 = analogRead(sensorPin5); 

    Serial.print(sensorValue); //prints the values coming from the sensors on the screen
    Serial.print(","); 
    Serial.print(sensorValue2); 
    Serial.print(","); 
    Serial.print(sensorValue3); 
    Serial.print(","); 
    Serial.print(sensorValue4); 
    Serial.print(","); 
    Serial.println(sensorValue5); 

}
