#include<stdio.h>
#include<stdlib.h>
#include<time.h>
#include<string.h>

#define scanUserdata fscanf(fp,"%s\t%s\t%d\t%c\t%s\t%d",u[testcount].username,u[testcount].password,&u[testcount].age,&u[testcount].gender,u[testcount].location,&u[testcount].hobby)!=EOF

void welcomeScreen();

void loadingScreen();
void delay(float);

void header();
void homeScreen();

void signup();
void signin();

void loggedIn(char [],int,char,char [],int);
void matchmaking(char [],int,char,char [],int);

typedef struct userDatabase {
   char username[20];
   char password[20];
   int age;
   char gender;
   char location[20];
   int hobby;
}users;
users u[1000];
FILE *fp;

main () {
  fp=fopen("userDetails.txt","a+");
  welcomeScreen();
}


void welcomeScreen(){
  printf("\n\n\n\n\n\n\n");
  printf("\t \t \t \t  ******************************************************\n\n");
  printf("\t \t \t \t \t \t WELCOME TO CARA-APP \n \t \t \t \t \t \t \n\n");
  printf("\t\t \t \t \t cara : portugese for friendship ;)\n\n");
  printf("\t \t \t \t  ******************************************************\n");
  printf("\n\n\n\t\t\t\t\t   Please press 1 to Continue\n \t\t\t\t\t\t        2 to Exit\n\n\n Enter your choice: ");
    int choice;
 scanf("%d", &choice);
 switch (choice){
 case 1: homeScreen();
               break;
 case 2: exit(0);
               break;
 default: printf("Enter a valid choice");
 }
}

void loadingScreen(){
    system("cls");
    printf("\n\n\n\n\n\n\n\n\n\n\n\t\t\t\t\t\t\t  LOADING");
    printf("\n     \t\t\t\t\t\t\t");
    int j;
   for (j=1;j<=12;j++){
        delay(0.1);
printf("%c",177);
}
system("cls");
}
void delay (float Nseconds){
float miliseconds=1000*Nseconds;
clock_t startTime=clock();
while(clock()<startTime + miliseconds);
}

void header(){
  printf("\t \t \t \t  ====================================================\n\n");
  printf("\t \t \t \t \t \t  \t CARA-APP \n \t \t \t \t \t \t \n");
  printf("\t \t \t \t \t  'friends are siblings god never gave us' \n \t \t \t \t \t \t \n");
  printf("\t \t \t \t =====================================================\n\n");
}

void homeScreen(){
    loadingScreen();
    printf("\n\n\n\n\n\n\n");
   header();
   printf("\n\t\t\t\t\t   For new users, after signing up\n\t");
   printf("\t\t\tpress 3 to exit & restart it to complete you registration.");
  printf("\n\n\t\t\t\t\t   Please press 1 to Sign Up\n \t\t\t\t\t\t        2 to Sign In\n \t\t\t\t\t\t        3 to Exit\n\n\n Enter your choice: ");
    int choice;
 scanf("%d", &choice);
 switch (choice){
 case 1: signup();
               break;
 case 2: signin();
               break;
 case 3: exit(0);
               break;
 default: printf("Next time enter a valid choice.");
 }
}

int countingTotalUsers(){
 rewind(fp);
 char lines;
 int c=0;
 for (lines= getc(fp); lines != EOF; lines = getc(fp))
        if (lines == '\n')
            c++;
  return c;
}

