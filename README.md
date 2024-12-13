# MYSQL Brukerveiledning
## Nedlastning
* Download mysql -->
* Download dbeaver -->

## Logg inn
Nå skal du gå inn i my sql med root brukeren din, root brukeren din kan kort defineres som admin brukeren på maskinen din så du skal ha tilgang fra den
* For og logge seg inn på root brukeren din kan du skrive (mysql -u root -p)
* husk at der du skiriver root er plasen hvor du kommer til og skriver inn navnet til alle brukerene du skriver i fremtiden. Husk at denne komandoen siden du kommer til og bruke den gjennom hele arbeidet ditt 
* Etter du har skervet inn dette skal du være inne på brukeren for og se privilegiene til brukeren og få en bekreftelse om at du er inne i riktig bruker kan du skrive SHOW GRANT
* Når du har lyst til og gå ut av brukeren skriver du exit  
## Lag database
## Lag ny brukter
Lag ny bruker i terminal = mysql> CREATE USER 'username'@'localhost' IDENTIFIED BY 'password';
* Når du skriver inn dette i terminalen bytter du ut 'username' med det du vil at brukeren skal hete og 'password' med passordet du vil at denne brukeren skal ha
* Når du har skrevet dette er du mest sansyneling inni denne nye brukeren nå så for og kjekke hvilken bruker du er inni og se hvaslags til gang den har kan du skrive SHOW GRANTS
* 
<br>

#### Om du vil se flere grants du kan gi kan du trykke på denne lengken 

#### Om du ikke forstår noe eller sitter fast kan du trykke på denne lenken <br>
Les alt her: https://www.digitalocean.com/community/tutorials/how-to-create-a-new-user-and-grant-permissions-in-mysql 

## Naviger mysql terminal
* I root brukeren har du tilgang til all privl


# dbeaver
### Connect
* Klikk på data på toppen av skjermen<br>
![data](https://github.com/user-attachments/assets/11ae0a7d-e13b-46f3-b291-4d7940c6e965)
* Så klikker du på NEW Database connection
* Når du har trykket velger du der etter mysql<br>
  ![Screenshot from 2024-12-13 12-31-59](https://github.com/user-attachments/assets/1f5a5bb3-ae3e-4e04-a07b-12e92bd535df)


