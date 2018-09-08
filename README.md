# Service Report #

[API Documentation](https://documenter.getpostman.com/view/5097449/RWaGVA8g)

### Description ###

+ Applied patterns of **HTTP/RESTFul**
+ Service of Report to retrieve information on complaints by a company in the determined city

### Tests ###
+   Run command line:

   + run test unit
        `pytest test_unit_controllers.py`
   
   + run test integration
        `pytest test_integration_app.py`
   


### This API is defined in: ###

   + **Programming Language:** [Python](https://www.python.org/) - [Flask](http://flask.pocoo.org/)
   + **Data:** Connect in Data Storage of Complains and Companies

### Access on AWS EC2 ###

+ **URL** <http://18.223.203.222:5020/>

+ **/GET** <http://18.223.203.222:5020/report?city=VAR_CITY&uf=VAR_UF&company=VAR_COMPANY_ID>
