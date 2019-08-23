### Getting started with [nodejs](https://codeburst.io/the-only-nodejs-introduction-youll-ever-need-d969a47ef219).

1. create your project folder
2. initialize the node project:

```bash
$ npm init
```
This will guide your through the package.json creation

3. create server.js - content is given in this repository.
4. test your first nodejs application:

```bash
$ node server.js
```
Open your browser and hit localhost:3000. You should see a Hello worldmessage.


5. install express to make better use of web and API

```bash
$ npm install express --save
```


### Docker

you can build the docker image by running:

```bash
$ docker build . -t nodejs-rest
```

Docker container is run with exposing port 3000 from the container to port 9000 on the host with the following command:

```bash
$ docker run -e VERSION=1.1 -p 9000:3000 nodejs-rest
```

Notice the -e VERSION=1.1 which sets an environment variable to be used inside the container. The intention is to use this variable in the application. This can be enabled with modifying config.js file by changing to: version: process.env.VERSION || ‘1.0’. If environment variable VERSION is available then save it in version, if not use 1.0.

Note that the run command expose the docker to port 9000 where node runs inside the docker at port 3000.
