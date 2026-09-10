# Exigences par Projet - Contrôle Moteur Électrique Automobile

## 1. VESC Project (vedderb/bldc)

### Exigences Fonctionnelles - Capacités et modes de fonctionnement du système
- **Types de contrôle supportés**:
  - Field-Oriented-Control (FOC) complet pour moteurs brushless
  - Contrôle en courant
  - Contrôle en rapport cyclique (duty cycle)
  - Contrôle en vitesse
  - Contrôle en position
- **Modes de fonctionnement**:
  - Support sensorless (sans capteurs)
  - Support sensored avec capteurs Hall
  - Support encodeurs ABI
  - Support encodeurs magnétiques SPI
- **Techniques avancées**:
  - Overmodulation
  - Field weakening
  - High frequency injection (HFI)
- **Types de moteurs**: DC, BLDC, PMSM

### Exigences de Performance - Spécifications électriques et paramètres opérationnels
- **Spécifications électriques**:
  - Tension d'entrée: 12V à 100V (selon modèle)
  - Courant moteur: 160A continu (Classic), 150A continu (Pronto), 660A continu (Maxim Plus)
  - Courant crête: 200A (Classic/Pronto), 1000A (Maxim Plus)
  - Puissance continue: jusqu'à 10kW avec refroidissement adéquat
- **Fréquence PWM**: 30-50 kHz
- **Précision**: Mesure précise des courants de phase

### Exigences Matérielles - Composants électroniques et architecture système
- **Microcontrôleur**: STM32F405
- **Capteurs intégrés**:
  - IMU avec accéléromètre 3-axes
  - Gyroscope 3-axes
  - Capteurs de température multiples
- **Architecture de puissance**:
  - Per-phase phase shunts et amplificateurs
  - Signal processing précis pour mesure courant
- **Options additionnelles** (selon modèle):
  - ESP32-C3 intégré (Pronto/Maxim Plus)
  - 4GB mémoire chip (Pronto/Maxim Plus)
  - GPS module optionnel (Maxim Plus)

### Exigences de Communication - Protocoles et interfaces de transfert de données
- **Interfaces disponibles**:
  - USB
  - CAN
  - SPI
  - I2C
  - UART
  - PWM
  - ADC inputs
  - Bluetooth (certains modèles)
  - WiFi (certains modèles)
- **Vitesse CAN**: jusqu'à 5 Mbps

### Exigences de Sécurité - Protection et monitoring du système
- **Protection thermique**:
  - Capteurs de température intégrés
  - Réduction progressive du courant en cas de surchauffe
- **Protection électrique**:
  - Surveillance surintensité
  - Protection surtension/sous-tension
- **Sorties protégées**:
  - 12V switched output jusqu'à 0.5A (Classic)
  - 12V 5A switchable outputs (Pronto/Maxim Plus)

### Exigences Logicielles - Firmware, outils de développement et licences
- **Firmware**: Open source avec support scripting
- **Personnalisation**:
  - Scripts personnalisés sur STM32F405
  - Support applications custom
- **Outils de configuration**:
  - VESC TOOL Desktop
  - VESC TOOL Phone applications
- **Licence**: GPL (General Public License)

---

## 2. Tesla Model 3/Y Inverter Firmware (techn0zahrt-ctrl/c2000-inverter-M3-Y)

### Exigences Fonctionnelles - Capacités et modes de fonctionnement du système
- **Types de contrôle**:
  - Contrôle SINE pour moteurs induction (front drive units)
  - Contrôle FOC avec resolver pour PMSM (rear drive units)
- **Modes de fonctionnement**:
  - Support Tesla Model 3 front drive units (induction motor)
  - Support Tesla Model 3/Y rear drive units (PMSM)
  - Compatible tous les 6 variants connus Tesla Model 3/Y
- **Intégration véhicule**:
  - Communication CAN/SDO validée pour RDU
  - Integration complete vehicle systems

