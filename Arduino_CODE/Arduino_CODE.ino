int ledPin = 13;
int ignition = 12;
int fanPin = 9;
int fanSpeed = 50;

void setup() {
  pinMode(ledPin, OUTPUT);
  pinMode(ignition, OUTPUT);
  pinMode(fanPin, OUTPUT);
  Serial.begin(9600);
}

void loop() {
  if (Serial.available() > 0) {
    char command = Serial.read();
    
    // Turn on LED
    if (command == '1') {
      digitalWrite(ledPin, HIGH);
    }
    // Turn off LED
    else if (command == '2') {
      digitalWrite(ledPin, LOW);
    }

    // Turn on IGNITION
    else if (command == '3') {
      digitalWrite(ignition, HIGH);
    }

    // Turn off IGNITION
    else if (command == '4') {
      digitalWrite(ignition, LOW);
    }

    // Turn on fan
    else if (command == '5') {
      analogWrite(fanPin, fanSpeed);
    }

    // Turn off fan
    else if (command == '6') {
      analogWrite(fanPin, 0);
    }

    // Set fan speed
    else if (command == '7') {
      while (Serial.available() == 0) {
        // Wait for the speed value
      }
      fanSpeed = Serial.parseInt();
      analogWrite(fanPin, fanSpeed);
    }
  }
}
