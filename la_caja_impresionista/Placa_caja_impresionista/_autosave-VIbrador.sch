EESchema Schematic File Version 4
EELAYER 30 0
EELAYER END
$Descr A4 8268 11693 portrait
encoding utf-8
Sheet 1 1
Title "Sistema de vibracion "
Date "2020-03-15"
Rev "PIERRI, Matias"
Comp "Ojo de Van Gogh"
Comment1 ""
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L VIbrador-rescue:HC-05-Modulos-VIbrador-rescue U4
U 1 1 5E6EC1C3
P 5750 4100
F 0 "U4" V 6050 4100 50  0000 L CNN
F 1 "HC-05" V 5600 3850 50  0000 L CNN
F 2 "VibradorPCB:HC-05" H 5750 4100 50  0001 C CNN
F 3 "" H 5750 4100 50  0001 C CNN
	1    5750 4100
	0    1    1    0   
$EndComp
Wire Wire Line
	5350 6050 5250 6050
Wire Wire Line
	5250 6050 5250 6150
Text GLabel 5450 5400 1    50   Input Italic 0
OUT-
Wire Wire Line
	5250 5850 5250 5750
Wire Wire Line
	5250 5850 5350 5850
Text GLabel 5800 4800 3    50   Input ~ 0
OUT+
Text GLabel 5700 4800 3    50   Input ~ 0
OUT-
Wire Wire Line
	5500 4450 5500 4550
Wire Wire Line
	5500 4550 5550 4550
Wire Wire Line
	5550 4550 5550 4700
Wire Wire Line
	5550 4700 5500 4700
Wire Wire Line
	5500 4700 5500 4800
Wire Wire Line
	5600 4800 5600 4700
Wire Wire Line
	5600 4700 5650 4700
Wire Wire Line
	5650 4700 5650 4550
Wire Wire Line
	5650 4550 5600 4550
Wire Wire Line
	5600 4550 5600 4450
Wire Wire Line
	5700 4450 5700 4550
Wire Wire Line
	5700 4550 5750 4550
Wire Wire Line
	5750 4550 5750 4750
Wire Wire Line
	5750 4750 5700 4750
Wire Wire Line
	5700 4750 5700 4800
Wire Wire Line
	5800 4450 5800 4550
Wire Wire Line
	5800 4550 5850 4550
Wire Wire Line
	5850 4550 5850 4750
Wire Wire Line
	5850 4750 5800 4750
Wire Wire Line
	5800 4750 5800 4800
$Comp
L VIbrador-rescue:Buzzer-Modulos-VIbrador-rescue U3
U 1 1 5E6F1D29
P 5600 6000
F 0 "U3" H 5550 6050 50  0000 C CNN
F 1 "Buzzer" H 5650 5950 50  0000 C CNN
F 2 "VibradorPCB:Vibrador" H 5600 6000 50  0001 C CNN
F 3 "" H 5600 6000 50  0001 C CNN
	1    5600 6000
	-1   0    0    1   
$EndComp
Wire Wire Line
	6200 6100 6100 6100
Wire Wire Line
	6100 6100 6100 6200
Text GLabel 6350 5400 1    50   Input ~ 0
OUT-
Wire Wire Line
	6100 5900 6200 5900
$Comp
L VIbrador-rescue:Buzzer-Modulos-VIbrador-rescue U5
U 1 1 5E8A4DBD
P 6450 6050
F 0 "U5" H 6350 6100 50  0000 C CNN
F 1 "Buzzer" H 6500 6000 50  0000 C CNN
F 2 "VibradorPCB:Vibrador" H 6450 6050 50  0001 C CNN
F 3 "" H 6450 6050 50  0001 C CNN
	1    6450 6050
	-1   0    0    1   
$EndComp
$Comp
L VIbrador-rescue:PiZeroW U6
U 1 1 5E9167F3
P 2800 4300
F 0 "U6" H 3100 2350 50  0000 C CNN
F 1 "PiZeroW" H 2650 4384 50  0000 C CNN
F 2 "Module:Raspberry_Pi_Zero_Socketed_THT_FaceDown_MountingHoles" H 2800 4300 50  0001 C CNN
F 3 "" H 2800 4300 50  0001 C CNN
	1    2800 4300
	1    0    0    -1  