### Exigences de Performance - Spécifications électriques et paramètres opérationnels
- **Cible hardware**: TMS320F28377D MCU (TI C2000 family)
- **Support multi-variant**:
  - Flag compile-time CONTROL pour sélectionner type
  - CONTROL=FOC: rear drive unit (PMSM, resolver-based FOC)
  - CONTROL=SINE: front drive unit (induction motor, V/Hz with slip control)
- **Validation**:
  - Tesla Model 3 FDU first successful spin
  - Motor controlled via oic commands
  - Running smoothly à 1A, 120V DC

### Exigences Matérielles - Composants électroniques et architecture système
- **Microcontrôleur**: TI TMS320F28377D (C2000 family)
- **Compatibility hardware**:
  - Tesla Model 3/Y front drive units (induction motor)
  - Tesla Model 3/Y rear drive units 1120980-00-G, 1120990-00-G (PMSM)
  - Texas Instruments LAUNCHXL-F28379D development board
- **Portabilité**:
  - Implémentation portable des algorithmes openinverter
  - Testable/simulable hors embedded hardware

### Exigences de Communication - Protocoles et interfaces de transfert de données
- **Protocoles**:
  - CAN/SDO communication
  - Support vehicle network integration
- **Interface de contrôle**:
  - oic write commands pour motor control
  - ampnom (amplitude nominale)
  - fslipspnt (fréquence de glissement)

### Exigences de Sécurité - Protection et monitoring du système
- **Statut développement**:
  - Software not yet validated on hardware
  - NOT suitable for use in vehicles at this time
- **Objectifs sécurité**:
  - Créer système de contrôle usable et safe
  - Support Tesla drive units dans véhicules non-Tesla

### Exigences Logicielles - Firmware, outils de développement et licences
- **Architecture**:
  - Portage de Huebner inverter project
  - Architecture portable C++
  - Branch active: portable-cpp
- **Développement**:
  - Simulation support
  - Validation hardware en cours
- **Licence**: GNU General Public License v3.0

---

## 3. Cornell Electric Vehicles Motor Controller (cornellev/CEV_MCont_V1.0)

### Exigences Fonctionnelles - Capacités et modes de fonctionnement du système
- **Type de contrôle**:
  - Sensored trapezoidal commutation
  - Six-step trapezoidal avec capteurs
  - V/Hz control algorithm
- **Modes de fonctionnement**:
  - Hall sensor processing
  - Speed estimation
  - PWM duty control
  - Gate drive timing coordination
- **Application cible**: Shell Eco-Marathon Urban Concept competition

### Exigences de Performance - Spécifications électriques et paramètres opérationnels
- **Spécifications électriques**:
  - Bus voltage: 48V nominal
  - Maximum bus voltage: 60V
  - Continuous current: ~110A (avec heatsink)
  - Peak current: ~160A (~2s)
- **Paramètres de commutation**:
  - Switching frequency: 5kHz
  - Deadtime: 256ns
  - Gate drive voltage: 15V
- **Objectifs design**:
  - High efficiency
  - High current capability
  - Deterministic switching behavior
  - Minimal firmware complexity

### Exigences Matérielles - Composants électroniques et architecture système
- **Microcontrôleur**: RP2040
- **Architecture de contrôle**:
  - PIO PWM generator (state machines)
  - PIO gate-drive timing
  - Nanosecond-scale deadtime control
- **Composants de puissance**:
  - External Gate Drivers: UCC27301
  - 3-Phase MOSFET Inverter
  - MOSFETs: NTBLS0D8N08XTXG (100V VDS, 0.79 mΩ RDS(on))
- **Gate resistors**:
  - Low side: 1 Ω
  - High side: 4.02 Ω

### Exigences de Communication - Protocoles et interfaces de transfert de données
- **Interface véhicule**:
  - SPI communication avec vehicle control system
  - Digital isolator pour isolation
- **Télémétrie**:
  - Throttle reporting
  - Motor telemetry transmission

### Exigences de Sécurité - Protection et monitoring du système
- **Protection système**:
  - Deadtime control précis
  - Thermal management via heatsink
  - Current limiting (110A continu, 160A crête)
- **Contrôle qualité**:
  - Deterministic switching behavior
  - Minimal firmware complexity pour réduction bugs

