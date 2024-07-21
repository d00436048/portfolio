#include <FastLED.h>

//pins------------------------------------------------
#define LED_PIN     7
#define NUM_LEDS    75

int GREEN_LED = 3;
int BLUE_LED = 5;
int YELLOW_LED = 12;
int RED_LED = 13;

int GREEN_BUTTON = 2;
int BLUE_BUTTON = 4;
int YELLOW_BUTTON = 6;
int RED_BUTTON = 9;

//teams-------------------------------------------------
bool GREEN = false;
bool BLUE = false;
bool YELLOW = false;
bool RED = false;

//color defs-----------------------------------------------
//green = 57, 204, 0
//blue = 5,140,250
//yellow = 250, 174, 52
//red = 245, 53, 15
#define GREEN_COLOR  CRGB(57, 204, 0)
#define BLUE_COLOR   CRGB(5, 140, 250)
#define YELLOW_COLOR CRGB(255, 100, 0)
#define RED_COLOR    CRGB(255, 0, 0)

CRGB leds[NUM_LEDS];
int i = 0;

// Timer variables
unsigned long lastButtonPress[4] = {0, 0, 0, 0}; // Stores the time of the last button press for each button
const unsigned long holdTime = 17000; // Time in milliseconds to hold the button (10 seconds)

//led strip variables
unsigned long rgby[4] = {0, 0, 0, 0};

//----------------------------------------------------------------------------------

void setup() {
  // Set team to green
  BLUE = true;

  // Setup LED controller
  FastLED.addLeds<WS2812, LED_PIN, GRB>(leds, NUM_LEDS);

  // Setup buttons as input with pull-up resistors
  pinMode(GREEN_BUTTON, INPUT_PULLUP);
  pinMode(BLUE_BUTTON, INPUT_PULLUP);
  pinMode(YELLOW_BUTTON, INPUT_PULLUP);
  pinMode(RED_BUTTON, INPUT_PULLUP);

  // Setup LEDs as output
  pinMode(GREEN_LED, OUTPUT);
  pinMode(BLUE_LED, OUTPUT);
  pinMode(YELLOW_LED, OUTPUT);
  pinMode(RED_LED, OUTPUT);

  // Start serial monitor
  Serial.begin(9600);
}

void loop() {
  FastLED.addLeds<WS2812B, LED_PIN, GRB>(leds, NUM_LEDS);
  FastLED.setBrightness(255);
  // Read button states
  int GB = digitalRead(GREEN_BUTTON);
  int BB = digitalRead(BLUE_BUTTON);
  int YB = digitalRead(YELLOW_BUTTON);
  int RB = digitalRead(RED_BUTTON);

  // Update team states based on button hold time
  if (GB == LOW && millis() - lastButtonPress[0] < holdTime && GREEN == false){
    rgby[0] = 0;
    rgby[2] = 0;
    rgby[3] = 0;

    lastButtonPress[1] = millis();
    lastButtonPress[2] = millis();
    lastButtonPress[3] = millis();

    rgby[1]++;
    for (int j = 0; j < rgby[1]; j++){
      leds[j] = CRGB(GREEN_COLOR);
    }
    FastLED.show();
    delay(100);
  }
  if (BB == LOW && millis() - lastButtonPress[1] < holdTime && BLUE == false){
    rgby[0] = 0;
    rgby[1] = 0;
    rgby[3] = 0;

    lastButtonPress[0] = millis();
    lastButtonPress[2] = millis();
    lastButtonPress[3] = millis();

    rgby[2]++;
    for (int j = 0; j < rgby[2]; j++){
      leds[j] = CRGB(BLUE_COLOR);
    }
    FastLED.show();
    delay(100);
  }
  if (YB == LOW && millis() - lastButtonPress[2] < holdTime && YELLOW == false){
    rgby[0] = 0;
    rgby[1] = 0;
    rgby[2] = 0;

    lastButtonPress[0] = millis();
    lastButtonPress[1] = millis();
    lastButtonPress[3] = millis();

    rgby[3]++;
    for (int j = 0; j < rgby[3]; j++){
      leds[j] = CRGB(YELLOW_COLOR);
    }
    FastLED.show();
    delay(100);
  }
  if (RB == LOW && millis() - lastButtonPress[3] < holdTime && RED == false){
    rgby[1] = 0;
    rgby[2] = 0;
    rgby[3] = 0;

    lastButtonPress[0] = millis();
    lastButtonPress[1] = millis();
    lastButtonPress[2] = millis();

    rgby[0]++;
    for (int j = 0; j < rgby[0]; j++){
      leds[j] = CRGB(RED_COLOR);
    }
    FastLED.show();
    delay(100);
  }




  
  if (GB == LOW && millis() - lastButtonPress[0] >= holdTime) {
    GREEN = true;
    BLUE = false;
    YELLOW = false;
    RED = false;
    lastButtonPress[0] = millis();
    lastButtonPress[1] = millis();
    lastButtonPress[2] = millis();
    lastButtonPress[3] = millis();
  } else if (BB == LOW && millis() - lastButtonPress[1] >= holdTime) {
    GREEN = false;
    BLUE = true;
    YELLOW = false;
    RED = false;
    lastButtonPress[0] = millis();
    lastButtonPress[1] = millis();
    lastButtonPress[2] = millis();
    lastButtonPress[3] = millis();
  } else if (YB == LOW && millis() - lastButtonPress[2] >= holdTime) {
    GREEN = false;
    BLUE = false;
    YELLOW = true;
    RED = false;
    lastButtonPress[0] = millis();
    lastButtonPress[1] = millis();
    lastButtonPress[2] = millis();
    lastButtonPress[3] = millis();
  } else if (RB == LOW && millis() - lastButtonPress[3] >= holdTime) {
    GREEN = false;
    BLUE = false;
    YELLOW = false;
    RED = true;
    lastButtonPress[0] = millis();
    lastButtonPress[1] = millis();
    lastButtonPress[2] = millis();
    lastButtonPress[3] = millis();
  }

    // Set LED colors based on team states
    if (GREEN) {
        // Set LED color to green
      digitalWrite(GREEN_LED,HIGH);
      digitalWrite(BLUE_LED,LOW);
      digitalWrite(YELLOW_LED,LOW);
      digitalWrite(RED_LED,LOW);

      //leds
      fill_solid(leds, NUM_LEDS, GREEN_COLOR);
        // ...
    } else if (BLUE) {
        // Set LED color to blue
      digitalWrite(GREEN_LED,LOW);
      digitalWrite(BLUE_LED,HIGH);
      digitalWrite(YELLOW_LED,LOW);
      digitalWrite(RED_LED,LOW);

      fill_solid(leds, NUM_LEDS, BLUE_COLOR);

    } else if (YELLOW) {
        // Set LED color to yellow
      digitalWrite(GREEN_LED,LOW);
      digitalWrite(BLUE_LED,LOW);
      digitalWrite(YELLOW_LED,HIGH);
      digitalWrite(RED_LED,LOW);

      fill_solid(leds, NUM_LEDS, YELLOW_COLOR);

    } else if (RED) {
        // Set LED color to red
      digitalWrite(GREEN_LED,LOW);
      digitalWrite(BLUE_LED,LOW);
      digitalWrite(YELLOW_LED,LOW);
      digitalWrite(RED_LED,HIGH);

      fill_solid(leds, NUM_LEDS, RED_COLOR);
    }

  // Update LED strip
  FastLED.show();

  // Delay for stability
  delay(100);
}
