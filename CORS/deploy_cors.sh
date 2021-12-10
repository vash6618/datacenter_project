docker build -t cors .
docker tag cors gcr.io/third-pen-318122/cors
docker push gcr.io/third-pen-318122/cors
kubectl delete pod cors
kubectl apply -f cors.yaml
echo "----"
echo "Run 'kubectl logs cors cors' for logs"
echo "kubectl exec -it cors -c cors -- sh"