EESchema Schematic File Version 2
LIBS:cargador-pila-3,7v
LIBS:pila-3,7v
LIBS:switching-220v-12v
EELAYER 25 0
EELAYER END
$Descr A4 8268 11693 portrait
encoding utf-8
Sheet 1 1
Title "Cargador de 3 pilas 186500 para ciegos"
Date "2020-02-29"
Rev ""
Comp "Ojo de Van Gogh"
Comment1 "Esquematico por PIERRI, Matias Gabriel"
Comment2 ""
Comment3 ""
Comment4 ""
$EndDescr
$Comp
L Cargador-Pila-3,7V U?
U 1 1 5E59F84C
P 2750 3950
F 0 "U?" H 2150 3800 60  0000 C CNN
F 1 "Cargador-Pila-3,7V" H 2700 4050 60  0000 C CNN
F 2 "" H 2750 3950 60  0001 C CNN
F 3 "" H 2750 3950 60  0001 C CNN
	1    2750 3950
	1    0    0    -1  
$EndComp
$Comp
L Pila-3,7V U?
U 1 1 5E59FB66
P 2650 2100
F 0 "U?" H 2650 2100 60  0000 C CNN
F 1 "Pila-3,7V" H 2650 2200 60  0000 C CNN
F 2 "" H 2650 2100 60  0001 C CNN
F 3 "" H 2650 2100 60  0001 C CNN
	1    2650 2100
	1    0    0    -1  
$EndComp
$Comp
L Pila-3,7V U?
U 1 1 5E59FC71
P 4700 2100
F 0 "U?" H 4700 2100 60  0000 C CNN
F 1 "Pila-3,7V" H 4700 2200 60  0000 C CNN
F 2 "" H 4700 2100 60  0001 C CNN
F 3 "" H 4700 2100 60  0001 C CNN
	1    4700 2100
	1    0    0    -1  
$EndComp
$Comp
L Pila-3,7V U?
U 1 1 5E59FCE2
P 6600 2100
F 0 "U?" H 6600 2100 60  0000 C CNN
F 1 "Pila-3,7V" H 6600 2200 60  0000 C CNN
F 2 "" H 6600 2100 60  0001 C CNN
F 3 "" H 6600 2100 60  0001 C CNN
	1    6600 2100
	1    0    0    -1  
$EndComp
Text GLabel 2200 3150 1    60   Input ~ 0
B+
Wire Wire Line
	2200 3150 2200 3350
Wire Wire Line
	2200 3350 2150 3350
Wire Wire Line
	2150 3350 2150 3550
Text GLabel 2550 3150 1    60   Input ~ 0
B2
Text GLabel 3150 3150 1    60   Input ~ 0
B1
Text GLabel 3100 4400 3    60   Input ~ 0
B-
Text GLabel 3800 3800 2    60   Input ~ 0
P-
Text GLabel 3800 3950 2    60   Input ~ 0
P+
Wire Wire Line
	3800 3800 3550 3800
Wire Wire Line
	3550 3800 3550 3750
Wire Wire Line
	3550 3750 3350 3750
Wire Wire Line
	3350 3900 3550 3900
Wire Wire Line
	3550 3900 3550 3950
Wire Wire Line
	3550 3950 3800 3950
Wire Wire Line
	3100 4400 3100 4350
Wire Wire Line
	3100 4350 2950 4350
Wire Wire Line
	2950 4350 2950 4150
Wire Wire Line
	3050 3550 3050 3350
Wire Wire Line
	3050 3350 3150 3350
Wire Wire Line
	3150 3350 3150 3150
Wire Wire Line
	2500 3550 2500 3350
Wire Wire Line
	2500 3350 2550 3350
Wire Wire Line
	2550 3350 2550 3150
Text GLabel 1850 2200 3    60   Input ~ 0
B+
Text GLabel 3700 2250 3    60   Input ~ 0
B2
Text GLabel 5700 2250 3    60   Input ~ 0
B1
Text GLabel 7500 2250 3    60   Input ~ 0
B-
Wire Wire Line
	7500 2250 7500 2100
Wire Wire Line
	7500 2100 7450 2100
Wire Wire Line
	7450 2100 7450 2050
Wire Wire Line
	7450 2050 7250 2050
Wire Wire Line
	6000 2050 5800 2050
Wire Wire Line
	5800 2050 5800 2100
Wire Wire Line
	5800 2100 5550 2100
Wire Wire Line
	5700 2100 5700 2250
Wire Wire Line
	5550 2100 5550 2050
Wire Wire Line
	5550 2050 5350 2050
Connection ~ 5700 2100
Wire Wire Line
	3500 2050 3500 2100
Wire Wire Line
	3500 2100 3900 2100
Wire Wire Line
	3700 2100 3700 2250
Wire Wire Line
	3900 2100 3900 2050
Wire Wire Line
	3900 2050 4100 2050
Connection ~ 3700 2100
Wire Wire Line
	2050 2050 1850 2050
Wire Wire Line
	1850 2050 1850 2200
$Comp
L Switching-220V-12V U?
U 1 1 5E5A0CA4
P 5750 3850
F 0 "U?" H 5250 3500 60  0000 C CNN
F 1 "Switching-220V-12V" H 5800 3850 60  0000 C CNN
F 2 "" H 5750 3850 60  0001 C CNN
F 3 "" H 5750 3850 60  0001 C CNN
	1    5750 3850
	1    0    0    -1  
$EndComp
Text GLabel 4800 3550 0    60   Input ~ 0
P-
Text GLabel 4800 4150 0    60   Input ~ 0
P+
Wire Wire Line
	5200 3700 5000 3700
Wire Wire Line
	5000 3700 5000 3550
Wire Wire Line
	5000 3550 4800 3550
Wire Wire Line
	5200 4000 5000 4000
Wire Wire Line
	5000 4000 5000 4150
Wire Wire Line
	5000 4150 4800 4150
$EndSCHEMATC
