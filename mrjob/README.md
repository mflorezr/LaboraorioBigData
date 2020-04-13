# LABORATORIO MRJOB
# Mateo Florez Restrepo


## Problema 

  1. Se tiene un conjunto de datos, que representan el salario anual de los empleados formales en Colombia por sector económico, según la DIAN.
  
          idemp,sececon,salary,year
      
          3233,1234,35000,1960
          3233,5434,36000,1961
          1115,3432,34000,1980
          3233,1234,40000,1965
          1115,1212,77000,1980
          1115,1412,76000,1981
          1116,1412,76000,1982

* Realizar un programa en Map/Reduce, con hadoop en Python o Java, que permita calcular:

  1. El salario promedio por Sector Económico (SE)
  2. El salario promedio por Empleado
  3. Número de SE por Empleado que ha tenido a lo largo de la estadística
  
## Solucion

   Antes de probarlos se debe descargar la libreria de mrjob para usar los recursos 
              
       $ pip install mrjob

   1. El salario promedio por Sector Económico (SE)
      
      El programa creado para resolver esta pregunta es : [AnnualSalary.py](AnnualSalary.py)
      
      Comando para probarlo con un dataset local [datasets](../datasets/)
   

  
