# example-selenium-python

Example UI testing using Selenium with Behave in Python.

# Run project

- Clone project

```
git clone https://github.com/marciovrl/example-selenium-python.git
```

# Run in a Docker

- Build conteiner

```
docker build -t docker-behave .
```

- Run conteiner

```
docker run docker-behave
```

# Run without Docker use

- Run test firefox headless

```
make test browser=firefox_headless
```

- Run test chrome headless

```
make test browser=chrome_headless
```

- Run test chrome

```
make test browser=chrome
```

# Doubt to execute?

```
make help
```
