# IPL
To access the running application:
1.	Please import the postman export to your machine.
2.	Open the imported collection and see all the API’s.
3.	Hit all of them to get the results.

Manual steps for application installation:

1. The application has been built on a Linux environment. 
2. To have it running in a docker please follow the steps.
3. Docker should be installed in your machine. Use this command: yum install docker
4. Git should be installed to fetch the repository. Use this command: yum install git
5. Clone the repository with this command: git clone https://github.com/Pankhuri1804/IPL.git
6. It will prompt you for your username and password.
7. Go to “IPL” directory: cd IPL/
8. You can build a local docker image: sudo docker build --tag iplanalysis .
9. You can run the docker container locally: docker run -d -p 5000:5000 iplanalysis


Begin of the application

1. The main.py denotes the beginning of the application.
2. The data has been kept in the data folder.
