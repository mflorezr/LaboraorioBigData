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

## 1. Creacion y gestión de archivos en EMR 

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
  
  ![KeyPair](EMR/emr6.png) 

* Destrucción de un cluster
  
  Interactivamente:
  
  ![KeyPair](EMR/emr7.png)
  
  Por línea de comandos:
      1.	Actualizamos las credenciales de AWS CLI
      2.	Ubico el id del cluster y lo destruyo con el siguiente comando
      
   ![KeyPair](EMR/emr8.png)
   
   ![KeyPair](EMR/emr9.png)
      
* Recreación/Clonación del cluster
  
  Interactivamente: 
  
   ![KeyPair](EMR/emr10.png)
   
  Por línea de comandos:
      1.	Entramos a la información del cluster
      2.	Consultamos el comando de AWS CLI
    
    ![KeyPair](EMR/emr11.png)
    
     3.	Ejecutamos
  
    ![KeyPair](EMR/emr12.png)  
      
    ![KeyPair](EMR/emr13.png)


  
  
  
  
  


