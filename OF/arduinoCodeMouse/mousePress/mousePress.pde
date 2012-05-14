char inByte = 0;         // incoming serial byte

void setup()
{
  // start serial port at 9600 bps:
  Serial.begin(9600);
  pinMode(7, OUTPUT);   // digital sensor is on digital pin 2
  
  pinMode(13, OUTPUT);  
  digitalWrite(13, HIGH);   // set the LED on
  delay(1000);              // wait for a second
  digitalWrite(13, LOW);    // set the LED off
  delay(1000);  
}

void loop()
{
  // if we get a valid byte, read analog ins:
  while(Serial.available() > 0) {
    digitalWrite(13, HIGH); 
    // get incoming byte:
    inByte = Serial.read();
    if(inByte=='p'){
      digitalWrite(7, HIGH);   // set the LED on
      delay(500);              // wait for a second
      digitalWrite(7, LOW);    // set the LED off
      delay(500);    
    }
    // delay 10ms to let the ADC recover:
    delay(10);
  }
  digitalWrite(13, LOW);
}


