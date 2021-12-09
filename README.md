# ppkwu_lab5

# Documentation API

API to search employee from the website https://panoramafirm.pl/
It generates vcard for the specified employee


## Downloading list of employees
Search specified employee, then click 'wygeneruj vCard'
to generate new vcf file with employee details

Example request

```
localhost:8080/api/search/elektryk
```

Example response</br>
![vca](https://user-images.githubusercontent.com/75738353/145409743-8b762bb2-ef00-4557-b18a-96991410549d.jpg)



## Generating vCard

Example request
```
localhost:8080/api/vcard
```