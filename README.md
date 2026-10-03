
# Fire & EMS Incidents

A minimal PlatformIO project for ESP32 with CYD display.
CYD used is the dual USB model

## Web Flasher

Flash the firmware to your display straight from Chrome or Edge — no tools to install:

**https://calthause.github.io/LebanonFireEMSIncidents-4inch/**

Amazon link for the 4" CYD Board with exposed SPI
https://a.co/d/0cNrjnoy

Repository for the 4" CYD used
https://github.com/Freenove/Freenove_ESP32_Display
<img width="2016" height="1512" alt="image1 (4)" src="https://github.com/user-attachments/assets/e382f330-f86e-4962-9d42-57f8184a64a0" />
<img width="2016" height="1512" alt="image0 (6)" src="https://github.com/user-attachments/assets/5b89b1a9-34c4-4c65-b36d-72edf6c96cb8" />
## Screenshots

Drop image files into `images/` and reference them here, e.g.:

```markdown
![Dashboard](images/dashboard.jpg)
![Unit Info popup](images/unit-info-popup.jpg)
![Incident map popup](images/county-map-popup.jpg)
```

## Build & Upload

- **Build**: `pio run -e esp32dev`
- **Upload**: `pio run --target upload -e esp32dev`
- **Monitor**: `pio device monitor`

## Adding Libraries

To add libraries later, update `platformio.ini` under `lib_deps`:

```ini
lib_deps =
    lovyan03/LovyanGFX @ ^1.1.16
    <new-library-name> @ ^<version>
```

Then rebuild.
