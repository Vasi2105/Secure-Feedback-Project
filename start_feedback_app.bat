@echo on

echo [Info] Verificam Python...
python --version
IF %ERRORLEVEL% NEQ 0 (
  echo [Eroare] Python nu este instalat sau nu este in PATH!
  pause
  exit /B 1
)

echo [Info] Verificam pip...
pip --version
IF %ERRORLEVEL% NEQ 0 (
  echo [Eroare] pip nu este instalat sau nu e in PATH!
  pause
  exit /B 1
)

echo [Info] Instalam pachetele din requirements.txt...
pip install -r requirements.txt
IF %ERRORLEVEL% NEQ 0 (
  echo [Eroare] Instalare pachete esuata!
  pause
  exit /B 1
)

echo [Info] Pornim serverul in background...
start /B python app.py

echo [Info] Asteptam 3 secunde sa se initializeze...
timeout /t 3 >nul

echo [Info] Deschidem browserul pe http://127.0.0.1:5000/
start "" http://127.0.0.1:5000/

pause
