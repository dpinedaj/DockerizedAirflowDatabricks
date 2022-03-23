echo "-----------Configure Databricks connection--------------"
echo "Write token: "
read token
echo "Write host:"
read host
airflow connections --add \
    --conn_id databricks_id \
    --conn_type databricks \
    --conn_login token \
    --conn_extra '{"token": "'"$token"'" , "host": "'"$host"'"}'

echo "-----------Create the first admin user------------------"
echo "Write email:"
read email
echo "Write username:"
read user

python3 userPrompt.py -s -e $email -u $user
