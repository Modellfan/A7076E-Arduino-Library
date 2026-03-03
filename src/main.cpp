#include <Arduino.h>

namespace {
constexpr unsigned long kBaudRate = 115200;
constexpr size_t kMaxLineLen = 64;
char gLineBuffer[kMaxLineLen];
size_t gLineLen = 0;
}

void setup() {
  Serial.begin(kBaudRate);
  delay(200);
  Serial.println("READY");
}

void loop() {
  while (Serial.available() > 0) {
    const char c = static_cast<char>(Serial.read());
    if (c == '\r' || c == '\n') {
      if (gLineLen == 0) {
        continue;
      }
      gLineBuffer[gLineLen] = '\0';
      if (strcmp(gLineBuffer, "PING") == 0) {
        Serial.println("PONG");
      } else {
        Serial.print("UNKNOWN:");
        Serial.println(gLineBuffer);
      }
      gLineLen = 0;
      continue;
    }
    if (gLineLen < (kMaxLineLen - 1)) {
      gLineBuffer[gLineLen++] = c;
    }
  }
}
