@echo off

rem Set the variable to the path of the directory
set "jutile_dir=D:\Projects\Xtensus\utile"

cd /d "%jutile_dir%"
start "" start_keycloak.bat
start "" start_jhipsterregistry.bat
timeout /t 100
start "" start_xteback.bat
timeout /t 50
start "" start_xtefront.bat
timeout /t 50
start "" start_stocks.bat
start "" start_vehicule.bat
start "" start_personnel.bat