@echo off
chcp 65001 >nul
setlocal
title Rellenar imagenes - Curso Gas B
echo ============================================================
echo   RELLENAR IMAGENES REALISTAS - Curso Gas B
echo ============================================================
echo.

REM 1) Comprobar Python
where python >nul 2>nul
if errorlevel 1 (
  echo [!] No se ha encontrado Python.
  echo     Instala Python 3 desde https://www.python.org/downloads/
  echo     IMPORTANTE: marca la casilla "Add python.exe to PATH" al instalar.
  echo.
  pause
  exit /b 1
)

REM 2) Instalar dependencias
echo Instalando dependencias (solo la primera vez)...
python -m pip install --quiet --upgrade python-pptx requests
echo.

REM 3) Pedir la clave y la carpeta
echo Necesitas una clave GRATUITA de Pexels: https://www.pexels.com/api/  (boton "Get Started")
set /p CLAVE=Pega aqui tu clave de Pexels y pulsa Enter:
echo.
echo Arrastra la carpeta "Curso Gas B" a esta ventana y pulsa Enter
set /p CARPETA=Carpeta:
echo.

REM 4) Ejecutar
python "%~dp0rellenar_imagenes.py" %CARPETA% %CLAVE%

echo.
echo ============================================================
echo   Listo. Busca los archivos "... (con imagenes).pptx"
echo ============================================================
pause
endlocal
