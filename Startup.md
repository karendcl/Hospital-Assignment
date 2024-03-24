# Como correr el proyecto?

> Es importante que tenga instalado Python 3.8 o superior.

1. Abra la terminal en la carpeta del proyecto.
2. Ejecute los siguientes comandos en la terminal:

```bash
cd logic
pip install -r requirements.txt
```

3. Para correr el proyecto ejecute el siguiente comando en la terminal:

```bash
uvicorn endpoints:app --reload
```

4. Luego de un tiempo debera salir en la consola un mensaje con un link. Use el link y se abre el navegador en la pagina