### Exigences Logicielles - Firmware, outils de développement et licences
- **Firmware**:
  - RP2040 PIO state machines pour timing précis
  - Trapezoidal commutation logic
  - Hall sensor decoding
- **Documentation**:
  - design-decisions.md
  - power-stage-design.md
  - layout-lessons.md
  - bringup.md
  - firmware.md
- **Licence**: MIT License

---

## 4. Axel BLDC Motor Controller Framework (KOT-LAB/axel)

### Exigences Fonctionnelles - Capacités et modes de fonctionnement du système
- **Type de framework**:
  - "Arduino pour BLDC motor control"
  - Framework hardware pour contrôleurs personnalisés
- **Types de contrôle**:
  - Full compatibility avec SimpleFOC
  - Field-Oriented Control support
  - Custom firmware development possible
- **Modes de capteurs**:
  - Built-in encoder pour mounting direct sur moteur
  - Support external encoders
  - Built-in current sensing pour vrai FOC

### Exigences de Performance - Spécifications électriques et paramètres opérationnels
- **Spécifications électriques**:
  - Input voltage: 10-54V
  - Peak phase current: 100A
  - Peak electrical power: 3100W
  - Continuous electrical power: 1100W
- **Performance système**:
  - High-performance STM32 architecture
  - Powerful gate driver avec external MOSFETs
- **Form factor**:
  - Dimensions: 50x50x9mm
  - Compact design

### Exigences Matérielles - Composants électroniques et architecture système
- **Microcontrôleur**: STM32F446RE
- **Gate driver**: TI DRV8302
- **Encodeur**: AS5047P (intégré)
- **Composants externes**:
  - External MOSFETs support
  - Power stage flexible
- **Interfaces hardware**:
  - Programming interfaces: SWD, DFU

### Exigences de Communication - Protocoles et interfaces de transfert de données
- **Interfaces disponibles**:
  - SPI
  - I2C
  - CAN FD
  - UART
  - USB-C
- **Connectivité étendue**:
  - Toutes interfaces populaires onboard
  - Integration seamless avec applications

### Exigences de Sécurité - Protection et monitoring du système
- **Current sensing**:
  - Built-in current sensing
  - Enables true FOC pour precise et efficient control
- **Reliability**:
  - High-performance design
  - Meets demands de any application

### Exigences Logicielles - Firmware, outils de développement et licences
- **Développement firmware**:
  - Basic firmware works out of the box
  - Custom firmware from scratch possible
  - SimpleFOC compatibility pour rapid development
- **Documentation**:
  - Extensive examples
  - Clear documentation
  - Beginner-friendly
- **Licence**: MIT License + LICENSE-HARDWARE.md séparée

### Exigences d'Application - Cas d'usage et domaines d'application
- **Applications supportées**:
  - Legged robots (high-speed, high-precision)
  - Exoskeletons (torque et speed control)
  - Electric vehicles (scalable design)
  - CNC machines & 3D printers (precise control)
  - Robotics général

---

## 5. FOC King - VESC6 Open Source (nordstream3/FOC)

### Exigences Fonctionnelles - Capacités et modes de fonctionnement du système
- **Type de contrôle**:
  - 3-phase FOC motor control
  - HFI (High Frequency Injection) pour sensorless control
  - Full torque at zero speed sans sensor feedback
- **Design architecture**:
  - "Driverless" design avec individual gate drivers
  - Modulaire: 3 sub-modules assemblés avec pin headers
- **Flexibilité MOSFET**:
  - Standard design: 12 MOSFETs
  - Fonctionne aussi avec 6 MOSFETs

### Exigences de Performance - Spécifications électriques et paramètres opérationnels
- **Spécifications électriques**:
  - 84V/200A continuous rating
  - 20s battery voltage rating
  - High power et voltages capability
- **Architecture modulaire**:
  - POWER BRIDGE module
  - MCU module (STM32F405 PILL)
  - SUPPLY module (+12,+5V,+3V)

### Exigences Matérielles - Composants électroniques et architecture système
- **Microcontrôleur**: STM32F405 PILL
- **Composants intégrés**:
  - IMU: Bosch BMI270
  - USB-C connector
  - Individual gate drivers pour all three phases
