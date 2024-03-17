you can use "simple requests" in CORS, which are requests with an Origin header but without additional CORS-related headers like Access-Control-Request-Method or Access-Control-Request-Headers. In this case, the server should respond with appropriate CORS headers without the need for a preflight OPTIONS request.

In FastAPI, you can achieve this by adding the CORSMiddleware with the allow_origins parameter set to ["*"], which allows requests from any origin, and other CORS-related parameters configured as needed.

Here's how you can configure FastAPI to handle simple requests:

```python
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI()

# Configure CORS middleware for simple requests
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allow requests from any origin
    allow_credentials=True,  # Allow credentials like cookies
    allow_methods=["GET", "POST", "PUT", "DELETE"],  # Allow these HTTP methods
    allow_headers=["*"],  # Allow any headers
)


```

With this configuration:

Requests with an Origin header will be considered simple requests.
FastAPI will automatically include appropriate CORS headers (Access-Control-Allow-Origin, Access-Control-Allow-Credentials, etc.) in the response, allowing the browser to process the response without any preflight OPTIONS requests.


This approach simplifies CORS handling for your FastAPI application, especially if you want to allow requests from any origin without restrictions. However, keep in mind that allowing requests from any origin (allow_origins=["*"]) may have security implications, so you should carefully consider your CORS policy based on your application's requirements and security considerations.