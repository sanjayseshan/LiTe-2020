int sensorPin = A0; // select the input pin for LDR
int sensorPin2 = A1; // select the input pin for LDR
int sensorPin3 = A2; // select the input pin for LDR
int sensorPin4 = A3; // select the input pin for LDR
int sensorPin5 = A4; // select the input pin for LDR

int sensorValue = 0; // variable to store the value coming from the sensor
int sensorValue2 = 0; // variable to store the value coming from the sensor
int sensorValue3 = 0; // variable to store the value coming from the sensor
int sensorValue4 = 0; 
int sensorValue5 = 0; // variable to store the value coming from the sensor

void setup() {
Serial.begin(9600); //sets serial port for communication
pinMode(LED_BUILTIN, OUTPUT);
}
void loop() {
sensorValue = analogRead(sensorPin); // read the value from the sensor
sensorValue2 = analogRead(sensorPin2); // read the value from the sensor
sensorValue3 = analogRead(sensorPin3); // read the value from the sensor
sensorValue4 = analogRead(sensorPin4); // read the value from the sensor
sensorValue5 = analogRead(sensorPin5); // read the value from the sensor

Serial.print(sensorValue); //prints the values coming from the sensor on the screen
Serial.print(","); //prints the values coming from the sensor on the screen
Serial.print(sensorValue2); //prints the values coming from the sensor on the screen
Serial.print(","); //prints the values coming from the sensor on the screen
Serial.print(sensorValue3); //prints the values coming from the sensor on the screen
Serial.print(","); //prints the values coming from the sensor on the screen
Serial.print(sensorValue4); //prints the values coming from the sensor on the screen
Serial.print(","); //prints the values coming from the sensor on the screen
Serial.println(sensorValue5); //prints the values coming from the sensor on the screen

digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
  
//delay(100);

}