- **Design PCB**:
  - 4-layer PCB design
  - FETs mounted on bottom side
  - Compact design
- **Alimentation**:
  - 12V pour gate drivers
  - 5V pour CAN et IMU
  - 3.3V pour MCU et op-amped current-sense

### Exigences de Communication - Protocoles et interfaces de transfert de données
- **Interfaces**:
  - CAN: 5 Mbps
  - USB-C
  - Momentary on/off switch (4-pin JST connector)
  - LED data pin pour programmable LEDs
- **Connectivité**: Extensive communication support

### Exigences de Sécurité - Protection et monitoring du système
- **Current sensing**:
  - Op-amped current-sense amplification
  - Precise phase current measurements
- **Protection**:
  - Integrated temperature monitoring
  - Overcurrent protection

### Exigences Logicielles - Firmware, outils de développement et licences
- **Firmware**:
  - Compatible VESC6 firmware
  - Open source implementation
- **Développement**:
  - Reference design pour further development
  - JLCPCB friendly design
- **Fabrication**:
  - Cheap components chez JLCPCB et LCSC
  - Well stocked components

### Exigences d'Application - Cas d'usage et domaines d'application
- **Applications cibles**:
  - Skateboards
  - OneWheels
  - Bicycles
  - Robotics
  - Boats
  - "Small" electric vehicles

---

## 6. Vehicle Management Unit - VMU (Guts-one/VMU-Vehicle-Management-Unit)

### Exigences Fonctionnelles - Capacités et modes de fonctionnement du système
- **Type de système**:
  - ECU superviseur pour powertrain hybride
  - Coordination ICE et moteur électrique
- **Modes de fonctionnement**:
  - STANDSTILL
  - EV (Electric Vehicle)
  - REGENB (Regenerative Braking)
  - START
  - ICE (Internal Combustion Engine)
  - HYBRID
- **Logique de contrôle**:
  - Sélection modes basée sur:
    - Driver power demand
    - Vehicle speed
    - Battery state of charge (SOC)
    - Engine speed
    - System limits

### Exigences de Performance - Spécifications électriques et paramètres opérationnels
- **Architecture de contrôle**:
  - Supervisory mode logic pour power-split hybrid
  - Basic protections pour smooth, efficient operation
- **Temps de réponse**:
  - Real-time control pour vehicle management
  - FTTI 200ms pour safety functions

### Exigences Matérielles - Composants électroniques et architecture système
- **Platform**: Embedded automotive ECU
- **Sensors integration**:
  - Speed input (speed_dkph)
  - Power demand input (p_dem_dkw)
  - Battery SOC input (soc_q10000)
  - Engine speed input (weng_rpm)
- **API embedded**:
  - Fixed-point input API
  - Integer threshold constants pour transitions
  - Per-state handlers structurés pour traceability

### Exigences de Communication - Protocoles et interfaces de transfert de données
- **Vehicle network**:
  - Communication avec ICE controller
  - Communication avec electric motor controller
  - Battery management system interface
- **Output mapping**:
  - Centralized output mapping
  - Motor enable signals
  - Generator enable signals
  - ICE enable signals
  - No one-step delay dans output mapping

### Exigences de Sécurité
- **Functional safety**:
  - MISRA C 2012 compliance
  - Basic system protections
  - Mode transition safety
- **Documentation sécurité**:
  - Complete V&V evidence versioned
  - Requirements linked dans Simulink model
  - MISRA_COMPLIANCE.md
  - MISRA_QUICKSTART.md

### Exigences Logicielles
- **Architecture**:
  - Mode enumeration et I/O structures
  - Per-state handlers structurés
  - MISRA-oriented coding style
  - Const inputs, explicit uint8_t booleans
  - Structured control flow
- **Développement**:
  - Model-based development (Simulink/Stateflow)
  - Requirements → Simulink/Stateflow model → fixed-point MISRA C 2012
  - Complete test, coverage, CI infrastructure
