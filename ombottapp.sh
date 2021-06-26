start=$SECONDS

# https://github.com/linkchecker/linkchecker/ 

linkchecker --check-extern  --no-robots  http://localhost:8000/bulma
linkchecker --check-extern  --no-robots  http://localhost:8000/lte3
linkchecker --check-extern  --no-robots  http://localhost:8000/volt

end=$SECONDS
#you can now either just print the difference:

echo "duration: $((end-start)) seconds."
