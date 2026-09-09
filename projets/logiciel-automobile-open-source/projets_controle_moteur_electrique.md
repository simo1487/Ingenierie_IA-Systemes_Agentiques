# Projets Open Source de Contrôle Moteur Électrique Automobile

## Liste des Projets GitHub

### 1. VESC Project
- **URL**: https://github.com/vedderb/bldc
- **Nom**: VESC firmware
- **Couverture**: 
  - Firmware open source pour contrôleurs DC/BLDC/FOC
  - Support complet Field-Oriented-Control pour moteurs brushless
  - Contrôle en courant, rapport cyclique, vitesse et position
  - Support sensorless et sensored avec capteurs Hall, encodeurs ABI, encodeurs magnétiques SPI
  - Techniques avancées: overmodulation, field weakening, high frequency injection
  - Basé sur STM32F405 MCU
  - Interfaces: USB, CAN, SPI, I2C, UART, PWM, ADC
  - IMU intégré (accéléromètre 3-axes, gyroscope 3-axes)
  - Plus de 3.4k stars, 1.9k forks
- **Application**: Véhicules électriques personnels, skateboards, e-bikes, robots

### 2. Tesla Model 3/Y Inverter Firmware
- **URL**: https://github.com/techn0zahrt-ctrl/c2000-inverter-M3-Y
- **Nom**: c2000-inverter-M3-Y
- **Couverture**:
  - Portage du projet Huebner inverter vers TI C2000
  - Cible: TMS320F28377D MCU (utilisé dans les Tesla Model 3/Y)
  - Support unités d'entraînement front (moteur induction, contrôle SINE)
  - Support unités d'entraînement rear (PMSM, contrôle FOC avec resolver)
  - Solution open source complète pour Tesla drive units
  - Compatible avec tous les 6 variants connus Tesla Model 3/Y
  - Communication CAN/SDO validée pour RDU
- **Application**: Conversion Tesla drive units pour véhicules non-Tesla

### 3. Cornell Electric Vehicles Motor Controller
- **URL**: https://github.com/cornellev/CEV_MCont_V1.0
- **Nom**: CEV Motor Controller V1.0
- **Couverture**:
  - Contrôleur BLDC open source pour compétition Shell Eco-Marathon
  - Système 48V nominal, 60V maximum
  - 110A continu (avec dissipateur), 160A crête (~2s)
  - Contrôle trapezoidal avec capteurs sur RP2040
  - PIO state machines pour PWM précis et timing gate drive
  - Deadtime de 256ns
  - Commutation six-step trapezoidal avec capteurs
  - Communication SPI avec isolateur numérique pour télémétrie
  - Fréquence de commutation 5kHz
- **Application**: Véhicules écologiques compétition, urban concept

### 4. Axel BLDC Motor Controller Framework
- **URL**: https://github.com/KOT-LAB/axel
- **Nom**: Axel - Custom BLDC Motor Controller Framework
- **Couverture**:
  - Framework hardware pour contrôleurs BLDC personnalisés
  - Concept "Arduino pour BLDC motor control"
  - STM32F446RE MCU + TI DRV8302 gate driver
  - Encodeur AS5047P intégré, support encodeurs externes
  - Courant de crête 100A, puissance électrique crête 3100W
  - Entrée 10-54V, puissance continue 1100W
  - Interfaces: SPI, I2C, CAN FD, UART, USB-C
  - Compatible SimpleFOC pour développement rapide
  - Dimensions: 50x50x9mm
- **Application**: Robots marcheurs, exosquelettes, véhicules électriques, CNC, imprimantes 3D

### 5. FOC King (VESC6 Open Source)
- **URL**: https://github.com/nordstream3/FOC
- **Nom**: King of FOC motor control hardware (FOC_KING)
- **Couverture**:
  - Design open source basé sur VESC6 75V/300A
  - STM32F405 MCU
  - 84V/200A continu, 20s batterie
  - Contrôle FOC 3-phase avec gate drivers individuels
  - Support HFI (High Frequency Injection) pour control sensorless
  - PCB 4 couches avec 12 MOSFETs (fonctionne aussi avec 6)
  - Design modulaire: POWER BRIDGE, MCU, SUPPLY
  - CAN 5 Mbps, USB-C, IMU Bosch BMI270
  - Alimentation: 12V (gate drivers), 5V (CAN/IMU), 3.3V (MCU)