- **Documentation**:
  - Requirements.pdf
  - HEV Powersplit_adapted_model_Document.pdf
  - Interactive web simulator

### Exigences de Certification
- **Standards**:
  - MISRA C 2012 compliance
  - Automotive-grade development process
  - Complete V&V (Verification & Validation)

---

## 7. Infineon IMR Motor Control (Infineon/IMR_IMD701_MC)

### Exigences Fonctionnelles
- **Type de contrôle**:
  - 3-phase BLDC motor control
  - Field Oriented Control (FOC) algorithm
  - PI controller based on fixed-point implementation
- **Algorithmes avancés**:
  - Hardware-accelerated CORDIC implementation
  - Optimized fixed-point arithmetic
- **Modes de capteurs**:
  - Position angle sensor support
  - Magnetic angle sensor integration
  - Absolute et incremental position possible

### Exigences de Performance
- **Algorithme FOC**:
  - Fixed-point implementation
  - CORDIC hardware acceleration
  - Optimized pour performance temps réel
- **Control loop**:
  - Real-time motor control
  - High precision position feedback

### Exigences Matérielles
- **MCU principal**: IMD701A-Q064X128-AA
  - Arm Cortex-M0 XMC1404 (32-bit microcontroller)
  - Smart 3-phase gate driver IC 6EDL7141
- **Hardware reference**:
  - DEMO_IMR_MTRCTRL_V1 - Demo board IMR motor control
  - DEMO_IMR_ANGLE_SENS_V1 - Demo board IMR encoder
- **Composants Infineon**:
  - ISZ053N08NM6 - OptiMOS 6 N-channel power MOSFET (80V, 5.3 mOhm)
  - TLE9351BVSJ - High speed CAN transceiver (CAN et CAN FD)
  - TLE5012B E1000 - XENSIV 360° GMR magnetic angle sensor
- **Sensors**:
  - Magnetic angle sensor sur separate board
  - Incremental Interface (IIF) - no SSC/SPI interface needed

### Exigences de Communication
- **Interfaces**:
  - CAN bus communication avec onboard CAN transceiver
  - SPI/IIF interface pour angle sensor
- **Identification**:
  - Onboard DIP switch pour unique board identification

### Exigences de Sécurité
- **Protection intégrée**:
  - Low Rds(on) MOSFETs pour high current
  - Automotive-grade components
  - Over-temperature, over-voltage, over-current protection
- **Reliability**:
  - Qualified pour automotive applications
  - Robust design pour mobile robots

### Exigences Logicielles
- **Development environment**:
  - ModusToolbox™ software
  - Official Infineon GitHub repository
- **Architecture**:
  - Motor control firmware optimisé
  - Position sensor processing
  - CAN communication stack
- **Documentation**:
  - Complete software package
  - Hardware reference documentation

### Exigences d'Application
- **Applications cibles**:
  - Infineon Mobile Robot (IMR)
  - Robotic applications
  - Automotive motor control

---

## 8. NXP PMSM FOC Motor Control (nxp-appcodehub/an-mc-pmsm-foc-2sh-s32k344)

### Exigences Fonctionnelles
- **Type de contrôle**:
  - Sensorless Field Oriented Control (FOC) pour PMSM
  - Dual shunt current sensing
- **Algorithmes**:
  - FOC implementation optimisée
  - Sensorless position estimation
  - Current control loops
- **Application note**: AN13767 - 3-phase Sensorless PMSM Motor Control Kit

### Exigences de Performance
- **Sensing architecture**:
  - Dual shunt current sensing
  - High precision current measurement
  - Sensorless position estimation
- **Control performance**:
  - Real-time FOC implementation
  - Optimized pour S32K344

### Exigences Matérielles
- **Microcontrôleur**: NXP S32K344
- **Hardware platform**:
  - FRDM-A-S32K344 - Freedom board
  - DEVKIT-MOTORGD - Motor control shield
  - Sunrise motor (du BLDC-KIT)