$EndComp
$Comp
L VIbrador-rescue:Arduino_Nano_v3.x-MCU_Module-VIbrador-rescue A1
U 1 1 5E91EE2F
P 2850 2500
F 0 "A1" H 2850 1411 50  0000 C CNN
F 1 "Arduino_Nano_v3.x" H 2850 1320 50  0000 C CNN
F 2 "Module:Arduino_Nano" H 3000 1550 50  0001 L CNN
F 3 "http://www.mouser.com/pdfdocs/Gravitech_Arduino_Nano3_0.pdf" H 2850 1500 50  0001 C CNN
	1    2850 2500
	1    0    0    -1  
$EndComp
Wire Wire Line
	2950 3800 2950 3500
Wire Wire Line
	2850 3500 2950 3500
Connection ~ 2950 3500
Wire Wire Line
	2750 1350 2750 1500
Wire Wire Line
	3400 4650 3200 4650
Wire Wire Line
	3400 4750 3200 4750
Text GLabel 3700 4350 2    50   Input ~ 0
OUT+
Wire Wire Line
	3600 4350 3600 4300
Wire Wire Line
	3600 4300 3400 4300
Wire Wire Line
	3400 4300 3400 4350
Wire Wire Line
	3400 4350 3200 4350
Text GLabel 3750 5300 2    50   Input ~ 0
OUT-
Wire Wire Line
	3400 5300 3400 5250
Wire Wire Line
	3400 5250 3200 5250
Wire Wire Line
	3700 4350 3600 4350
Text GLabel 2950 3800 2    50   Input ~ 0
OUT-
Text GLabel 2750 1350 2    50   Input ~ 0
OUT+
Wire Wire Line
	3400 5050 3200 5050
Wire Wire Line
	3400 5150 3200 5150
Text GLabel 5250 6150 3    50   Input ~ 0
GPIO11
Text GLabel 6100 6200 3    50   Input ~ 0
GPIO11
Text GLabel 1850 5450 0    50   Input ~ 0
GPIO11
Wire Wire Line
	2500 5450 2300 5450
Wire Wire Line
	2300 5450 2300 5500
Wire Wire Line
	2300 5500 1950 5500
Wire Wire Line
	1950 5500 1950 5450
Wire Wire Line
	1950 5450 1850 5450
Text GLabel 5600 4800 3    50   Input ~ 0
TX
Text GLabel 2350 1900 0    50   Input ~ 0
TX
Text GLabel 2350 2000 0    50   Input ~ 0
RX
Text GLabel 5500 4800 3    50   Input ~ 0
RX
$Comp
L VIbrador-rescue:Ultrasonico-VIbrador-rescue U?
U 1 1 5F11CF15
P 4250 1600
F 0 "U?" H 4450 1400 50  0000 L CNN
F 1 "Ultrasonico" H 3950 1700 50  0000 L CNN
F 2 "" H 4250 1600 50  0001 C CNN
F 3 "" H 4250 1600 50  0001 C CNN
	1    4250 1600
	1    0    0    -1  
$EndComp
Text GLabel 4100 2300 3    50   Input ~ 0
OUT+
Text GLabel 4400 2300 3    50   Input ~ 0
OUT-
Text GLabel 4200 2300 3    50   Input ~ 0
TRIG
Text GLabel 4300 2300 3    50   Input ~ 0
Echo
Text GLabel 3800 4850 2    50   Input ~ 0
TRIG
Wire Wire Line
	3800 4850 3750 4850
Wire Wire Line
	3750 4850 3750 4900
Wire Wire Line
	3750 4900 3400 4900
Wire Wire Line
	3400 4900 3400 4850
Wire Wire Line
	3400 4850 3200 4850
Wire Wire Line
	4100 1850 4100 1950
Wire Wire Line
	4100 1950 4150 1950
Wire Wire Line
	4150 1950 4150 2250
Wire Wire Line
	4150 2250 4100 2250
Wire Wire Line
	4100 2250 4100 2300
Wire Wire Line
	4400 1850 4400 1950
Wire Wire Line
	4400 1950 4450 1950
Wire Wire Line
	4450 1950 4450 2250
Wire Wire Line
	4450 2250 4400 2250
Wire Wire Line
	4400 2250 4400 2300
Wire Wire Line
	4200 2300 4200 2250
Wire Wire Line
	4200 2250 4250 2250
