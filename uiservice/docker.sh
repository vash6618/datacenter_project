# echo REACT_APP_POD_IP="$MY_POD_IP" > .env
sed -i '/localhost/d' .env
npm start