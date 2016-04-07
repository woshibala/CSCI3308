# Team Project Testing
##Team member
Yang Song          <br/><https://github.com/woshibala><br/>
Xiaojun Yin        <br/><https://github.com/xiyi8580><br/>
Yu Qiu             <br/><https://github.com/yuqi6824><br/>
Zichao Yang        <br/><https://github.com/ziya1666><br/>
Zanqing Feng       <br/><https://github.com/zanking><br/><br/>
##Title
HEO website
<br/>
##Vision
HEO(Help Each Other) is a website where people can post their small diffculties, and any stranger can come to help them out.<br/>
For instance, old people who live alone can ask someone to help change lamp or move furniture via our website.<br/>
Disabled people can ask someone to get grocery for him/her by posting in our website.<br/>
##Automated Tests
>###Explanation<br/>
We use a Python standard library module: TestCase.unittest to do the automated tests.<br/>
We mainly test the database models in this project by creating some instances of User and Article and checking checking the value in the instances.<br/>
>###Screenshot<br/>
![](https://raw.github.com/woshibala/team-project-for-csci3308/SY/test1.png "Optional Title")<br/>
![](https://raw.github.com/woshibala/team-project-for-csci3308/SY/test2.png "Optional Title")<br/>

##User Acceptance Tests

 Use Case ID |  UC-01
------------ | -------------
Use Case Name |  User sign up.
Description | New users need to sign up and provide some information for further login.
User | New users.
Pre-conditions | Using local server port 8000, go to "127.0.0.1:8000/heo/index/".
Post-conditions | Sign up and automatically login, user information stored in database.
Frequency of use | Every new user. 

Flow of events:<br/>

Actor Action | System Response | Comments
------------ | --------------- | ---------
1. Click sign up in index page| Redirect to sign up page|
2. Enter username,email and password|   |
3. Click "Sign up" button| go to index page | Automactically login
4. In index page | Show hello "username" |

Test Pass?: PASS <br/><br/><br/>

![](https://raw.github.com/woshibala/team-project-for-csci3308/SY/test3.png "Optional Title")<br/>
![](https://raw.github.com/woshibala/team-project-for-csci3308/SY/test6.png "Optional Title")<br/>



Use Case ID |  UC-02
------------ | -------------
Use Case Name |  User login.
Description | User need login to get access to some pages
User | Registered users.
Pre-conditions | Already registered in Sign up page.
Post-conditions | Login in, go to index page.
Frequency of use | Everytime using the website. 

Flow of events:<br/>

Actor Action | System Response | Comments
------------ | --------------- | ---------
1. Click login | Redirect to login page|
2. Enter email address and password|   |
3. Click "Login" button| go to index page or error message | 
4. In index page | Show hello "username" |

Test pass?: PASS <br/><br/><br/>

![](https://raw.github.com/woshibala/team-project-for-csci3308/SY/test5.png "Optional Title")<br/>


Use Case ID |  UC-03
------------ | -------------
Use Case Name |  Add difficulties.
Description | User can post difficulties.
User | Registered users.
Pre-conditions | User already login.
Post-conditions | Difficulties listed in index page.
Frequency of use | Everytime need add difficulty. 

Flow of events:<br/>

Actor Action | System Response | Comments
------------ | --------------- | ---------
1. Click "Need help?" | Redirect to add page|
2. Enter title category and content|   |
3. Click "Add" button| Redirect to success page, show information of post| Create instance in database
4. Click "Back to home" button | Redirect to index page  |

Test pass?: PASS <br/><br/><br/>

![](https://raw.github.com/woshibala/team-project-for-csci3308/SY/test4.png "Optional Title")<br/>









