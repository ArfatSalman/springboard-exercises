# Part One: Solidify Terminology
## In your own terms, define the following terms:
### - What is HTTP?
HTTP is a Hypertext Transfer Protocol. It is how browsers and web servers communicate.

### - What is a URL?
A URL is a Uniform Resource Locator. It is the 

### - What is DNS?
The DNS is a Domain Name Server. It converts URLs into IP addresses.

### - What is a query string?
A way of providing extra information for a URL.

### - What are two HTTP verbs and how are they different?
The two HTTP verbs are GET and POST. GET will get the data from the server, while POST will send some data to the server. A GET request will have no side effects (won't change the server data) while a POST request will have side effects (will change the server data).

### - What is an HTTP request?
An HTTP request is where you request from a client to a server, following HTTP protocol.

### - What is an HTTP response?
An HTTP response is where the server gives a response back, following HTTP protocol.

### - What is an HTTP header? Give a couple examples of request and response headers you have seen.
An HTTP header is additional information given from requests and responses. (Request examples: hostname you're asking about, date your browser thinks it is, language your browser wants information in) (Response examples: content type, date/time the server thinks it is, any caching information)

### - What are the processes that happen when you type “http://somesite.com/some/page.html” into a browser?
The browser turns the url into an IP address using DNS. The browser then makes a request to that IP address. The server then sends a response back. The browser then makes a DOM from the html in the response. The browser then makes separate HTTP requests to retrieve the other resources like JavaScript, CSS, and images. The browser finally recieves the responses from each, and you have the working website.