- **Périphériques utilisés**:
  - BCTU (Base Cross Triggering Unit)
  - eMIOS (Enhanced Modular Input/Output System)
  - ADC (Analog-to-Digital Converter)
  - PWM (Pulse Width Modulation)
  - SPI (Serial Peripheral Interface)
  - UART (Universal Asynchronous Receiver-Transmitter)

### Exigences de Communication
- **Interfaces**:
  - SPI pour sensor communication
  - UART pour debugging/communication
  - CAN support (via hardware)
- **Debug interface**:
  - FreeMASTER Run-Time Debugging Tool integration

### Exigences de Sécurité
- **Protection système**:
  - Overcurrent protection
  - Overvoltage protection
  - Temperature monitoring
- **Automotive compliance**:
  - Automotive-grade hardware
  - Qualified pour vehicle applications

### Exigences Logicielles
- **Development tools**:
  - S32 Design Studio IDE
  - FRDM Automotive Bundle pour S32K3
- **Libraries**:
  - AMMCLib (Automotive Math and Motor Control Library) Rev 1.1.44
  - RTD Low Level API
- **Debugging**:
  - FreeMASTER Run-Time Debugging Tool
  - Real-time monitoring et tuning
- **Documentation**:
  - Application note AN13767
  - Complete software package

### Exigences d'Application
- **Applications cibles**:
  - Automotive motor control development
  - PMSM motor control demonstration
  - Sensorless FOC implementation
  - NXP S32K3 platform evaluation

---

## 9. OpenVVVF RTE (OpenVVVF/RTE)

### Exigences Fonctionnelles
- **Type de plateforme**:
  - Model-based development toolchain pour motor drives
  - Design de contrôle comme node graph
  - Arbitrary control schemes support
- **Control strategies**:
  - Vector control (FOC)
  - Scalar V/Hz control
  - Arbitrary modulation schemes
  - Any control scheme expressible via node graph
- **Signal flow**:
  - Fully user-configurable signal flow via nodes
  - Non limité à V/Hz scalar control

### Exigences de Performance
- **Architecture temps réel**:
  - Real-time control loop
  - STM32H723 main processor
  - STM32G474 safety coprocessor
- **Simulation**:
  - Plant/inverter simulator basé sur ngspice (prévu)
  - Closed-loop testing avant hardware deployment

### Exigences Matérielles
- **Microcontrôleurs**:
  - STM32H723 - Main processor
  - STM32G474 - Safety coprocessor
- **Base firmware**:
  - STM32H723 base firmware image
  - Portable architecture
- **Portabilité**:
  - Any platform peut être targeted
  - Custom base image support
  - Platform API contract

### Exigences de Communication
- **Tools**:
  - RTE Studio editor - Live device/telemetry state
  - Portable automation backend
  - MCP stdio server support
- **Interfaces**:
  - Live device monitoring
  - Real-time telemetry
  - Node graph editing

### Exigences de Sécurité
- **Safety coprocessor**:
  - STM32G474 dedicated safety processor
  - Separate safety-critical functions
- **Monitoring**:
  - Real-time fault detection
  - Safety mechanism integration

### Exigences Logicielles
- **Toolchain components**:
  - RTE Studio - Lightweight editor
  - rte - Portable automation backend
  - InverterCodegen - Generates C++ domain files from NodeAPI graph JSON
  - RTECodeEmitter - Takes base firmware + graph → flashable binary
- **Node graph libraries**:
  - Base image pour OpenVVVF STM32H723 inverter
  - Extensible node libraries
- **Development workflow**:
  - Node graph design → Code generation → Flashable firmware
  - Simulation avant hardware deployment

### Exigences d'Application
- **Applications cibles**:
  - Advanced motor drives development
  - Research applications
  - Custom control scheme development
  - Educational platforms

---

## 10. SF-Motion (sirojudinMunir/sf-motion)

### Exigences Fonctionnelles
- **Type de plateforme**:
  - Open-source BLDC/PMSM motor control platform
  - Basée sur STM32 et Field-Oriented Control (FOC)
- **Control capabilities**:
  - FOC firmware complet
  - Custom motor driver hardware
  - High-performance motion control

### Exigences de Performance
- **Motor control**:
  - FOC implementation
  - High precision control
  - Real-time performance
