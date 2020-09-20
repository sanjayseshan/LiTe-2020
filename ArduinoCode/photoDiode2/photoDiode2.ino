int sensorPin = A0; // select the input pin for LDR(s)
int sensorPin2 = A1; 
int sensorPin3 = A2; 
int sensorPin4 = A3; 
int sensorPin5 = A4; 
int sensorPin6 = A5; // select the input pin for LDR(s)
int sensorPin7 = A6; 
int sensorPin8 = A7; 
int sensorPin9 = A8; 
int sensorPin10 = A9; 

int sensorValue = 0; // variable(s) to store the value coming from the sensor
int sensorValue2 = 0;
int sensorValue3 = 0; 
int sensorValue4 = 0; 
int sensorValue5 = 0;
int sensorValue6 = 0;
int sensorValue7 = 0; 
int sensorValue8 = 0; 
int sensorValue9 = 0;
int sensorValue10 = 0;

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
    sensorValue6 = analogRead(sensorPin6); // read the value(s) from the sensor(s)
    sensorValue7 = analogRead(sensorPin7);
    sensorValue8 = analogRead(sensorPin8);
    sensorValue9 = analogRead(sensorPin9); 
    sensorValue10 = analogRead(sensorPin10); 
    
    Serial.print(sensorValue); //prints the values coming from the sensors on the screen
    Serial.print(","); 
    Serial.print(sensorValue2); 
    Serial.print(","); 
    Serial.print(sensorValue3); 
    Serial.print(","); 
    Serial.print(sensorValue4);
//    Serial.println(to_string(sensorValue)+","+to_string(sensorValue2)+","+to_string(sensorValue3)+","+to_string(sensorValue4)); 
    Serial.print(","); 
    Serial.print(sensorValue5); 
    Serial.print(","); 
    Serial.print(sensorValue6); //prints the values coming from the sensors on the screen
    Serial.print(","); 
    Serial.print(sensorValue7); 
    Serial.print(","); 
    Serial.print(sensorValue8); 
    Serial.print(","); 
    Serial.print(sensorValue9);
//    Serial.println(to_string(sensorValue)+","+to_string(sensorValue2)+","+to_string(sensorValue3)+","+to_string(sensorValue4)); 
    Serial.print(","); 
    Serial.println(sensorValue10); 

}