void signup() {
 loadingScreen();
  header();
  char newuser[20],checkpass[20];
  validateUser:
  printf("\n\t\t\t\t\t\t  Enter Username: ");
  scanf("%s", newuser);
  int testcount=0;
  rewind(fp);
  int flag=0;
 while (scanUserdata)
         {
  if (strcmpi(u[testcount].username,newuser)==0){
      flag=1;
    }
  testcount++;
       }

       if (flag==1) {
            printf("\n\t\t\t\tUser already exists. Please enter a different username.\n");
       goto validateUser;
       }
       else {
    strcpy(u[testcount].username,newuser);
    fprintf(fp,"%s\t", u[testcount].username);
       }

 validatePass:
 printf("\n\t\t\t\t\t\t  Enter Password: ");
 scanf("%s",u[testcount].password);
 printf("\n\t\t\t\t\t\t  Confirm Password: ");
 scanf("%s",checkpass);
 if (strcmpi(u[testcount].password,checkpass)!=0){
    printf("\n\t\t\t\t \tPasswords don't match. Please enter again.\n ");
    goto validatePass;
 }
 printf("\n\t\t\t\t\t\t  Enter your age: ");
 scanf("%d",&u[testcount].age);
 printf("\n\t\t\t\t\t\t  Enter your gender, M for Male F for Female:  ");
 scanf(" %c", &u[testcount].gender);
 printf("\n\t\t\t\t\t\t Enter your location: ");
 scanf("%s",u[testcount].location);
 printf("\n\t\t\t\t\t Enter your favorite hobby from the list given below: \n\t\t\t\t\t\t\t 1 for Reading Books.");
 printf("\n\t\t\t\t\t\t\t 2 for Playing Sports.\n\t\t\t\t\t\t\t 3 for Watching Movies or TV. \n\t\t\t\t\t\t\t 4 for Cooking.\n\t\t\t\t\t\t\t 5 for Dancing.\n");
 printf("\n\t\t\t\t\t\tEnter your choice: ");
 scanf("%d", &u[testcount].hobby);
 fprintf(fp,"%s\t%d\t%c\t%s\t%d\n", u[testcount].password,u[testcount].age,u[testcount].gender,u[testcount].location,u[testcount].hobby);
 system("cls");
 homeScreen();
}

 void signin(){
 loadingScreen();
 header();
 int testcount=0,flag=0;
 char name[20],pass[20],z,ch;
 printf("\n\t\t\t\t\t\t  Enter Username: ");
  scanf("%s", name);
 printf("\n\t\t\t\t\t\t  Enter Password: ");
 scanf("%s",pass);
 rewind(fp);
  while(scanUserdata){
   if ( strcmpi(u[testcount].username,name)==0 && strcmp(u[testcount].password,pass)==0 ){
   loggedIn(u[testcount].username,u[testcount].age,u[testcount].gender,u[testcount].location,u[testcount].hobby);
   }
     testcount++;
   }
   if (!flag){
    printf("\t\t\t\tUser does not exist. Please enter again.");
   }
}
void loggedIn(char cUsername[20],int cAge,char cGender,char cLocation[20],int cHobby){
system("cls");
 loadingScreen();
 header();
 printf("\t\t\t\t\t\t     Welcome back %s\n\n", cUsername);
 printf("  Your Profile: \n");
 printf("  Age: %d\n",cAge);
 printf("  Gender: %c\n",cGender);
 printf("  Location: %s\n",cLocation);
 switch (cHobby){
    case 1:printf("  Hobby: Reading Books\n\n"); break;
    case 2:printf("  Hobby: Playing Sports\n\n"); break;
    case 3:printf("  Hobby: Watching TV or Movies\n\n"); break;
    case 4:printf("  Hobby: Cooking\n\n"); break;
    case 5:printf("  Hobby: Dancing\n\n"); break;
 }
 printf(" Click 1 to see people with similar age and hobby, Click 2 to exit: ");
 int ch;
 choice:
 scanf("%d",&ch);
 switch (ch){
 case 1:matchmaking(cUsername,cAge,cGender,cLocation,cHobby); break;
 case 2: exit(0); break;
 default: printf("Enter correct choice: "); goto choice;
 }
}

void matchmaking(char cUsername[20],int cAge,char cGender,char cLocation[20],int cHobby){
    int phoneNumber,fChoice,testcount=0,flag=1,usersMatched=0;

    rewind(fp);
  while(scanUserdata){
        phoneNumber = rand() % 90000000000 + 9999999999;
   if ((strcmp(cUsername,u[testcount].username)!=0) && (cAge == u[testcount].age || (cAge+10>=u[testcount].age || cAge+10<=u[testcount].age) || (cAge+10>=u[testcount].age ||
cAge+10<=u[testcount].age)) && (cHobby==u[testcount].hobby) ) {
        printf("\n\t\tWe have found a friend for you. Their name is %s\n", u[testcount].username);
        switch (u[testcount].hobby){
       case 1:printf("\t\tYou both love Reading Books\n"); break;
       case 2:printf("\t\tYou both love Playing Sports\n"); break;
       case 3:printf("\t\tYou both love Watching TV or Movies\n"); break;
       case 4:printf("\t\tYou both love Cooking\n"); break;
       case 5:printf("\t\tYou both love Dancing\n"); break;
    }
        printf("\t\tContact Number: %d\n\n",phoneNumber);
        printf("\t Age: %d\n\n",u[testcount].age);

        usersMatched++;
        }
        else flag=0;
    testcount++;
    }
    if (usersMatched==0 && flag==0)
        printf("\n\t\tWe cannot a find a match for you right now. Try again later.\n\n");

    printf(" Press 1 to logout. Press any key to Exit: ");
    scanf("%d",&fChoice);
    if (fChoice==1) {
            system("cls");
    welcomeScreen();
    }
    else {
        fclose(fp);
        exit(0);
    }
}