- **Motion capabilities**:
  - Speed control
  - Position control
  - Torque control

### Exigences Matérielles
- **Microcontrôleur**: STM32 (variant spécifié dans hardware)
- **Custom hardware**:
  - Custom motor driver hardware
  - KiCad design (schematic, PCB)
  - Gerber files
  - BOM (Bill of Materials)
- **Components**:
  - Optimized pour motion control applications

### Exigences de Communication
- **Control interfaces**:
  - Python communication tools
  - Custom control protocols
- **Monitoring**:
  - PyQt GUI pour motor monitoring
  - PyQtGraph pour testing
  - Real-time data visualization

### Exigences de Sécurité
- **Protection système**:
  - Overcurrent protection
  - Overvoltage protection
  - Temperature monitoring
- **Reliability**:
  - Robust FOC implementation
  - Tested hardware design

### Exigences Logicielles
- **Firmware**:
  - Complete FOC firmware
  - STM32-based implementation
- **Tools**:
  - Python communication et control tools
  - PyQt/PyQtGraph GUI
  - Motor monitoring software
  - Testing utilities
- **Documentation**:
  - Complete hardware design files
  - Software documentation
  - Usage examples

### Exigences d'Application
- **Applications cibles**:
  - Motion control projects
  - Robotics
  - Electric vehicles
  - Custom motor control applications

---

## 11. MiniBLDC TMC6200 (sschoedel/MiniBLDC_TMC6200_v2)

### Exigences Fonctionnelles
- **Type de contrôleur**:
  - BLDC motor controller basé sur TMC6200
  - ESP32S3 MCU integration
- **Configuration spéciale**:
  - Daisy-chain configuration pour multi-motor systems
  - Support 10-1000+ moteurs
- **Control modes**:
  - SimpleFOC integration
  - FOC control
  - Sensorless et sensored operation

### Exigences de Performance
- **Multi-motor scaling**:
  - Optimisé pour daisy-chain
  - Support high motor counts
  - Efficient communication entre controllers
- **Architecture dual-core**:
  - Core 1: FOC loop (max performance)
  - Core 2: Communication, state machines, external peripherals

### Exigences Matérielles
- **Motor controller**: TMC6200
  - Abordable (~$5.5)
  - Easy configurability
  - Fault monitoring over SPI
  - Inline current sense (torque control avec SimpleFOC)
  - Wide input voltage support
  - High efficiency
  - Small footprint
- **Microcontrôleur**: ESP32S3
  - Dual-core support
  - Wide peripheral support
  - Reprogrammable pin outputs (internal muxes)
  - Built-in JTAG to USB interface
  - No external serial peripheral needed
  - Breakpoint/watchpoint style debugging
- **Design**:
  - Small, dense board design
  - Inspired by XESC project
  - Easy routing grâce à ESP32 muxes

### Exigences de Communication
- **Daisy-chain protocols**:
  - CAN support pour daisy-chaining boards
  - Efficient multi-motor communication
- **Wireless capabilities**:
  - Built-in WiFi pour wireless motor control
  - Built-in Bluetooth
- **Wired interfaces**:
  - Hardware quadrature encoder support
  - SPI pour TMC6200 configuration
  - Multiple peripheral interfaces

### Exigences de Sécurité
- **TMC6200 features**:
  - Fault monitoring over SPI
  - Overcurrent protection
  - Overtemperature protection
  - Short-circuit detection
- **System reliability**:
  - Dedicated FOC core pour consistent performance
  - Isolated communication core

### Exigences Logicielles
- **Firmware architecture**:
  - SimpleFOC integration
  - Dual-core optimization
  - One core exclusif pour FOC loop
  - Other core pour communication et state machines
- **Development**:
  - JTAG debugging intégré
  - Breakpoint/watchpoint support
  - Easy firmware updates
- **Flexibility**:
  - Custom firmware development
  - Reprogrammable I/O via internal muxes

### Exigences d'Application
- **Applications cibles**:
  - Multi-motor systems (10-1000+ motors)
  - Complex robotics
  - Distributed motor control
  - Applications nécessitant many coordinated motors

