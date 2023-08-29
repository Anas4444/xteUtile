@echo off

rem Set the variable to the path of the directory
set "jboss_dir=D:\Projects\Xtensus\keycloak-16.1.1\bin"

echo Changing directory to: "%jboss_dir%"
cd /d "%jboss_dir%"

rem Display the contents of standalone.bat
type standalone.bat

rem Run the standalone.bat script with the specified system property
echo Running standalone.bat...
call standalone.bat -Djboss.http.port=9080