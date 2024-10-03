# Guia del Proyecto

## Installar Pyenv

- https://www.samwestby.com/tutorials/rpi-pyenv.html
- https://www.dedicatedcore.com/blog/install-pyenv-ubuntu/

## Crear ambiente virtual

1. Corre `python -m venv .venv` para crear un ambiente virtual llamado `.venv` en el directorio donde se corre el comando
2. Activalo con `source .venv/bin/activate`

## Usar GitHub

Cada vez que de la Raspberry quieras cambiar un archivo del repositorio:

1. Ejecutar `git pull`
2. Hacer los cambios que desees
3. Ejecutar `git add <archivo_modificado>`
4. Ejecutar `git commit -m "Mensaje de que cambio hice"`
5. Finalmente ejecutar `git push --set-upstream origin main`


