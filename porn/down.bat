echo off
REM use UTF-8
REM chcp 936
set rootDir=/d %~dp0
C:
REM cd C:\workspace\GitHub\DownPython\porn\
cd %rootDir%jh\zpdr_ycsq_jh\
call python Down-JH-ZPDRYCSQ.py
REM
cd %rootDir%all\zpdr_ycsq_all\
call python WriteToTxt-All-ZPDRYCSQ.py
REM
cd %rootDir%all\xqfx\
call python writeToTxt-all-xqfx.py
REM
cd %rootDir%all\wawq_all\
call python WriteToTxt-All-WAWQ.py