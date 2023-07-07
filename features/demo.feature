Feature: Feature Demo

 Scenario: login correcto
   Given el usuario está registrado
   When cuando introduce un nombre de usuario
   And cuando introduce su password
   And el usuario pulsa "Go"
   Then el usuario accede al portal


  Scenario: login incorrecto
   Given el usuario está registrado
   When cuando introduce un nombre de usuario
   And cuando introduce su password
   And el usuario pulsa "Go"
   Then el usuario accede al portal