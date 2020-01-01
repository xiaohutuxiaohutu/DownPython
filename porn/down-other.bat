echo off
REM use UTF-8
REM chcp 936
set rootDir=/d %~dp0
C:
REM
cd %rootDir%all\xqfx\
call python downPic-all-xqfx.py
REM
cd %rootDir%all\wawq_all\
call python Down-All-WAWQ.py