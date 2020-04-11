# Laboratorio BigData
# STO263 Tópicos especiales en telemática 

# Mateo Flórez Restrepo
# 2020-1

### Contenidos del laboratorio
* Creacion y gestion de archivos en EMR

* Gestion de archivos en HDFS Y S3

* Map/Reduce 

* Ejercicio Map/ Reduce con MRJob

# Bitácora

### 1. Creacion y gestión de archivos en EMR 

* Creación del cluster

  Ingresamos a nuestra cuenta AWS Educate e ingresamos a la consola de AWS.
  
  Creamos una KeyPair que ira asociada con el cluster
  
  ![KeyPair](EMR/emr1.png) 

  Cluster por método interactivo:
  
  Buscamos a EMR en la consola, y creamos un nuevo cluster.
  
  Recursos:
  
  ![EMR](EMR/emr2.png) 
  
  Cluster creado:
  
![KeyPair](EMR/emr3.png)
  
  ![KeyPair](EMR/emr4.png) 
  
  Se agrega las reglas para los puertos pertenecientes a Hue(8888) a Zeppelin(8890) y SSH(22)
  
  ![KeyPair](EMR/emr5.png) 
  
  Luego vamos a la seccion de Bloqueo de acceso publico y agregamos el rango de puertos de usaremos para este laboratorio.
  
  ![KeyPair](EMR/emr28.PNG) 
  
  ## Scripts importantes para creacion y destruccion de clusters
  
  ![KeyPair](EMR/emr6.PNG) 

* Destrucción de un cluster
  
  Interactivamente:
  
  ![KeyPair](EMR/emr7.PNG)
  
  Por línea de comandos:
  
    1.	Actualizamos las credenciales de AWS CLI
    
    2.	Ubico el id del cluster y lo destruyo con el siguiente comando
      
   ![KeyPair](EMR/emr8.PNG)
  
      
* Recreación/Clonación del cluster
  
  Interactivamente: 
  
   ![KeyPair](EMR/emr9-1.PNG)
   
  Por línea de comandos:
  
     1.	Entramos a la información del cluster
     
     2.	Consultamos el comando de AWS CLI
    
    ![KeyPair](EMR/emr9.PNG)
    
     3.	Ejecutamos
  
    ![KeyPair](EMR/emr10.PNG)  
      
    ![KeyPair](EMR/emr11.PNG)

  ## Habilitar entradas remotas
  
  * SSH
  
  Conexión mediante la herramienta putty:
  
  ![KeyPair](EMR/emr12.png)
  
  ![KeyPair](EMR/emr13.png)
  
  
  * HUE
  
 Interfaz para ingeniero de datos
 
 ![KeyPair](EMR/emr14.png)
 
 ## GESTIÓN DE ARCHIVOS A HDFS Y S3
 
 * Desde HUE:
 
  1.	A HDFS:
 
  Creamos los directorios y subimos los datasets.
  
  ![KeyPair](EMR/emr15.png)
  
  2. A S3
  
  Nos ubicamos en nuestro bucket, o creamos uno nuevo
  
  ![KeyPair](EMR/emr16.png)
  
  Creamos los directorios y subimos los archivos.
  
   ![KeyPair](EMR/emr17.png)
   
  [OPCIONAL] Crear un bucket nuevo desde HUE
  
  ![KeyPair](EMR/emr18.PNG)
  
  Crear directorios y subir archivos
 
  ![KeyPair](EMR/emr19.png)
  
  
 * Desde Shell:

  1.	A HDFS
  
  Accedemos al nodo maestro a través de ssh por putty, debido a que los datasets aún no están en el nodo local debemos descargarlos. Ya que no existe el comando git, lo traemos desde HDFS(tambien se puede desde s3) teniendo en cuenta que los datasets ya se encuentran ahí.
  
  ![KeyPair](EMR/emr20.png)
  
  Creamos un directorio y traemos todos los datasets a este.
  
  ![KeyPair](EMR/emr21.png)
  
  Para subir desde Shell a HDFS lo que hacemos es crear otra carpeta en HDFS y subimos los archivos. (El proceso inverso).
  
  ![KeyPair](EMR/emr22.png)
  
  ![KeyPair](EMR/emr23.png)
  
 2. A S3
  
  ![KeyPair](EMR/emr24.png)
  
  Copiaremos los archivos locales al directorio “datasetsshell”. Podemos copiar un archivo por uno con el comando cp o podemos subir los directorios con sync.
  
  ![KeyPair](EMR/emr25.PNG)
 
 Los archivos fueron copiados, podemos verificar por shell o de manera interactiva en la consola de AWS/S3:
 
 ![KeyPair](EMR/emr26.png)
 
 ![KeyPair](EMR/emr27.png)
 
 
  
  
  
  
  

 
   
  
 
 
  

  
  
  
  
  


