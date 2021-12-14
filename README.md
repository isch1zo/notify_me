# Notify me tool:
python script that notify the user if there is a change happend in a url page.

#### Note: There are few things you have to do before using the tool:

1- Edit the script with suitable settings

- In 'mail_subject' variable, type the subject to use in mail sending.
- In 'mail_content' variable, type your message that will be sent to your email. 
![image](https://user-images.githubusercontent.com/42019491/145918897-4441b5d6-360d-474e-9566-364eb86be114.png)

- Here write your gmail email and password if you don't have or scared from me create new one to use it.
![image](https://user-images.githubusercontent.com/42019491/145918490-bddc0420-bbe4-4e63-862f-eef2880799a6.png)

- Here write reciever mail.

![image](https://user-images.githubusercontent.com/42019491/145919006-452cf26a-54f1-4ccc-89f5-cca1d6e607aa.png)

- so far we done the main function in the tool which is send_mail() function.


- Here write the target url.

![image](https://user-images.githubusercontent.com/42019491/145919118-f781b72f-c95d-4f75-a6fb-7eb053de641b.png)

- THE LAST STEP is to find a way to check if the item is Avaliable or not (YOU NEED TO DO IT BY YOUR SELF).
  - YOU NEED TO FIND A WAY TO GET SPECIAL PART OF THE TARGETED PAGE.
  - FOR EXAMPLE:
  - I FOUND IN ONE WEBSITE IF THERE IS A 'span' TAG WITH 'not-available' CLASS MEANS THAT THE ITEM IS NOT AVAILABLE, AND IF THERE IS NO 'span' TAG WITH 'not-available' CLASS MEANS THE ITEM IS AVAILABLE.
  - SO MY CODE WAS AS SHOWN BELOW.
![image](https://user-images.githubusercontent.com/42019491/145919230-c2545fab-89ec-4ff9-979d-693263242d3c.png)

 ### NOTE THIS IS JUST EXAMPLE.

2- You need to have gmail account & and you need to turn on "Less secure app access" setting from Security Settings.
![image](https://user-images.githubusercontent.com/42019491/120665621-9f322680-c494-11eb-9148-70f9eb84125c.png)
![image](https://user-images.githubusercontent.com/42019491/120665757-bcff8b80-c494-11eb-8e02-ce4dd3c8eac5.png)

3- Then install python libraries used in the tool:

```pip install -r requirements.txt```

### لا تنسوني من دعائكم <3
