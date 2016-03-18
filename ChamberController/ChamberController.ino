double TOTAL_SOLAR_INTENSITY = 3892.78;
double TOTAL_ENERGY = 26103.74;

int voltageBase = 4.2; // in Volts

// time in orbit is 97mins
unsigned long TIME_LIGHT =       65;
unsigned long TIME_DARK =        32;
unsigned long DARK_TIME_HALF =   (TIME_DARK/2) * 60 * 1000;
unsigned long LIGHT_TIME =       TIME_LIGHT * 60 * 1000;

int enablePin0 = 8;
int enablePin1 = 9;
int enablePin2 = 10;
int enablePin3 = 11;

void setup() {
  Serial.begin(9600);
  pinMode(enablePin0, OUTPUT); // to double check
  pinMode(enablePin1, OUTPUT); // to double check
  pinMode(enablePin2, OUTPUT); // to double check
  pinMode(enablePin3, OUTPUT); // to double check
}

void loop() {
  /* 
   * Batteries initially charged to ~50%,
   * no energy for the first 16 mins (on dark side)
   */
  digitalWrite(enablePin0, LOW);
  digitalWrite(enablePin1, LOW);
  digitalWrite(enablePin2, LOW);
  digitalWrite(enablePin3, LOW);
  delay(DARK_TIME_HALF);

  /* 
   * Batteries initially charged to ~50%,
   * no energy for the first 15 mins (on light side)
   */
  // instead of TIME_LIGHT using 54 

  Serial.println("start of being on light side");
  for (int i = 0; i < 3240; ++i) { // 3240 is the number of secs once power average on W 54min instead
      int voltageBase = 4.2; // in Volts

      digitalWrite(enablePin0, HIGH);
      digitalWrite(enablePin1, HIGH);
      digitalWrite(enablePin2, HIGH);
      digitalWrite(enablePin3, HIGH);

      double currentSwitchVal0 = analogRead(A0);
      double powerSwitchVal0 = currentSwitchVal0 * voltageBase * 0.001;

      double currentSwitchVal1 = analogRead(A1);
      double powerSwitchVal1 = currentSwitchVal1 * voltageBase * 0.001;

      double currentSwitchVal2 = analogRead(A2);
      double powerSwitchVal2 = currentSwitchVal2 * voltageBase * 0.001;

      double currentSwitchVal3 = analogRead(A3);
      double powerSwitchVal3 = currentSwitchVal3 * voltageBase * 0.001;

      double currentVals[] = {currentSwitchVal0, currentSwitchVal1, currentSwitchVal2, currentSwitchVal3};
      double powerVals[] = {powerSwitchVal0, powerSwitchVal1, powerSwitchVal2, powerSwitchVal3};

      Serial.println(i);
      for (int j = 0; j < 4; j++) {
              Serial.print("switch ");
              Serial.print(j);
              Serial.print(" - current: ");
              Serial.print(currentSwitchVal0);
              Serial.print(" - power: ");
              Serial.println(powerSwitchVal0);
      }

      int valClosest = 0;
      double diff = abs(powerVals[0] - 8.05);
      for (int j = 1; j < 4; j++) {
        double newDiff = abs(powerVals[i] - 8.05);
        if (abs (newDiff - diff) < 0.001) {
          valClosest = j;
        }
      }

      if (valClosest == 0) {
          digitalWrite(enablePin0, HIGH);
          digitalWrite(enablePin1, LOW);
          digitalWrite(enablePin2, LOW);
          digitalWrite(enablePin3, LOW);
      } else if (valClosest == 1) {
          digitalWrite(enablePin0, LOW);
          digitalWrite(enablePin1, HIGH);
          digitalWrite(enablePin2, LOW);
          digitalWrite(enablePin3, LOW);
      } else if (valClosest  == 2) {
          digitalWrite(enablePin0, LOW);
          digitalWrite(enablePin1, LOW);
          digitalWrite(enablePin2, HIGH);
          digitalWrite(enablePin3, LOW);
      } else if (valClosest == 3) {
          digitalWrite(enablePin0, LOW);
          digitalWrite(enablePin1, LOW);
          digitalWrite(enablePin2, LOW);
          digitalWrite(enablePin3, HIGH);
      }

      delay(1185);
  }

  /* 
   * Last 16 mins of orbit on dark side
   */
  digitalWrite(enablePin0, LOW);
  digitalWrite(enablePin1, LOW);
  digitalWrite(enablePin2, LOW);
  digitalWrite(enablePin3, LOW);

  delay(DARK_TIME_HALF);

  /* 
   * 16*2 + 65 = 97mins in orbit.
   */
}