- **Application**: Skateboards, OneWheels, vélos, robots, bateaux

### 6. Vehicle Management Unit (VMU)
- **URL**: https://github.com/Guts-one/VMU-Vehicle-Management-Unit
- **Nom**: VMU-Vehicle-Management-Unit
- **Couverture**:
  - ECU superviseur pour powertrain hybride
  - Coordination ICE et moteur électrique
  - Sélection modes: EV, ICE, hybrid, regenerative braking
  - Basé sur demande conducteur, vitesse véhicule, SOC batterie
  - Modèle Simulink/Stateflow avec exigences liées
  - Implémentation C MISRA C 2012 avec preuves V&V
  - Modes: STANDSTILL, EV, REGENB, START, ICE, HYBRID
  - API à point fixe pour embedded
  - Documentation: Requirements.pdf, HEV Powersplit_adapted_model_Document.pdf
- **Application**: Véhicules hybrides power-split, démonstration automotive grade

### 7. Infineon IMR Motor Control
- **URL**: https://github.com/Infineon/IMR_IMD701_MC
- **Nom**: IMR Software for IMD701A Motor Control
- **Couverture**:
  - Software officiel Infineon pour ModusToolbox™
  - Contrôle moteur BLDC 3-phase avec FOC
  - Algorithme FOC avec contrôleur PI à point fixe
  - Implémentation optimisée CORDIC hardware-accelerated
  - IMD701A-Q064X128-AA: MCU Arm Cortex-M0 XMC1404 + gate driver 6EDL7141
  - Communication CAN avec transceiver intégré
  - Capteur d'angle magnétique TLE5012B E1000
  - Support ABSOLUTE et INCREMENTAL position
  - Hardware: DEMO_IMR_MTRCTRL_V1, DEMO_IMR_ANGLE_SENS_V1
- **Application**: Robots mobiles Infineon, applications automotive

### 8. NXP PMSM FOC Motor Control
- **URL**: https://github.com/nxp-appcodehub/an-mc-pmsm-foc-2sh-s32k344
- **Nom**: PMSM Motor Control Sensorless dual Shunt FOC on FRDM-A-S32K344
- **Couverture**:
  - Implémentation FOC sensorless pour PMSM
  - Sensing courant dual shunt
  - Basé sur NXP S32K344 microcontroller
  - Hardware: FRDM-A-S32K344 + DEVKIT-MOTORGD Shield
  - Sunrise motor du BLDC-KIT
  - Application note AN13767
  - AMMCLib (Automotive Math and Motor Control Library) Rev 1.1.44
  - FreeMASTER pour debugging runtime
  - Périphériques: BCTU, eMIOS, ADC, PWM, SPI, UART
- **Application: Développement automotive NXP, démonstration FOC

### 9. OpenVVVF RTE
- **URL**: https://github.com/OpenVVVF/RTE
- **Nom**: OpenVVVF/RTE - Real Time Examiner
- **Couverture**:
  - Toolchain model-based development pour motor drives
  - Design de contrôle comme node graph
  - Base firmware STM32H723 + STM32G474 safety coprocessor
  - Support arbitraire de schémas de modulation
  - Configurable signal flow via nodes
  - Non limité à V/Hz scalar control - support vector control (FOC)
  - RTE Studio editor pour live device/telemetry
  - Simulateur plant/inverter basé sur ngspice prévu
  - Portable: peut cibler n'importe quelle plateforme avec base image custom
- **Application: Développement avancé motor drives, recherche

### 10. SF-Motion
- **URL**: https://github.com/sirojudinMunir/sf-motion
- **Nom**: SF-Motion - Open-source Motion Control Platform
- **Couverture**:
  - Plateforme contrôle BLDC/PMSM basée sur STM32 et FOC
  - Firmware FOC complet
  - Hardware driver motor custom
  - Design KiCad (schematic, PCB, Gerber, BOM)
  - Outils Python communication et contrôle
  - GUI PyQt/PyQtGraph pour monitoring et testing
  - Plus de 63 stars, 15 forks
- **Application: Projets motion control, robotics, vélos électriques