Wire Wire Line
	4250 2250 4250 1950
Wire Wire Line
	4250 1950 4200 1950
Wire Wire Line
	4200 1950 4200 1850
Wire Wire Line
	4300 2300 4300 2250
Wire Wire Line
	4300 2250 4350 2250
Wire Wire Line
	4350 2250 4350 1950
Wire Wire Line
	4350 1950 4300 1950
Text GLabel 3700 4350 2    50   Input ~ 0
OUT+
Text GLabel 4750 5050 2    50   Input ~ 0
ECHO
Wire Wire Line
	3400 5300 3750 5300
Wire Wire Line
	3400 5150 3400 5100
Wire Wire Line
	3400 5100 3800 5100
Wire Wire Line
	3800 5100 3800 5050
$Comp
L VIbrador-rescue:R-Resistors R?
U 1 1 5F12F5BA
P 4300 5300
F 0 "R?" H 4370 5346 50  0000 L CNN
F 1 "470" V 4300 5250 50  0000 L CNN
F 2 "" V 4230 5300 50  0001 C CNN
F 3 "~" H 4300 5300 50  0001 C CNN
	1    4300 5300
	1    0    0    -1  
$EndComp
$Comp
L VIbrador-rescue:R-Resistors R?
U 1 1 5F12598C
P 4550 5050
F 0 "R?" V 4450 5050 50  0000 C CNN
F 1 "330" V 4550 5050 50  0000 C CNN
F 2 "" V 4480 5050 50  0001 C CNN
F 3 "~" H 4550 5050 50  0001 C CNN
	1    4550 5050
	0    1    1    0   
$EndComp
Wire Wire Line
	4750 5050 4700 5050
Wire Wire Line
	3800 5050 4300 5050
Wire Wire Line
	4300 5050 4300 5150
Connection ~ 4300 5050
Wire Wire Line
	4300 5050 4400 5050
Text GLabel 4300 5550 3    50   Input ~ 0
OUT-
Wire Wire Line
	4300 5450 4300 5550
$Comp
L VIbrador-rescue:Switch-4-posiciones-VIbrador-rescue U?
U 1 1 5F14136B
P 6450 1650
F 0 "U?" H 6800 1000 50  0000 C CNN
F 1 "Switch-4-posiciones" H 6400 1750 50  0000 C CNN
F 2 "" H 6450 1650 50  0001 C CNN
F 3 "" H 6450 1650 50  0001 C CNN
	1    6450 1650
	1    0    0    -1  
$EndComp
Text GLabel 6950 1650 2    50   Input ~ 0
OUT-
Text GLabel 5700 1750 0    50   Input ~ 0
OUT-
Wire Wire Line
	5950 1750 5700 1750
Text GLabel 5700 2050 0    50   Input ~ 0
OUT-
Text GLabel 6950 2150 2    50   Input ~ 0
OUT-
Wire Wire Line
	5950 2050 5700 2050
$Comp
L VIbrador-rescue:R-Resistors R?
U 1 1 5F14B51D
P 7400 1750
F 0 "R?" V 7600 1750 50  0000 C CNN
F 1 "10K" V 7400 1750 50  0000 C CNN
F 2 "" V 7330 1750 50  0001 C CNN
F 3 "~" H 7400 1750 50  0001 C CNN
	1    7400 1750
	0    1    1    0   
$EndComp
Text GLabel 7550 1750 2    50   Input ~ 0
OUT+
$Comp
L VIbrador-rescue:R-Resistors R?
U 1 1 5F14E26A
P 5250 1850
F 0 "R?" V 5150 1850 50  0000 C CNN
F 1 "10K" V 5250 1850 50  0000 C CNN
F 2 "" V 5180 1850 50  0001 C CNN
F 3 "~" H 5250 1850 50  0001 C CNN
	1    5250 1850
	0    1    1    0   
$EndComp
$Comp
L VIbrador-rescue:R-Resistors R?
U 1 1 5F14E782
P 5250 1950
F 0 "R?" V 5350 1950 50  0000 C CNN
F 1 "10K" V 5250 1950 50  0000 C CNN
F 2 "" V 5180 1950 50  0001 C CNN
F 3 "~" H 5250 1950 50  0001 C CNN
	1    5250 1950
	0    1    1    0   
