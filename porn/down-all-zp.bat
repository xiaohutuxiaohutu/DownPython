echo off
REM use UTF-8
REM chcp 936
set rootDir=/d %~dp0
C:
REM
cd %rootDir%all\zpdr_ycsq_all\
call python Down-Pic-All-ZPDRYCSQ.py