### 11. MiniBLDC TMC6200
- **URL**: https://github.com/sschoedel/MiniBLDC_TMC6200_v2
- **Nom**: MiniBLDC_TMC6200_v2
- **Couverture**:
  - Contrôleur BLDC basé sur TMC6200 + ESP32S3
  - Design inspiré par XESC project
  - Configuration daisy-chain pour 10-1000+ moteurs
  - TMC6200: abordable (~$5.5), SPI fault monitoring, courant inline
  - ESP32S3: dual-core (un core pour FOC loop, un pour communication)
  - Support CAN pour daisy-chaining
  - WiFi/BT intégré pour contrôle wireless
  - Support encodeur quadrature hardware
  - JTAG-USB intégré
- **Application: Systèmes multi-moteurs, robotics complexes

### 12. PCBasPRO Cheap FOC2VESC
- **URL**: https://github.com/PCBasPRO/PCBasPRO_0002_Cheap_FOC2VESC
- **Nom**: PCBasPRO_0002_Cheap_FOC2VESC
- **Couverture**:
  - Contrôleur 2-moteurs basé sur VESC6
  - 100V/200A continu (recommandation 84V/16A)
  - 22s batterie (6S à 21S LiPo/Li-ion)
  - STM32F405 CPU + BLE WT51822_S4AT
  - Clearance 1.5mm sur 100V (IPC-2221B)
  - Design 4 couches SMD avec gate drivers individuels
  - IMU intégré, USB-C, CAN et BLE
  - Trace 6mm pour rail cuivre
  - PCB 100x50mm, séparable en 2 PCBs
- **Application: Véhicules double moteur, développement low-cost

## Références Techniques et Documentation

### VESC Datasheets
- **VESC Classic**: https://vesclabs.com/datasheets/vesc_classic_datasheet.pdf
  - 100V, 160A continu, 200A crête
  - 10kW continu avec refroidissement
  
- **VESC Pronto**: https://www.vesclabs.com/wp-content/uploads/2026/02/vesc_pronto_datasheet.pdf
  - 100V, 150A continu, 200A crête
  - ESP32-C3 intégré, 4GB mémoire
  
- **VESC Maxim Plus 120V**: https://www.vesclabs.com/wp-content/uploads/2026/03/vesc_maxim_plus_120v_datasheet.pdf
  - 120V, 660A continu, 1000A crête
  - Haute puissance automotive

### Guides de Sélection
- **VESC Labs Motor Controller Selection**: https://www.vesclabs.com/2025/07/01/choosing-a-motor-controller/
  - Guide sélection tension, courant, caractéristiques moteur

### Standards de Sécurité
- **ISO 26262 Functional Safety**: Standard international pour systèmes E/E automobiles
  - ASIL levels (A à D) pour classification risques
  - FTTI (Fault Tolerant Time Interval) pour temps de réponse sécurité
  - Cycle de vie complet développement safety-critical

### Ressources Complémentaires
- **OpenInverter Project**: https://openinverter.org
  - Alternative aux solutions Tesla pour autres inverters
  
- **SimpleFOC Library**: Bibliothèque open source pour FOC sur Arduino/STM32
  - Supportée par Axel et autres projets

## Catégorisation par Application

### Véhicules Électriques Légers
- VESC Project (tous modèles)
- FOC King
- PCBasPRO Cheap FOC2VESC
- SF-Motion

### Conversion/Custom Automotive
- Tesla Model 3/Y Inverter
- VMU Vehicle Management Unit

### Compétition/Recherche
- Cornell Electric Vehicles
- OpenVVVF RTE
- SF-Motion

### Robotics/DIY
- Axel Framework
- MiniBLDC TMC6200
- Infineon IMR

### Développement Professional Automotive
- NXP PMSM FOC
- Infineon IMR
- VMU (MISRA C compliant)

## Notes sur les Licences
- **VESC**: GPL (General Public License)
- **Cornell CEV**: MIT License
- **Axel**: MIT License + Hardware License séparée
- **Tesla Inverter**: GPL v3.0
- **VMU**: Documentation MISRA compliant pour applications automotive
- **Infineon/NXP**: Licences manufacturer avec restrictions commerciales

## Statistiques GitHub (approximatives)
- **VESC**: 3.4k stars, 1.9k forks
- **Tesla Inverter**: 6 stars, 1 fork
- **FOC King**: 79 stars, 25 forks
- **Axel**: 12 stars, 0 forks
- **SF-Motion**: 63 stars, 15 forks
- **VMU**: 1 star, 0 forks

---

*Document généré le 2026-09-08*
*Basé sur recherche web et analyse des dépôts GitHub actifs*