# Receipt to point conversion manager
#
# Link to Github for project. https://github.com/MonkeyToji/receiptManager
<!-- ############################################## ##############################################  -->
# This application is designed to process receipts from a store. (Sent in a Json format)
# After downloading the application files from github there are two options for using this application.
#
# Method One:
# Step 1: Install Python 3.7
# Step 2: Once installed follow up installing Flask with < pip install flask>
# Step 3: (Optional) Pip install pytest to fun some built in testing for the python code
#
# Method Two:
# Step 1: Make sure your Docker is up and running
# Step 2: To build the docker container use < Docker Compose Build >
# Step 3: Once the build is complete you can run < Docker compose up > to run the container which will also output a postman test and pytest test
<!-- ############################################## ##############################################  -->
#
# Once the application is up and running a Json package can be sent to http://127.0.0.1:5000/receipts/process using the POST method.
# This will return an id generated using data from the receipt. As well as storing the modified receipt in a list (acting as a "database") for testing purposes.
#
# After a receipt has been processed by the application a user can use the returned id in http://127.0.0.1:5000/receipts/<id>/points
# Replace <id> with the id given which will return the points associated with the saved receipt.
