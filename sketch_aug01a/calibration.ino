//
//#include "HX711.h"
//#define DOUT 3
//#define CLK 2
//
//HX711 scale(DOUT, CLK);
//void setup() {
//  // put your setup code here, to run once:
//  Serial.begin(9600);
//  Serial.println("HX711 Calibration");
//  Serial.println("Remove all weight from scale");
//  Serial.println("This is for calculating the proper calibration factor");
//  scale.set_scale();
//  scale.tare(); //Reset the scale to 0
//  
//  long zero_factor = scale.read_average(); //Get a baseline reading
//  Serial.print("Zero factor: "); //This can be used to remove the need to tare the scale. Useful in permanent scale projects.
//  Serial.println(zero_factor); 
//  Serial.println("Now place a known wt to calculate factor"); 
//  Serial.println("Use the wt values displayed below divided by the original weight to get scale"); 
//}
//
//void loop() {
//  // put your main code here, to run repeatedly:
//  Serial.println(scale.get_units(), 3);
//  delay(3000);
//}
