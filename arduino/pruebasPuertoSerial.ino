
double variable;
void setup() {
  Serial.begin(9600);
  variable = 0;  
}
void loop() {
  variable = random(1023) * (5.0 / 1023.0);
  String s = String(variable);
  while(s.length() < 4){
    s.concat("0");
  }
  Serial.println(s);
  delay(500);
  }
