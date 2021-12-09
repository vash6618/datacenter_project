docker build -t foofi .
docker tag foofi gcr.io/sapient-zodiac-304803/foofi
docker push gcr.io/sapient-zodiac-304803/foofi
kubectl delete pod foofi
kubectl apply -f foofi.yaml
# kubectl exec -it foofi -c foofi -- sh -c 'echo REACT_APP_POD_IP="$MY_POD_IP" > .env'
echo "----"
echo "Run 'kubectl logs foofi foofi' for logs"
echo "kubectl exec -it foofi -c foofi -- sh"