---

## 12. PCBasPRO Cheap FOC2VESC (PCBasPRO/PCBasPRO_0002_Cheap_FOC2VESC)

### Exigences Fonctionnelles
- **Type de contrôleur**:
  - 2-motor controller basé sur VESC6
  - Dual motor control capability
- **Control capabilities**:
  - FOC control pour les deux moteurs
  - Independent motor control
  - Synchronized dual motor operation

### Exigences de Performance
- **Spécifications électriques**:
  - 100V/200A continuous rating
  - Raw recommendation: 84V/16A
  - 22s battery voltage rating
  - Safe pour 6S à 21S LiPo/Li-ion
  - Voltage spikes ne doivent pas excéder 100V
- **Power handling**:
  - High current capability
  - Dual motor power distribution
- **Design safety**:
  - 1.5mm clearance sur 100V (IPC-2221B, table 6-1, 51-100V on B3)

### Exigences Matérielles
- **Microcontrôleur**: STM32F405 CPU
- **Connectivité sans fil**: BLE WT51822_S4AT
- **Architecture de puissance**:
  - 4-layer SMD design
  - Individual gate drivers pour all three phases (per motor)
  - 6mm trace pour copper rail (current increase capability)
- **Integrated components**:
  - IMU intégré
  - USB-C connector
  - CAN interface
  - BLE interface
- **PCB design**:
  - 100x50mm (1 PCB)
  - 100x100mm with easybreak (2 PCBs, can be split later)
  - JLCPCB friendly design

### Exigences de Communication
- **Interfaces**:
  - CAN
  - USB-C
  - BLE (Bluetooth Low Energy)
  - IMU data
- **Dual motor coordination**:
  - Synchronized control
  - Independent addressing
  - Coordinated motion profiles

### Exigences de Sécurité
- **Electrical safety**:
  - 1.5mm clearance conformité IPC-2221B
  - Voltage spike protection
  - Overcurrent protection
- **Thermal management**:
  - High current trace design
  - 6mm copper rails
  - Proper PCB layout pour heat dissipation

### Exigences Logicielles
- **Firmware**:
  - Compatible VESC6 firmware
  - Dual motor control implementation
  - Open source development
- **Development**:
  - JLCPCB parts availability
  - Low-cost development approach
  - Rapid prototyping support
- **Fabrication**:
  - Cheap components available at JLCPCB et LCSC
  - Well stocked components
  - Easy assembly

### Exigences d'Application
- **Applications cibles**:
  - Dual motor vehicles
  - 4WD vehicles (2 controllers)
  - Differential drive systems
  - Low-cost development
  - DIY electric vehicles

---

## Résumé des Exigences Transversales

### Exigences Communes (Tous Projets)

#### Exigences de Base
- **Contrôle moteur**: BLDC/PMSM/Induction
- **Algorithme principal**: FOC (Field Oriented Control) ou trapezoidal
- **Microcontrôleurs**: STM32, TI C2000, RP2040, ESP32
- **Communication**: CAN, USB, SPI, I2C, UART
- **Sécurité**: Protection surintensité, surtension, température

#### Exigences de Performance Typiques
- **Tension**: 12V à 120V
- **Courant**: 100A à 660A continu
- **Puissance**: 1kW à 10kW
- **Fréquence PWM**: 5kHz à 50kHz
- **Précision**: ±1% courant, <200ms temps réponse sécurité

#### Exigences de Sécurité Automotive
- **ISO 26262**: ASIL A à D selon criticité
- **FTTI**: 200ms pour fonctions safety-critical
- **Protection**: Surveillance température, courant, tension
- **Diagnostics**: Autotests, watchdog, fault detection

#### Exigences de Développement
- **Outils**: IDE manufacturers, debugging tools
- **Documentation**: Spécifications, schémas, manuels
- **Tests**: Validation hardware, software verification
- **Licences**: GPL, MIT, ou licences manufacturers

---

*Document généré le 2026-09-08*
*Basé sur l'analyse détaillée des 12 projets open source de contrôle moteur électrique automobile*