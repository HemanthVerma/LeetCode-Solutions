Select firstName,LastName,city,state
from Person
LEFT JOIN Address
On Person.personID = Address.personId