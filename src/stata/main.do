clear all

cap clear
cap log close
set more 1
set matsize 10000
set maxvar 10000

log using "../../log/main_do", t replace

cap log close
