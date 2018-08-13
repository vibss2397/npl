/*
 * 
 * 2018 August 1
 * Load Cell HX711 Module Interface with Arduino to measure weight in grams
 Arduino 
 pin 
 8 -> HX711 CLK
 9 -> DOUT
 5V -> VCC
 GND -> GND
 
 Most any pin on the Arduino Uno will be compatible with DOUT/CLK.
 The HX711 board can be powered from 2.7V to 5V so the Arduino 5V power should be fine.
*/
 
#include "HX711.h"  //You must have this library in your arduino library folder
#include <LiquidCrystal.h>

#define DOUT  9
#define CLK  8
 
HX711 scale(DOUT, CLK);
 
//Change this calibration factor as per your load cell once it is found you many need to vary it in thousands
float calibration_factor = -5818.20; //-106600 worked for my 40Kg max scale setup 

const int rs = 12, en = 11, d4 = 5, d5 = 4, d6 = 3, d7 = 1;
LiquidCrystal lcd(rs, en, d4, d5, d6, d7);
 
//=============================================================================================
//                         SETUP
//=============================================================================================
void setup() {
    // set up the LCD's number of columns and rows:
  lcd.begin(16, 2);
  // Print a message to the LCD.
  lcd.print("digital weight");
  lcd.setCursor(0, 1);
  lcd.print("-vibss");
  Serial.begin(9600);
  Serial.println("HX711 Calibration");
  Serial.println("Remove all weight from scale");
  Serial.println("After readings begin, place known weight on scale");
  Serial.println("Press a,s,d,f to increase calibration factor by 10,100,1000,10000 respectively");
  Serial.println("Press z,x,c,v to decrease calibration factor by 10,100,1000,10000 respectively");
  Serial.println("Press t for tare");
  scale.set_scale();
  scale.tare(); //Reset the scale to 0
 
  long zero_factor = scale.read_average(); //Get a baseline reading
  Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
  Serial.println(zero_factor);
}
 
//=============================================================================================
//                         LOOP
//=============================================================================================
String uni2=" ";
void loop() {
  scale.set_scale(calibration_factor); //Adjust to this calibration factor
  float uni=scale.get_units();
  Serial.print("Reading: ");
  Serial.print(uni, 3);
  Serial.print(" g"); //Change this to kg and re-adjust the calibration factor if you follow SI units like a sane person
  Serial.print(" calibration_factor: ");
  Serial.print(calibration_factor);
  Serial.println();
  delay(2000);
  if(Serial.available())
  {
    char temp = Serial.read();
    if(temp == '+' || temp == 'a')
      calibration_factor += 10;
    else if(temp == '-' || temp == 'z')
      calibration_factor -= 10;
    else if(temp == 's')
      calibration_factor += 100;  
    else if(temp == 'x')
      calibration_factor -= 100;  
    else if(temp == 'd')
      calibration_factor += 1000;  
    else if(temp == 'c')
      calibration_factor -= 1000;
    else if(temp == 'f')
      calibration_factor += 10000;  
    else if(temp == 'v')
      calibration_factor -= 10000;  
    else if(temp == 't')
      scale.tare();  //Reset the scale to zero
  }
}
//=============== ==============================================================================

