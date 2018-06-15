#define clk 8
#define AB 9
String inputString;

byte num2Byte(char num){
  byte numBin=B11111111;
  switch (num){
   case '0':
            //abcdefg.
      numBin=B00000011;
      break;
   case '1':
            //abcdefg.
      numBin=B10011111;
      break;
   case '2':
           //abcdefg.
      numBin=B00100101;
      break;
   case '3':
      numBin=B00001101;
      break;
   case '4':
      numBin=B10011001;
      break;
   case '5':
      numBin=B01001001;
      break;
   case '6':
      numBin=B01000001;
      break;
   case '7':  
            //abcdefg.
      numBin=B00011111;
      break;
   case '8':
            //abcdefg.
      numBin=B00000001;
      break;
   case '9':
            //abcdefg.
      numBin=B00011001;
      break;
  }
  return numBin;
}

void setup() {
  Serial.begin(38400);
  pinMode(clk,OUTPUT);
  pinMode(AB,OUTPUT);
  for(int i = 2; i<8; i++){
    pinMode(i,OUTPUT);
  }
}

void loop() {
  delay(5);
}

void showValues(char leds[7],char num){
  shiftOut(AB, clk, LSBFIRST,num2Byte(num));
  for(int i = 0; i<6;i++){
    bool OnOff = false;
    if(leds[i]=='1'){OnOff = true;} 
    digitalWrite(i+2,OnOff);
  }
}
void serialEvent() {
  while (Serial.available()) {
    // get the new byte:
    char inChar = (char)Serial.read();
    // add it to the inputString:
    inputString += inChar;
    // if the incoming character is a newline, set a flag so the main loop can
    // do something about it:
    if (inChar == ';') {
        Serial.println(inputString);
        char energia [7];
        inputString.substring(5,13).toCharArray(energia,7);
        Serial.println(energia);
        char restantes = (inputString.substring(20,21))[0];
        showValues(energia,restantes);
        inputString="";
    }
  }
}


