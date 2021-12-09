# ppkwu_lab5

# Documentation API

API to search employee from the website https://panoramafirm.pl/
It generates vcard for the specified employee


## Downloading list of employees
Search specified employee, then click 'wygeneruj vCard'
to generate new vcf file with employee details

<b>Example request</b>

```
localhost:8080/api/search/elektryk
```

<b>Example response</br>
![vca](https://user-images.githubusercontent.com/75738353/145409743-8b762bb2-ef00-4557-b18a-96991410549d.jpg)



## Generating vCard

<b>Example request, after pressing the button 'wygeneruj vCard'</b>
```
localhost:8080/api/vcard
```

<b>Example response, fill will be downloaded from the browser</b></br>
![1_w](https://user-images.githubusercontent.com/75738353/145416285-a34af68b-30f6-4392-a5d8-8ff076400282.jpg)</br>
![2_w](https://user-images.githubusercontent.com/75738353/145416290-9709e5a5-90ab-4062-ae9c-fccc2f442c29.jpg)</br>