$EndComp
Text GLabel 5100 1850 0    50   Input ~ 0
OUT+
Text GLabel 5100 1950 0    50   Input ~ 0
OUT+
Wire Wire Line
	5950 1850 5400 1850
Wire Wire Line
	5950 1950 5400 1950
Text GLabel 7550 2050 2    50   Input ~ 0
OUT+
Text GLabel 1850 5450 0    50   Input ~ 0
GPIO11
Text GLabel 2350 1900 0    50   Input ~ 0
TX
Text GLabel 2350 2000 0    50   Input ~ 0
RX
$Comp
L VIbrador-rescue:R-Resistors R?
U 1 1 5F154336
P 7400 2050
F 0 "R?" V 7193 2050 50  0000 C CNN
F 1 "10K" V 7400 2050 50  0000 C CNN
F 2 "" V 7330 2050 50  0001 C CNN
F 3 "~" H 7400 2050 50  0001 C CNN
	1    7400 2050
	0    1    1    0   
$EndComp
Wire Wire Line
	6850 1750 7250 1750
Wire Wire Line
	7250 2050 6850 2050
Wire Wire Line
	6950 1650 6850 1650
Wire Wire Line
	6850 2150 6950 2150
Text GLabel 5400 2150 3    50   Input ~ 0
GPIO5
Text GLabel 5400 1650 1    50   Input ~ 0
GPIO6
Text GLabel 7250 1500 1    50   Input ~ 0
GPIO13
Text GLabel 7250 2250 3    50   Input ~ 0
GPIO19
Wire Wire Line
	7250 1500 7250 1750
Connection ~ 7250 1750
Wire Wire Line
	7250 2050 7250 2250
Connection ~ 7250 2050
Wire Wire Line
	5400 2150 5400 1950
Connection ~ 5400 1950
Wire Wire Line
	5400 1650 5400 1850
Connection ~ 5400 1850
Text GLabel 1800 5750 0    50   Input ~ 0
GPIO5
Text GLabel 1800 5850 0    50   Input ~ 0
GPIO6
Text GLabel 1800 5950 0    50   Input ~ 0
GPIO13
Text GLabel 1800 6050 0    50   Input ~ 0
GPIO19
Wire Wire Line
	2500 5750 2300 5750
Wire Wire Line
	2300 5750 2300 5800
Wire Wire Line
	2300 5800 1850 5800
Wire Wire Line
	1850 5800 1850 5750
Wire Wire Line
	1850 5750 1800 5750
Wire Wire Line
	1800 5850 1850 5850
Wire Wire Line
	1850 5850 1850 5900
Wire Wire Line
	1850 5900 2300 5900
Wire Wire Line
	2300 5900 2300 5850
Wire Wire Line
	2300 5850 2500 5850
Wire Wire Line
	1800 5950 1850 5950
Wire Wire Line
	1850 5950 1850 6000
Wire Wire Line
	1850 6000 2300 6000
Wire Wire Line
	2300 6000 2300 5950
Wire Wire Line
	2300 5950 2500 5950
Wire Wire Line
	1800 6050 1850 6050
Wire Wire Line
	1850 6050 1850 6100
Wire Wire Line
	1850 6100 2300 6100
Wire Wire Line
	2300 6100 2300 6050
Wire Wire Line
	2300 6050 2500 6050
$Comp
L VIbrador-rescue:R-Resistors R?
U 1 1 5F166DD1
P 6350 5550
F 0 "R?" H 6420 5596 50  0000 L CNN
F 1 "R-Resistors" H 6420 5505 50  0000 L CNN
F 2 "" V 6280 5550 50  0001 C CNN
F 3 "" H 6350 5550 50  0001 C CNN
	1    6350 5550
	1    0    0    -1  
$EndComp
$Comp
L VIbrador-rescue:R-Resistors R?
U 1 1 5F1677D6
P 5450 5550
F 0 "R?" H 5520 5596 50  0000 L CNN
F 1 "R-Resistors" H 5520 5505 50  0000 L CNN
F 2 "" V 5380 5550 50  0001 C CNN
F 3 "" H 5450 5550 50  0001 C CNN
	1    5450 5550
	1    0    0    -1  
$EndComp
Wire Wire Line
	6350 5700 6100 5700
Wire Wire Line
	6100 5700 6100 5900
$EndSCHEMATC
