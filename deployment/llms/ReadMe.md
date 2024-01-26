# Run LocalAI Docker
```
docker run -p 8080:8080 -v $PWD/models:/models -ti --rm quay.io/go-skynet/local-ai:latest --models-path /models --context-size 700 --threads 16
```

# Embedding Endpoint
```
curl <http://localhost:8080/embeddings> -X POST -H "Content-Type: application/json" -d '{
  "input": "Your text string goes here",
  "model": "text-embedding-ada-002"
}'
```

# Chat Templates
```
https://github.com/mudler/LocalAI/tree/master/examples/configurations/mistral
```

# Chat Endpoint

```
curl <http://localhost:8080/v1/chat/completions> -H "Content-Type: application/json" -d '{ "model": "mistral", "messages": [{"role": "user", "content": "How are you?"}], "temperature": 0.9 }'

```